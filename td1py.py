 

def solve(n):
    a=str(n)
    s=0
    for e in a:
        s+=int(e)
    return s
assert solve(2**15) == 26
print(solve(2**1000))
###
    

def solve():
    f = open("p022_names.txt","r")
    #trier-prenoms
    a=f.read()
    M=a.split(",")
    L=sorted(M,key=str.lower)
    scoreT=0
    for i in range(len(L)):
        ordre=i
        name=L[i]
        somme=0
        for i in range(1,len(name)):
            somme+=ord(name[i])-64
            score=somme*ordre
        scoreT+=score
    f.close()
    return scoreT
print(solve())
###

