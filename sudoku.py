import tkinter as tk
from tkinter import messagebox
import random

class SudokuGame:
    def __init__(self, master):
        self.master = master
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.sample_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.setup_ui()
        self.load_board(self.sample_board)

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
        
        clear_btn = tk.Button(btn_frame, text="Làm lại", font=("Helvetica", 12), bg="#F44336", fg="white", command=lambda: self.load_board(self.sample_board))
        clear_btn.grid(row=0, column=1, padx=10)

    def limit_input(self, sv):
        value = sv.get()
        if len(value) > 1:
            sv.set(value[-1])
        if not value.isdigit() or value == "0":
            sv.set("")

    def load_board(self, board):
        """Tải dữ liệu từ mảng 2 chiều lên giao diện."""
        for r in range(9):
            for c in range(9):
                self.cells[r][c].config(state="normal")
                self.cells[r][c].delete(0, tk.END)
                
                if board[r][c] != 0:
                    self.cells[r][c].insert(0, str(board[r][c]))
                    self.cells[r][c].config(state="readonly", readonlybackground="#e0e0e0", fg="blue")
                else:
                    self.cells[r][c].config(fg="black", bg="white")

    def get_current_board(self):
        """Lấy trạng thái bảng hiện tại thành dạng mảng 2 chiều."""
        current_board = []
        for r in range(9):
            row = []
            for c in range(9):
                val = self.cells[r][c].get()
                if val == "":
                    row.append(0)
                else:
                    row.append(int(val))
            current_board.append(row)
        return current_board

    def is_valid(self, board):
        """Kiểm tra tính hợp lệ của toàn bộ bảng Sudoku (không được có số trùng trên hàng, cột, khối 3x3)."""
        def is_valid_group(group):
            nums = [n for n in group if n != 0]
            return len(nums) == len(set(nums))

        for i in range(9):
            if not is_valid_group(board[i]):
                return False
            col = [board[r][i] for r in range(9)]
            if not is_valid_group(col):
                return False

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                block = [board[i][j] for i in range(r, r + 3) for j in range(c, c + 3)]
                if not is_valid_group(block):
                    return False
        return True

    def check_sudoku(self):
        current_board = self.get_current_board()
        
        is_full = all(0 not in row for row in current_board)
        
        if not self.is_valid(current_board):
            messagebox.showerror("Lỗi", "Bảng Sudoku hiện tại KHÔNG hợp lệ. Hãy kiểm tra lại các hàng, cột và khối 3x3.")
        elif not is_full:
            messagebox.showwarning("Cảnh báo", "Bảng Sudoku hợp lệ, nhưng bạn chưa điền hết các ô trống!")
        else:
            messagebox.showinfo("Chúc mừng", "Bạn đã giải thành công Sudoku!")