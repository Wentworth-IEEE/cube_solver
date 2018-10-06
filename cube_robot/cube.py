import solver as sv

class cube:
    def __init__(self):
        self.side_white = self.__init_side__('W')
        self.side_yellow = self.__init_side__('Y')
        self.side_blue = self.__init_side__('B')
        self.side_green = self.__init_side__('G')
        self.side_red = self.__init_side__('R')
        self.side_orange = self.__init_side__('O')
        self.sides = [self.side_white, self.side_yellow, self.side_blue, self.side_green, self.side_red, self.side_orange]
        self.colors = ['W', 'Y', 'B', 'G', 'R', 'O']

    def get_side(self, side): # returns a two-dimensionalarray of one side
        pass

    def set_side(self, side, colors): 
        pass

    def is_solved(self):
        solved = True
        for s in range(6):
            for i in range(3):
                for j in range(3):
                    if (self.sides[s][i][j] != self.colors[s]):
                        solved = False
        return solved

    def degree_unsolved(self):
        solution = sv.solve(self.__format_as_cube_def__(), 20, 2)
        pass

    def __format_as_cube_def__(self):
        cube_definition = ''
        color_dict = {'W': 'U',
                      'Y': 'D', 
                      'G': 'F',
                      'B': 'B',
                      'O': 'L',
                      'R': 'R'}
        sides_reordered = [self.side_white, self.side_red, self.side_green, self.side_yellow, self.side_orange, self.side_blue]

        for side in sides_reordered:
            for i in range(3):
                for j in range(3):
                    cube_definition += color_dict[side[i][j]]

        return cube_definition

    def do_move(self, move):
        pass

    def __init_side__(self, color):
        side = self.__zeros__(3, 3)
        side[1][1] = color
        return side

    def __zeros__(self, sizex, sizey):
        return [[0 for col in range(sizex)] for row in range(sizey)]
