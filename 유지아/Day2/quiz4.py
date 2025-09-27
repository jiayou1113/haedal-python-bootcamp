#4
n=int(input())
num=list(map(int,input().split()))

cnt=0
for i in num:
    if i<2:
        continue
    else :
        k=1
        for j in range(2,int(i**0.5) + 1):
            if i%j==0:
                k=0
                break
    if k==1:
        cnt+=1
print(cnt)



