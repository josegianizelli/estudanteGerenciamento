import json

# Função para chamada do primeiro menu e inicio do programa


def primeiroMenu():
    input("Bem vindo! Aperte enter para ir ao menu principal!")

    # Primeiro menu!
    print("------- Menu principal -------")
    print("1. Gerenciar estudantes.")
    print("2. Gerenciar professores.")
    print("3. Gerenciar disciplinas.")
    print("4. Gerenciar turmas.")
    print("5. Gerenciar matrículas.")
    print("0. Sair do menu.")

    return int(input("Digite uma opção válida:"))

# Função do menu de operações para cada opção de menu


def menuOperacoes():
    # Segundo menu!
    print("------- Menu de operações -------")
    print("1. Incluir.")
    print("2. Listar.")
    print("3. Atualizar.")
    print("4. Excluir.")
    print("0. Voltar ao menu principal.")

    return int(input("Digite uma opção válida:"))

# Função para processamento de dados do menu de operações


def processarMenuOperacao(opcao, arquivo, tipo):
    if opcao == 1:
        novoCadastro(arquivo, tipo)
    elif opcao == 2:
        listarCadastros(arquivo, tipo)
    elif opcao == 3:
        editarCadastro(arquivo, tipo)
    elif opcao == 4:
        removerCadastro(arquivo)
    elif opcao == 0:
        print("Voltando ao menu principal!")
        return False
    else:
        print("Opção inválida. Tente novamente.")

    return True


# Funções para todas as entidades (estudantes, professores, disciplinas, turmas, matrículas)
def novoCadastro(arquivo, tipo):
    registros = lerArquivo(arquivo)
    cadastro = {}

    if tipo == "estudante":
        codigo = int(input("Digite o código do estudante: "))
        # Verifica se já existe um estudante com o mesmo código
        if any(registro["codigo"] == codigo for registro in registros):
            print("Esse estudante já é cadastrado no sistema.")
            return  # Sai da função sem cadastrar um novo estudante

        cadastro = {
            "nome": input("Digite o nome do estudante: "),
            "codigo": codigo
        }

    elif tipo == "professor":
        codigo = int(input("Digite o código do professor: "))
        # Verifica se já existe um professor com o mesmo código
        if any(registro["codigo"] == codigo for registro in registros):
            print("Esse professor já é cadastrado no sistema.")
            return  # Sai da função sem cadastrar um novo professor

        cadastro = {
            "nome": input("Digite o nome do professor: "),
            "codigo": codigo,
            "cpf": input("Digite o CPF do professor: ")
        }

    elif tipo == "disciplina":
        codigo = int(input("Digite o código da disciplina: "))
        # Verifica se já existe uma disciplina com o mesmo código
        if any(registro["codigo"] == codigo for registro in registros):
            print("Essa disciplina já é cadastrada no sistema.")
            return  # Sai da função sem cadastrar uma nova disciplina

        cadastro = {
            "nome": input("Digite o nome da disciplina: "),
            "codigo": codigo
        }

    elif tipo == "turma":
        codigo = int(input("Digite o código da turma: "))
        # Verifica se já existe uma turma com o mesmo código
        if any(registro["codigo"] == codigo for registro in registros):
            print("Essa turma já é cadastrada no sistema.")
            return  # Sai da função sem cadastrar uma nova turma

        cadastro = {
            "codigo": codigo,
            "codigo_professor": int(input("Digite o código do professor: ")),
            "codigo_disciplina": int(input("Digite o código da disciplina: "))
        }

    elif tipo == "matricula":
        codigo_turma = int(input("Digite o código da turma: "))
        codigo_estudante = int(input("Digite o código do estudante: "))
        # Verifica se já existe uma matrícula com os mesmos códigos
        if any(registro["codigo_turma"] == codigo_turma and registro["codigo_estudante"] == codigo_estudante for registro in registros):
            print("Essa matrícula já existe no sistema.")
            return  # Sai da função sem cadastrar uma nova matrícula

        cadastro = {
            "codigo_turma": codigo_turma,
            "codigo_estudante": codigo_estudante
        }

    registros.append(cadastro)
    salvarArquivo(registros, arquivo)
    print(f"{tipo.capitalize()} cadastrado com sucesso!")

# Função de cadastro global


