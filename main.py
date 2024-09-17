# Declaração da lista
estudantes = []


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


def menuOperacoes():
    # Segundo menu!
    print("------- Menu de operações -------")

    print("1. Incluir.")
    print("2. Listar.")
    print("3. Atualizar.")
    print("4. Excluir.")
    print("0. Voltar ao menu principal.")

    return int(input("Digite uma opção válida:"))


def novoCadastro(estudantes):
    cadastro = {
        "nome": input("Digite o nome do estudante: "),
        "codigo": int(input("Digite o codigo do estudante: ")),
        "cpf": input("Digite o cpf do estudante: ")
    }
    estudantes.append(cadastro)


def listarCadastros(estudantes):
    if estudantes:
        print("Os estudantes cadastrados são:")
        for estudante in estudantes:
            print(f"Nome: {estudante['nome']}, Código: {
                estudante['codigo']}, CPF: {estudante['cpf']}")

    else:
        print("Nenhum estudante ainda foi cadastrado!")


def editarCadastro(estudantes):
    estudanteEdit = None
    codigoEdit = int(
        input("Digite o codigo do aluno que você deseja editar: "))

    for dicionarioEstudante in estudantes:
        if dicionarioEstudante["codigo"] == codigoEdit:
            estudanteEdit = dicionarioEstudante
            break

    if estudanteEdit is None:
        print(f"Não encontrei o estudante com o codigo {
              codigoEdit} na lista.")

    else:
        estudanteEdit["nome"] = (
            input("Digite o novo nome do estudante: "))
        estudanteEdit["codigo"] = int(
            input("Digite o novo codigo do estudante: "))
        estudanteEdit["cpf"] = (
            input("Digite o novo cpf do estudante: "))


def removerCadastro(estudantes):
    estudantRemove = None
    codigoRemove = int(
        input("Digite o codigo do aluno que você deseja remover: "))

    for dicionarioRemove in estudantes:
        if dicionarioRemove["codigo"] == codigoRemove:
            estudantRemove = dicionarioRemove
            break

    if estudantRemove is None:
        print(f"Não encontrei o estudante com o codigo {
            codigoRemove} na lista. ")

    else:
        estudantes.remove(estudantRemove)
        print("Estudante removido com sucesso.")


# Mensagem de boas vindas e a criação do loop com while!
while True:
    opcao_menu = primeiroMenu()

    # Segundo loop com o segundo menu!
    while opcao_menu == 1:

        opcao = menuOperacoes()

        if opcao >= 1 and opcao <= 4:
            print(f"Você escolheu a opção: {opcao}")
            print("A opção escolhida é válida!")

        if opcao == 0:
            print("Voltando ao menu principal!")
            break  # Aqui faz com que volte para o menu principal!

        if opcao == 1:
            novoCadastro(estudantes)

        if opcao == 2:
            listarCadastros(estudantes)

        if opcao == 3:
            editarCadastro(estudantes)

        if opcao == 4:
            removerCadastro(estudantes)

    if opcao_menu >= 2 and opcao_menu <= 5:
        print("Opção ainda em desenvolvimento...")
        continue

    if opcao_menu == 0:
        print("Saindo do menu...")
        break  # Sai do loop while quando a opção for escolhida.

    else:
        print("Você escolheu uma opção inválida!")
