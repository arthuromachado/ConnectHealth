import os
import utils



def start():
  # Apresentar o chatbot
  utils.create_lines()
  print("Olá! Bem-vindo a Connect Health.")
  utils.create_lines()
  # Pedir o nome
  nome = input("Digite o seu nome: ")
  
  # Pedir o e-mail
  email = input("Digite o seu e-mail: ")
  utils.create_lines()
  
  # Introduzir um laço de repetição 
  while True:
      # Validar o e-mail
    if not utils.validar_email(email):
      print("E-mail inválido. Digite um e-mail válido.")
      email = input("Digite o seu e-mail: ")
      utils.create_lines()
      return
    # Oferecer um menu de opções
    resposta = input(f"No que posso te ajudar?{os.linesep}[1] - Exames{os.linesep}[2] - Consultas{os.linesep}[3] - Análises clinicas{os.linesep}[4] - Planos{os.linesep}[5] - Sair{os.linesep}")
    utils.create_lines()
      # Processar resposta enviada
    utils.processar_opcao(resposta)
    # Processar resposta enviada
    if resposta == "5": # Verificar se o usuário escolheu sair
      print("Obrigado",nome+" por utilar nossos serviços. Volte sempre!") 
      break
  

start()

