# 1)Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
U=int(input('Ввеcти количество элементов списка:'))
list=[]
sum=0
for i in range(U):
   list.append(int(input('Ввеcти элемент:')))
   if i%2!=0:
    sum = list[i]+sum 
print(sum)


#2)Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import math
Q=int(input('Ввеcти количество элементов списка:'))
list2=[]
sum=0
k=Q
z=0
for i in range(Q):
   list2.append(int(input('Ввеcти элемент:')))
for z in range (math.ceil(Q/2)):
    print(list2[z]*list2[k-1])
    z=z+1
    k=k-1
    
#3)Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import math
G=int(input('Ввести количество элементов списка:'))
list3 = []
list4 = []
for i in range(G):
    list3.append(float(input('Ввести элемент:')))
    list4.append(list3[i]-math.floor(list3[i]))
print(max(list4)-min(list4))

#4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
n = int(input())
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)