def listarCadastros(arquivo, tipo):
    registros = lerArquivo(arquivo)
    if registros:
        print(f"Os registros cadastrados ({tipo}) são:")
        for registro in registros:
            if tipo == "estudante":
                print(f"Nome: {registro['nome']}, Código: {
                      registro['codigo']}")
            elif tipo == "professor":
                print(f"Nome: {registro['nome']}, Código: {
                      registro['codigo']}, CPF: {registro['cpf']}")
            elif tipo == "disciplina":
                print(f"Nome: {registro['nome']}, Código: {
                      registro['codigo']}")
            elif tipo == "turma":
                print(f"Código da turma: {registro['codigo']}, Código do professor: {
                      registro['codigo_professor']}, Código da disciplina: {registro['codigo_disciplina']}")
            elif tipo == "matricula":
                print(f"Código da turma: {registro['codigo_turma']}, Código do estudante: {
                      registro['codigo_estudante']}")
    else:
        print(f"Nenhum registro de {tipo} ainda foi cadastrado!")

# Função de edição de cadastro global


def editarCadastro(arquivo, tipo):
    registros = lerArquivo(arquivo)
    codigoEdit = int(input("Digite o código que você deseja editar: "))
    registroEdit = next(
        (r for r in registros if r["codigo"] == codigoEdit), None)

    if registroEdit is None:
        print(f"Não encontrei o registro com o código {codigoEdit}.")
        return

    if tipo == "estudante":
        registroEdit["nome"] = input("Digite o nome do estudante: ")
        registroEdit["codigo"] = int(input("Digite o código do estudante: "))

    elif tipo == "professor":
        registroEdit["nome"] = input("Digite o nome do professor: ")
        registroEdit["codigo"] = int(input("Digite o código do professor: "))
        registroEdit["cpf"] = input("Digite o CPF do professor: ")

    elif tipo == "disciplina":
        registroEdit["nome"] = input("Digite o nome da disciplina: ")
        registroEdit["codigo"] = int(input("Digite o código da disciplina: "))

    elif tipo == "turma":
        registroEdit["codigo"] = int(input("Digite o código da turma: "))
        registroEdit["codigo_professor"] = int(
            input("Digite o código do professor: "))
        registroEdit["codigo_disciplina"] = int(
            input("Digite o código da disciplina: "))

    elif tipo == "matricula":
        registroEdit["codigo_turma"] = int(input("Digite o código da turma: "))
        registroEdit["codigo_estudante"] = int(
            input("Digite o código do estudante: "))

    salvarArquivo(registros, arquivo)
    print("Registro atualizado com sucesso.")

# Função de remoção de cadastro global


def removerCadastro(arquivo):
    registros = lerArquivo(arquivo)
    codigoRemove = int(input("Digite o código que você deseja remover: "))
    registroRemove = next(
        (r for r in registros if r["codigo"] == codigoRemove), None)

    if registroRemove is None:
        print(f"Não encontrei o registro com o código {codigoRemove}.")
    else:
        registros.remove(registroRemove)
        salvarArquivo(registros, arquivo)
        print("Registro removido com sucesso.")

# Função para salvar os arquivos em json


def salvarArquivo(dados, nomeArquivo):
    with open(nomeArquivo, "w", encoding='utf-8') as arquivoAberto:
        json.dump(dados, arquivoAberto, ensure_ascii=False)

# Função para ler os arquivos em json


def lerArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, "r", encoding='utf-8') as arquivoAberto:
            return json.load(arquivoAberto)
    except FileNotFoundError:
        return []


# Declaração dos arquivos
arquivo_estudante = "cadastro_estudantes.json"
arquivo_professor = "cadastro_professores.json"
arquivo_disciplina = "cadastro_disciplinas.json"
arquivo_turma = "cadastro_turmas.json"
arquivo_matricula = "cadastro_matriculas.json"


# Mensagem de boas-vindas e a criação do loop com while!
while True:
    opcao_menu = primeiroMenu()

    if opcao_menu == 1:
        # Gerenciar estudantes
        while True:
            opcao_operacao = menuOperacoes()
            if not processarMenuOperacao(opcao_operacao, arquivo_estudante, "estudante"):
                break

    elif opcao_menu == 2:
        # Gerenciar professores
        while True:
            opcao_operacao = menuOperacoes()
            if not processarMenuOperacao(opcao_operacao, arquivo_professor, "professor"):
                break

    elif opcao_menu == 3:
        # Gerenciar disciplinas
        while True:
            opcao_operacao = menuOperacoes()
            if not processarMenuOperacao(opcao_operacao, arquivo_disciplina, "disciplina"):
                break

    elif opcao_menu == 4:
        # Gerenciar turmas
        while True:
            opcao_operacao = menuOperacoes()
            if not processarMenuOperacao(opcao_operacao, arquivo_turma, "turma"):
                break

    elif opcao_menu == 5:
        # Gerenciar matrículas
        while True:
            opcao_operacao = menuOperacoes()
            if not processarMenuOperacao(opcao_operacao, arquivo_matricula, "matricula"):
                break

    elif opcao_menu == 0:
        print("Saindo do programa.")
        break
