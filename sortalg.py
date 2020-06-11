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
        self.bs_button = tk.Button(self.root, text="BubbleSort", command=lambda: self.bubble_sort())
        self.qs_button = tk.Button(self.root, text="QucikSort", command=lambda: self.quick_sort(chr(0+65), chr(self.bars - 1 + 65)))
        self.reset_button = tk.Button(self.root, text="Reset", command=lambda: self.reset())
        self.label = tk.Label(self.root, text="Sort", bg="RoyalBlue2")
        self.bs_button.grid(row=0, column=0)
        self.qs_button.grid(row=0, column=1, pady=10)
        self.reset_button.grid(row=0, column=2)
        self.canvas.grid(row=1, column=0, columnspan=3, padx=10)
        self.label.grid(row=2, column=1, pady=5)

    def create_bars(self):
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

    def reset(self):
        self.canvas.delete('all')
        self.create_bars()

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
                        time.sleep(0.01)  # 0.05
                        self.canvas.update()
                    self.canvas.itemconfig(self.canvas.find_withtag(tg1), fill="blue", tag="tag1")
                    self.canvas.itemconfig(self.canvas.find_withtag(tg2), fill="blue", tag="tag2")

                    self.canvas.itemconfig(self.canvas.find_withtag("tag1"), tag=tg2)
                    self.canvas.itemconfig(self.canvas.find_withtag("tag2"), tag=tg1)
        print("done")

    def quick_sort(self, low, high):
        if low < high:
            p = self.partition(low, high)

            self.quick_sort(low, chr(ord(p)-1))
            self.quick_sort(chr(ord(p)+1), high)

    def partition(self, low, high):
        i = chr(ord(low) - 1)
        pivot = self.height - self.canvas.coords(self.canvas.find_withtag(high))[1]

        for j in range(ord(low) - 65, ord(high) - 65):
            tg = chr(j + 65)
            bheight = self.height - self.canvas.coords(self.canvas.find_withtag(tg))[1]
            if bheight <= pivot:
                i = chr(ord(i) + 1)
                xdistance = self.canvas.coords(self.canvas.find_withtag(i))[0] - self.canvas.coords(self.canvas.find_withtag(tg))[0]
                self.canvas.itemconfig(self.canvas.find_withtag(i), fill="orange")
                self.canvas.itemconfig(self.canvas.find_withtag(tg), fill="orange")
                for c in range(int(abs(xdistance))):
                    if xdistance > 0:
                        self.canvas.move(self.canvas.find_withtag(tg), 1, 0)
                        self.canvas.move(self.canvas.find_withtag(i), -1, 0)
                        time.sleep(0.005)
                        self.canvas.update()
                    elif xdistance < 0:
                        self.canvas.move(self.canvas.find_withtag(tg), -1, 0)
                        self.canvas.move(self.canvas.find_withtag(i), 1, 0)
                        time.sleep(0.005)
                        self.canvas.update()
                    else:
                        break
                self.canvas.itemconfig(self.canvas.find_withtag(tg), fill="blue", tag="tag1")
                self.canvas.itemconfig(self.canvas.find_withtag(i), fill="blue", tag="tag2")

                self.canvas.itemconfig(self.canvas.find_withtag("tag1"), tag=i)
                self.canvas.itemconfig(self.canvas.find_withtag("tag2"), tag=tg)

        newtg = chr(ord(i) + 1)
        xdistance = self.canvas.coords(self.canvas.find_withtag(high))[0] - self.canvas.coords(self.canvas.find_withtag(newtg))[0]
        self.canvas.itemconfig(self.canvas.find_withtag(high), fill="orange")
        self.canvas.itemconfig(self.canvas.find_withtag(newtg), fill="orange")
        for c in range(int(abs(xdistance))):
            if xdistance > 0:
                self.canvas.move(self.canvas.find_withtag(newtg), 1, 0)
                self.canvas.move(self.canvas.find_withtag(high), -1, 0)
                time.sleep(0.005)
                self.canvas.update()
            elif xdistance < 0:
                self.canvas.move(self.canvas.find_withtag(newtg), -1, 0)
                self.canvas.move(self.canvas.find_withtag(high), 1, 0)
                time.sleep(0.005)
                self.canvas.update()
            else:
                break
        self.canvas.itemconfig(self.canvas.find_withtag(newtg), fill="blue", tag="tag1")
        self.canvas.itemconfig(self.canvas.find_withtag(high), fill="blue", tag="tag2")

        self.canvas.itemconfig(self.canvas.find_withtag("tag1"), tag=high)
        self.canvas.itemconfig(self.canvas.find_withtag("tag2"), tag=newtg)
        return chr(ord(i) + 1)


if __name__ == '__main__':
    App()
