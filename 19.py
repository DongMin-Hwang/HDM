# c = input()
# d = c.split(' ')

# for i in d :
#     a = int(i[0])
#     b = int(i[1])


#     print(int(a**b))

# n = list(map(int, input().split()))

# print(n[0] ** n[1])


user_input = input()
l = user_input.split(' ')
changel = []
for i in l:
    changel.append(int(i))
print(changel[0]**changel[1])