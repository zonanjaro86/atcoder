def is_ok(i, key){
    return True
}
def binary_search(key):
    ng = -1
    ok = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, key):
            ok = mid
        else:
            ng = mid
    return ok