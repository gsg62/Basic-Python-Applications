
dict = {"A": [" ### ",
              " # # ",
              " ### ",
              " # # ",
              " # # "],

        "B": ["###  ",
              "#  # ",
              "###  ",
              "#  # ",
              "###  "],

        "C": ["#####",
              "#    ",
              "#    ",
              "#    ",
              "#####"],

        "D": ["#### ",
              "#   #",
              "#   #",
              "#   #",
              "#### "],

        "E": ["#####",
              "#    ",
              "###  ",
              "#    ",
              "#####"],

        "F": ["#####",
              "#    ",
              "###  ",
              "#    ",
              "#    "],

        "G": ["#####",
              "#    ",
              "#  ##",
              "#   #",
              "#####"],

        "H": ["#   #",
              "#   #",
              "#####",
              "#   #",
              "#   #"],

        "I": ["#####",
              "  #  ",
              "  #  ",
              "  #  ",
              "#####"],

        "J": ["#####",
              "  #  ",
              "  #  ",
              "# #  ",
              "###  "],

        "K": ["#   #",
              "#  # ",
              "###  ",
              "#  # ",
              "#   #"],

        "L": ["#    ",
              "#    ",
              "#    ",
              "#    ",
              "#####"],

        "M": ["#   #",
              "## ##",
              "# # #",
              "#   #",
              "#   #"],

        "N": ["#    #",
              "##   #",
              "# #  #",
              "#  # #",
              "#   ##"],

        "O": ["#####",
              "#   #",
              "#   #",
              "#   #",
              "#####"],

        "P": ["#####",
              "#   #",
              "#####",
              "#    ",
              "#    "],

        "Q": [" ### ",
              "#   #",
              "#   #",
              " ### ",
              "    #"],

        "R": ["#####",
              "#   #",
              "#####",
              "#  # ",
              "#   #"],

        "S": ["  ###",
              " ##  ",
              "  ###",
              "   ##",
              "###  "],

        "T": ["#####",
              "  #  ",
              "  #  ",
              "  #  ",
              "  #  "],

        "U": ["#    #",
             "#    #",
             "#    #",
             "#    #",
             " #### "],

        "V": ["#     #",
             " #   # ",
             "  # #  ",
             "   #   "],

        "W": ["#     #",
              "#     #",
              "#  #  #",
              "##  ###",
              "#     #"],

        "X": ["#     #",
              " #   # ",
              "  # #  ",
              " #   # ",
              "#     #"],

        "Y": ["#     #",
              " #   # ",
              "  ##   ",
              "  ##   ",
              "  ##   "],

        "Z": ["#####",
              "   # ",
              "  #  ",
              " #   ",
              "#####"]
        }



def banner(word, direction):
    if direction == "vertical":
        for letters in word:
            for i in range(5):
                print(dict[letters][i])
    else:
        for i in range(5):
            print()
            for letters in word:
                print(dict[letters][i], end= " ")


def main():
    word = input("Enter Word Here: ")
    direction = input("Enter direction here (vertical/horizontal): ")
    banner(word, direction)


main()
