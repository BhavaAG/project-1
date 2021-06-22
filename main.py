from collections import Counter
import re
def manipulate(f):
    file=open(f,'r')
    final=file.read().split()
    print(final)


    count=0
    for i in final:
        if(i[-3]=='i' and i[-2]=='n' and i[-1]=='g'):
            count+=1
    print("The number of words ending with 'ing' is",count)


    count=0
    for j in final:
        if(j[0]=='T' and j[1]=='o'):
            count+=1
    print("The number of words starting with 'To' is",count)



    char = ''
    number = 0
    counts = Counter(final)
    print(counts)
    for k in final:
        if(counts[k] > number):
            number = counts[k]
            char = k
        print('Maximum char is', char)



    for l in final:
        if (l == l[::-1]):
            print('The palindrome is', l)



    arr=[]
    for k in final:
        arr.append(k)
        print(arr)
        arr.pop(0)




    dict={}
    key=0
    for m in final:
        dict[key]=m
        key+=1
    print(dict)


    

    str = ''
    list = []
    for word in final:
        res = re.split('a|e|i|o|u', word)
        print(res)
        for b in res:
            str = str + b

        list.append(str)
        str = ''
    print(list)

    result = open("output.txt", "a")

    for upper in arr:
        if len(upper) > 3:

            result.write(upper[:2] + upper[2].swapcase() + upper[3:])

        else:
            continue

        if len(upper) > 5:
            result.write(upper[:4] + upper[4].swapcase() + upper[5:])

        if upper.isspace():
            result.write(upper.replace('-'))

        if upper.isalnum():
            result.write(upper[::-1] + ';')





manipulate('textfile.txt')