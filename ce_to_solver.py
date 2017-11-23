while True:
    scramble_ce = input("Enter Cube Explorer scramble: ")
    initIndex = 0
    scrambleSolver = ""
    if(scramble_ce == 'End'):
        break
    while True:
        move_dict_single = {"U": "UU",
                            "D": "DD",
                            "L": "LL",
                            "R": "RR",
                            "F": "FF",
                            "B": "BB"}
        move_dict_double = {"U'": "Ui",
                            "U2": "2U",
                            "D'": "Di",
                            "D2": "2D",
                            "L'": "Li",
                            "L2": "2L",
                            "R'": "Ri",
                            "R2": "2R",
                            "F'": "Fi",
                            "F2": "2F",
                            "B'": "Bi",
                            "B2": "2B"}

        if((scramble_ce[initIndex: initIndex + 2]) in move_dict_double.keys()):
            subStr = scramble_ce[initIndex: initIndex + 2]
            scrambleSolver += move_dict_double[subStr]
            initIndex += 3
        elif ((scramble_ce[initIndex: initIndex + 1]) in move_dict_single.keys()):
            subStr = scramble_ce[initIndex: initIndex + 1]
            scrambleSolver += move_dict_single[subStr]
            initIndex += 2
        else:
            initIndex += 1
        if(initIndex > len(scramble_ce) - 1):
            break
    print(scrambleSolver)
