# 25. Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# ababac
# a_1
# b_1
# a_2
# b_2
# a_3
# c_1


dict1 = dict()

symbols = input("Введите буквы: ")

for syn in symbols:
if syn in dict1:
dict1[syn] +=1
else:
dict1[syn] = 0

if dict1[syn] == 0:
print(syn)
else:
print(f"{syn}_{dict1[syn]}")