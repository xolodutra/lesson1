list_names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(name):
    count = 0
    while count < len(list_names):
        item = list_names[count]
        count += 1
        if item == name:
            print("Привет,", item)
            break
find_person('Петя')