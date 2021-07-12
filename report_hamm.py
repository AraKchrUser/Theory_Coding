def noOfParityBits(noOfBits):
    i = 0
    while 2. ** i <= noOfBits + i:
        i += 1
    return i


def appendParityBits(data):
    d = {}
    n = noOfParityBits(len(data))
    i = 0
    j = 0
    k = 0
    list1 = list()
    while i < n + len(data):
        if i == (2. ** j - 1):
            list1.insert(i, '0')
            j += 1
        else:
            list1.insert(i, data[k])
            k += 1
        i += 1
    return list1


def hammingCodes(data):
    n = noOfParityBits(len(data))
    list1 = appendParityBits(data)
    i = 0
    k = 1
    while i < n:
        pos = []
        k = 2. ** i
        j = 1
        total = 0
        while j * k - 1 < len(list1):
            if j * k - 1 == len(list1) - 1:
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]
            elif (j + 1) * k - 1 >= len(list1):
                lower_index = j * k - 1
                temp = list1[int(lower_index):len(list1)]
            elif (j + 1) * k - 1 < len(list1) - 1:
                lower_index = (j * k) - 1
                upper_index = (j + 1) * k - 1
                temp = list1[int(lower_index):int(upper_index)]

            total = total + sum(int(e) for e in temp)
            pos.extend(temp)

            j += 2
        if total % 2 > 0:
            list1[int(
                k) - 1] = '1'
        # print check system
        print(f'K{i + 1}{"+".join(pos)[1:]}->K{i + 1}={1 if total % 2 > 0 else 0}.')
        i += 1

    print('\n|------------------------------------------|')
    print('|позиция символов|------кодовое слово------|')
    print('|----------------|-------------|-----------|')
    j = 0
    for i, key in enumerate(list1):
        if (i + 1) & i == 0:
            j += 1
            k = f'K_{j}'
        else:
            k = f'_{key}_'
        print(f'|_______{i + 1}________|_____{k}_____|_____{key}_____|')
    print('|------------------------------------------|')

    return list1


code = '1100'
print('\ninput: '+code+'\n')
print('\ncode:'.upper() + ''.join(hammingCodes(code)))
