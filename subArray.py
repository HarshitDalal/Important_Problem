# Sub Array Using Recursion in Python
def subArray(arr,n):
    sub = []
    for i in range(n):
        for j in range(i+1,n+1):
            sub.append(arr[i:j])
    return sub
    
'''--------------------------------------------------------------------------------------------- '''

# Sub Array Using For loop in Python
def subArrayRecursiv(arr):
    if not arr:
        return []
    return [arr[i:] for i in range(len(arr))] + subArrayRecursiv(arr[:-1])


if __name__ == "__main__":
    arr = [1,2,3]
    n = len(arr)

    l = sorted(subArray(arr,n))
    print(l)
    # [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]

    r = sorted(subArrayRecursiv(arr))
    print(r)
    # [[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]