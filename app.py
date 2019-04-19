def find_missing(arr):
    for item in range(1, len(arr)+2):
        if item not in arr:
            return item
    if isinstance(arr, list):
        return 0
    return 0


if '__main__' == __name__:
    arr = (5, 6, 4, 7, 2, 1, 9, 8)
    result = find_missing(arr)
    if result:
        print('Lost number {}'.format(result))
    else:
        raise Exception('An error occurred while executing')