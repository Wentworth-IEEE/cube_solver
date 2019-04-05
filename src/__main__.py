import platform
# import cv2
# from cube import Cube
# from scramble_recog import gen_side
from tkinter import *
from tkinter import ttk


class SolverApp:

    def __init__(self, master):
        os = platform.system()
        master.title('Rubik\'s Cube Solver')

        # Camera grid
        camera_grid = ttk.Frame(master)
        camera_grid.grid(column=0, row=0, sticky='nw')

        camera_frame_0 = ttk.Frame(camera_grid, width=150, height=150)
        camera_frame_1 = ttk.Frame(camera_grid, width=150, height=150)
        camera_frame_2 = ttk.Frame(camera_grid, width=150, height=150)
        camera_frame_3 = ttk.Frame(camera_grid, width=150, height=150)
        camera_label_0 = ttk.Label(camera_frame_0, text='camera_0')
        camera_label_1 = ttk.Label(camera_frame_1, text='camera_1')
        camera_label_2 = ttk.Label(camera_frame_2, text='camera_2')
        camera_label_3 = ttk.Label(camera_frame_3, text='camera_3')

        camera_label_0.pack()
        camera_label_1.pack()
        camera_label_2.pack()
        camera_label_3.pack()
        camera_frame_0.grid(column=0, row=0, sticky='')
        camera_frame_1.grid(column=1, row=0, sticky='')
        camera_frame_2.grid(column=2, row=0, sticky='')
        camera_frame_3.grid(column=3, row=0, sticky='')

        # Buttons
        button_frame = ttk.Frame(master)
        solve_button = ttk.Button(button_frame, text='Solve', command=self.solve, width=14)
        scramble_button = ttk.Button(button_frame, text='Scramble', command=self.scramble, width=14)
        refresh_button = ttk.Button(button_frame, text='Refresh', command=self.refresh, width=14)
        save_button = ttk.Button(button_frame, text='Save', command=self.save, width=14)

        solve_button.pack(anchor='w')
        scramble_button.pack(anchor='w')
        refresh_button.pack(anchor='w')
        save_button.pack(anchor='w')
        button_frame.grid(column=0, row=1, sticky='nw')

        # Cube display
        cube_frame = ttk.Frame(master)

        face_w0 = ttk.Label(cube_frame, background='blue')
        '''
        face_w1 = ttk.Label(cube_frame, bg='white', width=20, height=20)
        face_w2 = ttk.Label(cube_frame, bg='white', width=20, height=20)
        face_w3 = ttk.Label(cube_frame, bg='white', width=20, height=20)
        face_w4 = ttk.Label(cube_frame, bg='white', width=20, height=20)
        face_w5 = ttk.Label(cube_frame, bg='white', width=20, height=20)
        face_w6 = ttk.Label(cube_frame, bg='white', width=20, height=20)
        face_w7 = ttk.Label(cube_frame, bg='white', width=20, height=20)
        face_w8 = ttk.Label(cube_frame, bg='white', width=20, height=20)
        face_y0 = ttk.Label(cube_frame, bg='yellow', width=20, height=20)
        face_y1 = ttk.Label(cube_frame, bg='yellow', width=20, height=20)
        face_y2 = ttk.Label(cube_frame, bg='yellow', width=20, height=20)
        face_y3 = ttk.Label(cube_frame, bg='yellow', width=20, height=20)
        face_y4 = ttk.Label(cube_frame, bg='yellow', width=20, height=20)
        face_y5 = ttk.Label(cube_frame, bg='yellow', width=20, height=20)
        face_y6 = ttk.Label(cube_frame, bg='yellow', width=20, height=20)
        face_y7 = ttk.Label(cube_frame, bg='yellow', width=20, height=20)
        face_y8 = ttk.Label(cube_frame, bg='yellow', width=20, height=20)
        face_b0 = ttk.Label(cube_frame, bg='blue', width=20, height=20)
        face_b1 = ttk.Label(cube_frame, bg='blue', width=20, height=20)
        face_b2 = ttk.Label(cube_frame, bg='blue', width=20, height=20)
        face_b3 = ttk.Label(cube_frame, bg='blue', width=20, height=20)
        face_b4 = ttk.Label(cube_frame, bg='blue', width=20, height=20)
        face_b5 = ttk.Label(cube_frame, bg='blue', width=20, height=20)
        face_b6 = ttk.Label(cube_frame, bg='blue', width=20, height=20)
        face_b7 = ttk.Label(cube_frame, bg='blue', width=20, height=20)
        face_b8 = ttk.Label(cube_frame, bg='blue', width=20, height=20)
        face_g0 = ttk.Label(cube_frame, bg='green', width=20, height=20)
        '''
        face_w0.grid(column=3, row=0, padx=10, pady=10, sticky='nesw')
        cube_frame.columnconfigure(3, weight=4)

        cube_frame.grid(column=1, row=1, sticky='nesw')

    @staticmethod
    def scramble():
        print('scramble')

    @staticmethod
    def solve():
        print('solve')

    @staticmethod
    def refresh():
        print('refresh')

    @staticmethod
    def save():
        print('save')


def main():

    root = Tk()
    app = SolverApp(root)
    root.mainloop()


if __name__ == '__main__': main()

