word_of_simbol = {
    "плюс":"+",
    "минус":"-",
    "умножить":"*",
    "разделить":"/",
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
get_change("/calc сколько будет два умножить на три", word_of_simbol)
