import tensorflow as tf
import pandas as pd

#Defining solved state
cubie_solved = [[['WBO', 'WB', 'WBR'], ['WO', 'W', 'WR'], ['WGO', 'WG', 'WGR']],
                [['BO', 'B', 'BR'], ['O', 'C', 'R'], ['GO', 'G', 'GR']],
                [['YBO', 'YB', 'YBR'], ['YO', 'Y', 'YR'], ['YGO', 'YG', 'YGR']]]

# Define cubie array from facelet
def face_to_cube(facelet):
    cubie = [[[(facelet[0][0][0] + facelet[5][0][2] + facelet[2][0][0]), (facelet[0][0][1] + facelet[5][0][1]), (facelet[0][0][2] + facelet[5][0][0] + facelet[3][0][2])],
            [(facelet[0][1][0] + facelet[2][0][1]), facelet[0][1][1], (facelet[0][1][2] + facelet[3][0][1])],
            [(facelet[0][2][0] + facelet[4][0][0] + facelet[2][0][2]), (facelet[0][2][1] + facelet[4][0][1]), (facelet[0][2][2] + facelet[4][0][2] + facelet[3][0][0])]],
            [[(facelet[5][1][2] + facelet[2][1][0]), facelet[5][1][1], (facelet[5][1][0] + facelet[3][1][2])],
            [facelet[2][1][1], 'C', facelet[3][1][1]],
            [(facelet[4][1][0] + facelet[2][1][2]), facelet[4][1][1], (facelet[4][1][2] + facelet[3][1][0])]],
            [[(facelet[1][2][0] + facelet[5][2][2] + facelet[2][2][0]), (facelet[1][2][1] + facelet[5][2][1]), (facelet[1][2][2] + facelet[5][2][0] + facelet[3][2][2])],
            [(facelet[1][1][0] + facelet[2][2][1]), facelet[1][1][1], (facelet[1][1][2] + facelet[3][2][1])],
            [(facelet[1][0][0] + facelet[4][2][0] + facelet[2][2][2]), (facelet[1][0][1] + facelet[4][2][1]), (facelet[1][0][2] + facelet[4][2][2] + facelet[3][2][0])]]]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                UD_facelet = FB_facelet = LR_facelet = C_facelet = ''
                for u in range(len(cubie[i][j][k])):
                    if cubie[i][j][k][u:u+1] == 'W' or cubie[i][j][k][u:u+1] == 'Y':
                        UD_facelet = cubie[i][j][k][u:u+1]
                    elif cubie[i][j][k][u:u+1] == 'G' or cubie[i][j][k][u:u+1] == 'B':
                        FB_facelet = cubie[i][j][k][u:u+1]
                    elif cubie[i][j][k][u:u+1] == 'R' or cubie[i][j][k][u:u+1] == 'O':
                        LR_facelet = cubie[i][j][k][u:u+1]
                    elif cubie[i][j][k][u:u+1] == 'C':
                        C_facelet = cubie[i][j][k][u:u+1]
                cubie[i][j][k] = (UD_facelet + FB_facelet + LR_facelet + C_facelet)

    return cubie


# Defining scrambled state
facelet_scrambled = scramble.generate()
cubie_scrambled = face_to_cube(facelet_scrambled)

