list = ["qwe", "asd", "zxc", "qwe","asdasd"]
string = input("введите строку:")
index1 = list.index(string) #выведет 0 если нашлось
count = 0
i=0
flag = True
while i < len(list) and flag:
    if string == list[i]:
        count += 1
        if count == 2:
            flag = False
            print(i)
    i += 1
if flag:
    print(-1)