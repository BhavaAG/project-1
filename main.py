from collections import Counter
import configparser
day=configparser.ConfigParser()
path='basicconfig'
day.read(path)
path1=day.get('bhava','abc')
print(path1)
path2=day.get('bhava','def')
print(path2)
import logging
logging.basicConfig(filename="test.log",level=logging.INFO)
import re
class filehandling():
    def __init__(self,filename,outputfile):
        self.textfile = filename
        self.write = outputfile

    def readfile(self):
        file=open(path1,'r')
        reads=file.read().split()
        return reads

    def writefile(self):
        op = open(path,'a')
        return op

class subclass(filehandling):
    def prefix(self):
        count=0
        final = filehandling.readfile(self)
        for i in final:
            if(i[-3]=='i' and i[-2]=='n' and i[-1]=='g'):
                count+=1
        self.pr("The number of words ending with 'ing' is",count)
    def suffix(self):
        counts=0
        final = filehandling.readfile(self)
        for j in final:
            if(j[0]=='T' and j[1]=='o'):
                counts+=1
        self.pr("The number of words starting with 'To' is",counts)

    def max_num(self):
        char = ''
        number = 0
        final = filehandling.readfile(self)
        counts = Counter(final)
        self.pr('',counts)
        for k in final:
            if(counts[k] > number):
                number = counts[k]
                char = k
        self.pr('Maximum char is', char)


    def palindrome(self):
        final = filehandling.readfile(self)
        for l in final:
            if (l == l[::-1]):
                self.pr('The palindrome is', l)

    def uniquename(self):
        arr=[]
        final = filehandling.readfile(self)
        for k in final:
            arr.append(k)
            self.pr('',arr)
            arr.pop(0)

    def dictionary(self):
        dict={}
        key=0
        final = filehandling.readfile(self)
        for m in final:
            dict[key]=m
            key+=1
        self.pr('',dict)

    def vowels(self):
        str = ''
        list = []
        arr = ''
        final = filehandling.readfile(self)
        for word in final:
            res = re.split('a|e|i|o|u', word)
            self.pr('',res)
            for b in res:
                str = str + b

            list.append(str)
            str = ''
        self.pr('',list)

        result = open("output.txt", "a")
        wr = filehandling.writefile(self)

        for upper in list:
            if len(upper) > 3:

                wr.write(upper[:2] + upper[2].swapcase() + upper[3:])

            else:
                continue

            if len(upper) > 5:
                wr.write(upper[:4] + upper[4].swapcase() + upper[5:])

            if upper.isspace():
                wr.write(upper.replace('-'))

            if upper.isalnum():
                wr.write(upper[::-1] + ';')
    def pr(self,str,msg):
        print(str,msg)
        logging.info('{} {}'.format(str,msg))


ab = subclass('textfile.txt','output.txt')
ab.prefix()
ab.suffix()
ab.max_num()
ab.palindrome()
ab.uniquename()
ab.dictionary()
ab.vowels()





#anipulate('textfile.txt')

ob1 = filehandling('textfile.txt','output.txt')