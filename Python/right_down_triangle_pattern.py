def downTrianglePattern(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    a = int(input("Enter number of rows to print : "))
    downTrianglePattern(a)