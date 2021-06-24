from collections import Counter
import configparser
import logging
import re
day=configparser.ConfigParser()
PATH='basicconfig'
day.read(PATH)
PATH1=day.get('bhava','abc')
print(PATH1)
PATH2=day.get('bhava','ghi')
print(PATH2)
logging.basicConfig(filename="test.log",level=logging.INFO)
class Filehandling():
    def __init__(self,filename,outputfile):
        self.filename = filename
        self.outputfile = outputfile


    def readfile(self):
        file=open(self.filename,'r')      #pylint: disable=consider-using-with
        reads=file.read().split()
        return reads

    def writefile(self):
        writes = open(self.outputfile,'w')        #pylint: disable=consider-using-with
        return writes

class Subclass(Filehandling):
    def prefix(self):
        count=0
        final = Filehandling.readfile(self)
        for i in final:
            if i[-3]=='i' and i[-2]=='n' and i[-1]=='g':
                count+=1
        self.printstmt("The number of words ending with 'ing' is",count)
        return count
    def suffix(self):
        counts=0
        final = Filehandling.readfile(self)
        for j in final:
            if j[0]=='T' and j[1]=='o':
                counts+=1
        self.printstmt("The number of words starting with 'To' is",counts)
        return counts

    def max_num(self):
        char = ''
        number = 0
        final = Filehandling.readfile(self)
        counts = Counter(final)
        self.printstmt('',counts)
        for k in final:
            if counts[k] > number:
                number = counts[k]
                char = k
        self.printstmt('Maximum char is', char)
        return char


    def palindrome(self):
        final = Filehandling.readfile(self)
        for length in final:
            if length == length[::-1]:
                self.printstmt('The palindrome is', length)
                return length

    def uniquename(self):
        arr=[]
        final = Filehandling.readfile(self)
        for k in final:
            arr.append(k)
            self.printstmt('',arr)
            arr.pop(0)
            return arr

    def dictionary(self):
        dic={}
        key=0
        final = Filehandling.readfile(self)
        for line in final:
            dic[key]=line
            key+=1
        self.printstmt('',dic)
        return dic

    def vowels(self):
        out = ''
        array = []
        final = Filehandling.readfile(self)
        for word in final:
            res = re.split('a|e|i|o|u', word)
            self.printstmt('',res)
            for var in res:
                out = out + var

            array.append(out)
            out = ''
        self.printstmt('',array)

        #result = open("output.txt", "a")
        output = Filehandling.writefile(self)

        for upper in final:
            if len(upper) > 3:

                output.write(upper[:2] + upper[2].swapcase() + upper[3:])

            if len(upper) > 5:
                output.write(upper[:4] + upper[4].swapcase() + upper[5:])
            if upper.isalnum():
                output.write(upper[::-1] + ';')

    def printstmt(self,string,msg):                         #pylint: disable=no-self-use
        print(string,msg)
        logging.info('{} {}'.format(string,msg))            #pylint: disable=logging-format-interpolation

ab = Subclass(PATH1,PATH2)
ab.prefix()
ab.suffix()
ab.max_num()
ab.palindrome()
ab.uniquename()
ab.dictionary()
ab.vowels()
