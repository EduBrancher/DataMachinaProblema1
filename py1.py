# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:41:13 2021

@author: Windows
"""


F = [[1,1],[1,0]]
T = [[1,2],[3,4]]


def copy(A, B): #copies matrix B into matrix A. Matrixes must be 2 by 2.
   
    A[0][0] = B[0][0]
    A[0][1] = B[0][1]
    A[1][0] = B[1][0]
    A[1][1] = B[1][1]
    
    pass

def multiply(A, B): #Multiplies matrix A by matrix B. Matrixes must be 2 by 2. Result is stored in matrix A.
    
    R = [[0,0],[0,0]]
    
    R[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    R[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    R[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    R[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    
    copy(A,R)
    
    pass

def power(A, n): #Fast exponentiation on the fibonacci matrix.
    
    copy(F, A)   #time: 1
    
    if (n == 1):        #time: 1
        return
    
    power(A, n//2)       #time: T[n/2]
    multiply(A, A)      #time: 1

    if (n % 2 == 1):    #time: 1
        multiply(A, F)  #time: 1

    pass

# T[n] = T[n/2] + 5 
# 2^k = n => T[2^k] = T[2^k-1] + 5
# T[2^k] = 5k + 2
# T[n] = 5 log(n) + 2

 
def fib(n): #Gets the n-th term of the Fibonacci sequence in O(log(n)) time.
    
    if (n == 0):
        return 0
    if (n == 1):
        return 1
   
    F = [[1,1],[1,0]]
    power(F, n)
    return(F[0][1])

    pass

def fib2_fake(n): #slower
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    i = 1;
    fn = 1
    fnn = 1
    while (i < n):
        aux = fnn
        fnn = fnn + fn
        fn = aux
        i = i + 1
    
    return fn
    
def main():
    
    print("Olá, usuário. Esse é o solucionador de fibonacci. Seguem as instruções de uso:")
    print("Para usar a implementação rapida de fibonacci(n), digite: fib n e aperte enter.")
    print("Para usar a implementação lenta de fibonacci(n), digite: fake n e aperte enter.")
    print("O programa imprimirá na tela o resultado da sequência. Você pode pedir outras instruções.")
    print("Digite qualquer coisa diferente dos comandos acima e aperte enter para terminar o programa.")
    
    
    running = 1
    
    while running:
        
        usinput = input()
        inputlist = usinput.split()
        
        if (inputlist[0] == "fib"):
            print(str(fib(int(inputlist[1]))))
        elif (inputlist[0] == "fake"):
            print(str(fib2_fake(int(inputlist[1]))))
        else:
            running = 0
        pass
    
    
    pass
    
if __name__ == "__main__":
    main()
