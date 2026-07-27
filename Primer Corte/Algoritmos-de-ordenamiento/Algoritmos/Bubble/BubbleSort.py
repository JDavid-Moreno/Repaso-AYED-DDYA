
def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def main():
    array = [4,1,3,8,5,7,2,6]
    print(bubblesort(array))
main()

# Output: [1,2,3,4,5,6,7,8]