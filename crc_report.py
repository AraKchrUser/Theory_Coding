def sum_mode_to(data_1, data_2):
    res = []
    for i in range(len(data_1)):
        res.append((data_1[i] + data_2[i]) % 2)
    return res


# написать функцию для полного деления многочленов
def div(word, key, n_u):

    #
    print('*--' * 20)
    print('\t'.join(list(word)), ' |__ ', key, ' __')

    for _ in range(n_u):
        d = sum_mode_to(list(map(int, list(word[word.find('1'):word.find('1') + n]))), list(map(int, list(key))))
        if len(d) != len(key):
            break
        s = list(word[:word.find('1')].replace('0', ' ')) + d + list(word[word.find('1') + n:])

        #
        print('\t'.join(list(' ' * (word.find('1')) + key)))

        word = ''.join(map(str, list(s)))

        #
        print('\t'.join(list(word)))

    # word ---> r
    return word.replace(' ', '0'), d

# #'1101110' #
key = '1011'
word = '1000110'
wrd = word
err = 1
n = len(key)
n_u = 4


w, d = div(word, key, n_u)

i = 0
word = wrd
d = list(map(int, w))
while sum(list(map(int, w))) > err:
    i += 1
    wrd = wrd[1:] + wrd[0]
    w, _ = div(wrd, key, n_u)
    print('iter -- > ', i)
print('\n\n\t', '\t'.join(list(wrd)))
print('⊕\t')
print('\t', '\t'.join(list(w.replace('0', ' '))))
r = sum_mode_to(list(map(int, wrd)), list(map(int, w)))
print('\t', '---' * (len(r) + 1))
print('\t', '\t'.join(list(map(str, r))))
print('\n|Final ------> ', r[-i:] + r[:-i])
print()
