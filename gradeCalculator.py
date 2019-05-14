# Greg Geary
# Grade Calculator for a student
# takes in txt file of current grades and max grades
# displays output data to html file


# Average Function
def average(score_list, max_list):
    average = score_list / max_list
    return round(average, 2)


# Letter Grade Function
def letter_grade(percent):
    if percent >= 90:
        PercentGrade = 'A'
    elif percent <= 89 and percent >= 80:
        PercentGrade = 'B'
    elif percent <= 79 and percent >= 70:
        PercentGrade = 'C'
    elif percent <= 69 and percent >= 60:
        PercentGrade = 'D'
    elif percent <= 59:
        PercentGrade = 'F'
    return PercentGrade


# Average Weighted Function
def average_weighted(score_list, max_list, weight):
    x = average(score_list, max_list) * weight
    return round(x, 3)


# Lab 8 Code
def read_grade_data(filehandle):
    inputfile = open(filehandle, 'r')
    categories = inputfile.readlines()
    cat_dict = {}
    for pos, cat in enumerate(categories):
        cat = categories[pos].split(' ', 2)
        cat[2] = cat[2].replace(' ', '')
        cat[2] = cat[2].strip('\n')
# For Weight
        weight = float(cat[1].strip('%')) / 100
# For Scores
        scores = cat[2].split(',')
# For Earned Score
        totalearned = 0
        totalpossible = 0
        for item, earnedpoints in enumerate(scores):
            earnedpoints = scores[item].split('/')
            possiblepoints = int(earnedpoints[1])
            earnedpoints = int(earnedpoints[0])
            totalearned += earnedpoints
            totalpossible += possiblepoints
        cat_dict[(cat[0])] = [weight, totalearned, totalpossible]
    inputfile.close()
    write_grade_scores(inputfile, cat_dict)


def write_grade_scores(filehandle, data):
    output = open('output.html', 'w')
    ordered_list = ['Homework', 'Quizzes',
                    'Tests', 'Projects', 'Final']
    cumulativegrade = 0
    grades = {}
    for pos, category in enumerate(ordered_list):
        posholder = data[category]
        earnscore = data[category][1]
        posscore = data[category][2]
        weight = data[category][0]
        averagescore = average(earnscore, posscore)
        contribution = average_weighted(earnscore, posscore, weight)
        letter = letter_grade((averagescore * 100))
        grades[category] = [weight, averagescore,
                            contribution, letter]
        output.write('<h1>%s Statistics(%.1f)</h1>' % (
            category, (weight * 100)))
        output.write('<ul>')
        output.write('<li><b>Average: </b>%.2f</li>' % averagescore)
        output.write('<li><b>Letter Grade: </b>%s</li>' % letter)
        output.write('<li><b>Overall Grade Contribution: </b>%.3f</li>'
                     % contribution)
        output.write('</ul>')
        cumulativegrade += weight * averagescore
    cgrade = round(cumulativegrade, 2)
    cletter = letter_grade((cumulativegrade * 100))
    output.write('<h1>Cumulative Grade</h1>')
    output.write('<ul>')
    output.write('<li><b>Average: </b>%.2f</li>' % cgrade)
    output.write('<li><b>Letter Grade: </b>%s</li>' % cletter)
    output.write('</ul>')
    output.flush()

fh = 'input.txt'
read_grade_data(fh)
