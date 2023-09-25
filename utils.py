import re

# Criar um dicionário com as opções em cascata
opcoes = {
  "1": ["Data e Horário de atendimento", "Agendamento", "Exame de análises clínicas", "Exame de imagens", "Cancelamento", "Voltar ao início"],
  "2": ["Data e Horário de atendimento", "Agendamento", "Consulta médica", "Consulta odontológica","Resultados", "Cancelamento", "Voltar ao início"],
  "3": ["Análise de sangue", "Análise de urina", "Análise de fezes","Cancelamento", "Voltar ao início"],
  "4": ["Individual", "Familiar", "Coletivo", "Voltar ao inicio"],
  "5": ["Sair"]
}
#resposta_opcoes

# Criar linhas
def create_lines(): 
    print(30*"-=")


# Definir uma função para validar o e-mail
def validar_email(email):
  # Usar uma expressão regular para verificar o formato do e-mail
  padrao = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
  # Retornar True se o e-mail for válido, ou False se não for
  return re.match(padrao, email) 



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
      create_lines()
      for i, subopcao in enumerate(subopcoes):
        print(f"[{i+1}] - {subopcao}")
        # Pedir ao usuário que escolha uma subopção
      create_lines()
      escolha = input("Digite um número para a opção desejada: ")
      create_lines()
         # Chamar a função novamente, passando a subopção como parâmetro
      processar_opcao(escolha)
    else:
      # Mostrar uma resposta final ao usuário
      print(f"Você escolheu a opção {opcao}. {subopcoes[0]}")
  else:
    # Mostrar uma mensagem de erro ao usuário
    print("Digite apenas um número válido")