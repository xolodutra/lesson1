def calculate():
    task = input('Введите задачу:__')
    if '=' in task:
        repl_task = task.replace('=', '')
        if '+' in repl_task:
            numbers = repl_task.split("+")
            x, y = numbers
            print(str(int(x)+int(y)))
        elif '-' in repl_task:
            numbers = repl_task.split("-")
            i, j = numbers
            print(str(int(i)-int(j)))
        elif '*' in repl_task:
            numbers = repl_task.split("*")
            a, b = numbers
            print(str(int(a)*int(b)))
        elif '/' in repl_task:
            numbers = repl_task.split("/")
            o, v = numbers
            print(str(int(o)/int(v)))
        else:
            print('пока')
    else:
        print('вы забыли знак равно')

if __name__ == '__main__':
    calculate()

