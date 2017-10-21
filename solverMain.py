import tensorflow as tf

#Defining scrambled state
faceletScrambled = [[[]]]
cubieScrambled = [[[]]]

#Defining solved state
faceletSolved = [[['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']],
                 [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']],
                 [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']],
                 [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']],
                 [['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']],
                 [['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']]]
cubieSolved = [[['WBO', 'WB', 'WBR'], ['WO', 'W', 'WR'], ['WGO', 'WG', 'WGR']],
                [['BO', 'B', 'BR'], ['O', 'C', 'R'], ['GO', 'G', 'GR']],
                [['YBO', 'YB', 'YBR'], ['YO', 'Y', 'YR'], ['YGO', 'YG', 'YGR']]]

#Define cubie array from facelet
def FacetoCube(facelet):
    cubie = [[[(facelet[0][0][0] + facelet[5][0][2] + facelet[2][0][0]), (facelet[0][0][1] + facelet[5][0][1]), (facelet[0][0][2] + facelet[5][0][0] + facelet[3][0][2])],
                [(facelet[0][1][0] + facelet[2][0][1]), facelet[0][1][1], (facelet[0][1][2] + facelet[3][0][1])],
                [(facelet[0][2][0] + facelet[4][0][0] + facelet[2][0][2]), (facelet[0][2][1] + facelet[4][0][1]), (facelet[0][2][2] + facelet[4][0][2] + facelet[3][0][0])]],
                [[(facelet[5][1][2] + facelet[2][1][0]), facelet[5][1][1], (facelet[5][1][0] + facelet[3][1][2])],
                [facelet[2][1][1], 'C', facelet[3][1][1]],
                [(facelet[4][1][0] + facelet[2][1][2]), facelet[4][1][1], (facelet[4][1][2] + facelet[3][1][0])]],
                [[(facelet[1][2][0] + facelet[5][2][2] + facelet[2][2][0]), (facelet[1][2][1] + facelet[5][2][1]), (facelet[1][2][2] + facelet[5][2][0] + facelet[3][2][2])],
                [(facelet[1][1][0] + facelet[2][2][1]), facelet[1][1][1], (facelet[1][1][2] + facelet[3][2][1])],
                [(facelet[1][0][0] + facelet[4][2][0] + facelet[2][2][2]), (facelet[1][0][1] + facelet[4][2][1]), (facelet[1][0][2] + facelet[4][2][2] + facelet[3][2][0])]]]
    return cubie

print(FacetoCube(faceletSolved))

#Move functions
def UFacelet(facelet):
    tempFacelet = [[[facelet[0][2][0], facelet[0][1][0], facelet[0][0][0]], [facelet[0][2][1], 0, facelet[0][0][1]],
                    [facelet[0][2][2], facelet[0][1][2], facelet[0][0][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[4][0][0], facelet[4][0][1], facelet[4][0][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[5][0][0], facelet[5][0][1], facelet[5][0][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[3][0][0], facelet[3][0][1], facelet[3][0][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[2][0][0], facelet[2][0][1], facelet[2][0][2]], [0, 0, 0], [0, 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def UiFacelet(facelet):
    tempFacelet = [[[facelet[0][0][2], facelet[0][1][2], facelet[0][2][2]], [facelet[0][0][1], 0, facelet[0][2][1]],
                    [facelet[0][0][0], facelet[0][1][0], facelet[0][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[5][2][0], facelet[5][2][1], facelet[5][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[4][2][0], facelet[4][2][1], facelet[4][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[2][2][0], facelet[2][2][1], facelet[2][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[3][2][0], facelet[3][2][1], facelet[3][2][2]], [0, 0, 0], [0, 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def DFacelet(facelet):
    tempFacelet = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[0][2][0], facelet[0][1][0], facelet[0][0][0]], [facelet[0][2][1], 0, facelet[0][0][1]],
                    [facelet[0][2][2], facelet[0][1][2], facelet[0][0][2]]],
                   [[facelet[5][2][0], facelet[5][2][1], facelet[5][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[4][2][0], facelet[4][2][1], facelet[4][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[2][2][0], facelet[2][2][1], facelet[2][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[3][2][0], facelet[3][2][1], facelet[3][2][2]], [0, 0, 0], [0, 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def DiFacelet(facelet):
    tempFacelet = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[0][0][2], facelet[0][1][2], facelet[0][2][2]], [facelet[0][0][1], 0, facelet[0][2][1]],
                    [facelet[0][0][0], facelet[0][1][0], facelet[0][2][2]]],
                   [[facelet[4][2][0], facelet[4][2][1], facelet[4][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[5][2][0], facelet[5][2][1], facelet[5][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[3][2][0], facelet[3][2][1], facelet[3][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[facelet[2][2][0], facelet[2][2][1], facelet[2][2][2]], [0, 0, 0], [0, 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def LFacelet(facelet):
    return
def LiFacelet(facelet):
    return
def RFacelet(facelet):
    return
def RiFacelet(facelet):
    return
def FFacelet(facelet):
    return
def FiFacelet(facelet):
    return
def BFacelet(facelet):
    return
def BiFacelet(facelet):
    return