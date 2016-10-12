#!/usr/bin/python

def enumeration(A):
    max_sum = float('-inf')
    start = end = float('-inf')

    for i in range(len(A)):
        for j in range(i, len(A)):
            current = 0
            for k in range(i, j + 1):
                current += A[k]
            if current > max_sum:
                max_sum = current
                start = i
                end = j + 1
    return(A[start:end], max_sum)

def betterEnumeration(A):
    max_sum = float('-inf')
    start = end = float('-inf')

    for i in range(len(A)):
        current = 0
        for j in range(i, len(A)):
            current += A[j]
            if current > max_sum:
                max_sum = current
                start = i
                end = j + 1
    return(A[start:end], max_sum)

def divideAndConquer(A):
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return(A[0:1], A[0])
    return divideAndConquerMain(A, 0, n - 1)

def divideAndConquerMain(A, start, end):
    if start == end:
        return(A, A[start])
    else:
        mid = (start + end) / 2
        left = divideAndConquerMain(A, start, mid)
        right = divideAndConquerMain(A, mid + 1, end)
        cross = crossingSubArray(A, start, end)

        if left[1] >= right[1] and left[1] >= cross[1]:
            return left
        elif right[1] >= left[1] and right[1] >= cross[1]:
            return right
        else:
            return cross

def crossingSubArray(A, start, end):
    left_sum = right_sum = float('-inf')
    max_sum = 0
    mid = (start + end) / 2
    left_idx = mid
    right_idx = mid + 1

    for i in range(mid, start -1 , -1):
        max_sum += A[i]
        if max_sum > left_sum:
            left_sum = max_sum
            left_idx = i
    max_sum = 0
    for i in range(mid + 1, end + 1):
        max_sum += A[i]
        if max_sum > right_sum:
            right_sum = max_sum
            right_idx = i + 1
    return(A[left_idx:right_idx], left_sum + right_sum)

def iterative(A):
    max_sum = float('-inf')
    suffix_sum = float('-inf')

    for i in range(len(A)):
        suffix_right = i
        if suffix_sum > 0:
            suffix_sum += A[i]
        else:
            suffix_left = i
            suffix_sum = A[i]
        if suffix_sum > max_sum:
            max_sum = suffix_sum
            max_left = suffix_left
            max_right = suffix_right + 1
    return(A[max_left:max_right], max_sum)

"""set_1 = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
set_2 = [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7, -2]
set_3 = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7, -8, 19]
set_4 = [31,-41, 59, 26, -53, 58, 97, -93, -23, 84]
set_5 = [3, 2, 1, 1, -8, 1, 1, 2, 3]
set_6 = [12, 99, 99, -99, -27, 0, 0, 0, -3, 10]
set_7 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
testSets = [set_1, set_2, set_3, set_4, set_5, set_6, set_7]

for i in range(len(testSets)):

    print("set_" + str(i + 1) + ": ")

    enumRes = enumeration(testSets[i])
    print(enumRes[0])
    print(enumRes[1])

    betRes = betterEnumeration(testSets[i])
    print(betRes[0])
    print(betRes[1])

    divRes = divideAndConquer(testSets[i])
    print(divRes[0])
    print(divRes[1])

    iterRes = iterative(testSets[i])
    print(iterRes[0])
    print(iterRes[1])"""
