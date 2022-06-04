import time
import random
import re
import pyautogui as pag
#from mofang import array2D

class char():

    #not sure why do I necessarily need two list, but I just do not want to change
    number = []
    character = []
    
    def __init__(self):

        #init list
        for i in range(0,52):
            self.number.append(i)
        for i in range(65,91):
            self.character.append(chr(i))
        for i in range(97,123):
            self.character.append(chr(i))

    def __str__(self):
        return "This is no longer the well-known ASCII code. Now, please call this --- PHHGS code!!!"
            
    def get_char(self):
        return self.character

    def set_char(self,string:str,loc:int):

        #add new char
        assert loc == len(self.character), ("Must add after the last character.")
        self.number.append(loc)
        self.character.append(string)
        return (loc, string)

    def reset(self):

        #get two list
        newNum = self.number[:]
        newChar = self.character[:]
        
        self.number = []
        self.character = []
        
        #init list
        for i in range(0,52):
            self.number.append(i)
        for i in range(65,91):
            self.character.append(chr(i))
        for i in range(97,123):
            self.character.append(chr(i))

        #cut list
        dif = len(self.number) - len(newNum)
        newNum = newNum[dif:]
        newChar = newChar[dif:]
        for i in range(len(newNum)):
            newChar[i] = (newNum[i],newChar[i])
        return newChar

    def get_string(self,num:int):

        #get string for loc
        assert num <= len(self.number), ("Over phhgs storage")
        return self.character[num]

    def get_num(self,string:str):

        #get loc for string
        try:
            return self.number[self.character.index(string)]
        except ValueError:
            raise ValueError ("Over phhgs storage")

    def reference(self):

        #return a list for ref
        refList = []
        for i in range(len(self.number)):
            refList.append("char {} = {}".format(self.number[i],self.character[i]))
        return refList

