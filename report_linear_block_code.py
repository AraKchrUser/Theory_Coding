import numpy as np
from math import log2, ceil
import pandas as pd

d = 3
W_i = 1
N = 16
n_u = ceil(log2(N))
n_k = ceil(log2((n_u + 1) + log2(n_u + 1)))
n = n_k + n_u
W_p = d - W_i
print('Число информационных разрядов ----> ', n_u, '\nЧисло контрольных разрядов ----> ', n_k)
print()

# ----

P = []
for i in range(2 ** n_k):
    P.append(list(map(int, f'{i:0{n_k}b}')))
P = list(filter(lambda x: sum(x) >= W_p, P))[:n_u]

#
# C = [[0] * n for _ in range(n_u)]
# # ---замена на numpy
# for i in range(n_u):
#     C[i][i] = 1
#     C[i][-n_k:] = P[i]

I = np.eye(n_u, dtype=int)
P = np.array(P, dtype=int)
# pprint(I)
# pprint(P)
C = np.concatenate([I, P], axis=1)
print('Образующая матрица: ---------> ')
print(pd.DataFrame(C, columns=[f'' for _ in range(n)]).to_csv(sep='\t', index=False))

H = np.concatenate([C[:, n_u:].T, np.eye(n_k, dtype=int)], axis=1)
print('Контрольная матрица ---------> ')
col_name_1 = [f'a{i + 1}' for i in range(n_u)]
col_name_2 = [f'p{i + 1}' for i in range(n_k)]
col_name_1.extend(col_name_2)
H_df = pd.DataFrame(H, index=None, columns=col_name_1)
print(H_df.to_csv(sep='\t', index=False))

c = np.array([1, 0, 0, 1])
linear_code = c.dot(C) % 2
print(f'\nЛинейный код для ----> ', end=' ')
print(''.join(list(map(str, map(int, list(c))))), end=' ---------> ')
print(''.join(list(map(str, map(int, list(linear_code)))))) # 110011111


correct_word = c.dot(C) % 2  # np.array(list(map(int, list(input()))))
correct_word[0] = 0
print('Искаженное слово ----> ', ''.join(list(map(str, map(int, correct_word)))))

# ------- print check system

# s = np.sum(C[:, -n_k:], axis=0)
p = correct_word[-n_k:]
lst = []
print('\nСистема проверок:')
for i in range(n_k):
    mask = H[i, :n_u]
    s = (np.sum(correct_word[:n_u][mask == 1]) + p[i]) % 2
    lst.append(s)
    print(' ⊕ '.join([H_df.columns[-n_k:][i]] + H_df.columns[:n_u][mask == 1].to_list()), end=' = ')
    print(' ⊕ '.join(list(map(str, map(int, [p[i]] + list(correct_word[:n_u][mask == 1]))))), ' = ', int(s))

print()
ind = np.array(lst)
print('Синдром ---->', ''.join(list(map(str, map(int, ind)))))
for i in range(H.shape[1]):
    if all(ind == H[:, i]):
        print('Инвертируемый разряд = ', i + 1)






# s = set()
# import itertools
#
# while len(s) < n_u:
#     for i in range(W_p):
#         l = [1] * (n_k - i)
#         l.extend([0] * i)
#         for j in itertools.permutations(l):
#             s.add(''.join([str(d) for d in j]))
# p = np.array([list(map(int, list(d))) for d in s])
# #pprint(p[:n_u-1, :].shape)
# C = np.concatenate([np.eye(n_u), p], axis=1)
# pprint(C.shape)
# c = np.array([1, 1, 0, 0])#([1, 1, 0, 0, 1])
# linear_code = c.dot(C) % 2
# print('linear_code', linear_code)
# H = np.concatenate([C[:, n_u:].T, np.eye(n_k)], axis=1)
# # ------
# linear_code[2] = 0 if linear_code[2] == 1 else 1
# correct_code = linear_code#([1, 1, 1, 0, 1, 0, 1, 1, 0])
# print('correct_code', correct_code)
# s = np.sum(C[:, n_u:], axis=0)
# #print(s)
# s1 = (correct_code[-n_k] + s[0]) % 2
# s2 = (correct_code[-n_k+1] + s[1]) % 2
# s3 = (correct_code[-n_k+2] + s[2]) % 2
#
# print('H\n', H)
# print(s1, s2, s3)
