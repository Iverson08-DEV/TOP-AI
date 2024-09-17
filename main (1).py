# chatbot_logic.py

import random

# Frases de saudação e despedida
GREETING_INPUTS = ("olá", "oi", "saudações", "bom dia", "boa tarde", "boa noite")
GREETING_RESPONSES = ["Olá!", "Oi, como posso te ajudar?", "Olá, o que você precisa saber hoje?", "Oi!"]
EXIT_INPUTS = ("tchau", "obrigado", "até logo", "valeu", "sair", "fechar")
EXIT_RESPONSES = ["Até logo!", "Obrigado por falar conosco!", "Tenha um bom dia!"]

# Procedimentos operacionais para TOTVS RM e TOPCONECTA
procedimentos_rm = {
    "gerar nota fiscal": """1. Emissão de Nota Fiscal no TOTVS RM:
Acesse o módulo de Faturamento: Procure pelo módulo "Faturamento" ou "NF-e" no menu principal do TOTVS RM.
Crie uma nova nota fiscal: Clique no botão "Nova Nota Fiscal" ou "Emitir Nota Fiscal".
Preencha os dados da nota fiscal:
Dados do Cliente: Selecione o cliente ou insira os dados manualmente.
Itens da Nota: Adicione os produtos ou serviços com a descrição, quantidade e valor unitário.
Impostos: Selecione o tipo de imposto e os valores aplicáveis.
Verifique e finalize: Revise os dados da nota fiscal e finalize a emissão.
Imprima ou envie a nota fiscal: Imprima a nota fiscal ou envie-a eletronicamente para o cliente.""",
    "emitir relatório financeiro": "Acesse o módulo Finanças do TOTVS RM, selecione o relatório desejado e gere o relatório.",
    "registrar fornecedor": "No módulo de Compras do TOTVS RM, clique em 'Novo Fornecedor' e preencha os dados.",
    "integração bancária": "Vá ao módulo de Finanças e siga os passos para a integração bancária no TOTVS RM."
}

procedimentos_topconecta = {
    "gerar nota fiscal": """1. Emissão de Nota Fiscal no TOPCONECTA:
Acesse o módulo de Faturamento: Procure pelo módulo 'Faturamento' no TOPCONECTA.
Crie uma nova nota fiscal: Clique em 'Nova Nota' e preencha os dados necessários.
Finalize e envie a nota fiscal: Verifique os detalhes e envie eletronicamente.""",
    "emitir relatório financeiro": "Acesse o módulo Relatórios no TOPCONECTA e escolha o tipo de relatório financeiro para gerar.",
    "registrar fornecedor": "Vá ao módulo de Compras do TOPCONECTA, clique em 'Adicionar Fornecedor' e preencha os dados.",
    "integração bancária": "Use o módulo de Finanças no TOPCONECTA para configurar a integração bancária."
}

# Lista de apelidos que se referem ao TOTVS RM
rm_aliases = ["rm", "totvs rm", "sistema rm", "erp rm"]

# Adicionando também o TOPCONECTA como outro sistema
topconecta_aliases = ["topconecta", "top conecta", "sistema topconecta"]

# Variável de estado para armazenar a escolha do sistema
chosen_system = None

# Função para respostas de saudação
def greeting(sentence):
    if any(word in sentence for word in GREETING_INPUTS):
        return random.choice(GREETING_RESPONSES)
    return None

# Função para encerrar a conversa
def end_conversation(sentence):
    if any(word in sentence for word in EXIT_INPUTS):
        return random.choice(EXIT_RESPONSES)
    return None

# Função principal do chatbot
def chatbot_response(user_input):
    global chosen_system  # Variável para rastrear o sistema escolhido pelo usuário
    user_input = user_input.lower()

    # Verifica saudações
    greet = greeting(user_input)
    if greet:
        return greet

    # Verifica encerramento
    exit_resp = end_conversation(user_input)
    if exit_resp:
        return exit_resp

    # Se o sistema já foi escolhido, responde baseado nesse sistema
    if chosen_system:
        if chosen_system == "TOTVS RM":
            for key in procedimentos_rm:
                if key in user_input:
                    return procedimentos_rm[key]
        elif chosen_system == "TOPCONECTA":
            for key in procedimentos_topconecta:
                if key in user_input:
                    return procedimentos_topconecta[key]
        return "Desculpe, não encontrei o procedimento que você está procurando. Pergunte novamente."

    # Verifica se o usuário mencionou "nota fiscal" sem especificar o sistema
    if "nota fiscal" in user_input and not any(alias in user_input for alias in rm_aliases + topconecta_aliases):
        return "Você gostaria de saber como emitir uma nota fiscal no TOTVS RM ou no TOPCONECTA?"

    # Verifica se o usuário mencionou um dos sistemas diretamente após a pergunta
    if "totvs rm" in user_input:
        chosen_system = "TOTVS RM"
        return "Você escolheu o TOTVS RM. Pergunte sobre nota fiscal, relatório financeiro ou outro procedimento."

    if "topconecta" in user_input:
        chosen_system = "TOPCONECTA"
        return "Você escolheu o TOPCONECTA. Pergunte sobre nota fiscal, relatório financeiro ou outro procedimento."

    # Verifica outros procedimentos ou TOTVS RM
    for key in procedimentos_rm:
        if key in user_input:
            return "Você gostaria de saber isso no TOTVS RM ou no TOPCONECTA?"

    return "Desculpe, não entendi sua pergunta. Pergunte sobre procedimentos ou sistemas como TOTVS RM ou TOPCONECTA."
