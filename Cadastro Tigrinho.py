from datetime import date
import time
import random
                   #>>>>Cadastro<<<<
nome = str(input('Digite o seu nome de Usuario:')).strip().title()

#strings
time.sleep(0.2)
print('\nBem vindo, {} a nossa casa de aposta, oq deseja hoje? \nDia de hoje:{}'.format(nome, date.today()))
time.sleep(0.4)

#       >>>>Escolha de jogos<<<<
jogos = ['Corrida de Cavalos', 'Aviator']

print('\nQual jogo você irá jogar?')
time.sleep(0.5)
for i, jogo in enumerate(jogos, start=1):
    print(f"{i}.{jogo}")
while True:
    try:
        escolha = int(input('\nSelecione a opção do jogo desejado! (o número deve ser correspondente):'))
        if 1 <= escolha <= len(jogos):
            break
        else:
            print('\nPor favor, selecione uma opção válida:')
    except ValueError:
        print('\nEntrada invalida: insira uma opção valida')


#                    >>>1<<<Corrida de Cavalos
cavalos = ['Cleide', 'Carlinhos', 'Dalva', 'Gregory']
if escolha == 1:
    print('\nVocê selecionou a Corrida de cavalos!')

    #verificação do dinheiro (se e numero inteiro ou nao)
    while True:
        try:
            money = float(input('\nDigite um valor para apostar: R$'))
            if money < 1:
                raise ValueError('Insira um valor positivo.')
            break
        except ValueError as i:
            print(f'Erro com o valor digitado:{i}')
#indice de escolha de cavalos:
    print('\nQuais do cavalos abaixo você irá apostar?')
    for i, cavalo in enumerate(cavalos, start=1):
        print(f"{i}.{cavalo}")
    while True:
        try:
            escolha_cavalo = int(input('\nSelecione das opções a cima para apostar (o numero deve ser correspondente):'))
            if 1 <= escolha_cavalo <= len(cavalos):
                cavalo_escolhido = cavalos[escolha_cavalo - 1]
                break
            else:
                print('\nPor favor selecione uma opção valida.')
        except ValueError:
            print('\n Entrada invalida:insira opção valida')
    #             >>>if e elif dos cavalos<<<
    ganhador = random.choice(cavalos)
    print(f'\nO cavalo vencedor foi: {ganhador}')
    if cavalo_escolhido == ganhador:
        print('Parabéns! Você ganhou a aposta com o cavalo {}.\nO valor retornado foi de:R${}'.format(ganhador, money * 10))
    else:
        print('Você perdeu. Tente novamente!')