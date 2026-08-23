import tkinter as tk
import os
from caro import CaroGame

class GameHub:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Game Hub")
        self.root.geometry("800x600")
        
        self.center_window(800, 600)
        
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(expand=True, fill="both")
        
        self.create_menu()
        self.show_welcome_screen()

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        game_menu = tk.Menu(menubar, tearoff=0)
        game_menu.add_command(label="Cờ Caro (Gomoku)", command=lambda: self.load_game(CaroGame))
        game_menu.add_command(label="Sudoku", command=lambda: self.show_placeholder("Sudoku"))
        game_menu.add_command(label="Dò mìn (Minesweeper)", command=lambda: self.show_placeholder("Dò Mìn"))
        game_menu.add_command(label="Cờ Othello", command=lambda: self.show_placeholder("Cờ Othello"))
        game_menu.add_separator()
        game_menu.add_command(label="Thoát", command=self.root.quit)
        
        menubar.add_cascade(label="Chọn Game", menu=game_menu)
        self.root.config(menu=menubar)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_frame()
        title = tk.Label(self.main_frame, text="Chào mừng đến với\nPython Game Hub", 
                         font=("Helvetica", 24, "bold"), bg="#f0f0f0", fg="#333333")
        title.pack(expand=True, pady=(150, 20))
        
        subtitle = tk.Label(self.main_frame, text="Vui lòng chọn một trò chơi từ thanh Menu phía trên.", 
                            font=("Helvetica", 14), bg="#f0f0f0", fg="#666666")
        subtitle.pack(expand=True, pady=(0, 200))

    def show_placeholder(self, game_name):
        self.clear_frame()
        label = tk.Label(self.main_frame, text=f"{game_name}\n(Chưa tích hợp)", 
                         font=("Helvetica", 20, "bold"), bg="#f0f0f0", fg="#cc0000")
        label.pack(expand=True)

    def load_game(self, GameClass):
        """Hàm chính để nạp một class Game vào Frame"""
        self.clear_frame()
        GameClass(self.main_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = GameHub(root)
    root.mainloop()