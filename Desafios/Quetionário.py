def main():
    questions = [
        {
            "question": "Quanto é 5 + 7?\n"
                        "a) 10\n"
                        "b) 11\n"
                        "c) 12\n",
            "answer": "a"
        },
        {
            "question": "Qual é a capital da França?\n",
            "answer": "paris"
        },
        {
            "question": "Complete a frase: 'O sol é uma estrela de...'\n",
            "answer": "fusão nuclear"
        },
        {
            "question": "Quem escreveu a peça de teatro 'Romeu e Julieta'?\n"
                        "a) William Shakespeare\n"
                        "b) Charles Dickens\n"
                        "c) Jane Austen\n",
            "answer": "a"
        },
        {
            "question": "Qual é o maior planeta do nosso sistema solar?\n",
            "answer": "júpiter"
        },
        {
            "question": "Quanto é a raiz quadrada de 64?\n",
            "answer": "8"
        },
        {
            "question": "Qual é o processo pelo qual as plantas produzem seu próprio alimento?\n",
            "answer": "fotossíntese"
        },
        {
            "question": "Quem pintou a Mona Lisa?\n",
            "answer": "leonardo da vinci"
        },
        {
            "question": "Qual é o único mamífero capaz de voar?\n",
            "answer": "morcego"
        },
        {
            "question": "Qual é o oceano mais profundo do mundo?\n",
            "answer": "oceano pacífico"
        }
    ]

    score = 0

    for question in questions:
        user_answer = input(question["question"]).strip().lower()
        if user_answer == question["answer"]:
            score += 1

    print(f"\nVocê respondeu corretamente a {score} perguntas. Parabéns!")
    print(f"Romulo, você atingiu {score} pontos")

if __name__ == "__main__":
    main()
