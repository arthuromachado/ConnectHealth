def linha():
  print(40*"-")

# Saudação inicial
linha()
print("Olá! Bem-vindo a Connect Health. No que posso te ajudar hoje?")
linha()
nome_usuario = input("Digite o seu nome: ")
linha()

# Dicionário com as opções do menu principal e suas respostas
menu_principal = {
    1: "Informações de Saúde",
    2: "Agendamento de Consultas",
    3: "Informações Médicas",
    4: "Suporte",
    5: "Plano de Saúde",
    0: "Sair"
}

# Função para mostrar o menu principal
def mostrar_menu_principal():
    print("Menu Principal:")
    for key, value in menu_principal.items():
        print(f"[{key}] - {value}")

# Dicionários com as opções dos submenus e suas respostas
submenu_saude = {
    1: "Prevenção",
    2: "Doenças Comuns",
    3: "Dicas de Bem-Estar",
    4: "Voltar ao Menu Principal"
}

submenu_agendamento = {
    1: "Agendar Exame",
    2: "Análises Clínicas",
    3: "Marcar Consulta Médica",
    4: "Voltar ao Menu Principal"
}

submenu_informacoes_medicas = {
    1: "Condições Médicas para Cirurgia",
    2: "Medicamentos",
    3: "Procedimentos",
    4: "Voltar ao Menu Principal"
}

submenu_suporte = {
    1: "Suporte Psicológico",
    2: "Emergência",
    3: "Orientações de Primeiros Socorros",
    4: "Voltar ao Menu Principal"
}

submenu_plano_saude = {
    1: "Plano de Saúde Individual",
    2: "Plano de Saúde Familiar",
    3: "Plano de Saúde Coletivo",
    4: "Voltar ao Menu Principal"
}

