#  选择排序算法
#  时间复杂度： O(n²)
#  表现稳定

a = [2, 3, 1, 4, 5]
temp = 0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
print (a)                     # [1,2,3,4,5]


for i in range(len(a)):
    minindex = i
    for j in range(i+1, len(a)):       # 正规选择排序
        if a[i] > a[j]:                # 选出最小的数，并交换之
            minindex = j
        temp = a[minindex]
        a[minindex] = a[i]
        a[i] = temp
print (a)                      # [1,2,3,4,5]
