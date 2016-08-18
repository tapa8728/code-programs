'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

http://stackoverflow.com/questions/22562023/n-steps-with-1-2-or-3-steps-taken-how-many-ways-to-get-to-the-top 
https://plus.maths.org/content/fibonacci-sequence-brief-introduction

Fibonacci Series
'''
n = 5

  a = b = 1 #base case
        
for _ in range(n):
   a , b = b, a+b
   
print a