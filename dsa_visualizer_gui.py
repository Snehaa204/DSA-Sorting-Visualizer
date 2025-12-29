import tkinter as tk
from tkinter import ttk
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------------- ARRAY GENERATION ----------------------
def generate_array(size):
    return [random.randint(10, 100) for _ in range(size)]

# ---------------------- SORTING ALGORITHMS ----------------------
def bubble_sort(arr):
    steps = []
    colors = []
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            step_colors = ["skyblue"] * n
            step_colors[j] = "red"
            step_colors[j + 1] = "red"
            colors.append(step_colors)
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

            steps.append(arr.copy())
    return steps, colors


def insertion_sort(arr):
    steps = []
    colors = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]

            step_colors = ["skyblue"] * len(arr)
            step_colors[j] = "red"
            step_colors[j + 1] = "red"
            colors.append(step_colors)

            steps.append(arr.copy())
            j -= 1

        arr[j + 1] = key
        steps.append(arr.copy())
        colors.append(["skyblue"] * len(arr))

    return steps, colors


def selection_sort(arr):
    steps = []
    colors = []
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            step_colors = ["skyblue"] * n
            step_colors[min_idx] = "yellow"
            step_colors[j] = "red"
            colors.append(step_colors)
            steps.append(arr.copy())

            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())
        colors.append(["green"] * n)

    return steps, colors


def merge_sort(arr):
    steps = []
    colors = []

    def merge(left, right, full_arr, start_index):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            step_colors = ["skyblue"] * len(full_arr)
            for idx in range(start_index, start_index + len(left) + len(right)):
                step_colors[idx] = "red"
            colors.append(step_colors)

            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

            steps.append(full_arr.copy())

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def divide(lst, start_index, full_arr):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = divide(lst[:mid], start_index, full_arr)
        right = divide(lst[mid:], start_index + mid, full_arr)
        merged = merge(left, right, full_arr, start_index)

        for idx, val in enumerate(merged):
            full_arr[start_index + idx] = val
            steps.append(full_arr.copy())
            colors.append(["skyblue"] * len(full_arr))

        return merged

    divide(arr, 0, arr)
    return steps, colors


def quick_sort(arr):
    steps = []
    colors = []

    def partition(low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            step_colors = ["skyblue"] * len(arr)
            step_colors[j] = "red"
            step_colors[high] = "yellow"
            colors.append(step_colors)
            steps.append(arr.copy())

            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(arr.copy())
                colors.append(["skyblue"] * len(arr))

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append(arr.copy())
        colors.append(["green"] * len(arr))
        return i + 1

    def quick(low, high):
        if low < high:
            p = partition(low, high)
            quick(low, p - 1)
            quick(p + 1, high)

    quick(0, len(arr) - 1)
    return steps, colors

# ---------------------- VISUALIZATION ----------------------
def visualize(steps, colors):
    for i in range(len(steps)):
        ax.clear()
        ax.bar(range(len(steps[i])), steps[i], color=colors[i])
        ax.set_title(f"Step {i + 1} / {len(steps)}")
        canvas.draw()
        canvas.get_tk_widget().update()

        delay = 0.3 - (speed_slider.get() / 500)
        time.sleep(max(0.01, delay))

# ---------------------- START SORT ----------------------
def start_sort():
    algo = algo_dropdown.get()
    size = size_slider.get()

    arr = generate_array(size)

    info_label.config(text=f"Array generated with {size} values")

    if algo == "Bubble Sort":
        steps, colors = bubble_sort(arr)
        tc = "O(n²)"
    elif algo == "Insertion Sort":
        steps, colors = insertion_sort(arr)
        tc = "O(n²)"
    elif algo == "Selection Sort":
        steps, colors = selection_sort(arr)
        tc = "O(n²)"
    elif algo == "Merge Sort":
        steps, colors = merge_sort(arr)
        tc = "O(n log n)"
    else:
        steps, colors = quick_sort(arr)
        tc = "O(n log n)"

    complexity_label.config(text=f"Time Complexity: {tc}")
    visualize(steps, colors)

# ---------------------- UI ----------------------
root = tk.Tk()
root.title("Advanced Sorting Visualizer")
root.geometry("950x650")
root.config(bg="#f2f2f2")

title = tk.Label(root, text="🧠 Advanced Sorting Algorithm Visualizer",
                 font=("Arial", 22, "bold"), bg="#f2f2f2")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack()

tk.Label(frame, text="Algorithm:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=0)
algo_dropdown = ttk.Combobox(frame,
    values=["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Quick Sort"],
    state="readonly", width=20)
algo_dropdown.grid(row=0, column=1, padx=10)
algo_dropdown.set("Bubble Sort")

tk.Label(frame, text="Array Size:", font=("Arial", 12), bg="#f2f2f2").grid(row=1, column=0)
size_slider = tk.Scale(frame, from_=10, to=60, orient="horizontal", length=200)
size_slider.grid(row=1, column=1)
size_slider.set(25)

tk.Label(frame, text="Speed:", font=("Arial", 12), bg="#f2f2f2").grid(row=2, column=0)
speed_slider = tk.Scale(frame, from_=1, to=100, orient="horizontal", length=200)
speed_slider.grid(row=2, column=1)
speed_slider.set(50)

start_button = tk.Button(root, text="Start Sorting", font=("Arial", 14),
                         command=start_sort, bg="#4CAF50", fg="white")
start_button.pack(pady=10)

info_label = tk.Label(root, text="", font=("Arial", 12), bg="#f2f2f2")
info_label.pack()

complexity_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f2f2f2")
complexity_label.pack()

fig, ax = plt.subplots(figsize=(7, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()
