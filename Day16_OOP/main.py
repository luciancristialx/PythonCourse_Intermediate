# from turtle import Turtle, Screen
#
# #Construct object
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkSeaGreen4")
# timmy.forward(100)
#
# #Object attributes
# my_screen = Screen()
# print(my_screen.canvheight)
#
# #Object methods
# my_screen.exitonclick()

from prettytable import PrettyTable, DOUBLE_BORDER
table = PrettyTable()
table.set_style(DOUBLE_BORDER)
table.align = "l"
# print(table)

table.field_names = ["Pokemon", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)

print(table)


