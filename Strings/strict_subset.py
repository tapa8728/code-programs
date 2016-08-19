

class Superset(object):
    
    
    def __init__(self):
        self.superset = set(map(int,raw_input().split()))
        self.numInput()
    def numInput(self):
        self.numTest = input()
    
    def inputTestCases(self):
        self.testList=[]
        for each in range(self.numTest):
            self.testList.append(  set(map(int,raw_input().split() ) ))
    def result(self):
        for each in self.testList:
            if(each in self.superset and (len(self.superset)-len(each))>=1    ):
            #if (len(self.superset.difference(each)) >=1 and each == self.superset.intersection(each)):
                flag = True
            else:
                flag =  False
                break
        print  flag
        
            
inp = Superset()
inp.inputTestCases()
inp.result()