# hannah siegel
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
#find the sum of the even-valued terms.

#E(n) = 4*E(n-1) + E(n-2) is a recursive relation for just the even nums

limit = 4000000

# a,b,c are the intial even values in the Fibonacci sequence
a = 2 
b = 8 
c = 34
sum = 10 # a+b 

while c < limit:
    sum += c 
    a = b 
    b = c 
    c = 4 * b + a 
    
print (sum)
