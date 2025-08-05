A = [[90, 35, 20],[40, 55, 85],[10, 65, 90]]
B=[[95,60,35],[20,55,40],[30,25,15]]
result=[[0,0,0],[0,0,0],[0,0,0]]

# Add matrices
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]+B[i][j]

# Print result
for row in result:
    print(row)
