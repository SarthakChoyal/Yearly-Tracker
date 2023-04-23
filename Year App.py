import tkinter as tk
import time

class Clock(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.day_counter = tk.Label(self, text="", font=("Retro Computer", 18), bg="white")
        self.percentage_of_year = tk.Label(self, text="", font=("Retro Computer", 18), bg="white")

        self.day_counter.pack(fill="x", pady=10, padx=10)
        self.percentage_of_year.pack(fill="x", pady=10, padx=10)

        self.font_menu = tk.Menu(self, tearoff=0)
        self.font_menu.add_command(label="Retro Computer", command=lambda: self.set_font("Retro Computer"))
        self.font_menu.add_command(label="Arial", command=lambda: self.set_font("Arial"))
        self.font_menu.add_command(label="Times New Roman", command=lambda: self.set_font("Times New Roman"))

        self.color_menu = tk.Menu(self, tearoff=0)
        self.color_menu.add_command(label="Black", command=lambda: self.set_color("black"))
        self.color_menu.add_command(label="White", command=lambda: self.set_color("white"))
        self.color_menu.add_command(label="Red", command=lambda: self.set_color("red"))
        self.color_menu.add_command(label="Yellow", command=lambda: self.set_color("yellow"))
        self.color_menu.add_command(label="Green", command=lambda: self.set_color("green"))
        self.color_menu.add_command(label="Blue", command=lambda: self.set_color("blue"))
        self.color_menu.add_command(label="Cyan", command=lambda: self.set_color("cyan"))
        self.color_menu.add_command(label="Purple", command=lambda: self.set_color("purple"))

        self.bg_color_menu = tk.Menu(self, tearoff=0)
        self.bg_color_menu.add_command(label="White", command=lambda: self.set_background_color("white"))
        self.bg_color_menu.add_command(label="Black", command=lambda: self.set_background_color("black"))
        self.bg_color_menu.add_command(label="Blue", command=lambda: self.set_background_color("blue"))
        self.bg_color_menu.add_command(label="Yellow", command=lambda: self.set_background_color("yellow"))
        self.bg_color_menu.add_command(label="Red", command=lambda: self.set_background_color("red"))

        self.menu_bar = tk.Menu(self.master)
        self.menu_bar.add_cascade(label="Font", menu=self.font_menu)
        self.menu_bar.add_cascade(label="Color", menu=self.color_menu)
        self.menu_bar.add_cascade(label="Background Color", menu=self.bg_color_menu)
        self.master.config(menu=self.menu_bar)

        self.update_day_counter()
        self.update_percentage_of_year()

    def set_font(self, font_name):
        self.day_counter.config(font=(font_name, 18))
        self.percentage_of_year.config(font=(font_name, 18))

    def set_color(self, color):
        self.day_counter.config(fg=color)
        self.percentage_of_year.config(fg=color)

    def set_background_color(self, color):
        self.configure(bg=color)
        self.day_counter.config(bg=color)
        self.percentage_of_year.config(bg=color)

    def update_day_counter(self):
        now = time.localtime()
        self.day_counter.config(text=f"Day Count: {now.tm_yday}")

    def get_current_day(self):
        now = time.localtime()
        return now.tm_yday - 1

    def update_percentage_of_year(self):
        current_day = self.get_current_day()
        total_days_in_year = 365
        self.percentage_of_year.config(text=f"Year Completed: {round(current_day / total_days_in_year * 100, 1)}%")

    def update_labels(self):
        self.update_day_counter()
        self.update_percentage_of_year()

        self.after(1000, self.update_labels)

def main():
    root = tk.Tk()
    root.title("Yearly Tracker")
    clock = Clock(root)
    clock.pack(fill="both", expand=True)
    clock.update_labels()
    root.mainloop()

if __name__ == "__main__":
    main()