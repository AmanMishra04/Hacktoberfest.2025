def get3largest(arr):
    fst = sec = thd = float('-inf')

    for x in arr:
        # If current element is greater than fst
        if x > fst:
            thd = sec
            sec = fst
            fst = x
        # If x is between fst and sec
        elif x > sec and x != fst:
            thd = sec
            sec = x
        # If x is between sec and thd
        elif x > thd and x != sec and x != fst:
            thd = x

    res = []
    if fst == float('-inf'):
        return res
    res.append(fst)
    if sec == float('-inf'):
        return res
    res.append(sec)
    if thd == float('-inf'):
        return res
    res.append(thd)

    return res


# Driver code
arr = [12, 13, 1, 10, 34, 1]
res = get3largest(arr)
print(" ".join(map(str, res)))
