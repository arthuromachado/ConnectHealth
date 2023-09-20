import os


def processar_resposta(resposta, nome):
    if resposta == "1":
        print(
            f'\n{nome}, que tipo de médico você gostaria de marcar? \n')

    elif resposta == "2":
        print(
            f'\n{nome}, insira o dia e horário da consulta que você gostaria de desmarcar: \n')

    elif resposta == "3":
        print(
            f'\n{nome}, estou te transferindo para um de nossos colaboradores \n')
    else:
        print('Digite apenas as opções 1, 2 ou 3') 



def start():
    #apresentar o chatbox
    print("Olá! Bem vindo Connect Health \nMeu nome é Connie, sou a assistente digital que vai te auxiliar hoje")

    #pedir nome
    nome = input("Digite seu nome completo: ")


  #oferecer um menu de opções
    resposta = input(
          f'O que você gostaria de fazer hoje? \n[1] - Marcar consulta \n[2] - Cancelar consulta \n[3] - Falar com atendente \n ')
      
      #processar a resposta enviada
    processar_resposta(resposta, nome)

         
if __name__ == '__main__':
    start()
    
