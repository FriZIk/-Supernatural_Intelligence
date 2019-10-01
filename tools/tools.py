import random
#n - value, a - array
def genTest(n,left,right):
    random.seed()
    res = []
    for i in range(0,n):
        res.append(random.randint(left,right))
    return res

def getSample(a,n):
    random.seed()
    targ = a
    res = []
    for i in range(0,min(len(a),n)):
        idx = random.randint(0,len(targ))
        res.append(targ[idx])
        del targ[idx]
    return res
        
def middle(a):
    res = 0
    for i in a:
        res += i
    return res/len(a)

def med(a):
    if len(a) % 2 == 0:
        return (a[len(a)//2] + a[len(a)//2 -1])/2
    else:
        return a[len(a)//2]

def disp(a):
    mid = middle(a)
    res = 0
    for i in a:
        res += (i-mid)**2
    return res/(len(a)-1)

def sigma(a):
    return (disp(a))**0.5

def zStandart(a):
    res = []
    mid = middle(a)
    sg = sigma(a)
    for i in a:
        res.append((i-mid)/sg)
    return res
