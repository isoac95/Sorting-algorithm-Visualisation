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
        self.alg = tk.StringVar()
        self.alg.set("BubbleSort")
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.create_ui()
        self.create_bars()
        self.canvas.after(0, self.animate)
        self.root.mainloop()

    def create_ui(self):
        self.reset_button = tk.Button(self.root, text="Reset", command=lambda: self.reset())
        self.play_button = tk.Button(self.root, text="Play", command=lambda: self.play())
        self.drop_menu = tk.OptionMenu(self.root, self.alg, "BubbleSort", "HeapSort", "MergeSort", "QuickSort")
        self.label = tk.Label(self.root, text="Choose the sorting alogrithm", bg="RoyalBlue2")
        self.drop_menu.grid(row=0, column=0, pady=10)
        self.play_button.grid(row=0, column=1)
        self.reset_button.grid(row=0, column=2)
        self.canvas.grid(row=1, column=0, columnspan=3, padx=10)
        self.label.grid(row=2, column=1, pady=5)

    def create_bars(self):
        bar_width = self.width // self.bars
        x = 0
        y = self.height
        for i in range(self.bars):
            tg = chr(i + 65)
            self.canvas.create_rectangle(x, y, x + bar_width, random.randint(5, 45)*10, fill="DodgerBlue3", tag=tg)
            x += bar_width

    def animate(self):
        self.canvas.update()
        self.canvas.after(12, self.animate)

    def play(self):
        self.reset_button.configure(state="disabled")
        self.play_button.configure(state="disabled")
        self.drop_menu.configure(state="disabled")
        if self.alg.get() == "BubbleSort":
            self.bubble_sort([chr(c+65) for c in range(20)])
            self.label.configure(text="BubbleSorted! ;)")
        elif self.alg.get() == "HeapSort":
            self.heap_sort()
            self.label.configure(text="HeapSorted! ;)")
        elif self.alg.get() == "MergeSort":
            self.canvas.create_rectangle(0, 0, 20, 20, fill="CadetBlue1", tag="larray")
            self.canvas.create_rectangle(0, 20, 20, 40, fill="CadetBlue4", tag="rarray")
            self.canvas.create_text(25, 10, text="Left Array", anchor="w", tag="ltext")
            self.canvas.create_text(25, 30, text="Right Array", anchor="w", tag="rtext")
            self.merge_sort([chr(c+65) for c in range(20)])
            self.label.configure(text="MergeSorted! ;)")
            self.canvas.delete('larray')
            self.canvas.delete('rarray')
            self.canvas.delete('ltext')
            self.canvas.delete('rtext')
        elif self.alg.get() == "QuickSort":
            self.quick_sort(chr(0+65), chr(self.bars - 1 + 65))
            self.label.configure(text="QuickSorted! ;)")
        self.reset_button.configure(state="active")

    def reset(self):
        self.canvas.delete('all')
        self.create_bars()
        self.label.configure(text="Choose the sorting algorithm")
        self.play_button.configure(state="active")
        self.drop_menu.configure(state="active")

    def bubble_sort(self, arr):
        self.label.configure(text="BubbleSorting...")
        n = len(arr)
        self.canvas.create_text(250, 0, text="", anchor="n", tag="bs")
        for i in range(n-1):
            self.canvas.itemconfig(self.canvas.find_withtag("bs"), text="{}. iteration".format(i+1))
            for j in range(n-1):
                tg1 = arr[j]
                tg2 = arr[j+1]
                bheight1 = self.height - self.canvas.coords(self.canvas.find_withtag(tg1))[1]
                bheight2 = self.height - self.canvas.coords(self.canvas.find_withtag(tg2))[1]
                self.canvas.itemconfig(self.canvas.find_withtag(tg1), fill="DodgerBlue2")
                self.canvas.itemconfig(self.canvas.find_withtag(tg2), fill="DodgerBlue2")
                self.canvas.update()
                time.sleep(0.1)
                xdistance = self.canvas.coords(self.canvas.find_withtag(tg2))[0] - self.canvas.coords(self.canvas.find_withtag(tg1))[0]
                if bheight1 > bheight2:
                    self.canvas.itemconfig(self.canvas.find_withtag(tg1), fill="orange")
                    self.canvas.itemconfig(self.canvas.find_withtag(tg2), fill="orange")
                    for c in range(int(xdistance)):
                        self.canvas.move(self.canvas.find_withtag(tg1), 1, 0)
                        self.canvas.move(self.canvas.find_withtag(tg2), -1, 0)
                        time.sleep(0.01)
                        self.canvas.update()
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                self.canvas.itemconfig(self.canvas.find_withtag(tg1), fill="DodgerBlue3")
                self.canvas.itemconfig(self.canvas.find_withtag(tg2), fill="DodgerBlue3")
        self.canvas.delete('bs')

    def quick_sort(self, low, high):
        self.label.configure(text="QuickSorting....pivot element has darker color")
        if low < high:
            p = self.partition(low, high)

            self.quick_sort(low, chr(ord(p)-1))
            self.quick_sort(chr(ord(p)+1), high)

    def partition(self, low, high):
        i = chr(ord(low) - 1)
        pivot = self.height - self.canvas.coords(self.canvas.find_withtag(high))[1]
        self.canvas.itemconfig(self.canvas.find_withtag(high), fill="DodgerBlue4")

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
                        time.sleep(0.01)
                        self.canvas.update()
                    elif xdistance < 0:
                        self.canvas.move(self.canvas.find_withtag(tg), -1, 0)
                        self.canvas.move(self.canvas.find_withtag(i), 1, 0)
                        time.sleep(0.01)
                        self.canvas.update()
                    else:
                        break
                self.canvas.itemconfig(self.canvas.find_withtag(tg), fill="DodgerBlue3", tag="tag1")
                self.canvas.itemconfig(self.canvas.find_withtag(i), fill="DodgerBlue3", tag="tag2")

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
                time.sleep(0.01)
                self.canvas.update()
            elif xdistance < 0:
                self.canvas.move(self.canvas.find_withtag(newtg), -1, 0)
                self.canvas.move(self.canvas.find_withtag(high), 1, 0)
                time.sleep(0.01)
                self.canvas.update()
            else:
                break
        self.canvas.itemconfig(self.canvas.find_withtag(newtg), fill="DodgerBlue3", tag="tag1")
        self.canvas.itemconfig(self.canvas.find_withtag(high), fill="DodgerBlue3", tag="tag2")

        self.canvas.itemconfig(self.canvas.find_withtag("tag1"), tag=high)
        self.canvas.itemconfig(self.canvas.find_withtag("tag2"), tag=newtg)
        return chr(ord(i) + 1)

    def heap_sort(self):
        self.label.configure(text="HeapSorting")
        n = self.bars
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(n, i)

        for i in range(n-1, 0, -1):
            tgz = chr(0 + 65)
            tgi = chr(i + 65)

            xdistance = self.canvas.coords(self.canvas.find_withtag(tgi))[0] - self.canvas.coords(self.canvas.find_withtag(tgz))[0]
            self.canvas.itemconfig(self.canvas.find_withtag(tgz), fill="orange")
            self.canvas.itemconfig(self.canvas.find_withtag(tgi), fill="orange")
            for c in range(int(abs(xdistance))):
                self.canvas.move(self.canvas.find_withtag(tgz), 1, 0)
                self.canvas.move(self.canvas.find_withtag(tgi), -1, 0)
                time.sleep(0.01)
                self.canvas.update()
            self.canvas.itemconfig(self.canvas.find_withtag(tgi), fill="DodgerBlue3", tag="tag1")
            self.canvas.itemconfig(self.canvas.find_withtag(tgz), fill="DodgerBlue3", tag="tag2")
            self.canvas.itemconfig(self.canvas.find_withtag("tag1"), tag=tgz)
            self.canvas.itemconfig(self.canvas.find_withtag("tag2"), tag=tgi)
            self.heapify(i, 0)

    def heapify(self, n, i):
        largest = chr(i + 65)
        left = 2 * i + 1
        right = 2 * i + 2
        tgl = chr(left + 65)
        tgr = chr(right + 65)
        tgi = chr(i + 65)
        bheighti = self.height - self.canvas.coords(self.canvas.find_withtag(tgi))[1]

        if left < n:
            bheightl = self.height - self.canvas.coords(self.canvas.find_withtag(tgl))[1]
            if bheighti < bheightl:
                largest = tgl

        bheightlrg = self.height - self.canvas.coords(self.canvas.find_withtag(largest))[1]
        if right < n:
            bheightr = self.height - self.canvas.coords(self.canvas.find_withtag(tgr))[1]
            if bheightlrg < bheightr:
                largest = tgr

        if largest != tgi:
            xdistance = self.canvas.coords(self.canvas.find_withtag(largest))[0] - self.canvas.coords(self.canvas.find_withtag(tgi))[0]
            self.canvas.itemconfig(self.canvas.find_withtag(tgi), fill="orange")
            self.canvas.itemconfig(self.canvas.find_withtag(largest), fill="orange")
            for c in range(int(abs(xdistance))):
                if xdistance > 0:
                    self.canvas.move(self.canvas.find_withtag(tgi), 1, 0)
                    self.canvas.move(self.canvas.find_withtag(largest), -1, 0)
                    time.sleep(0.01)
                    self.canvas.update()
                elif xdistance < 0:
                    self.canvas.move(self.canvas.find_withtag(tgi), -1, 0)
                    self.canvas.move(self.canvas.find_withtag(largest), 1, 0)
                    time.sleep(0.01)
                    self.canvas.update()
                else:
                    break
            self.canvas.itemconfig(self.canvas.find_withtag(tgi), fill="DodgerBlue3", tag="tag1")
            self.canvas.itemconfig(self.canvas.find_withtag(largest), fill="DodgerBlue3", tag="tag2")

            self.canvas.itemconfig(self.canvas.find_withtag("tag1"), tag=largest)
            self.canvas.itemconfig(self.canvas.find_withtag("tag2"), tag=tgi)

            self.heapify(n, ord(largest)-65)

    def merge_sort(self, arr):
        self.label.configure(text="MergeSorting...")
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            for item in L:
                self.canvas.itemconfig(self.canvas.find_withtag(item), fill="CadetBlue1")
            for item in R:
                self.canvas.itemconfig(self.canvas.find_withtag(item), fill="CadetBlue4")
            time.sleep(0.1)
            self.canvas.update()
            i = j = k = 0
            dist = xdistance = self.canvas.coords(self.canvas.find_withtag(L[0]))[0]
            while i < len(L) and j < len(R):
                bheightl = self.height - self.canvas.coords(self.canvas.find_withtag(L[i]))[1]
                bheightr = self.height - self.canvas.coords(self.canvas.find_withtag(R[j]))[1]
                if bheightl < bheightr:
                    arr[k] = L[i]
                    self.canvas.itemconfig(self.canvas.find_withtag(L[i]), fill="orange")
                    xdistance = self.canvas.coords(self.canvas.find_withtag(L[i]))[0] - dist
                    for c in range(int(abs(xdistance))):
                        if xdistance > 0:
                            self.canvas.move(self.canvas.find_withtag(L[i]), -1, 0)
                            time.sleep(0.01)
                            self.canvas.update()
                        elif xdistance < 0:
                            self.canvas.move(self.canvas.find_withtag(L[i]), 1, 0)
                            time.sleep(0.01)
                            self.canvas.update()
                        else:
                            break
                    self.canvas.itemconfig(self.canvas.find_withtag(L[i]), fill="CadetBlue1")
                    i += 1
                else:
                    arr[k] = R[j]
                    self.canvas.itemconfig(self.canvas.find_withtag(R[j]), fill="orange")
                    xdistance = self.canvas.coords(self.canvas.find_withtag(R[j]))[0] - dist
                    for c in range(int(abs(xdistance))):
                        if xdistance > 0:
                            self.canvas.move(self.canvas.find_withtag(R[j]), -1, 0)
                            time.sleep(0.01)
                            self.canvas.update()
                        elif xdistance < 0:
                            self.canvas.move(self.canvas.find_withtag(R[j]), 1, 0)
                            time.sleep(0.01)
                            self.canvas.update()
                        else:
                            break
                    self.canvas.itemconfig(self.canvas.find_withtag(R[j]), fill="CadetBlue4")
                    j += 1
                k += 1
                dist += 25

            while i < len(L):
                arr[k] = L[i]
                self.canvas.itemconfig(self.canvas.find_withtag(L[i]), fill="orange")
                xdistance = self.canvas.coords(self.canvas.find_withtag(L[i]))[0] - dist
                for c in range(int(abs(xdistance))):
                    if xdistance > 0:
                        self.canvas.move(self.canvas.find_withtag(L[i]), -1, 0)
                        time.sleep(0.01)
                        self.canvas.update()
                    elif xdistance < 0:
                        self.canvas.move(self.canvas.find_withtag(L[i]), 1, 0)
                        time.sleep(0.01)
                        self.canvas.update()
                    else:
                        break
                self.canvas.itemconfig(self.canvas.find_withtag(L[i]), fill="CadetBlue1")
                i += 1
                k += 1
                dist += 25

            while j < len(R):
                arr[k] = R[j]
                self.canvas.itemconfig(self.canvas.find_withtag(R[j]), fill="orange")
                xdistance = self.canvas.coords(self.canvas.find_withtag(R[j]))[0] - dist
                for c in range(int(abs(xdistance))):
                    if xdistance > 0:
                        self.canvas.move(self.canvas.find_withtag(R[j]), -1, 0)
                        time.sleep(0.01)
                        self.canvas.update()
                    elif xdistance < 0:
                        self.canvas.move(self.canvas.find_withtag(R[j]), 1, 0)
                        time.sleep(0.01)
                        self.canvas.update()
                    else:
                        break
                self.canvas.itemconfig(self.canvas.find_withtag(R[j]), fill="CadetBlue4")
                j += 1
                k += 1
                dist += 25
            for item in arr:
                self.canvas.itemconfig(self.canvas.find_withtag(item), fill="DodgerBlue3")


if __name__ == '__main__':
    App()
