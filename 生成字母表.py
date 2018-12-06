list_1 = [chr(i) for i in range(65,91)]
list_2 = [chr(i) for i in range(97,123)]

list_3 = list_1 + list_2

list_3 = ";".join(list_3)

with open("letter.txt","w+") as let:
    let.write(list_3)