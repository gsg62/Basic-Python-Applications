# Greg Geary
# User can take a simple math quiz based off
# user chosen prefrences such as the number of questions and level of difficulty

# We are going to import some random number generation.
from random import randint

print('Welcome to MathQuiz!')

# This line is to ask the user how many questions they want to answer.
questions = int(input('How many questions do you want to answer? '))
diff = int(input('Please select difficulty from 1, 2, or 3: '))
correct = 0

# We can use that number of difficulty in a ifelse branch to define the number of iterations
# and the difficulty of them
if diff == 1:
    for i in range(questions):
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        op = randint(1, 2)

        if op == 1:
            ans1 = n1 + n2
            uans = int(input('What is %d plus %d? ' % (n1, n2)))
            if uans == ans1:
                print('You are correct!')
                correct += 1
            else:
                print('That is not quite right; the answer was ', ans1, '.')
        else:
            ans1 = n1 - n2
            uans = int(input('What is %d minus %d? ' % (n1, n2)))
            if uans == ans1:
                print('You are correct!')
                correct += 1
            else:
                print('That is not quite right; the answer was ', ans1, '.')
elif diff == 2:
    for i in range(questions):
        n1 = randint(1, 25)
        n2 = randint(1, 25)
        op = randint(1, 4)

        if op == 1:
            ans2 = n1 + n2
            uans = int(input('What is %d plus %d? ' % (n1, n2)))
            if uans == ans2:
                print('You are correct!')
                correct += 1
            else:
                print('That is not quite right; the answer was ', ans2, '.')
        elif op == 2:
            ans2 = n1 - n2
            uans = int(input('What is %d minus %d? ' % (n1, n2)))
            if uans == ans2:
                print('You are correct!')
                correct += 1
            else:
                print('That is not quite right; the answer was ', ans2, '.')
        elif op == 3:
            ans2 = n1 * n2
            uans = int(input('What is %d times %d? ' % (n1, n2)))
            if uans == ans2:
                print('You are correct!')
                correct += 1
            else:
                print('That is not quite right; the answer was ', ans2, '.')
        elif op == 4:
            ans2 = round(n1 / n2, 2)
            uans = float(input('What is %d divided by %d? (round to 2 decimal places) ' % (n1, n2)))
            if uans == ans2:
                print('You are correct!')
                correct += 1
            else:
                print('That is not quite right; the answer was ', ans2, '.')
elif diff == 3:
    for i in range(questions):
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        n3 = randint(1, 10)
        op = randint(1, 5)

        if op == 1:
            ans3 = (n1 ** n2) // n3
            uans = int(input('What is %d raised to the %d floor divided by %d? ' % (n1, n2, n3)))
            if uans == ans3:
                print('You are correct!')
                correct += 1
            else:
                print('That is not quite right; the answer was ', ans3, '.')
        elif op == 2:
            ans3 = n1 * (n2 * (n3)) % 10
            uans = int(input('What is %d times %d times %d mod 10? ' % (n1, n2, n3)))
            if uans == ans3:
                print('You are correct!')
                correct += 1
            else:
                print('That is not quite right; the answer was ', ans3, '.')
        elif op == 3:
            ans3 = n1 % n2 // n3
            uans = int(input('What is %d mod %d floor divided by %d? ' % (n1, n2, n3)))
            if uans == ans3:
                print('You are correct!')
                correct += 1
            else:
                print('That is not quite right; the answer was ', ans3, '.')
        elif op == 4:
            ans3 = round(((n1 * n2) / n3) * n2, 2)
            uans = float(input('What is %d times %d divided by %d all times %d? ' % (n1, n2, n3, n2)))
            if uans == ans3:
                print('You are correct!')
                correct += 1
            else:
                print('That is not quite right; the answer was ', ans3, '.')
        elif op == 5:
            ans3 = (n1 % 3) - (n2 % 5) * (n3 % 8)
            uans = int(input('What is %d mod 3 minus %d mod 5 times %d mod 8? ' % (n1, n2, n3)))
            if uans == ans3:
                print('You are correct!')
                correct += 1
            else:
                print('That is not quite right; the answer was ', ans3, '.')

score = (correct / questions) * 100
print("You got ", correct, " out of ", questions, " correct and recieved a score of ", score, "%.")
if score >= (2 / 3) * 100:
    print('Well done!')
elif score < (2 / 3) * 100 and score >= (1 / 3) * 100:
    print('You need more practice.')
else:
    print('Please ask your math teacher for help!')
