def atividade1():
    def fat(n):
        if n == 0:
            return 1
        else:
            return n*fat(n-1)
    print(fat(int(input("informe um valor para o fatorial: "))))

def atividade2():
    def fib(n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        else: 
            return fib(n-1)+fib(n-2)
    print(fib(int(input("informe qual termo da sequencia de fibonnaci você deseja: "))))

def atividade4():#-arrumar para ser vetor variavel (=
    b = [1,2,7,3,5,7,9]
    leng = len(b)
    def vet(n,b):
        if n==-1:
            return 0
        else:
            return b[n]+vet(n-1,b)
    print(vet(leng-1,b))

def atividade5():
    def soma(n):
        if n==1:
            return 1
        else:
            return n+soma(n-1)
    print(soma(int(input("informe um número para soma de todos os números anteriores até ele: ")))) 

def atividade6():
    def pot(k,n):
        if n==0:
            return 1
        if n==1:
            return k
        else:
            return k*pot(k,n-1)
    print(pot(int(input("informe a base: ")), (int(input("informe o expoente: ")))))

def atividade8():
    def mdc(x,y):
        if y==0:
            return 0
        else:
            return mdc(y,x%y)
    print(mdc(int(input("informe um valor: ")),int(input("informe outro valor: "))))


def atividade10():
    def mult(x,y):
        if y==1:
            return x
        else:
            return x+mult(x,y-1)
    print(mult(int((input())),int(input())))


