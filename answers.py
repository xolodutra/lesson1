answers = {
    "привет": "И тебе привет!", 
    "как дела?": "Лучше всех", 
    "пока": "Увидимся"
}

def get_answer(question, answers):
    return answers.get(question)

def ask_user(answer):
    try:
        while True:
            user_input = input('Скажи что-нибудь:  ').lower()
            answer = get_answer(user_input, answers)
            print(answer)

            if (user_input == "пока"): 
                break 

    except KeyboardInterrupt: 
        print('\n\nУходите? Что, даже чаю не попьёте?\n\n')

if __name__ == "__main__":
    ask_user(answers)
