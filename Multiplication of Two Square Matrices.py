a=int(input("dimension: "))
matrix_1 =[]
matrix_2 = []
print("first matrix:")
for i in range(a):
	row= list(map(int,input().split()))
	matrix_1.append(row)
print("second matrix:")
for i in range(a):
	row_2= list(map(int,input().split()))
	matrix_2.append(row_2)
result = []
for i in range(a):
	row=[]
	for j in range(a):
		row.append(0)
	result.append(row)
for i in range(a):
	for j in range(a):
		for k in range(a):
			result[i][j] += matrix_1[i][k] * matrix_2[k][j]
print("Resultant Matrix:")
for i in range(a):
	print(" ".join(map(str,result[i])))
