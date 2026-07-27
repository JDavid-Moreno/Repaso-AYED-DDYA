def max_min(array, left, right):
    if left == right:
        return array[left], array[left]
    half = (left + right) // 2

    max_left, min_left = max_min(array, left, half)
    max_right, min_right = max_min(array, half + 1, right)

    if max_left > max_right:
        max = max_left
    else:
        max = max_right

    if min_left < min_right:
        min = min_left
    else:
        min = min_right

    return max, min

def main():
    array = [3,6,1,2,9,4,5,8,7]
    max, min = max_min(array, 0, len(array) - 1)
    print(max, min)
main()