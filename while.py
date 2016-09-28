list1 = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

item = 0

while item < len(list1):
    names = list1[item]
    item += 1
    if names == 'Валера':
        print("Привет, Валера")
        break
        #list1.pop([item])