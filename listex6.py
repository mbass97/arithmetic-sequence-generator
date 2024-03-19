n = int(input("enter an target integer:\t"))
d = int(input("enter a distance\t"))
my_list = [1]

value = 1
while(value < n) or (value == n):
    value += d
    if value > n:
        break
    my_list.append(value)

print(my_list)