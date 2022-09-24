# Sub Sequence Using For loop in Python
def combinations(iterable, r):
    pool = iterable
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield [pool[i] for i in indices]
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield [pool[i] for i in indices]

def subSequence(arr,n):
    sub = []
    for i in range(n+1):
        for j in combinations(arr,i):
            sub.append(j)
    return list(sub)

'''--------------------------------------------------------------------------------------------- '''

# Sub Sequence Using Recursion in Python
def subSequenceRecursiv(arr,sub,i,n):
    temp = []
    if i == n:
        return [sub]
    else:
        temp.extend(subSequenceRecursiv(arr,sub+[arr[i]], i+1,n))
        temp.extend(subSequenceRecursiv(arr, sub, i+1,n))
        return temp


if __name__ == "__main__":
    arr = [1,2,3]
    n = len(arr)

    l = sorted(subSequence(arr,n))
    print(l)
    # [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

    r = sorted(subSequenceRecursiv(arr,[],0,n))
    print(r)
    #  [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]