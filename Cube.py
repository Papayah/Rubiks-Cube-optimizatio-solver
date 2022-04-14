import numpy as np
from Color import *
from Piece import Piece


# representing a cube as a 3-dimensional array (starting from front face, ending on back face)

class Cube:
    def __init__(self):
        self.model = np.array([[[Piece(O, G, W), Piece(None, G, W), Piece(R, G, W)],
                                [Piece(O, G, None), Piece(None, G, None), Piece(R, G, None)],
                                [Piece(O, G, Y), Piece(None, G, Y), Piece(R, G, Y)]],

                               [[Piece(O, None, W), Piece(None, None, W), Piece(R, None, W)],
                                [Piece(O, None, None), Piece(None, None, None), Piece(R, None, None)],
                                [Piece(O, None, Y), Piece(None, None, Y), Piece(R, None, Y)]],

                               [[Piece(O, B, W), Piece(None, B, W), Piece(R, B, W)],
                                [Piece(O, B, None), Piece(None, B, None), Piece(R, B, None)],
                                [Piece(O, B, Y), Piece(None, B, Y), Piece(R, B, Y)]]])

    def xRotate(self, row_num, clockwise=True):
        if clockwise:
            self.model[row_num, :, :] = np.rot90(self.model[row_num, :, :], axes=(1, 0))
        else:
            self.model[row_num, :, :] = np.rot90(self.model[row_num, :, :], axes=(0, 1))
        for i in range(3):
            for j in range(3):
                self.model[row_num, j, i].xSwap()
        return

    def yRotate(self, col_num, clockwise=True):
        if clockwise:
            self.model[:, col_num, :] = np.rot90(self.model[:, col_num, :], axes=(1, 0))
        else:
            self.model[:, col_num, :] = np.rot90(self.model[:, col_num, :], axes=(0, 1))
        for i in range(3):
            for j in range(3):
                self.model[j, col_num, i].ySwap()
        return

    def zRotate(self, slice_num, clockwise=True):
        if clockwise:
            self.model[:, :, slice_num] = np.rot90(self.model[:, :, slice_num], axes=(1, 0))
        else:
            self.model[:, :, slice_num] = np.rot90(self.model[:, :, slice_num], axes=(0, 1))
        for i in range(3):
            for j in range(3):
                self.model[j, i, slice_num].zSwap()
        return

    def apply_algorithm(self, alg):
        alg = ''.join(alg.split())
        cache = ''
        for i in range(len(alg)):
            if alg[i] in ('\'', '2'):
                self.parse_move(cache + alg[i])
                cache = ''
            elif cache != '':
                self.parse_move(cache)
                cache = alg[i]
            else:
                cache = alg[i]
        self.parse_move(cache)



    def parse_move(self, move):
        match move:
            case 'R':
                self.R()
            case 'R\'':
                self.R_prime()
            case 'R2':
                self.R2()
            case 'L':
                self.L()
            case 'L\'':
                self.L_prime()
            case 'L2':
                self.L2()
            case 'U':
                self.U()
            case 'U\'':
                self.U_prime()
            case 'U2':
                self.U2()
            case 'F':
                self.F()
            case 'F\'':
                self.F_prime()
            case 'F2':
                self.F2()
            case 'D':
                self.D()
            case 'D\'':
                self.D_prime()
            case 'D2':
                self.D2()
            case 'B':
                self.B()
            case 'B\'':
                self.B_prime()
            case 'B2':
                self.B2()
            case '':
                pass


    def F(self):
        self.xRotate(0)

    def F_prime(self):
        self.xRotate(0, False)

    def F2(self):
        self.F()
        self.F()

    def B(self):
        self.xRotate(2, False)

    def B_prime(self):
        self.xRotate(2)

    def B2(self):
        self.B()
        self.B()

    def U(self):
        self.yRotate(0, False)

    def U_prime(self):
        self.yRotate(0)

    def U2(self):
        self.U()
        self.U()

    def D(self):
        self.yRotate(2)

    def D_prime(self):
        self.yRotate(2, False)

    def D2(self):
        self.D()
        self.D()

    def L(self):
        self.zRotate(0)

    def L_prime(self):
        self.zRotate(0, False)

    def L2(self):
        self.L()
        self.L()

    def R(self):
        self.zRotate(2, False)

    def R_prime(self):
        self.zRotate(2)

    def R2(self):
        self.R()
        self.R()

    def str_to_piece(self, s):
        return Piece(s[1], s[2], s[3])

    def copy_cube(self, cube_data):
        self.model = np.array([[[]]])

    def get_side(self, side):
        res = ''
        if side == 'F':
            for x in range(3):
                for y in range(3):
                    res += color(self.model[0, x, y].colors[1]) + '  '
                res += '\n'
        elif side == 'B':
            for x in range(3):
                for y in range(3):
                    res += color(self.model[2, x, y].colors[1]) + '  '
                res += '\n'
        elif side == 'U':
            for x in range(3):
                for y in range(3):
                    res += color(self.model[x, 0, y].colors[2]) + '  '
                res += '\n'
        elif side == 'D':
            for x in range(3):
                for y in range(3):
                    res += color(self.model[x, 2, y].colors[2]) + '  '
                res += '\n'
        elif side == 'L':
            for x in range(3):
                for y in range(3):
                    res += color(self.model[x, y, 0].colors[0]) + '  '
                res += '\n'
        elif side == 'R':
            for x in range(3):
                for y in range(3):
                    res += color(self.model[x, y, 2].colors[0]) + '  '
                res += '\n'
        return res

    def get_all_sides(self):
        res = ''
        for side in ['F', 'R', 'B', 'L', 'U', 'D']:
            res += self.get_side(side) + '\n\n'
        return res

    def __str__(self):
        res = ''
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    res += str(self.model[x, y, z]) + ' ' * (10 - len(str(self.model[x, y, z])))
                res += '\n\n'
            res += '\n\n\n'
        return res
