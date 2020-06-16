import tkinter as tk
from tkinter import messagebox
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
        self.frame = tk.Frame(self.root, bg="RoyalBlue2")
        self.canvas = tk.Canvas(self.frame, width=self.width+1, height=self.height+1,
                                bd=0, highlightthickness=0)
        self.create_ui()
        self.create_bars()
        self.canvas.after(0, self.animate)
        self.root.mainloop()

    def create_ui(self):
        self.reset_button = tk.Button(self.frame, text="Reset", width=5,
                                      command=lambda: self.reset())
        self.play_button = tk.Button(self.frame, text="Play", width=5, command=lambda: self.play())
        self.drop_menu = tk.OptionMenu(self.frame, self.alg,
                                       "BubbleSort", "HeapSort", "MergeSort", "QuickSort")
        self.drop_menu.configure(highlightthickness=0)
        self.pause_button = tk.Button(self.frame, text="Pause", width=5, state="disabled",
                                      command=lambda: self.pause())
        self.label = tk.Label(self.root, text="Choose the sorting alogrithm", bg="RoyalBlue2")
        self.frame.pack()
        self.label.pack(pady=5)
        self.drop_menu.grid(row=0, column=1, pady=5)
        self.play_button.grid(row=0, column=5)
        self.pause_button.grid(row=0, column=6)
        self.reset_button.grid(row=0, column=7)
        self.canvas.grid(row=1, column=0, columnspan=9, padx=10)

    def create_bars(self):
        bar_width = self.width // self.bars
        x = 0
        y = self.height
        for i in range(self.bars):
            tg = chr(i + 65)
            self.canvas.create_rectangle(x, y, x + bar_width, random.randint(5, 45)*10,
                                         fill="DodgerBlue3", tag=tg)
            x += bar_width

    def animate(self):
        self.canvas.update()
        self.canvas.after(12, self.animate)

    def play(self):
        self.reset_button.configure(state="disabled")
        self.play_button.configure(state="disabled")
        self.drop_menu.configure(state="disabled")
        self.pause_button.configure(state="active")
        if self.alg.get() == "BubbleSort":
            self.label.configure(text="BubbleSorting...")
            self.bubble_sort([chr(c+65) for c in range(20)])
            self.pause_button.configure(state="disabled")
            self.label.configure(text="BubbleSorted! ;)")
        elif self.alg.get() == "HeapSort":
            self.label.configure(text="HeapSorting...")
            self.heap_sort([chr(c+65) for c in range(20)])
            self.pause_button.configure(state="disabled")
            self.label.configure(text="HeapSorted! ;)")
        elif self.alg.get() == "MergeSort":
            self.canvas.create_rectangle(0, 0, 20, 20, fill="CadetBlue1", tag="larray")
            self.canvas.create_rectangle(0, 20, 20, 40, fill="CadetBlue4", tag="rarray")
            self.canvas.create_text(25, 10, text="Left Array", anchor="w", tag="ltext")
            self.canvas.create_text(25, 30, text="Right Array", anchor="w", tag="rtext")
            self.label.configure(text="MergeSorting...")
            self.merge_sort([chr(c+65) for c in range(20)])
            self.pause_button.configure(state="disabled")
            self.label.configure(text="MergeSorted! ;)")
            self.canvas.delete('larray')
            self.canvas.delete('rarray')
            self.canvas.delete('ltext')
            self.canvas.delete('rtext')
        elif self.alg.get() == "QuickSort":
            self.canvas.create_rectangle(0, 0, 20, 20, fill="DodgerBlue4", tag="qspiv")
            self.canvas.create_text(25, 10, text="Pivot element", anchor="w", tag="txtpiv")
            self.label.configure(text="QuickSorting...")
            self.quick_sort([chr(c+65) for c in range(20)], 0, self.bars-1)
            self.pause_button.configure(state="disabled")
            self.label.configure(text="QuickSorted! ;)")
            self.canvas.delete('qspiv')
            self.canvas.delete('txtpiv')
        self.reset_button.configure(state="active")

    def reset(self):
        self.canvas.delete('all')
        self.create_bars()
        self.label.configure(text="Choose the sorting algorithm")
        self.play_button.configure(state="active")
        self.drop_menu.configure(state="active")

    def pause(self):
        messagebox.showinfo("Animation paused!", "Press \"OK\" to resume")

    def bubble_sort(self, arr):
        n = len(arr)
        self.canvas.create_text(250, 0, text="", anchor="n", tag="bs")
        for i in range(n-1):
            self.canvas.itemconfig(self.canvas.find_withtag("bs"), text="{}. iteration".format(i+1))
            for j in range(n-1):
                bheight1 = self.height - self.canvas.coords(self.canvas.find_withtag(arr[j]))[1]
                bheight2 = self.height - self.canvas.coords(self.canvas.find_withtag(arr[j+1]))[1]
                self.canvas.itemconfig(self.canvas.find_withtag(arr[j]), fill="DodgerBlue2")
                self.canvas.itemconfig(self.canvas.find_withtag(arr[j+1]), fill="DodgerBlue2")
                self.canvas.update()
                time.sleep(0.1)
                xdistance = (self.canvas.coords(self.canvas.find_withtag(arr[j+1]))[0]
                             - self.canvas.coords(self.canvas.find_withtag(arr[j]))[0])
                if bheight1 > bheight2:
                    self.canvas.itemconfig(self.canvas.find_withtag(arr[j]), fill="orange")
                    self.canvas.itemconfig(self.canvas.find_withtag(arr[j+1]), fill="orange")
                    for c in range(int(xdistance)):
                        self.canvas.move(self.canvas.find_withtag(arr[j]), 1, 0)
                        self.canvas.move(self.canvas.find_withtag(arr[j+1]), -1, 0)
                        time.sleep(0.01)
                        self.canvas.update()
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                self.canvas.itemconfig(self.canvas.find_withtag(arr[j]), fill="DodgerBlue3")
                self.canvas.itemconfig(self.canvas.find_withtag(arr[j+1]), fill="DodgerBlue3")
        self.canvas.delete('bs')

    def quick_sort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)

            self.quick_sort(arr, low, p-1)
            self.quick_sort(arr, p+1, high)

    def partition(self, arr, low, high):
        i = low - 1
        pivot = self.height - self.canvas.coords(self.canvas.find_withtag(arr[high]))[1]
        self.canvas.itemconfig(self.canvas.find_withtag(arr[high]), fill="DodgerBlue4")

        for j in range(low, high):
            bheight = self.height - self.canvas.coords(self.canvas.find_withtag(arr[j]))[1]
            if bheight <= pivot:
                i += 1
                xdistance = (self.canvas.coords(self.canvas.find_withtag(arr[i]))[0]
                             - self.canvas.coords(self.canvas.find_withtag(arr[j]))[0])

                self.canvas.itemconfig(self.canvas.find_withtag(arr[i]), fill="orange")
                self.canvas.itemconfig(self.canvas.find_withtag(arr[j]), fill="orange")
                for c in range(int(abs(xdistance))):
                    if xdistance > 0:
                        self.canvas.move(self.canvas.find_withtag(arr[j]), 1, 0)
                        self.canvas.move(self.canvas.find_withtag(arr[i]), -1, 0)
                        time.sleep(0.01)
                        self.canvas.update()
                    elif xdistance < 0:
                        self.canvas.move(self.canvas.find_withtag(arr[j]), -1, 0)
                        self.canvas.move(self.canvas.find_withtag(arr[i]), 1, 0)
                        time.sleep(0.01)
                        self.canvas.update()
                    else:
                        break
                self.canvas.itemconfig(self.canvas.find_withtag(arr[j]), fill="DodgerBlue3")
                self.canvas.itemconfig(self.canvas.find_withtag(arr[i]), fill="DodgerBlue3")
                arr[i], arr[j] = arr[j], arr[i]

        xdistance = (self.canvas.coords(self.canvas.find_withtag(arr[high]))[0]
                     - self.canvas.coords(self.canvas.find_withtag(arr[i+1]))[0])

        self.canvas.itemconfig(self.canvas.find_withtag(arr[high]), fill="orange")
        self.canvas.itemconfig(self.canvas.find_withtag(arr[i+1]), fill="orange")
        for c in range(int(abs(xdistance))):
            if xdistance > 0:
                self.canvas.move(self.canvas.find_withtag(arr[i+1]), 1, 0)
                self.canvas.move(self.canvas.find_withtag(arr[high]), -1, 0)
                time.sleep(0.01)
                self.canvas.update()
            elif xdistance < 0:
                self.canvas.move(self.canvas.find_withtag(arr[i+1]), -1, 0)
                self.canvas.move(self.canvas.find_withtag(arr[high]), 1, 0)
                time.sleep(0.01)
                self.canvas.update()
            else:
                break
        self.canvas.itemconfig(self.canvas.find_withtag(arr[i+1]), fill="DodgerBlue3")
        self.canvas.itemconfig(self.canvas.find_withtag(arr[high]), fill="DodgerBlue3")
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def heap_sort(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n-1, 0, -1):

            xdistance = (self.canvas.coords(self.canvas.find_withtag(arr[i]))[0]
                         - self.canvas.coords(self.canvas.find_withtag(arr[0]))[0])

            self.canvas.itemconfig(self.canvas.find_withtag(arr[0]), fill="orange")
            self.canvas.itemconfig(self.canvas.find_withtag(arr[i]), fill="orange")
            for c in range(int(abs(xdistance))):
                self.canvas.move(self.canvas.find_withtag(arr[0]), 1, 0)
                self.canvas.move(self.canvas.find_withtag(arr[i]), -1, 0)
                time.sleep(0.01)
                self.canvas.update()
            self.canvas.itemconfig(self.canvas.find_withtag(arr[i]), fill="DodgerBlue3")
            self.canvas.itemconfig(self.canvas.find_withtag(arr[0]), fill="DodgerBlue3")
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        bheighti = self.height - self.canvas.coords(self.canvas.find_withtag(arr[i]))[1]

        if left < n:
            bheightl = self.height - self.canvas.coords(self.canvas.find_withtag(arr[left]))[1]
            if bheighti < bheightl:
                largest = left

        bheightlrg = self.height - self.canvas.coords(self.canvas.find_withtag(arr[largest]))[1]
        if right < n:
            bheightr = self.height - self.canvas.coords(self.canvas.find_withtag(arr[right]))[1]
            if bheightlrg < bheightr:
                largest = right

        if largest != i:
            xdistance = (self.canvas.coords(self.canvas.find_withtag(arr[largest]))[0]
                         - self.canvas.coords(self.canvas.find_withtag(arr[i]))[0])

            self.canvas.itemconfig(self.canvas.find_withtag(arr[i]), fill="orange")
            self.canvas.itemconfig(self.canvas.find_withtag(arr[largest]), fill="orange")
            for c in range(int(abs(xdistance))):
                if xdistance > 0:
                    self.canvas.move(self.canvas.find_withtag(arr[i]), 1, 0)
                    self.canvas.move(self.canvas.find_withtag(arr[largest]), -1, 0)
                    time.sleep(0.01)
                    self.canvas.update()
                elif xdistance < 0:
                    self.canvas.move(self.canvas.find_withtag(arr[i]), -1, 0)
                    self.canvas.move(self.canvas.find_withtag(arr[largest]), 1, 0)
                    time.sleep(0.01)
                    self.canvas.update()
                else:
                    break
            self.canvas.itemconfig(self.canvas.find_withtag(arr[i]), fill="DodgerBlue3")
            self.canvas.itemconfig(self.canvas.find_withtag(arr[largest]), fill="DodgerBlue3")
            arr[i], arr[largest] = arr[largest], arr[i]

            self.heapify(arr, n, largest)

    def merge_sort(self, arr):
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
            dist = self.canvas.coords(self.canvas.find_withtag(L[0]))[0]
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
