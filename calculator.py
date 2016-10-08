def calculate(user_task):
    if '=' in user_task:
        repl_task = user_task.replace('=', '')
        if '+' in repl_task:
            numbers = repl_task.split("+")
            x, y = numbers
            return (str(int(x)+int(y)))
        elif '-' in repl_task:
            numbers = repl_task.split("-")
            i, j = numbers
            return (str(int(i)-int(j)))
        elif '*' in repl_task:
            numbers = repl_task.split("*")
            a, b = numbers
            return (str(int(a)*int(b)))
        elif '/' in repl_task:
            numbers = repl_task.split("/")
            o, v = numbers
            return (str(int(o)/int(v)))
    else:
        return 'вы забыли знак равно'


if __name__ == '__main__':
    calculate()