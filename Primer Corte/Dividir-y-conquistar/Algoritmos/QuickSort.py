def quick_sort(array, low, high):
    if low < high:
        part = partition(array, low, high)

        quick_sort(array, low, part - 1)
        quick_sort(array, part + 1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def main():
    array = [4,1,3,8,5,7,2,6]
    quick_sort(array, 0, len(array) - 1)
    print(array)
main()