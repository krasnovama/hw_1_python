# 17. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на введенных пользователем позициях.

n = int(input("Введите число N: "))
el1=int(input("Введите позицию элемента 1 для умножения: "))
el2=int(input("Введите позицию элемента 2 для умножения: "))
my_list=[]
for i in range(-n,n+1):
    my_list.append(i)
print("Последовательность элементов: ", my_list)
print(f'Произведение элементов {el1} и {el2}: {my_list[el1]} * {my_list[el2]} = {my_list[el1]*my_list[el2]}')