# Dicionário com as respostas dos submenus
respostas_submenus = {
    "Prevenção": " Vacinação: Mantenha-se atualizado com as vacinas recomendadas, incluindo vacinas específicas para pandemias ou epidemias em curso.\nHigiene das Mãos: Lave as mãos regularmente com água e sabão por pelo menos 20 segundos ou use desinfetante à base de álcool.\nDistanciamento Social: Mantenha distância física de outras pessoas, especialmente em áreas de surto.\nMáscaras: Use máscaras faciais em público, especialmente quando o distanciamento social não é possível.\nEvite Multidões: Evite grandes aglomerações e eventos lotados.\nLimpeza e Desinfecção: Limpe e desinfete superfícies frequentemente tocadas, como maçanetas e telefones",
    "Doenças Comuns": "Resfriado Comum: Tratamento: Descanso, hidratação e medicamentos para aliviar sintomas, como analgésicos e descongestionantes.\nGripe (Influenza): Tratamento: Descanso, hidratação e medicamentos antivirais, se prescritos pelo médico.\nHipertensão (Pressão Alta): Tratamento: Dieta saudável com baixo teor de sódio, exercícios regulares e, às vezes, medicamentos prescritos.\nDiabetes Tipo 2: Tratamento: Controle da dieta, exercícios, monitoramento dos níveis de açúcar no sangue e, em alguns casos, medicação.\nAsma: Tratamento: Inaladores de alívio rápido para crises agudas e inaladores de controle a longo prazo para prevenção. Evitar gatilhos.",
    "Dicas de Bem-Estar": "Alimentação Equilibrada: Consuma uma variedade de alimentos frescos, incluindo frutas, vegetais, proteínas magras e grãos integrais.\nHidratação: Beba água regularmente ao longo do dia para manter-se hidratado.\nExercício Regular: Faça atividades físicas que você goste, como caminhar, nadar ou andar de bicicleta, pelo menos 30 minutos por dia.\nSono Adequado: Tente dormir de 7 a 9 horas por noite para descanso e recuperação.\nCheck-ups de Saúde Regulares: Faça exames médicos de rotina e siga as orientações do seu médico",
    "Agendar Exame": "Para agendar um exame, você precisa encontrar o número de telefone do laboratório ou clínica, falar com um atendente, fornecer suas informações pessoais, escolher uma data e horário disponíveis, confirmar os detalhes, anotar as informações do agendamento, verificar se há preparações especiais necessárias e obter uma confirmação do agendamento, como um número de referência.",
    "Análises Clínicas": "Através do nosso site ou uma de nossas filiais, com suas informações pessoais, como nome, data de nascimento e número de telefone, quando solicitado.\nEscolha a data e o horário disponíveis que melhor se ajustem à sua agenda.\nConfirme os detalhes da consulta, como data, horário e local.\nSiga quaisquer instruções específicas fornecidas pelo chatbot, como preparações necessárias para os exames.\nReceba uma confirmação do agendamento com os detalhes da consulta.",
    "Marcar Consulta Médica": "Ligue para o número (21) 2606-0708 ou através do nosso WhatsApp (21) 991234-5678. Fale com o Atendente e informe que deseja marcar uma consulta médica. Forneça Suas Informações: seu nome, data de nascimento e detalhes de contato quando solicitado. Escolha uma Data e Hora: Pergunte sobre os horários disponíveis e escolha um que seja conveniente para você.\nConfirme os Detalhes: Verifique se todas as informações, incluindo data, hora e local da consulta, estão corretas. Receba uma Confirmação: Anote qualquer número de referência ou confirmação fornecido pelo atendente.\nChegue à Consulta: No dia e horário marcados, vá à clínica para a consulta médica.",
    "Condições Médicas para Cirurgia": "A cirurgia só será considerada quando há uma necessidade médica, você está em condição estável, concorda com o procedimento, tem uma equipe médica competente de plantão, instalações adequadas disponíveis e o paciente está disposto a seguir cuidados pós-cirúrgicos.",
    "Medicamentos": "Compareça ao setor responsável da sua clínica para dúvidas ou entre em contato pelo WhatsApp (21) 991234-5678 para dúvidas sobre as dosagens, horários e condições para fazer o bom uso do medicamento.",
    "Procedimentos": "Pré-cirúrgico: Antes da cirurgia, você passará por avaliação médica, jejum por um período determinado e seguirá instruções específicas do médico. Certifique-se de entender os detalhes da cirurgia e fazer todas as perguntas que tiver.\nPós-cirúrgico: Após a cirurgia, você será monitorado na sala de recuperação. Depois, seguirá recomendações médicas para repouso, medicamentos e cuidados com feridas, além de acompanhamento médico regular para garantir uma recuperação segura e eficaz. É importante seguir todas as instruções médicas cuidadosamente.",
    "Suporte Psicológico": "Nas suas consultas, você terá um incrível suporte psicológico. Isso significa que um profissional estará disponível para conversar sobre seus sentimentos, preocupações e qualquer estresse relacionado à sua saúde. Eles estão aqui para te ajudar a enfrentar desafios emocionais e a lidar com a jornada da melhor forma possível, proporcionando apoio emocional durante todo o processo.",
    "Emergência": "Para acionar a emergência da clínica, basta ligar para o número de emergência fornecido (por exemplo, 911) e informar que você é paciente da clínica. Explique a situação e forneça sua localização para que a equipe médica possa responder rapidamente às suas necessidades médicas.",
    "Orientações de Primeiros Socorros": "Ferimentos Pequenos e Cortes: Lave e cubra o ferimento.\nQueimaduras Leves: Lave com água fria e proteja.\nEntorses ou Luxações: Imobilize a área afetada.\nReações Alérgicas Leves: Tome um anti-histamínico se disponível.\nDesmaio: Deite-se e levante as pernas.\nParada Respiratória ou Cardíaca: Ligue para o serviço de emergência e inicie a RCP.\nHemorragia Grave: Aplique pressão direta e eleve a área sangrando.\nEngasgo: Tussa vigorosamente ou faça a Manobra de Heimlich.\nSempre lembrando de contatar as autoridades.",
    "Plano de Saúde Individual": "Este plano é para uma única pessoa. Você paga por sua própria cobertura de saúde e recebe serviços médicos de acordo com o plano escolhido. Através de uma das nossas filiais ou Whatsapp (21) 991234-5678. Com seus documentos em mãos você consegue garantir ainda hoje o seu plano de saúde.",
    "Plano de Saúde Familiar": "Este plano cobre toda a sua família, incluindo cônjuge e filhos. Geralmente, é mais econômico do que ter planos individuais separados para cada membro da família. Através de uma das nossas filiais ou Whatsapp (21) 991234-5678. Com seus documentos em mãos você consegue garantir ainda hoje o plano de saúde para sua família.",
    "Plano de Saúde Coletivo": "Este plano é geralmente oferecido por empregadores ou grupos, como sindicatos. Os membros do grupo têm acesso ao mesmo plano de saúde, e os custos são frequentemente compartilhados entre o empregador e os funcionários. Através de uma das nossas filiais ou Whatsapp (21) 991234-5678. Com seus documentos em mãos você consegue garantir ainda hoje o plano de saúde para sua empresa.",
}

# Função para mostrar a resposta de um submenu
def mostrar_resposta_submenu(opcao_submenu):
    resposta = respostas_submenus.get(opcao_submenu)
    if resposta:
        print(resposta)
        escolha = input("Pressione Enter para continuar...")
    else:
      print("Opção inválida. Tente novamente.")

# Função para mostrar um submenu e obter a escolha do usuário
def mostrar_submenu(submenu):
    while True:
        for key, value in submenu.items():
            print(f"[{key}] - {value}")
        escolha_submenu = int(input("Escolha uma opção: "))
        if escolha_submenu in submenu:
            if escolha_submenu == 4:  # Voltar ao Menu Principal
                return
            else:
                mostrar_resposta_submenu(submenu[escolha_submenu])
        else:
            print("Opção inválida. Tente novamente.")

# Loop principal do chatbot
while True:
    mostrar_menu_principal()
    escolha_principal = int(input("Escolha uma opção: "))
    if escolha_principal in menu_principal:
        if escolha_principal == 0:
            print(f"{nome_usuario} obrigado por usar os nossos serviços, volte sempre.")
            break
        elif escolha_principal == 1:
            mostrar_submenu(submenu_saude)
        elif escolha_principal == 2:
            mostrar_submenu(submenu_agendamento)
        elif escolha_principal == 3:
            mostrar_submenu(submenu_informacoes_medicas)
        elif escolha_principal == 4:
            mostrar_submenu(submenu_suporte)
        elif escolha_principal == 5:
            mostrar_submenu(submenu_plano_saude)
        else:
            print("Opção inválida. Tente novamente.")
    else:
        print("Opção inválida. Tente novamente.")
