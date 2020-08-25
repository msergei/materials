def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(list):
    if len(list) < 2:
        print('return mergesort', list)
        return list
    middle = len(list) // 2
    left = mergesort(list[:middle])
    print('left', left)
    right = mergesort(list[middle:])
    print('right', right)
    return merge(left, right)

if __name__ == '__main__':
    tr = [3, 8, 1, 45, 12, 78, 3, 6, 0, 1]
    print(mergesort(tr))