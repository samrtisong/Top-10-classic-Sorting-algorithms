#  插入排序算法
#  时间复杂度： O(n²)
#

a = [2,3,1,4,5]

for i in range(1, len(a)):
	index = i
	curr = a[i]
	while curr < a[index-1]:
		a[index] = a[index-1]
		index= index-1
		if index-1 < 0:
			break
	a[index] = curr

print a
