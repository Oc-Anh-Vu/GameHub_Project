import tkinter as tk
from tkinter import messagebox
import random

class MinesweeperGame:
    def __init__(self, master):
        self.master = master
        self.rows = 10
        self.cols = 10
        self.num_mines = 15
        
        self.buttons = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.mines = set()     
        self.flags = set()     
        self.revealed = set()  
        self.game_over = False
        
        self.setup_ui()
        self.start_new_game()

    def setup_ui(self):
        header_frame = tk.Frame(self.master, bg="#f0f0f0")
        header_frame.pack(pady=10)
        
        self.lbl_mines = tk.Label(header_frame, text=f"🚩 Mìn: {self.num_mines}", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
        self.lbl_mines.pack(side=tk.LEFT, padx=20)
        
        btn_reset = tk.Button(header_frame, text="Chơi lại", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=self.start_new_game)
        btn_reset.pack(side=tk.LEFT, padx=20)

        self.grid_frame = tk.Frame(self.master, bg="#999999", bd=2)
        self.grid_frame.pack()

        for r in range(self.rows):
            for c in range(self.cols):
                btn = tk.Button(self.grid_frame, width=3, height=1, font=("Helvetica", 12, "bold"), relief="raised", bg="#e0e0e0")
                
                btn.bind("<Button-1>", lambda e, r=r, c=c: self.on_left_click(r, c))
                btn.bind("<Button-3>", lambda e, r=r, c=c: self.on_right_click(r, c))
                
                btn.grid(row=r, column=c, padx=1, pady=1)
                self.buttons[r][c] = btn

    def start_new_game(self):
        """Reset trạng thái và tạo bàn mìn mới"""
        self.game_over = False
        self.mines.clear()
        self.flags.clear()
        self.revealed.clear()
        self.lbl_mines.config(text=f"🚩 Mìn: {self.num_mines}")
        
        for r in range(self.rows):
            for c in range(self.cols):
                self.buttons[r][c].config(text="", bg="#e0e0e0", relief="raised", state="normal")
        all_positions = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        self.mines = set(random.sample(all_positions, self.num_mines))

    def count_adjacent_mines(self, r, c):
        """Đếm số mìn xung quanh 1 ô (8 hướng)"""
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if (r + dr, c + dc) in self.mines:
                    count += 1
        return count

    def on_left_click(self, r, c):
        if self.game_over or (r, c) in self.flags or (r, c) in self.revealed:
            return
        
        if (r, c) in self.mines:
            self.trigger_game_over(r, c)
        else:
            self.reveal_cell(r, c)
            self.check_win()

    def on_right_click(self, r, c):
        if self.game_over or (r, c) in self.revealed:
            return
            
        if (r, c) in self.flags:
            self.flags.remove((r, c))
            self.buttons[r][c].config(text="")
        else:
            self.flags.add((r, c))
            self.buttons[r][c].config(text="🚩", fg="red")
            
        self.lbl_mines.config(text=f"🚩 Mìn: {self.num_mines - len(self.flags)}")

    def reveal_cell(self, r, c):
        """Thuật toán loang (Flood Fill) để mở ô"""
        if (r, c) in self.revealed or (r, c) in self.flags:
            return
        
        self.revealed.add((r, c))
        self.buttons[r][c].config(relief="sunken", bg="#ffffff", state="disabled")
        
        adj_mines = self.count_adjacent_mines(r, c)
        
        if adj_mines > 0:
            colors = {1: "blue", 2: "green", 3: "red", 4: "purple", 5: "maroon"}
            self.buttons[r][c].config(text=str(adj_mines), disabledforeground=colors.get(adj_mines, "black"))
        else:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        self.reveal_cell(nr, nc)

    def trigger_game_over(self, hit_r, hit_c):
        self.game_over = True
        for r, c in self.mines:
            if (r, c) == (hit_r, hit_c):
                self.buttons[r][c].config(text="💥", bg="red")
            else:
                self.buttons[r][c].config(text="💣", bg="#ffffff")
        messagebox.showerror("Game Over", "BÙMMM! Bạn đã đạp trúng mìn!")

    def check_win(self):
        if len(self.revealed) == (self.rows * self.cols) - self.num_mines:
            self.game_over = True
            messagebox.showinfo("Chiến thắng", "Chúc mừng! Bạn đã gỡ sạch mìn!")