if __name__ == '__main__':
    import tkinter as tk

    top = tk.Tk()

    C = tk.Canvas(top, bg='blue', height=250, width=300)

    coord = 10, 50, 240, 210
    arc = C.create_arc(coord, start=0, extent=150, fill='red')
    
    line = C.create_line(10, 10, 200, 200, fill='white')
    
    C.pack()
    
    top.mainloop()

