def median3(a, b, c):
    arr = sorted([a, b, c, 5])
    length = len(arr)
    if length % 2:
        return arr[int((length-1)/2)]
    return None


if __name__ == '__main__':
    median = median3(5, 1, 3)
    print(median)