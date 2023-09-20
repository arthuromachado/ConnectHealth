import os
import re
#import time
#import sys

# Criar um dicionário com as opções em cascata
opcoes = {
  "1": ["Data e Horário de atendimento", "Agendamento", "Exame de análises clínicas", "Exame de imagens", "Cancelamento", "Voltar ao início"],
  "2": ["Data e Horário de atendimento", "Agendamento", "Consulta médica", "Consulta odontológica","Resultados", "Cancelamento", "Voltar ao início"],
  "3": ["Análise de sangue", "Análise de urina", "Análise de fezes","Cancelamento", "Voltar ao início"],
  "4": ["Individual", "Familiar", "Coletivo", "Voltar ao inicio"],
  "5": ["Sair"]
}
#resposta_opcoes
# Definir uma função para validar o e-mail
def validar_email(email):
  # Usar uma expressão regular para verificar o formato do e-mail
  padrao = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
  # Retornar True se o e-mail for válido, ou False se não for
  return re.match(padrao, email) is not None

# Definir uma função recursiva para processar as opções em cascata
def processar_opcao(opcao):
  # Verificar se a opção é válida
  if opcao in opcoes:
    # Obter a lista de subopções da opção escolhida
    subopcoes = opcoes[opcao]
    # Verificar se há mais de uma subopção
    if len(subopcoes) > 1:
        # Mostrar as subopções ao usuário
      print(f"Você escolheu a opção {opcao}. Estas são as subopções disponíveis:")
      print(30*"-=")
      for i, subopcao in enumerate(subopcoes):
        print(f"[{i+1}] - {subopcao}")
        # Pedir ao usuário que escolha uma subopção
      print(30*"-=")
      escolha = input("Digite um número para a opção desejada: ")
      print(30*"-=")
         # Chamar a função novamente, passando a subopção como parâmetro
      processar_opcao(escolha)
    else:
      # Mostrar uma resposta final ao usuário
      print(f"Você escolheu a opção {opcao}. {subopcoes[0]}")
  else:
    # Mostrar uma mensagem de erro ao usuário
    print("Digite apenas um número válido")

def start():
  # Apresentar o chatbot
  print(30*"-=")
  print("Olá! Bem-vindo a Connect Health.")
  print(30*"-=")
  # Pedir o nome
  nome = input("Digite o seu nome: ")
  
  # Pedir o e-mail
  email = input("Digite o seu e-mail: ")
  print(30*"-=")
  # Validar o e-mail
  while not validar_email(email):
    print("E-mail inválido. Digite um e-mail válido.")
    email = input("Digite o seu e-mail: ")
    print(30*"-=")
    # Introduzir um laço de repetição 
  while True:
    # Oferecer um menu de opções
    resposta = input(
        f"No que posso te ajudar?{os.linesep}[1] - Exames{os.linesep}[2] - Consultas{os.linesep}[3] - Análises clinicas{os.linesep}[4] - Planos{os.linesep}[5] - Sair{os.linesep}")
    print(30*"-=")
      # Processar resposta enviada
    processar_opcao(resposta)
    # Processar resposta enviada
    if resposta == "5": # Verificar se o usuário escolheu sair
      print("Obrigado",nome+" por utilar nossos serviços. Volte sempre!") 
      #sys.exit() # Encerrar o programa
      break
    else:
      continue
  
if __name__ == "__main__":
  start()
