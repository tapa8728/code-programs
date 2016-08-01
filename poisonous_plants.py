class Plant:
    def __init__(self, pesticide, days):
        self.pesticide = pesticide
        self.days = days

    def __str__(self):
    	return "Pesticide {} alive for {} days".format(self.pesticide, self.days)


 
def solvePlants(a):
    stack = []
    maxDaysAlive = 0
     
    for pesticide in a:
        daysAlive = 0
        while len(stack)>0 and pesticide <= stack[-1].pesticide:
            daysAlive = max(daysAlive, stack.pop().days)
             
        if not stack:
            daysAlive = 0
        else:
            daysAlive += 1
             
        maxDaysAlive = max(maxDaysAlive, daysAlive)
         
        stack.append(Plant(pesticide, daysAlive))
        for each in stack:
        	print each
       	print " ------------------------- "
    print maxDaysAlive
 
def main():
    N = 7#input()
    numbers = [6,5, 8, 4,7, 10, 9]#map(int, raw_input().split())
    solvePlants(numbers)
      
  
if __name__ == '__main__':
    main()