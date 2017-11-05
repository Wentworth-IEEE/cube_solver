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
    for i in range(3):
        for j in range(3):
            for k in range(3):
                UDFacelet = ''
                FBFacelet = ''
                LRFacelet = ''
                CFacelet = ''
                for u in range(len(cubie[i][j][k])):
                    if cubie[i][j][k][u:u+1] == 'W' or cubie[i][j][k][u:u+1] == 'Y':
                        UDFacelet = cubie[i][j][k][u:u+1]
                    elif cubie[i][j][k][u:u+1] == 'G' or cubie[i][j][k][u:u+1] == 'B':
                        FBFacelet = cubie[i][j][k][u:u+1]
                    elif cubie[i][j][k][u:u+1] == 'R' or cubie[i][j][k][u:u+1] == 'O':
                        LRFacelet = cubie[i][j][k][u:u+1]
                    elif cubie[i][j][k][u:u+1] == 'C':
                        CFacelet = cubie[i][j][k][u:u+1]
                cubie[i][j][k] = (UDFacelet + FBFacelet + LRFacelet + CFacelet)
    return cubie

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
def TUFacelet(facelet):
    facelet = UFacelet(UFacelet(facelet))
    return facelet
def DFacelet(facelet):
    tempFacelet = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[1][2][0], facelet[1][1][0], facelet[1][0][0]], [facelet[1][2][1], 0, facelet[1][0][1]],
                    [facelet[1][2][2], facelet[1][1][2], facelet[1][0][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[5][2][0], facelet[5][2][1], facelet[5][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[4][2][0], facelet[4][2][1], facelet[4][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[2][2][0], facelet[2][2][1], facelet[2][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[3][2][0], facelet[3][2][1], facelet[3][2][2]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def DiFacelet(facelet):
    tempFacelet = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[1][0][2], facelet[1][1][2], facelet[1][2][2]], [facelet[1][0][1], 0, facelet[1][2][1]],
                    [facelet[1][0][0], facelet[1][1][0], facelet[1][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[4][2][0], facelet[4][2][1], facelet[4][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[5][2][0], facelet[5][2][1], facelet[5][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[3][2][0], facelet[3][2][1], facelet[3][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [facelet[2][2][0], facelet[2][2][1], facelet[2][2][2]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def TDFacelet(facelet):
    facelet = DFacelet(DFacelet(facelet))
    return facelet
def LFacelet(facelet):
    tempFacelet = [[[facelet[5][2][2], 0, 0], [facelet[5][1][2], 0, 0], [facelet[5][0][2], 0, 0]],
                   [[facelet[4][0][0], 0, 0], [facelet[4][1][0], 0, 0], [facelet[4][2][0], 0, 0]],
                   [[facelet[2][0][2], facelet[2][1][2], facelet[2][2][2]], [facelet[2][0][1], 0, facelet[2][2][1]],
                    [facelet[2][0][0], facelet[2][1][0], facelet[2][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[0][0][0], 0, 0], [facelet[0][1][0], 0, 0], [facelet[0][2][0], 0, 0]],
                   [[0, 0, facelet[1][2][0]], [0, 0, facelet[1][1][0]], [0, 0, facelet[1][0][0]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def LiFacelet(facelet):
    tempFacelet = [[[facelet[4][0][0], 0, 0], [facelet[4][1][0], 0, 0], [facelet[4][2][0], 0, 0]],
                   [[facelet[5][2][2], 0, 0], [facelet[5][1][2], 0, 0], [facelet[5][0][2], 0, 0]],
                   [[facelet[2][2][0], facelet[2][1][0], facelet[2][0][0]], [facelet[2][2][1], 0, facelet[2][0][1]],
                    [facelet[2][2][2], facelet[2][1][2], facelet[2][0][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[1][0][0], 0, 0], [facelet[1][1][0], 0, 0], [facelet[1][2][0], 0, 0]],
                   [[0, 0, facelet[0][2][0]], [0, 0, facelet[0][1][0]], [0, 0, facelet[0][0][0]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def TLFacelet(facelet):
    facelet = LFacelet(LFacelet(facelet))
    return facelet
def RFacelet(facelet):
    tempFacelet = [[[0, 0, facelet[4][0][2]], [0, 0, facelet[4][1][2]], [0, 0, facelet[4][2][2]]],
                   [[0, 0, facelet[5][2][0]], [0, 0, facelet[5][1][0]], [0, 0, facelet[5][0][0]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[3][0][2], facelet[3][1][2], facelet[3][2][2]], [facelet[3][0][1], 0, facelet[3][2][1]],
                    [facelet[3][0][0], facelet[3][1][0], facelet[3][2][2]]],
                   [[0, 0, facelet[1][0][2]], [0, 0, facelet[1][1][2]], [0, 0, facelet[1][2][2]]],
                   [[facelet[0][2][2], 0, 0], [facelet[0][1][2], 0, 0], [facelet[0][0][2], 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def RiFacelet(facelet):
    tempFacelet = [[[0, 0, facelet[5][2][0]], [0, 0, facelet[5][1][0]], [0, 0, facelet[5][0][0]]],
                   [[0, 0, facelet[4][0][2]], [0, 0, facelet[4][1][2]], [0, 0, facelet[4][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[3][2][0], facelet[3][1][0], facelet[3][0][0]], [facelet[3][2][1], 0, facelet[3][0][1]],
                    [facelet[3][2][2], facelet[3][1][2], facelet[3][0][2]]],
                   [[0, 0, facelet[0][0][2]], [0, 0, facelet[0][1][2]], [0, 0, facelet[0][2][2]]],
                   [[facelet[1][2][2], 0, 0], [facelet[1][1][2], 0, 0], [facelet[1][0][2], 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def TRFacelet(facelet):
    facelet = RFacelet(RFacelet(facelet))
    return facelet
def FFacelet(facelet):
    tempFacelet = [[[0, 0, 0], [0, 0, 0], [facelet[2][2][2], facelet[2][1][2], facelet[2][0][2]]],
                   [[facelet[3][0][0], facelet[3][1][0], facelet[3][2][0]], [0, 0, 0], [0, 0, 0]],
                   [[0, 0, facelet[1][0][0]], [0, 0, facelet[1][0][1]], [0, 0, facelet[1][0][2]]],
                   [[facelet[0][2][0], 0, 0], [facelet[0][2][1], 0, 0], [facelet[0][2][2], 0, 0]],
                   [[facelet[4][0][2], facelet[4][1][2], facelet[4][2][2]], [facelet[4][0][1], 0, facelet[4][2][1]],
                    [facelet[4][0][0], facelet[4][1][0], facelet[4][2][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def FiFacelet(facelet):
    tempFacelet = [[[0, 0, 0], [0, 0, 0], [facelet[3][0][0], facelet[3][1][0], facelet[3][2][0]]],
                   [[facelet[2][0][2], facelet[2][1][2], facelet[2][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[0, 0, facelet[0][0][2]], [0, 0, facelet[0][1][2]], [0, 0, facelet[0][2][2]]],
                   [[facelet[1][0][2], 0, 0], [facelet[1][0][1], 0, 0], [facelet[1][0][0], 0, 0]],
                   [[facelet[4][2][0], facelet[4][1][0], facelet[4][0][0]], [facelet[4][2][1], 0, facelet[4][0][1]],
                    [facelet[4][2][2], facelet[4][1][2], facelet[4][0][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def TFFacelet(facelet):
    facelet = FFacelet(FFacelet(facelet))
    return facelet
def BFacelet(facelet):
    tempFacelet = [[[facelet[3][0][2], facelet[3][1][2], facelet[3][2][2]], [0, 0, 0], [0, 0, 0]],
                   [[0, 0, 0], [0, 0, 0], [facelet[2][0][0], facelet[2][1][0], facelet[2][2][0]]],
                   [[facelet[0][0][2], 0, 0], [facelet[0][0][1], 0, 0], [facelet[0][0][0], 0, 0]],
                   [[0, 0, facelet[1][2][2]], [0, 0, facelet[1][2][1]], [0, 0, facelet[1][2][0]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[5][0][2], facelet[5][1][2], facelet[5][2][2]], [facelet[5][0][1], 0, facelet[5][2][1]],
                    [facelet[5][0][0], facelet[5][1][0], facelet[5][2][2]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def BiFacelet(facelet):
    tempFacelet = [[[facelet[2][2][0], facelet[2][1][0], facelet[2][0][0]], [0, 0, 0], [0, 0, 0]],
                   [[0, 0, 0], [0, 0, 0], [facelet[3][2][2], facelet[3][1][2], facelet[3][0][2]]],
                   [[facelet[1][2][0], 0, 0], [facelet[1][2][1], 0, 0], [facelet[1][2][2], 0, 0]],
                   [[0, 0, facelet[0][0][0]], [0, 0, facelet[0][0][1]], [0, 0, facelet[0][0][2]]],
                   [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                   [[facelet[5][2][0], facelet[5][1][0], facelet[5][0][0]], [facelet[5][2][1], 0, facelet[5][0][1]],
                    [facelet[5][2][2], facelet[5][1][2], facelet[5][0][2]]]]
    for i in range(6):
        for j in range(3):
            for k in range(3):
                if tempFacelet[i][j][k] != 0:
                    facelet[i][j][k] = tempFacelet[i][j][k]
    return facelet
def TBFacelet(facelet):
    facelet = BFacelet(BFacelet(facelet))
    return facelet

#Excecutes a moveset
def doMoveset(moveset, facelet):
    move_dict = {'UU' : UFacelet,
                 'Ui' : UiFacelet,
                 '2U' : TUFacelet,
                 'DD' : DFacelet,
                 'Di' : DiFacelet,
                 '2D' : TDFacelet,
                 'LL' : LFacelet,
                 'Li' : LiFacelet,
                 'TL' : TLFacelet,
                 'RR' : RFacelet,
                 'Ri' : RiFacelet,
                 '2R' : TRFacelet,
                 'FF' : FFacelet,
                 'Fi' : FiFacelet,
                 '2F' : TFFacelet,
                 'BB' : BFacelet,
                 'Bi' : BiFacelet,
                 '2B' : TBFacelet}
    for i in range(int(len(moveset) / 2)):
        try:
            move_dict[moveset[i*2:(i*2)+2]](facelet)
        except KeyError:
            print('Specified move not found. Possible error in moveset.')
            break
    return facelet
