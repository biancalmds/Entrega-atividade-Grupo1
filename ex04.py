gabarito = {
    "questao1": "A",
    "questao2": "E",
    "questao3": "B",
    "questao4": "C",
    "questao5": "B",
    "questao6": "A",
    "questao7": "A",
    "questao8": "D",
    "questao9": "E",
    "questao10": "D"
}

lista_alunos = []

while True:
    acertos = 0
    print("Bem-vindo a correção da prova! Digite suas respostas conforme o número da questão.")
    
    for i in range(10):
        resposta = input(f"Questão {i+1}: ").upper()
        if resposta == gabarito[f"questao{i+1}"]:
            acertos+=1
    lista_alunos.append(acertos)

    continuar = input("Outro aluno irá realizar a prova? (S/N): ").upper()
    
    if continuar == "N":
        break

print(f'''RESULTADOS DA PROVA
Maior número de acertos: {max(lista_alunos)}
Menor número de acertos: {min(lista_alunos)}
Total de alunos que utilizaram o sistema: {len(lista_alunos)}
Média das notas da turma: {sum(lista_alunos)/len(lista_alunos)}
''')