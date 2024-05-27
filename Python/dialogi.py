from datetime import datetime

banco_de_dados = []

def iniciar_dialogo():
    print("Bem-vindo ao nosso projeto ambiental!")
    contribuicao = input("Você gostaria de contribuir com a nossa causa ambiental? (sim/não): ").strip().lower()

    if contribuicao in ("não", "nao"):
        print("Agradecemos pelo seu tempo. Tenha um ótimo dia!")
        return

    if contribuicao == "sim":
        anonimo = input("Você gostaria de contribuir de forma anônima? (sim/não): ").strip().lower()

        if anonimo == "sim":
            print("Agradecemos pela sua contribuição anônima!")
            armazenar_contribuicao({}, anonimo=True)
            return

        if anonimo in ("não", "nao"):
            login_opcao = input("Você já possui cadastro? (sim/não): ").strip().lower()

            if login_opcao == "sim":
                login()
            elif login_opcao in ("não", "nao"):
                respostas = coletar_informacoes()
                armazenar_contribuicao(respostas, anonimo=False)
            else:
                print("Opção inválida. Por favor, responda com 'sim' ou 'não'.")
                iniciar_dialogo()
            return

    print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")
    iniciar_dialogo()

def coletar_informacoes():
    respostas = {}

    # Perguntas para o usuário
    perguntas = [
        ("Qual é o seu nome?", "nome"),
        ("Qual é a sua data de nascimento? (DD/MM/AAAA)", "data_nascimento"),
        ("Digite seu email:", "email"),
        ("Digite um nome de usuário para login:", "usuario"),
        ("Digite uma senha para login (mínimo 6 caracteres):", "senha")
    ]

    print("Por favor, responda às seguintes perguntas:")

    for pergunta, chave in perguntas:
        resposta = input(pergunta + " ").strip()
        # Validar formato da data de nascimento
        if chave == "data_nascimento":
            while not validar_data_nascimento(resposta):
                print("Formato de data de nascimento inválido. Por favor, digite novamente.")
                resposta = input(pergunta + " ").strip()
            # Verificar se a idade é maior ou igual a 18 anos
            if not verificar_maioridade(resposta):
                print("Você precisa ter mais de 18 anos para se cadastrar.")
                return coletar_informacoes()
        # Validar formato do email
        if chave == "email":
            while not validar_email(resposta):
                print("Formato de email inválido. Por favor, digite novamente.")
                resposta = input(pergunta + " ").strip()
        # Validar formato da senha
        if chave == "senha":
            while not validar_senha(resposta):
                print("Senha muito curta. A senha deve ter no mínimo 6 caracteres. Por favor, digite novamente.")
                resposta = input(pergunta + " ").strip()
        respostas[chave] = resposta

    return respostas

def armazenar_contribuicao(dados, anonimo):
    if anonimo:
        print("Contribuição armazenada anonimamente.")
        print("\nObrigado por sua contribuição! Você pode fazer uma doação clicando no link abaixo:")
        print("https://www.doeagora.com")  # Link de exemplo
    else:
        banco_de_dados.append(dados)
        print("\nSuas respostas foram armazenadas com sucesso:")
        for chave, resposta in dados.items():
            if chave != "senha":
                print(f"{chave.capitalize()}: {resposta}")
        print("\nObrigado por se cadastrar! Você pode fazer uma doação clicando no link abaixo:")
        print("https://www.doeagora.com")  # Link de exemplo

def login():
    print("\nLogin")
    usuario = input("Digite seu nome de usuário: ").strip()
    senha = input("Digite sua senha: ").strip()

    for usuario_cadastrado in banco_de_dados:
        if usuario_cadastrado["usuario"] == usuario and usuario_cadastrado["senha"] == senha:
            print("Login bem-sucedido!")
            print("Suas informações:")
            for chave, resposta in usuario_cadastrado.items():
                if chave != "senha":
                    print(f"{chave.capitalize()}: {resposta}")
            print("\nObrigado por sua contribuição! Você pode fazer uma doação clicando no link abaixo:")
            print("https://www.doeagora.com")  # Link de exemplo
            return

    print("Nome de usuário ou senha incorretos. Tente novamente.")
    login()

def validar_data_nascimento(data):
    # Verificar se a data possui o formato DD/MM/AAAA
    partes = data.split('/')
    if len(partes) != 3:
        return False
    dia, mes, ano = partes
    return dia.isdigit() and mes.isdigit() and ano.isdigit() and len(dia) == 2 and len(mes) == 2 and len(ano) == 4

def verificar_maioridade(data_nascimento):
    # Verificar se o usuário é maior de 18 anos
    hoje = datetime.now()
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade >= 18

def validar_email(email):
    # Verificar se o email possui o formato válido
    return '@' in email and '.' in email

def validar_senha(senha):
    # Verificar se a senha tem pelo menos 6 caracteres
    return len(senha) >= 6

if __name__ == "__main__":
    iniciar_dialogo()






