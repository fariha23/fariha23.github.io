from bisect import bisect_left


def two_sum(lst, K):
    lst.sort()
    print(lst)

    for i in range(len(lst)):
        target = K - lst[i]

        j = binary_search(lst, target)
        print('j: ' + str(j))

        # Check that binary search found the target and that it's not in the same index
        # as i. If it is in the same index, we can check lst[i + 1] and lst[i - 1] to see
        #  if there's another number that's the same value as lst[i].
        if j == -1:
            continue
        elif j != i:
            return True
        elif j + 1 < len(lst) and lst[j + 1] == target:
            return True
        elif j - 1 >= 0 and lst[j - 1] == target:
            return True
    return False

def binary_search(lst, target):
    lo = 0
    hi = len(lst)
    ind = bisect_left(lst, target, lo, hi)
    print('ind:' + str(ind))

    if 0 <= ind < hi and lst[ind] == target:
        return ind
    return -1


nums=[10,15,3,7]
k=17

print(two_sum(nums,k))
