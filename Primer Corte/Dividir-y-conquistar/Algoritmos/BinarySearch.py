def binary_search(array, number):
    left = 0
    right = len(array) - 1
    while left <= right:
        half = (left + right) // 2
        if number == array[half]:
            return half
        elif number > array[half]:
            left = half + 1
        else:
            right = half - 1
    return -1

def main():
    array = [1,2,3,4,5,6,7,8]
    number = 7
    position = binary_search(array, number)
    print(f"the element {number} is in position {position}")
main()