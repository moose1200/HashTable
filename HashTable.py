import random
import time
class Node:
    #data is designed to be a (string,int)
    def __init__(self,data):
        self.payload = data
        self.rightChild = None
        self.leftChild = None
        self.root = None
    #Sets Right child
    def setRight(self,node):
        self.rightChild = node
    #sets Left child
    def setLeft(self,node):
        self.leftChild = node
    #sets new data
    def setData(self,payload):
        self.payload = payload
# Traversal function for BST
def inOrder(tree):
    if(tree!=None):
        inOrder(tree.leftChild)
        print(tree.payload)
        inOrder(tree.rightChild)
        




class HashTable:
    #table holds (name,age) tuples
    #Each element of the table is a Binary Search Tree
    #Accepts the size of the table as the parameter
    #Inserting (key,value) where key already exist will update value
    def __init__(self,size):
        self.size = size
        self.data = [None]*size
    def hasher(self,name):
        _sum = 0
        for i in name:
            _sum+=ord(i)
        return (_sum*len(name))% self.size
    #add a new element
    def add(self,s):
        index = self.hasher(s[0])
        data = self.data
        if(data[index] == None):
            data[index] = Node(s)
        else:
            current = data[index]
            prev = None
            while(current !=None):
                prev = current
                if(s[0]<current.payload[0]):
                    current = current.leftChild
                elif(s[0]>current.payload[0]):
                    current = current.rightChild
                else:
                    current.setData(s);break;
            if(s[0]<prev.payload[0]):
                prev.setLeft(Node(s))
            elif(s[0]>prev.payload[0]):
                prev.setRight(Node(s))
                    
                


    #retruns the age associated with name
    def getAge(self,name):
        index= self.hasher(name)
        current = self.data[index]
        while(current !=None):
                
                if(name<current.payload[0]):
                    current = current.leftChild
                elif(name>current.payload[0]):
                    current = current.rightChild
                else:
                    return current.payload[1]
        return None
        
    #adds n random values to the table
    def addRand(self, n):
        for i in range(0,n):
            self.add((chr(random.randint(65,90))+chr(random.randint(97,122)),random.randint(1,100)))
        
    def printTable(self):
        for i in table.data:
            if i != None:
                print("[");
                inOrder(i)
                print("]")
            else:
                print (None)
        
class Test:
    def __init__(self):
        self.Pass = 0
        self.Fail = 0
        
    def run(self,e,a,message=""):
        if(e == a):
            self.Pass+=1
        else:
            self.Fail+=1
            print(message)
    def result(self):
        print("Passed "+str(self.Pass)+ " Failed "+str(self.Fail))
        
#Linear Searching

    
def linearSearch(list,name):
    for i in list:
        if i[0] == name:
            return i[1]
    return None

#Testing
test = Test()  
table = HashTable(11)
table.add(("Person 1",34))
table.add(("John",12))
table.add(("Person 2",14))
table.add(("Person 2",25))

test.run(34,table.getAge("Person 1"))
test.run(12,table.getAge("John"))
test.run(25,table.getAge("Person 2"))
test.run(None,table.getAge("Mike"))


test.result();

#Comparing Times, Table Search vs Linear Search
#n is the number of Elements, size is the size of the Hash Table
def compTime(n,size):
    print(str(n)+" Elements, Table size " + str(size))
    hTable = HashTable(size)
    hTable.add(("John",12))
    hTable.addRand(n)
    start = time.time()
    hTable.getAge("John")
    print("Hash Search : " + str(((time.time()-start)*1000)))
    l = []
    
    #randomly insert the value to be searched
    for i in range(0,n):
            l.append((chr(random.randint(65,90))+chr(random.randint(97,122)),random.randint(1,100)))
    l[random.randint(0,len(l)-1)] = ("John",12)
    start = time.time()
    linearSearch(l,"John")
    print("Linear Search : " + str(((time.time()-start)*1000)))
#compTime(10000000,11)

        
