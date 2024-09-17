# Declaração da lista
estudantes = []

# Mensagem de boas vindas e a criação do loop com while!
while True:

    input("Bem vindo! Aperte enter para ir ao menu principal!")

    # Primeiro menu!
    print("------- Menu principal -------")

    print("1. Gerenciar estudantes.")
    print("2. Gerenciar professores.")
    print("3. Gerenciar disciplinas.")
    print("4. Gerenciar turmas.")
    print("5. Gerenciar matrículas.")
    print("0. Sair do menu.")

    opcao = int(input("Digite uma opção válida:"))

    if opcao == 1:
        print(f"Você escolheu a opção: {opcao}")
        print("A opção escolhida é válida!")

        # Segundo loop com o segundo menu!
        while True:
            # Segundo menu!
            print("------- Menu de operações -------")

            print("1. Incluir.")
            print("2. Listar.")
            print("3. Atualizar.")
            print("4. Excluir.")
            print("0. Voltar ao menu principal.")

            opcao2 = int(input("Digite uma opção válida:"))

            if opcao2 >= 1 and opcao2 <= 4:
                print(f"Você escolheu a opção: {opcao2}")
                print("A opção escolhida é válida!")

            if opcao2 == 0:
                print("Voltando ao menu principal!")
                break  # Aqui faz com que volte para o menu principal!

            if opcao2 == 1:
                novoEstudante = {
                    "nome": input("Digite o nome do estudante: "),
                    "codigo": int(input("Digite o codigo do estudante: ")),
                    "cpf": input("Digite o cpf do estudante: ")
                }
                estudantes.append(novoEstudante)

            if opcao2 == 2:
                if estudantes:
                    print("Os estudantes cadastrados são:")
                    for estudante in estudantes:
                        print(f"Nome: {estudante['nome']}, Código: {
                            estudante['codigo']}, CPF: {estudante['cpf']}")

                else:
                    print("Nenhum estudante ainda foi cadastrado!")

            if opcao2 == 3:
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

            if opcao2 == 4:
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

    if opcao == 0:
        print("Saindo do menu...")
        break  # Sai do loop while quando a opção for escolhida.

    else:
        print("Você escolheu uma opção inválida!")
        continue  # Caso seja escolhida uma opção invalida o loop para.
