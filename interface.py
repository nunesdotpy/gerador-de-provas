import prova
from os import path, makedirs

diret_atividade = 'provas/atividade'
diret_gabarito = 'provas/gabarito'


if not path.exists(diret_atividade):
    makedirs(diret_atividade)
if not path.exists(diret_gabarito):
    makedirs(diret_gabarito)

def criarProvas():
    for i in range(1, 36):
        atividade, respostas = prova.criarAtv()

        perguntas = path.join(diret_atividade, f'prova-{i}.txt')
        gabarito = path.join(diret_gabarito, f'gabarito-{i}.txt')

        with open(perguntas, 'w', encoding='utf-8') as arquivo:
            arquivo.write(atividade)

        with open(gabarito, 'w', encoding='utf-8') as arquivo:
            for resposta in respostas:
                arquivo.write(str(resposta) + '\n')

    print("\nProvas criadas")

def userCli():
    while True:
        ui = int(input("Deseja gerar uma nova prova?\n1 - Sim | 2 - Não\n>> "))
        if ui == 1:
            criarProvas()
        else:
            print("Até mais!")
            exit()