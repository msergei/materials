def crypt(offset, message):
    # Set dictionary of algotithm
    dictionary = ' abcdefghijklmnopqrstuvwxyz'

    # We can set offset to original task work
    # print('Please, input offset:')
    # offset = int(input())
    # print('Offset is:', offset)
    #
    # print('Input message:')
    # message = input()
    # print('Message is:', message)

    answer = []
    # For iteration at 0
    limit = len(dictionary)
    correct_offset = offset%limit
    for letter in message:
        pos = dictionary.find(letter)
        if pos == -1:
            return -1
        new_pos = (pos+offset)%limit
        answer.append(dictionary[new_pos])

    return ''.join(answer)

if __name__ == '__main__':
    result = crypt(-4, 'az')
    print('Result: "{}"'.format(result))
