import sys

import numpy as np
from Color import *
from Cube import Cube

second_slice = 162
third_slice = 324


if __name__ == '__main__':
    cube = Cube()

    print(cube)

    print(cube.get_all_sides())

    cube.apply_algorithm('L2 U\' L2 U L2 F2 D L2 R2 D\' U2 B U\' L U2 B D\' R\' D U B2')

    print(''.join(str(cube).split()))
    # test = np.array([[[1,2,3],
    #          [4,5,6],
    #          [7,8,9]],
    #
    #           [[9,8,7],
    #            [6,5,4],
    #            [3,2,1],],
    #
    #           [[0,0,0],
    #            [0,0,0],
    #            [0,0,0]]])
    #
    # print(np.rot90(test[0,:,:], axes=(1,0)))
    sys.exit(1)