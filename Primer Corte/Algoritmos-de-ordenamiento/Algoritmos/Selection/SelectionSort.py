def selection(array):
    n = len(array)
    for i in range(n):
        minium = i
        for j in range(i+1, n):
            if array[j] < array[minium]:
                minium = j
        if minium != i:
            array[i], array[minium] = array[minium], array[i]
    return array

def main():
    array = [4,1,3,8,5,7,2,6]
    print(selection(array))
main()