class integer():

    #get ready for the methods
    base = 10
    baseHex = {}
    
    def __init__(self):
        self.baseHex = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}

    #change base
    def baseshift(self,number,baseFrom:int, baseTo:int):
        assert 16 >= baseFrom >= 2,("base only ranges from 2 to 16")
        assert 16 >= baseTo >= 2,("base only ranges from 2 to 16")
        assert baseFrom != baseTo,("cannot have the same bases")

        #turn to base 10
        number = str(number)
        baseDecNum = 0
        numlen = len(number)-1
        for i in number:
            getNum = self.baseHex.get(i) if i in "ABCDEF" else eval(i)
            baseDecNum += getNum*baseFrom**numlen
            numlen-=1

        #get loop time
        looptime = 0
        while baseTo**(looptime+1) <= baseDecNum:
            looptime += 1

        #turn to target base
        test = baseTo ** looptime
        restr = ""
        for i in range(looptime+1): 
            baseToNum = int(baseDecNum // test)
            baseDecNum = int(baseDecNum % test)
            if baseToNum == 10:
                restr += "A"
            elif baseToNum == 11:
                restr += "B"
            elif baseToNum == 12:
                restr += "C"
            elif baseToNum == 13:
                restr += "D"
            elif baseToNum == 14:
                restr += "E"
            elif baseToNum == 15:
                restr += "F"
            else:
                restr += str(baseToNum)
            test /= baseTo
        return restr
            
class dcml():

    separate = []
    
    def __init__(self):
        pass

    def __str__(self):
        return "This is no longer the float type. Now, this is called dcml(decimal)!!!"

    def get_part(number:float):

        #get 3 part of a decimal
        number = str(number)
        self.separate.append(number[0:number.index(".")])
        self.separate.append(".")
        self.separate.append(number[number.index(".")+1:])
        return self.separate

    def round(number:float,place:int):

        #round to certain place
        numStr = str(number)
        index = numStr.get(".")
        num = "1"+numStr[index+1:]
        num = int(num[0:place+1])
        if num % 10 >= 5:
            num += 10
        numStr = numStr[0:index+1]+str(num)[1:]
        return eval(numStr)   
                
class read():
    
    def __init__(self,code):
        self.code = code
        if type(self.code) != str:
            raise TypeError("Required str type instead of others")
        
    def analyze(self):
        
        #setVariable 
        if re.match(r"init\s.*?",self.code) != None:
            return "variable init"
        
        #x set type = int/dcml/str/char/list/...
        elif re.match(r".*?\sset\stype\s=\s.*?", self.code) != None:
            return "set variable type"
        
        #x set value
        elif re.match(r".*?\sset\svalue\s=\s.*?",self.code) != None:
            return "set variable value"

        #output
        elif re.match(r"out\s.*?[.].*?:",self.code) != None:
            return "output"

        #exit
        elif re.match(r"stop",self.code) != None:
            return "stop"
        
        #input
        elif re.match(r"in\s\[.*?\]|in",self.code) != None:
            return "input"
        
        else:
            return "error"


class operation(read):

    def __init__(self,code):
        super(operation,self).__init__(code)

    #only cal between int and dcml
    def numop(self):

        #add, subtract, multiply, divide, module, expo, floor divide
        if re.match(r".*?\s[+-*/%][*/]?\s.*?",self.code) != None: #simple regular expression nesting
            pass

        #greatest common divider
        elif re.match(r"gcd\s\[.*?,.*?\]",self.code) != None:
            pass
        
        #largest common multiple
        elif re.match(r"lcm\s\[.*?,.*?\]",self.code) != None:
            pass

        #factorial
        elif re.match(r"[1-9][0-9]*?!|0!",self.code) != None:
            pass
        
        else:
            raise SyntaxError("Not arithemetical operation")

    def varop(self):
        pass

class identify():

    def __init__(self,code):
        self.code = code
        if type(self.code) != str:
            raise TypeError("Required str type instead of others")

    def numORvar(self):
        pass
                    
storeVar = []
inVar = {}
variableType = ["int","dcml","str","char","list"]
inVal = None

class interpret():

    def __init__(self,code:str):
        self.code = code
        if type(self.code) != str:
            raise TypeError("Required str type instead of others")

    def decode(self):
        #global value to use
        global storeVar
        global inVar
        global variableType
        global inVal

        inVar = {}

        #get action
        action = read(self.code).analyze()
        
        #if want to init, just init
        if action == "variable init":
            inVar["name"] = self.code[5:].replace(" ","")
            storeVar.append(inVar)

        #set variable type
        elif action == "set variable type":
            
            #ensure variable init
            getName = self.code.index("set")
            getName = self.code[0:getName-1]
            test = -1
            for i in range(len(storeVar)):
                if str(storeVar[i]["name"]) == getName:
                    test = i
            if test == -1:
                raise SyntaxError("{} not found".format(getName))

            #get type loc
            index = self.code.index("=") + 1
            for i in range(index,len(self.code)):
                if self.code[i] != " ":
                    indexOfs = i
                    break
                
            #get variable type    
            var = self.code[indexOfs:]

            #ensure is legal type
            if var in variableType:
                if var == "int":
                    storeVar[test]["type"] = "int"
                elif var == "dcml":
                    storeVar[test]["type"] = "dcml"
                elif var == "str":
                    storeVar[test]["type"] = "str"
                elif var == "list":
                    storeVar[test]["type"] = "list"
                elif var == "char":
                    storeVar[test]["type"] = "char"
            else:
                raise SyntaxError("Undetectable variable type")

        elif action == "set variable value":
            
            #ensure variable init
            getName = self.code.index("set")
            getName = self.code[0:getName-1]
            test = -1
            for i in range(len(storeVar)):
                if str(storeVar[i]["name"]) == getName:
                    test = i
            if test == -1:
                raise SyntaxError("{} not found".format(getName))

            #get value loc
            index = self.code.index("=") + 1
            for i in range(index,len(self.code)):
                if self.code[i] != " ":
                    indexOfs = i
                    break

            #get variable value
            value = self.code[indexOfs:]

            #use input as value, only be no type or str
            if re.match(r"in\s\[.*?\]|(in)$",value) != None:
                storeVar[test]["type"] = "str"
                if "[" in value:
                    lindex = value.index("[")
                    rindex = value.index("]")
                    word = input(value[lindex+1:rindex]+" ")
                else:
                    word = input()
                storeVar[test]["value"] = word
            elif re.match(r"inVal",value) != None:
                if inVal != None:
                    storeVar[test]["type"] = "str"
                    storeVar[test]["value"] = inVal
                    
            #ensure type init
            try:
                varType = str(storeVar[test]["type"])
            except:
                raise SyntaxError("variable type must initialized before giving any value")
            
            #ensure type match
            if re.match(r"[+-]?[1-9][0-9]*?|0",value) != None and varType == "int":
                storeVar[test]["value"] = int(value)
            elif re.match(r"[+-]?0?[.][0-9]*?[1-9]|[+-]?[1-9][0-9]*[.][0-9]*?[1-9]",value) != None and varType == "dcml":
                storeVar[test]["value"] = eval(str(value))
            elif re.match(r'".*"',value) != None and varType == "str":
                storeVar[test]["value"] = value[1:len(value)-1]   
            elif len(re.findall(r".*?;",value)) != 0 and varType == "list":
                value = value[0:len(value)].split(",")
                print(value)
                for i in range(len(value)):
                    if (r"[+-]?[1-9][0-9]*?|0",value[i]) != None and "." not in value[i] and '"' not in value[i]:
                        value[i] = int(value[i])   
                    elif re.match(r"[+-]?0?[.][0-9]*?[1-9]|[+-]?[1-9][0-9]*[.][0-9]*?[1-9]",value[i]) != None:
                        value[i] = eval(str(value[i]))   
                    elif re.match(r'".*?"',value[i]) != None:
                        value[i] = value[i][1:len(value[i])-1]   
                storeVar[test]["value"] = value
            elif re.match(r"[1-9]?[0-9]",value) != None and varType == "char":
                number = int(re.findall(r"[1-9]?[0-9]",value)[0])
                charac = char()
                storeVar[test]["value"] = charac.get_char()[number]
                
        elif action == "output":

            #ensure output value init
            getNameFrom = self.code.index("out")
            getNameTo = self.code.index(".")
            getName = self.code[getNameFrom+4:getNameTo]
            test = -1
            for i in range(len(storeVar)):
                if str(storeVar[i]["name"]) == getName:
                    test = i
            if test == -1:
                raise SyntaxError("{} not found".format(getName))

            #get output thing
            getOutput = self.code[getNameTo+1:self.code.index(":")]
            if getOutput == "type":
                try:
                    print(storeVar[test]["type"])
                except:
                    print("type not declared")
            elif getOutput == "value":
                try:
                    print(storeVar[test]["value"])
                except:
                    print("value not initialized")
            else:
                raise SyntaxError("Not outputting correct thing")

        elif action == "stop":
            pag.hotkey("ctrl","c")

        elif action == "input":
            value = self.code
            if "[" in value:
                lindex = value.index("[")
                rindex = value.index("]")
                inVal = input(value[lindex+1:rindex]+": ")
            else:
                inVal = input()

if __name__ == '__main__':
    while True:
        a = interpret(input())
        a.decode()
        print(storeVar)
