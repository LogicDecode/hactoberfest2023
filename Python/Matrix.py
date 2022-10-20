R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
  

matrix = []
print("Enter the entries rowwise:")
  

for i in range(R):          # A for loop for row entries
    a =[]
    for j in range(C):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)
  

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()
