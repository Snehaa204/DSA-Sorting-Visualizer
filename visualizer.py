import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# --- Generate random array ---
def generate_array(n=20):
    return [random.randint(1, 100) for _ in range(n)]

# --- Bubble Sort (with step tracking) ---
def bubble_sort_steps(arr):
    steps = []
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            steps.append(a.copy())
    return steps

# --- Animate Sorting ---
def visualize_sorting(arr):
    steps = bubble_sort_steps(arr)

    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, color="skyblue")

    def update(step):
        for rect, height in zip(bar_rects, steps[step]):
            rect.set_height(height)
        ax.set_title(f"Sorting Step: {step+1}/{len(steps)}")

    ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=200, repeat=False)
    plt.show()

# --- Main Code ---
if __name__ == "__main__":
    arr = generate_array(20)
    print("Generated Array:", arr)
    visualize_sorting(arr)
