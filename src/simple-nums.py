def simple_nums(array=(i for i in range(2, 110))):
    result = []
    for item in array:
        if item == 2:
            result.append(2)
            continue

        flag = True
        for elem in result:
            if item%elem == 0:
                flag *= False
                break
        if flag:
            result.append(item)
    return result

if __name__ == '__main__':
    r = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, ]
    new = simple_nums()
    print(new == r)

