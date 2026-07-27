def insertion(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i
        while j > 0 and array[j - 1] > key:
            array[j] = array[j - 1]
            j -= 1
        array[j] = key
    return array

def main():
    array = [4,1,3,8,5,7,2,6]
    print(insertion(array))
main()
