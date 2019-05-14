# Greg Geary
# User can play a sports themed game show 

from random import shuffle

scores = {}

questions = [{"question": "What color jersey is worn by the winners of each "

              # entering questions into a list of dictionaries

                          "stage of the Tour De France?",

              "answers": ["red",

                          "yellow",

                          "green",

                          "blue"],

              "correct": "2"},

             {"question": "Which chess piece can only move diagonally?",

              "answers": ["bishop",

                          "pawn",

                          "king",

                          "queen",

                          "knight"],

              "correct": "1"},

             {"question": "Lambeau field is the home of which NFL Team?",

              "answers": ["New Orleans",

                          "Arizona",

                          "Green Bay",

                          "Carolina"],

              "correct": "3"},

             {"question": "What sport did Anthony Jerome 'Spud' Web retire from in 1997?",

              "answers": ["tennis",

                          "football",

                          "baseball",

                          "basketball"],

              "correct": "4"},

             {"question": "In what year did the Houstan Texans join the NFL?",

              "answers": ["2002",

                          "2009",

                          "1999",

                          "2001"],

              "correct": "1"},

             {"question": "What is the most common pitch thrown by pitchers in baseball?",

              "answers": ["curve ball",

                          "change up",

                          "fast ball",

                          "slider"],

              "correct": "3"},

             {"question": "Who is the longest reigning heavyweight boxing champion?",

              "answers": ["Mike Tyson",

                          "Joe Louis",

                          "Floyd Mayweather",

                          "Mohammed Ali"],

              "correct": "2"},

             {"question": "What team is one of the six original Hockey teams in the NHL?",

              "answers": ["Phoenix Coyotes",

                          "Detroit Redwings",

                          "Pittsburgh Penguins",

                          "Vancouver Canucks"],

              "correct": "1"},

             {"question": "Barry Bonds holds the MLB homerun record with how many homeruns?",

              "answers": ["404",

                          "690",

                          "203",

                          "762"],

              "correct": "4"},

             {"question": "Which tennis player has won the most grand slam titles?",

              "answers": ["Rafael Mendall",

                          "Roger Federer",

                          "Novak Djokovic",

                          "Andy Murray"],

              "correct": "2"}]

print("Welcome to Sports Trivia!!")

print("How well do YOU know yours sports? ")

print("Please give all answers in lowercase")

# prints the intro



def play_game():

    # function for plauying the game

    score = 0

    shuffle(questions)

    for question in questions:

        print(question["question"])

        # prints the question in a random order

        for i, choice in enumerate(question["answers"]):

            print(str(i + 1) + ". " + choice)

        answer = input("Choose an answer: ")

        if answer == question["correct"]:

            score += 1

            print(" ")

            print("Great job. You hit it right out of the ball park!")

            print("Your current score is " + str(score))

            print(" ")

            # adds a personal touch with the score at the end of questions

        else:

            print(" ")

            print("Incorrect, If youre going to win the stair climbing"

                  " competition youre going to need to step up your game")

            # incorrect answer prints

    name = input("Enter your name: ")

    # for highscore



    def highscore(name, score):

        scores[name] = score

        final = "Your high-scores are " + str(scores)

        return final



    print(highscore(name, score))



while True:

    print(" ")

    main_menu = input("Would you like to 1: Play the game, "

                      "2: View the credits, or 3: Quit: ")

    # main menu asks if you want to play quit or go to credits

    if main_menu == "1":

        play_game()

        continue

    # plays the game

    elif main_menu == "2":

        print(" ")

        print("Today's Sports Trivia is brought to you by...")

        print("Jackson Braudaway and Greg Geary")

        # credits

    elif main_menu == "3":

        print(" ")

        print("You decided to quit, thanks for playing")

        print("... Even though my father taught me to never quit...")

        print("... Have a nice day!")

        break # quits

