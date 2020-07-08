from board import Board
import constants as c


def click_callback(board, canvas):
    def callback(event):
        turn = board.turn

        if turn == Board.PLAYER_1:
            color = c.PLAYER_1_COLOR
        else:
            color = c.PLAYER_2_COLOR
        
        for i in range(1, c.BOARD_WIDTH + 1):
            if event.x < i * c.COLUMN_WIDTH:
                if board.make_move(i):
                    j = board.get_column_height(i)
                    
                    x0 = (i-1) * c.COLUMN_WIDTH + c.TOKEN_MARGIN
                    y0 = canvas.winfo_height() - (j-1) * c.COLUMN_WIDTH - c.TOKEN_MARGIN - 2

                    x1 = i * c.COLUMN_WIDTH - c.TOKEN_MARGIN
                    y1 = canvas.winfo_height() - j * c.COLUMN_WIDTH + c.TOKEN_MARGIN - 2

                    canvas.create_oval(x0, y0, x1, y1, fill=color, outline='')

                break

    return callback


if __name__ == '__main__':
    import tkinter as tk

    board = Board(c.BOARD_WIDTH, c.BOARD_HEIGHT)

    app = tk.Tk()
    app.resizable(False, False)
    app.geometry(f'{c.WINDOW_WIDTH}x{c.WINDOW_HEIGHT}')
    app.title(c.WINDOW_TITLE)
    
    canvas_width = c.COLUMN_WIDTH * c.BOARD_WIDTH
    canvas_height = c.COLUMN_WIDTH * c.BOARD_HEIGHT
    canvas = tk.Canvas(app, bg='white', width=canvas_width, height=canvas_height)

    for i in range(1, c.BOARD_WIDTH):
        canvas.create_line(i*c.COLUMN_WIDTH, 0, i*c.COLUMN_WIDTH, c.WINDOW_HEIGHT)

    canvas.bind('<Button-1>', click_callback(board, canvas))

    canvas.pack()
    
    app.mainloop()
