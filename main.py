if __name__ == '__main__':
    import tkinter as tk

    from board import Board

    BOARD_WIDTH = 7
    BOARD_HEIGHT = 6

    WINDOW_WIDTH = 490
    WINDOW_HEIGHT = 420
    WINDOW_TITLE = 'Connect Four'

    COLUMN_WIDTH = 70

    board = Board(BOARD_WIDTH, BOARD_HEIGHT)

    app = tk.Tk()
    app.resizable(False, False)
    app.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
    app.title(WINDOW_TITLE)

    canvas_width = COLUMN_WIDTH * BOARD_WIDTH
    canvas_height = COLUMN_WIDTH * BOARD_HEIGHT
    canvas = tk.Canvas(app, bg='white', width=canvas_width, height=canvas_height)

    for i in range(1, BOARD_WIDTH):
        canvas.create_line(i*COLUMN_WIDTH, 0, i*COLUMN_WIDTH, WINDOW_HEIGHT)

    canvas.create_oval(2, 2, COLUMN_WIDTH-2, COLUMN_WIDTH-2, fill='red', outline='')

    canvas.bind('<Button-1>', lambda e: print(e.x))

    canvas.pack()
    
    app.mainloop()
