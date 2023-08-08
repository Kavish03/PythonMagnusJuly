N= input("Enter the N value:")
input_list=[]

for _ in range(int(N)):
    user_value =input("Enter the input")
    input_list.append(user_value)
for N in input_list:
    if int(N)%5==0:
        print(N)
