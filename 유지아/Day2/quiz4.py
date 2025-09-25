#4
n=int(input())
num=list(map(int,input().split()))

cnt=0
for i in num:
    if i<2:
        continue
    else :
        for j in range(2,i+1):
            if j%i==0:
                cnt+=1
print(cnt)



