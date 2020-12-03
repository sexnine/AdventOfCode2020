list = []
target_num = 2020

with open("input.txt", "r") as f:
    for line in f:
        list.append(int(line.strip()))

for num in list:
    res = target_num - num
    if res in list:
        print("Found solution: " + str(res*num))
        break