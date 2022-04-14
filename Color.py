# from enum import Enum
#
#
# class Color(Enum):
#     W = 0
#     G = 1
#     O = 2
#     B = 3
#     R = 4
#     Y = 5

W = 0
G = 1
O = 2
B = 3
R = 4
Y = 5

def color(integer):
    match integer:
        case 0:
            return 'W'
        case 1:
            return 'G'
        case 2:
            return 'O'
        case 3:
            return 'B'
        case 4:
            return 'R'
        case 5:
            return 'Y'