#Move functions
def U_facelet(facelet):
    temp_facelet = [[[facelet[0][2][0], facelet[0][1][0], facelet[0][0][0]], [facelet[0][2][1], 0, facelet[0][0][1]],
                    [facelet[0][2][2], facelet[0][1][2], facelet[0][0][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[4][0][0], facelet[4][0][1], facelet[4][0][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[5][0][0], facelet[5][0][1], facelet[5][0][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[3][0][0], facelet[3][0][1], facelet[3][0][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[2][0][0], facelet[2][0][1], facelet[2][0][2]], [0, 0, 0], [0, 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def Ui_facelet(facelet):
    temp_facelet = [[[facelet[0][0][2], facelet[0][1][2], facelet[0][2][2]], [facelet[0][0][1], 0, facelet[0][2][1]],
                    [facelet[0][0][0], facelet[0][1][0], facelet[0][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[5][2][0], facelet[5][2][1], facelet[5][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[4][2][0], facelet[4][2][1], facelet[4][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[2][2][0], facelet[2][2][1], facelet[2][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[3][2][0], facelet[3][2][1], facelet[3][2][2]], [0, 0, 0], [0, 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def TU_facelet(facelet):
    temp_facelet = [[[facelet[0][2][2], facelet[0][2][1], facelet[0][2][0]], [facelet[0][1][2], 0, facelet[0][1][0]],
                    [facelet[0][0][2], facelet[0][0][1], facelet[0][0][0]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[3][0][0], facelet[3][0][1], facelet[3][0][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[2][0][0], facelet[2][0][1], facelet[2][0][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[5][0][0], facelet[5][0][1], facelet[5][0][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[4][0][0], facelet[4][0][1], facelet[4][0][2]], [0, 0, 0], [0, 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def D_facelet(facelet):
    temp_facelet = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[1][2][0], facelet[1][1][0], facelet[1][0][0]], [facelet[1][2][1], 0, facelet[1][0][1]],
                    [facelet[1][2][2], facelet[1][1][2], facelet[1][0][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[5][2][0], facelet[5][2][1], facelet[5][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[4][2][0], facelet[4][2][1], facelet[4][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[2][2][0], facelet[2][2][1], facelet[2][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[3][2][0], facelet[3][2][1], facelet[3][2][2]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def Di_facelet(facelet):
    temp_facelet = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[1][0][2], facelet[1][1][2], facelet[1][2][2]], [facelet[1][0][1], 0, facelet[1][2][1]],
                    [facelet[1][0][0], facelet[1][1][0], facelet[1][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[4][2][0], facelet[4][2][1], facelet[4][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[5][2][0], facelet[5][2][1], facelet[5][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[3][2][0], facelet[3][2][1], facelet[3][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[2][2][0], facelet[2][2][1], facelet[2][2][2]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def TD_facelet(facelet):
    temp_facelet = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[1][2][2], facelet[1][2][1], facelet[1][2][0]], [facelet[1][1][2], 0, facelet[1][1][0]],
                    [facelet[1][0][2], facelet[1][0][1], facelet[1][0][0]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[3][2][0], facelet[3][2][1], facelet[3][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[2][2][0], facelet[2][2][1], facelet[2][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[5][2][0], facelet[5][2][1], facelet[5][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[4][2][0], facelet[4][2][1], facelet[4][2][2]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def L_facelet(facelet):
    temp_facelet = [[[facelet[5][2][2], 0, 0], [facelet[5][1][2], 0, 0], [facelet[5][0][2], 0, 0]],
                   [[facelet[4][0][0], 0, 0], [facelet[4][1][0], 0, 0], [facelet[4][2][0], 0, 0]],
                   [[facelet[2][0][2], facelet[2][1][2], facelet[2][2][2]], [facelet[2][0][1], 0, facelet[2][2][1]],
                    [facelet[2][0][0], facelet[2][1][0], facelet[2][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[0][0][0], 0, 0], [facelet[0][1][0], 0, 0], [facelet[0][2][0], 0, 0]],
                   [[0, 0, facelet[1][2][0]], [0, 0, facelet[1][1][0]], [0, 0, facelet[1][0][0]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def Li_facelet(facelet):
    temp_facelet = [[[facelet[4][0][0], 0, 0], [facelet[4][1][0], 0, 0], [facelet[4][2][0], 0, 0]],
                   [[facelet[5][2][2], 0, 0], [facelet[5][1][2], 0, 0], [facelet[5][0][2], 0, 0]],
                   [[facelet[2][2][0], facelet[2][1][0], facelet[2][0][0]], [facelet[2][2][1], 0, facelet[2][0][1]],
                    [facelet[2][2][2], facelet[2][1][2], facelet[2][0][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[1][0][0], 0, 0], [facelet[1][1][0], 0, 0], [facelet[1][2][0], 0, 0]],
                   [[0, 0, facelet[0][2][0]], [0, 0, facelet[0][1][0]], [0, 0, facelet[0][0][0]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def TL_facelet(facelet):
    temp_facelet = [[[facelet[1][0][0], 0, 0], [facelet[1][1][0], 0, 0], [facelet[1][2][0], 0, 0]],
                   [[facelet[0][0][0], 0, 0], [facelet[0][1][0], 0, 0], [facelet[0][2][0], 0, 0]],
                   [[facelet[2][2][2], facelet[2][2][1], facelet[2][2][0]], [facelet[2][1][2], 0, facelet[2][1][0]],
                    [facelet[2][0][2], facelet[2][0][1], facelet[2][0][0]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[5][2][2], 0, 0], [facelet[5][1][2], 0, 0], [facelet[5][0][2], 0, 0]],
                   [[0, 0, facelet[4][2][0]], [0, 0, facelet[4][1][0]], [0, 0, facelet[4][0][0]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def R_facelet(facelet):
    temp_facelet = [[[0, 0, facelet[4][0][2]], [0, 0, facelet[4][1][2]], [0, 0, facelet[4][2][2]]],
                   [[0, 0, facelet[5][2][0]], [0, 0, facelet[5][1][0]], [0, 0, facelet[5][0][0]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[3][0][2], facelet[3][1][2], facelet[3][2][2]], [facelet[3][0][1], 0, facelet[3][2][1]],
                    [facelet[3][0][0], facelet[3][1][0], facelet[3][2][2]]],
                   [[0, 0, facelet[1][0][2]], [0, 0, facelet[1][1][2]], [0, 0, facelet[1][2][2]]],
                   [[facelet[0][2][2], 0, 0], [facelet[0][1][2], 0, 0], [facelet[0][0][2], 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def Ri_facelet(facelet):
    temp_facelet = [[[0, 0, facelet[5][2][0]], [0, 0, facelet[5][1][0]], [0, 0, facelet[5][0][0]]],
                   [[0, 0, facelet[4][0][2]], [0, 0, facelet[4][1][2]], [0, 0, facelet[4][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[3][2][0], facelet[3][1][0], facelet[3][0][0]], [facelet[3][2][1], 0, facelet[3][0][1]],
                    [facelet[3][2][2], facelet[3][1][2], facelet[3][0][2]]],
                   [[0, 0, facelet[0][0][2]], [0, 0, facelet[0][1][2]], [0, 0, facelet[0][2][2]]],
                   [[facelet[1][2][2], 0, 0], [facelet[1][1][2], 0, 0], [facelet[1][0][2], 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def TR_facelet(facelet):
    temp_facelet = [[[0, 0, facelet[1][0][2]], [0, 0, facelet[1][1][2]], [0, 0, facelet[1][2][2]]],
                   [[0, 0, facelet[0][0][2]], [0, 0, facelet[0][1][2]], [0, 0, facelet[0][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[3][2][2], facelet[3][2][1], facelet[3][2][0]], [facelet[3][1][2], 0, facelet[3][1][0]],
                    [facelet[3][0][2], facelet[3][0][1], facelet[3][0][0]]],
                   [[0, 0, facelet[5][2][0]], [0, 0, facelet[5][1][0]], [0, 0, facelet[5][0][0]]],
                   [[facelet[4][2][2], 0, 0], [facelet[4][1][2], 0, 0], [facelet[4][0][2], 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def F_facelet(facelet):
    temp_facelet = [[[0, 0, 0], [0, 0, 0], [facelet[2][2][2], facelet[2][1][2], facelet[2][0][2]]],
                   [[facelet[3][0][0], facelet[3][1][0], facelet[3][2][0]], [0, 0, 0], [0, 0, 0]],
                   [[0, 0, facelet[1][0][0]], [0, 0, facelet[1][0][1]], [0, 0, facelet[1][0][2]]],
                   [[facelet[0][2][0], 0, 0], [facelet[0][2][1], 0, 0], [facelet[0][2][2], 0, 0]],
                   [[facelet[4][0][2], facelet[4][1][2], facelet[4][2][2]], [facelet[4][0][1], 0, facelet[4][2][1]],
                    [facelet[4][0][0], facelet[4][1][0], facelet[4][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def Fi_facelet(facelet):
    temp_facelet = [[[0, 0, 0], [0, 0, 0], [facelet[3][0][0], facelet[3][1][0], facelet[3][2][0]]],
                   [[facelet[2][0][2], facelet[2][1][2], facelet[2][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[0, 0, facelet[0][0][2]], [0, 0, facelet[0][1][2]], [0, 0, facelet[0][2][2]]],
                   [[facelet[1][0][2], 0, 0], [facelet[1][0][1], 0, 0], [facelet[1][0][0], 0, 0]],
                   [[facelet[4][2][0], facelet[4][1][0], facelet[4][0][0]], [facelet[4][2][1], 0, facelet[4][0][1]],
                    [facelet[4][2][2], facelet[4][1][2], facelet[4][0][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def TF_facelet(facelet):
    temp_facelet = [[[0, 0, 0], [0, 0, 0], [facelet[1][0][2], facelet[1][0][1], facelet[1][0][0]]],
                   [[facelet[0][2][2], facelet[0][2][1], facelet[0][2][0]], [0, 0, 0], [0, 0, 0]],
                   [[0, 0, facelet[3][2][0]], [0, 0, facelet[3][1][0]], [0, 0, facelet[3][0][0]]],
                   [[facelet[2][2][2], 0, 0], [facelet[2][1][2], 0, 0], [facelet[2][0][2], 0, 0]],
                   [[facelet[4][2][2], facelet[4][2][1], facelet[4][2][0]], [facelet[4][1][2], 0, facelet[4][1][0]],
                    [facelet[4][0][2], facelet[4][0][1], facelet[4][0][0]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def B_facelet(facelet):
    temp_facelet = [[[facelet[3][0][2], facelet[3][1][2], facelet[3][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[0, 0, 0], [0, 0, 0], [facelet[2][0][0], facelet[2][1][0], facelet[2][2][0]]],
                   [[facelet[0][0][2], 0, 0], [facelet[0][0][1], 0, 0], [facelet[0][0][0], 0, 0]],
                   [[0, 0, facelet[1][2][2]], [0, 0, facelet[1][2][1]], [0, 0, facelet[1][2][0]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[5][0][2], facelet[5][1][2], facelet[5][2][2]], [facelet[5][0][1], 0, facelet[5][2][1]],
                    [facelet[5][0][0], facelet[5][1][0], facelet[5][2][2]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def Bi_facelet(facelet):
    temp_facelet = [[[facelet[2][2][0], facelet[2][1][0], facelet[2][0][0]], [0, 0, 0], [0, 0, 0]],
                   [[0, 0, 0], [0, 0, 0], [facelet[3][2][2], facelet[3][1][2], facelet[3][0][2]]],
                   [[facelet[1][2][0], 0, 0], [facelet[1][2][1], 0, 0], [facelet[1][2][2], 0, 0]],
                   [[0, 0, facelet[0][0][0]], [0, 0, facelet[0][0][1]], [0, 0, facelet[0][0][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[5][2][0], facelet[5][1][0], facelet[5][0][0]], [facelet[5][2][1], 0, facelet[5][0][1]],
                    [facelet[5][2][2], facelet[5][1][2], facelet[5][0][2]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet
def TB_facelet(facelet):
    temp_facelet = [[[facelet[1][2][2], facelet[1][2][1], facelet[1][2][0]], [0, 0, 0], [0, 0, 0]],
                   [[0, 0, 0], [0, 0, 0], [facelet[0][0][2], facelet[0][0][1], facelet[0][0][0]]],
                   [[facelet[3][2][2], 0, 0], [facelet[3][1][2], 0, 0], [facelet[3][0][2], 0, 0]],
                   [[0, 0, facelet[2][2][0]], [0, 0, facelet[2][1][0]], [0, 0, facelet[2][0][0]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[5][2][2], facelet[5][2][1], facelet[5][2][0]], [facelet[5][1][2], 0, facelet[5][1][0]],
                    [facelet[5][0][2], facelet[5][0][1], facelet[5][0][0]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if temp_facelet[i][j][k] != 0:
                    facelet[i][j][k] = temp_facelet[i][j][k]
    return facelet


# Excecutes a moveset
def do_moveset(moveset, facelet):
    move_dict = {'UU': U_facelet,
                 'Ui': Ui_facelet,
                 '2U': TU_facelet,
                 'DD': D_facelet,
                 'Di': Di_facelet,
                 '2D': TD_facelet,
                 'LL': L_facelet,
                 'Li': Li_facelet,
                 '2L': TL_facelet,
                 'RR': R_facelet,
                 'Ri': Ri_facelet,
                 '2R': TR_facelet,
                 'FF': F_facelet,
                 'Fi': Fi_facelet,
                 '2F': TF_facelet,
                 'BB': B_facelet,
                 'Bi': Bi_facelet,
                 '2B': TB_facelet}
    for i in range(int(len(moveset) / 2)):
        try:
            move_dict[moveset[i*2:(i*2)+2]](facelet)
        except KeyError:
            print('Specified move not found. Possible error in moveset.')
            break
    return facelet


# Tensorflow

# Import training data
training_data_df = pd.read_csv('training_data.csv', dtype=string)

x_training = training_data_df[['scramble']].values
y_training = training_data_df[['solution']].values

with tf.Session() as session:
    pass
