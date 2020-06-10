import tkinter as tk
import random
import time


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Visualisation of Sorting algorithms by Ante Culo")
        self.root.configure(bg="RoyalBlue2")
        self.width = 500
        self.height = 500
        self.bars = 20
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.create_ui()
        self.create_bars()
        self.canvas.after(0, self.animate)
        self.root.mainloop()

    def create_ui(self):
        self.play_button = tk.Button(self.root, text="Play", command=lambda: self.bubble_sort())
        self.play_button.pack(pady=10)
        self.canvas.pack()

    def create_bars(self):
        # self.canvas.update()
        # print(self.canvas.winfo_width(), self.canvas.winfo_height())
        bar_width = self.width // self.bars
        x = 0
        y = self.height
        for i in range(self.bars):
            tg = chr(i + 65)
            self.canvas.create_rectangle(x, y, x + bar_width, random.randint(5, 45)*10, fill="blue", tag=tg)
            x += bar_width

    def animate(self):
        self.canvas.update()
        self.canvas.after(12, self.animate)

    def bubble_sort(self):
        n = self.bars
        for i in range(n-1):
            for j in range(n-i-1):
                tg1 = chr(j + 65)
                tg2 = chr(j + 1 + 65)
                bheight1 = self.height - self.canvas.coords(self.canvas.find_withtag(tg1))[1]
                bheight2 = self.height - self.canvas.coords(self.canvas.find_withtag(tg2))[1]
                xdistance = self.canvas.coords(self.canvas.find_withtag(tg2))[0] - self.canvas.coords(self.canvas.find_withtag(tg1))[0]
                if bheight1 > bheight2:
                    self.canvas.itemconfig(self.canvas.find_withtag(tg1), fill="orange")
                    self.canvas.itemconfig(self.canvas.find_withtag(tg2), fill="orange")
                    for c in range(int(xdistance)):
                        self.canvas.move(self.canvas.find_withtag(tg1), 1, 0)
                        self.canvas.move(self.canvas.find_withtag(tg2), -1, 0)
                        time.sleep(0.05)
                        self.canvas.update()
                    self.canvas.itemconfig(self.canvas.find_withtag(tg1), fill="blue", tag="tag1")
                    self.canvas.itemconfig(self.canvas.find_withtag(tg2), fill="blue", tag="tag2")

                    self.canvas.itemconfig(self.canvas.find_withtag("tag1"), tag=tg2)
                    self.canvas.itemconfig(self.canvas.find_withtag("tag2"), tag=tg1)
        print("done")


if __name__ == '__main__':
    App()
