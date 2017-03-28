'''
Uses python 3.4.2
Run on Windows
'''
import sys
import cProfile

'''
This function was provided by the company and they asked for the results
  of passing in 7, 17, and 90
'''
def specialMath_OLD(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    return n + specialMath_OLD(n-1) + specialMath_OLD(n-2)

#print(specialMath(int(sys.argv[1])))


'''
This function is more efficient than the original function.
The old function is unable to calculate 90 in a decent amount of time.
This function has been tested up to the input of 100000.
Uses cProfile to calculate CPU usage time. 
'''
def specialMath(n):        
        #This function turns the sigma summation of the given index n 
        def sigma(n):
            #Recursive implementation of sigma
            '''if(n == 0):
                return 0
            return n + sigma(n-1)'''

            #linear implementation of sigma
            '''result = 0
            while n > 0:
                result += n
                n -= 1
            return result'''

            #sum multiplication implemntation of sigma
            if n%2 == 0:
                return int((n*(n+1))/2)
            else:
                return int(((n-1)*((n-1)+1))/2) + n
        
        #this function will return the fobonacci value for the given index n
        #  It uses the fast doubling fibonacci algorithm O(log n)
        def fibonacci(n):
            if n < 0:
                raise ValueError("Negative arguments not implemented")
            return fib(n)[0]

        def fib(n):
            if n == 0:
                return (0, 1)
            else:
                a, b = fib(n // 2)
                c = a * (b * 2 - a)
                d = a * a + b * b
                if n%2 == 0:
                    return (c, d)
                else:
                    return(d, c + d)

        # this def is the linear approach to the fibonacci numbers O(n)
        '''def fibonacci(n):
            a,b = 1,1
            for i in range(n-1):
                a,b = b,a+b
            return a'''
            
        result = 0
        #get the nth summation
        result = sigma(n)

        #calculate the terms from 1 to n-2
        a = n-2
        fibIndex = 1
        while(a >= 0):
                result += sigma(a) * fibonacci(fibIndex)
                a = a - 1
                fibIndex += 1        
        return result
    
'''
This function is providing an easy way to print out the result and the cProfile.
Makes 2 different calls  to specialMath(), one for result and one to Profile. 
'''
def printProfile(value):
    if value < 20:
        print("The old result is: %s" %(specialMath_OLD(value)))
    else:
        print("The old result will take to long")
    print("Calculating specialMath(%s)..." %(value))
    #print("Result is: %s" %(specialMath(value)))
    cProfile.run('specialMath(%s)' %(value))

def main():
    values = [7, 17, 90, 125, 1000, 10000]
    for value in values:
        printProfile(value)
main()
