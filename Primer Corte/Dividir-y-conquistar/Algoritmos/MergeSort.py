def merge(array):
    if len(array) == 1:
        return array
    half = len(array) // 2
    left = array[:half]
    right = array[half:]

    sorted_left = merge(left)
    sorted_right = merge(right)

    return merge_sort(sorted_left, sorted_right)

def merge_sort(left, right):
    array_sort = []
    while len(left) > 0 and len(right):
        if left[0] > right[0]:
            array_sort.append(right[0])
            right.pop(0)
        else:
            array_sort.append(left[0])
            left.pop(0)

    while len(left) > 0:
        array_sort.append(left[0])
        left.pop(0)
    while len(right) > 0:
        array_sort.append(right[0])
        right.pop(0)

    return array_sort

def main():
    array = [4,1,3,8,5,7,2,6]
    print(merge(array))
main()
