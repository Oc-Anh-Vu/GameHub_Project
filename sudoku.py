import tkinter as tk
from tkinter import messagebox
import random

class SudokuGame:
    def __init__(self, master):
        self.master = master
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.setup_ui()
        
        self.start_new_game(holes=45)

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
        
        new_game_btn = tk.Button(btn_frame, text="Tạo đề mới", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=lambda: self.start_new_game(45))
        new_game_btn.grid(row=0, column=1, padx=10)
        
        clear_btn = tk.Button(btn_frame, text="Xóa bảng", font=("Helvetica", 12), bg="#F44336", fg="white", command=self.clear_user_inputs)
        clear_btn.grid(row=0, column=2, padx=10)

    def limit_input(self, sv):
        value = sv.get()
        if len(value) > 1:
            sv.set(value[-1])
        if not value.isdigit() or value == "0":
            sv.set("")

    # ==========================================
    # LOGIC TẠO ĐỀ SUDOKU
    # ==========================================
    def start_new_game(self, holes):
        """Khởi tạo toàn bộ quy trình tạo đề mới"""
        board = [[0 for _ in range(9)] for _ in range(9)]
        self.fill_board(board)
        self.remove_cells(board, holes)
        
        self.current_puzzle = [row[:] for row in board]
        self.load_board(board)

    def fill_board(self, board):
        """Thuật toán Backtracking để sinh bảng kín hợp lệ"""
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)
                    for num in nums:
                        if self.is_safe(board, r, c, num):
                            board[r][c] = num
                            if self.fill_board(board):
                                return True
                            board[r][c] = 0
                    return False
        return True

    def is_safe(self, board, row, col, num):
        """Kiểm tra xem đặt 'num' vào vị trí (row, col) có hợp lệ không"""
        if num in board[row]:
            return False
        if num in [board[r][col] for r in range(9)]:
            return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def remove_cells(self, board, holes):
        """Xóa ngẫu nhiên 'holes' ô trên bảng để tạo thành câu đố"""
        count = holes
        while count > 0:
            r = random.randint(0, 8)
            c = random.randint(0, 8)
            if board[r][c] != 0:
                board[r][c] = 0
                count -= 1

    # ==========================================
    # LOGIC HIỂN THỊ VÀ KIỂM TRA
    # ==========================================
    def load_board(self, board):
        for r in range(9):
            for c in range(9):
                self.cells[r][c].config(state="normal")
                self.cells[r][c].delete(0, tk.END)
                
                if board[r][c] != 0:
                    self.cells[r][c].insert(0, str(board[r][c]))
                    self.cells[r][c].config(state="readonly", readonlybackground="#e0e0e0", fg="blue")
                else:
                    self.cells[r][c].config(fg="black", bg="white")

    def clear_user_inputs(self):
        """Chỉ xóa các ô người chơi nhập, giữ nguyên đề bài"""
        self.load_board(self.current_puzzle)

    def get_current_board(self):
        current_board = []
        for r in range(9):
            row = []
            for c in range(9):
                val = self.cells[r][c].get()
                row.append(0 if val == "" else int(val))
            current_board.append(row)
        return current_board

    def is_valid_final(self, board):
        def is_valid_group(group):
            nums = [n for n in group if n != 0]
            return len(nums) == len(set(nums))

        for i in range(9):
            if not is_valid_group(board[i]) or not is_valid_group([board[r][i] for r in range(9)]):
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
        
        if not self.is_valid_final(current_board):
            messagebox.showerror("Lỗi", "Bảng Sudoku hiện tại KHÔNG hợp lệ. Hãy kiểm tra lại.")
        elif not is_full:
            messagebox.showwarning("Cảnh báo", "Bảng hợp lệ, nhưng bạn chưa điền hết các ô trống!")
        else:
            messagebox.showinfo("Chúc mừng", "Bạn đã giải thành công Sudoku!")