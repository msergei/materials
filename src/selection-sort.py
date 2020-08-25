def selection_sort(array):
    sorted_array = []
    # For every index in array we search max element
    for i in range(len(array)):
        print('Iteration', i)
        max = 0
        for j in range(1, len(array)):
            if array[max] < array[j]:
                max = j
        sorted_array.append(array.pop(max))

    return sorted_array

if __name__ == '__main__':
    arr = [5, 6, 2, 7, 9, 1]
    print(selection_sort(arr))
