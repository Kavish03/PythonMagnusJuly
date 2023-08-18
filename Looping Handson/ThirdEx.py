rows= int(input("Enter the total number of rows:"))
columns= int(input("Enter the total number of columns:"))

print("Rectangle # patterns")

for i in range(rows):
    for j in range(columns):
        print('#',end=' ')
    print()    
