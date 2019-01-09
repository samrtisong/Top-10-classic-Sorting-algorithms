
# 希尔排序算法  ## shell_sort #

def shell_sort(a):
    n = len(a)
    dk = n//2    # 整除
    while dk >= 1:
        shell_insert_sort(a, dk)
        dk = dk // 2
    return a

def shell_insert_sort(a, dk):
    n = len(a)
    for i in range(dk):
        for j in range(i+dk, n, dk):
            temp = a[j]
            k = j - dk
            while k >= i and a[k] > temp:
                a[k+dk] = a[k]
                k = k -dk
            a[k+dk] = temp
        # print(a)

a = [2,3,1,4,5,]
b = shell_sort(a)
print(b)
