b = [1,2,7,3,5,7,9]
leng = len(b)
def vet(n,b):
    if n == -1:
        return 0
    else:
        return b[n]+vet(n-1,b)

print(vet(leng-1,b))