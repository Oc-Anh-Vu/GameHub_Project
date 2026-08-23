import tkinter as tk
from tkinter import messagebox

class SudokuGame:
    def __init__(self, master):
        self.master = master
        
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        
        self.setup_ui()

    def setup_ui(self):
        title_label = tk.Label(self.master, text="Sudoku", font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#333")
        title_label.pack(pady=(20, 10))
        
        grid_frame = tk.Frame(self.master, bg="black", bd=2)
        grid_frame.pack()

        for r in range(9):
            for c in range(9):
                pad_bottom = 2 if r % 3 == 2 and r != 8 else 1
                pad_right = 2 if c % 3 == 2 and c != 8 else 1
                
                var = tk.StringVar()
                var.trace_add("write", lambda name, index, mode, sv=var: self.limit_input(sv))
                
                entry = tk.Entry(grid_frame, width=2, font=("Helvetica", 18, "bold"), 
                                 justify="center", textvariable=var, relief="flat")
                
                entry.grid(row=r, column=c, padx=(1, pad_right), pady=(1, pad_bottom), ipady=5)
                self.cells[r][c] = entry

        btn_frame = tk.Frame(self.master, bg="#f0f0f0")
        btn_frame.pack(pady=20)
        
        check_btn = tk.Button(btn_frame, text="Kiểm tra", font=("Helvetica", 12), bg="#2196F3", fg="white", command=self.check_sudoku)
        check_btn.grid(row=0, column=0, padx=10)
        
        clear_btn = tk.Button(btn_frame, text="Xóa bảng", font=("Helvetica", 12), bg="#F44336", fg="white", command=self.clear_board)
        clear_btn.grid(row=0, column=1, padx=10)

    def limit_input(self, sv):
        value = sv.get()
        if len(value) > 1:
            sv.set(value[-1])
        if not value.isdigit() or value == "0":
            sv.set("")

    def check_sudoku(self):
        messagebox.showinfo("Thông báo", "Thuật toán kiểm tra Sudoku đang được phát triển!")

    def clear_board(self):
        for r in range(9):
            for c in range(9):
                self.cells[r][c].delete(0, tk.END)