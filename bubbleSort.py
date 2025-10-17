import time

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


def load_dataset(filename):
    with open(filename, "r") as f:
        
        numbers = list(map(int, f.read().split()))
    return numbers


if __name__ == "__main__":
    dataset_file = "large_set1.txt"   
    arr = load_dataset(dataset_file)

    start_time = time.time()   
    bubbleSort(arr)
    end_time = time.time()     

    print(f"Sorted {dataset_file}:")
    print(arr[:100000], "...")  
    print(f"Execution time: {end_time - start_time:.6f} seconds")