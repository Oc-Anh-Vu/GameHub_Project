import tkinter as tk
from tkinter import messagebox

class CaroGame:
    def __init__(self, master):
        self.master = master
        self.board_size = 10
        self.current_player = "X"
        self.board = [["" for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]
        
        self.setup_ui()

    def setup_ui(self):
        self.turn_label = tk.Label(self.master, text="Cờ Caro - Lượt của: X", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.turn_label.pack(pady=(20, 10))
        
        grid_frame = tk.Frame(self.master, bg="#333333", bd=2)
        grid_frame.pack()
        
        for r in range(self.board_size):
            for c in range(self.board_size):
                btn = tk.Button(grid_frame, text="", font=("Helvetica", 14, "bold"), width=3, height=1,
                                bg="white", relief="ridge",
                                command=lambda r=r, c=c: self.on_click(r, c))
                btn.grid(row=r, column=c, padx=1, pady=1)
                self.buttons[r][c] = btn

        reset_btn = tk.Button(self.master, text="Chơi Lại", font=("Helvetica", 12), 
                              bg="#4CAF50", fg="white", command=self.reset_game)
        reset_btn.pack(pady=20)

    def on_click(self, r, c):
        if self.board[r][c] != "":
            return
        
        self.board[r][c] = self.current_player
        color = "#2196F3" if self.current_player == "X" else "#F44336"
        self.buttons[r][c].config(text=self.current_player, fg=color)
        
        if self.check_win(r, c):
            messagebox.showinfo("Chiến thắng!", f"Người chơi {self.current_player} đã giành chiến thắng!")
            self.reset_game()
            return
            
        self.current_player = "O" if self.current_player == "X" else "X"
        self.turn_label.config(text=f"Cờ Caro - Lượt của: {self.current_player}")

    def check_win(self, r, c):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 1
            i, j = r + dr, c + dc
            while 0 <= i < self.board_size and 0 <= j < self.board_size and self.board[i][j] == self.current_player:
                count += 1
                i += dr
                j += dc
            i, j = r - dr, c - dc
            while 0 <= i < self.board_size and 0 <= j < self.board_size and self.board[i][j] == self.current_player:
                count += 1
                i -= dr
                j -= dc
            if count >= 5:
                return True
        return False

    def reset_game(self):
        """Xóa trắng frame hiện tại và load lại màn chơi"""
        for widget in self.master.winfo_children():
            widget.destroy()
        self.__init__(self.master)