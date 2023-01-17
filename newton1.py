nkx=list(map(int,input().split()))
no=sorted(list(map(int,input().split())))[::-1]
ld=[]
n=0
for i in no:
    if n<nkx[1]:
        if (i-nkx[2]>=0):
            ld.append(i-nkx[2])
        else:
            ld.append(0)
    else:
        ld.append(i)
    n+=1
print(ld)