import random
import time

# --- Sorting Algorithms ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# --- Generate Datasets ---
def generate_dataset(size, filename):
    data = [random.randint(1, 1000000) for _ in range(size)]
    with open(filename, "w") as f:
        for num in data:
            f.write(str(num) + "\n")

# Example: generate small, medium, large datasets
generate_dataset(100, "small.txt")
generate_dataset(1000, "medium.txt")
generate_dataset(100000, "large.txt")

# --- Load Dataset from File ---
def load_dataset(filename):
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f]

# --- Timing Function ---
def time_algorithm(algorithm, data):
    arr = data.copy()  # avoid modifying original
    start = time.time()
    algorithm(arr)
    end = time.time()
    return end - start

# --- Run Experiments ---
for dataset_file in ["small.txt", "medium.txt", "large.txt"]:
    data = load_dataset(dataset_file)
    print(f"\nDataset: {dataset_file}, Size: {len(data)}")

    t_bubble = time_algorithm(bubble_sort, data)
    t_merge = time_algorithm(merge_sort, data)

    print(f"Bubble Sort: {t_bubble:.6f} sec")
    print(f"Merge Sort:  {t_merge:.6f} sec")