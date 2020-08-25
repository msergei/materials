def binary_search(array, item):
    print('We got', array, item)
    # Lets set min, max and mid
    min = 0
    max = len(array) - 1

    # Set interger middle
    def get_mid(low, high):
        return (low+high)//2
    mid = get_mid(min, max)

    i = 0
    while array[mid] != item:
        print('At', i, 'min', min, 'mid', mid, 'max', max)
        i += 1
        if mid == min == max:
            return False
        if item > array[mid]:
            min = mid + 1
        else:
            max = mid - 1

        mid = get_mid(min, max)

    print('We find item {} in array {} at position {} with {} iterations'.format(*map(lambda x: str(x), (item, array, mid, i))))
    return True

if __name__ == '__main__':
    test_array = [54, 12, 89, 34, 43, 76, 90, 4, 6]
    test_array.sort()
    print(binary_search(test_array, 34))
