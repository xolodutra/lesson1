word_of_simbol = {
    "плюс":"+",
    "минус":"-",
    "умножить":"*",
    "делить":"/",
    "ноль":"0",
    "один":"1",
    "два":"2",
    "три":"3",
    "четыре":"4",
    "пять":"5",
    "шесть":"6",
    "семь":"7",
    "восемь":"8",
    "девять":"9",
    "сколько": "="
}

def get_change(user_task, word_of_simbol):
    user_task = user_task.replace("/calc", '')
    user_task = user_task.replace("на", '')
    user_task = user_task.replace("будет", '')

    split_task = user_task.split(" ")
    list_task = []
    for word in split_task:
        if word:
            list_task.append(word_of_simbol.get(word))
    str_task = "".join(list_task)

    return int_calculate(str_task)


def calculate(user_task):
        if '=' in user_task:
            return int_calculate(user_task)
        elif "сколько" in user_task:
            return get_change(user_task, word_of_simbol)


def int_calculate(user_task):
    user_task = user_task.replace('/calc', '')

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
   calculate("/calc сколько будет три умножить на два")