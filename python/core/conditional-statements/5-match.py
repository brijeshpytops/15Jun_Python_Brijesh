"""
Match case in python?

syntax:

match <expression>:
    case 1:
        statement1
    case 2:
        statement2
        .
        .
        .
    case _:
        default statement

"""

# fruit = "apple"

# match fruit:
#     case "apple":
#         print("The fruit is an apple.")
#     case "banana":
#         print("The fruit is a banana.")
#     case "orange":
#         print("The fruit is an orange.")
#     case _:
#         print("The fruit is not recognized.")

"""
0 -monday
1 - tuesday
2 - wednesday
3 - thursday
4 - friday
5 - saturday
6 - sunday
"""

import datetime

current_day = datetime.datetime.now().weekday()


match current_day:
    case 0:
        print("The day is Monday.")
    case 1:
        print("The day is Tuesday.")
    case 2:
        print("The day is Wednesday.")
    case 3:
        print("The day is Thursday.")
    case 4:
        print("The day is Friday.")
    case 5:
        print("The day is Saturday.")
    case 6:
        print("The day is Sunday.")
    case _:
        print("The day is not recognized.")