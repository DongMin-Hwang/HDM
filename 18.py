# data = list(map(int,input().split()))

# print(int(sum(data)/3))

user_input = input()
l = user_input.split(' ')
chanagel = []
for i in l :
    chanagel.append(int(i))
print(sum(chanagel)//3)