def car():
    f = open("car.txt","r")
    text = f.read().split()
    FileNew = open("carnew.txt","w")
    print(text)
    list=[]
    for i in text:
        if i not in list:
            list.append(i)
    list.sort(key=len)
    print(list)

    for j in list:
        FileNew.write(j + ":" +str(len(j)) + "\n")
car()







