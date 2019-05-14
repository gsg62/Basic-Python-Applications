# @author Greg Geary
# takes in a txt file that has the coordinates and
# magnitude of around 3,000 stars and displays them as
# if you were looking through a telescope

# import turtle
import turtle


# read_coords function to read through file and get star data
def read_coords(file):
    x = open(file, "r")
    star_dict1 = {}
    star_dict2 = {}
    star_dict3 = {}
    # Goes through each line and separates the star data in dictionaries
    for i in x.readlines():
        star_name = ""
        # Splits each line at spaces
        i = i.split(" ")
        # If a name exists, rejoins the name(s) and splits them at ;
        if len(i) >= 7:
            star_name = i[6:]
            star_data = i[:6]
            star_name = ("".join(star_name)).strip().split(";")
        # If there is no name, returns normal list
        else:
            i[5] = i[5].strip()
            star_data = i
        # Sets dict key to Henry Draper and data to coordinates
        star_dict1[star_data[3]] = [float(star_data[0]), float(star_data[1])]
        # Sets dict key to Henry Draper and data to magnitudes
        star_dict2[star_data[3]] = float(float(star_data[4]))
        # If star has a name, sets dict keys as name and data to Henry Draper
        if star_name:
            for k in star_name:
                star_dict3[k] = star_data[3]
    # Creates tuple of all 3 dicts
    star_tuple = (star_dict1, star_dict2, star_dict3)
    return star_tuple


# plot_plain_stars function to draw the stars
def plot_plain_stars(picture_size, coordinates_dict):
    # creates turtle screen
    screen = turtle.Screen()
    screen.screensize(500, 500)
    # fills background black
    t = turtle.Turtle()
    # Creates black background
    t.begin_fill()
    t.color("black")
    t.speed(0)
    t.forward(picture_size[0] / 2)
    t.right(90)
    t.fd(picture_size[1] / 2)
    t.right(90)
    t.fd(picture_size[0])
    t.right(90)
    t.fd(picture_size[1])
    t.right(90)
    t.fd(picture_size[0])
    t.right(90)
    t.fd(picture_size[1] / 2)
    t.end_fill()

    t.ht()
    t.up()
    t.color("white")
    # Plots each star by coordinates
    for i in coordinates_dict:
        t.goto(coordinates_dict[i][0] * 250, coordinates_dict[i][1] * 250)
        # Draws stars as a square
        t.begin_fill()
        for l in range(4):
            t.forward(2)
            t.left(90)
        t.end_fill()

    turtle.done()


# plot_by_magnitude function to draw the stars with magnitude
def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    # creates turtle screen
    screen = turtle.Screen()
    screen.screensize(500, 500)
    # fills background black
    t = turtle.Turtle()
    # Creates black background
    t.begin_fill()
    t.color("black")
    t.speed(0)
    t.forward(picture_size[0] / 2)
    t.right(90)
    t.fd(picture_size[1] / 2)
    t.right(90)
    t.fd(picture_size[0])
    t.right(90)
    t.fd(picture_size[1])
    t.right(90)
    t.fd(picture_size[0])
    t.right(90)
    t.fd(picture_size[1] / 2)
    t.end_fill()

    t.ht()
    t.up()
    t.color("white")
    # Plots each star by coordinates
    for i in coordinates_dict:
        t.goto(coordinates_dict[i][0] * 250, coordinates_dict[i][1] * 250)
        # Measures each star's magnitude and draws their size according
        star_size = round(10.0/(magnitudes_dict[i] + 2))
        if star_size > 8:
            star_size = 8
        # Draws stars as a square
        t.begin_fill()
        for l in range(4):
            t.forward(star_size)
            t.left(90)
        t.end_fill()

    turtle.done()

# Executes the drawing
plot_by_magnitude([500, 500], read_coords("stars.txt")[0],
                  read_coords("stars.txt")[1])
