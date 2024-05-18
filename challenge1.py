
# Online IDE - Code Editor, Compiler, Interpreter

sum = 0

for i in range(1000):    # for all the real numbers between 999 and 0. the range function is not inclusive 
    if (i%3 == 0 or i%5 ==0):  # if the remainder of i divided by either 3 or 5 is 0, then add i to the sum
        sum = sum + i 

print (sum) 
