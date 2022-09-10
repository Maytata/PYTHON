#Зад 1
n=int(input())
ed=0
nu=0
for i in range (1,n+1):
    if 1 == int (input()):
        ed+=1
    else:
        nu+=1
if ed>nu:
    print(nu)
else:
     print(ed)


# Зад2
k=int(input('Ввеcти N:'))
sum=0
for i in range(1,k+1):
    sum=sum+i
print(sum)

# Зад3
l=int(input('Ввеcти N:'))
i=l
list = []
j=0
while i>1:
    a=l%i
    if a==0:
        list.append(i)
        j+=1
    i-=1
print(list[j-1])


#Зад4
N = int(input('Ввеcти количество учеников:'))
HeightMain = int(input('Ввеcти рост Пети:'))
count=0
for i in range(N+1):
    HeightOther = int(input('Ввеcти рост ученика:'))
    if HeightMain <= HeightOther:
        count+=1
    else:
         print(f'Место Пети в шеренге:{count}')
         break


#Доп
U=int(input('Ввеcти количество кустов:'))
listBerries=[]
for i in range(U):
    amount=int(input('Ввеcти количество ягод на кусте:'))
    listBerries.append(amount)
r=0
SumBer=0
maxsum=0
while r<(len(listBerries)-1):
    SumBer = listBerries[r-1] + listBerries[r] + listBerries[r+1]
    r=r+1
    if SumBer>maxsum:
        maxsum=SumBer
SumBer=listBerries[r-1] + listBerries[r] + listBerries[0]
if SumBer>maxsum:
    maxsum=SumBer
print(maxsum)
