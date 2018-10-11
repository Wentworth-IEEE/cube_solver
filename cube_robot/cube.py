import solver as sv # kociemba two-phase solver

'''
The names of the facelet positions of the cube
                    |****White*****|
                    |*00* *01* *02*|
                    |**************|
                    |*10* *11* *12*|
                    |**************|
                    |*20* *21* *22*|
                    |**************|
     |****Orange****|****Green*****|*****Red******|*****Blue*****|
     |*00* *01* *02*|*00* *01* *02*|*00* *01* *02*|*00* *01* *02*|
     |**************|**************|**************|**************|
     |*10* *11* *12*|*10* *11* *12*|*10* *11* *12*|*10* *11* *12*|
     |**************|**************|**************|**************|
     |*20* *21* *22*|*20* *21* *22*|*20* *21* *22*|*20* *21* *22*|
     |**************|**************|**************|**************|
                    |****Yellow****|
                    |*00* *01* *02*|
                    |**************|
                    |*10* *11* *12*|
                    |**************|
                    |*20* *21* *22*|
                    |**************|
'''
class cube:
    def __init__(self):
        self.side_white = self.__init_side__('W') # initialize each side with the specified color for all facelets
        self.side_yellow = self.__init_side__('Y')
        self.side_blue = self.__init_side__('B')
        self.side_green = self.__init_side__('G')
        self.side_red = self.__init_side__('R')
        self.side_orange = self.__init_side__('O')
        self.sides = [self.side_white, self.side_yellow, self.side_blue, self.side_green, self.side_red, self.side_orange]
        self.colors = ['W', 'Y', 'B', 'G', 'R', 'O']
        self.side_dict = {'W': self.side_white,
                          'Y': self.side_yellow,
                          'B': self.side_blue,
                          'G': self.side_green,
                          'R': self.side_red,
                          'O': self.side_orange}

    def get_side(self, side): # returns a two-dimensional array of one side
        return self.side_dict[side]
        
    def set_side(self, side, colors): # sets the values of a side, with the side name and a 2D array of the facelets
        self.side_dict[side] = colors

    def is_solved(self):
        solved = True
        for s in range(6):
            for i in range(3):
                for j in range(3):
                    if (self.sides[s][i][j] != self.colors[s]): # checks that all facelets are the correct colors for each given side
                        solved = False
        return solved

    def degree_unsolved(self):
        solution = sv.solve(self.__format_as_cube_def__(), 20, 2)
        #TODO:
        # length of solution is the degree unsolved

        pass

    def __format_as_cube_def__(self):
        cube_definition = ''
        color_dict = {'W': 'U', # cube explorer refers to the facelet colors as which side they are on, color-neutral
                      'Y': 'D', 
                      'G': 'F',
                      'B': 'B',
                      'O': 'L',
                      'R': 'R'}

        # cube explorer lists the sides in a cifferent order; U, R, F, D, L, B
        sides_reordered = [self.side_white, self.side_red, self.side_green, self.side_yellow, self.side_orange, self.side_blue]

        # iterate through all facelets and append to cube definition
        for side in sides_reordered:
            for i in range(3):
                for j in range(3):
                    cube_definition += color_dict[side[i][j]] 

        return cube_definition

    def do_move(self, move):
        pass

    def __init_side__(self, color):
        # creates a 3x3 array of the color specified
        return [[color for col in range(3)] for row in range(3)]
