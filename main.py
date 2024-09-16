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

        # Declaração da lista
        estudantes = []

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
                estudantes.append(input("Escreva o nome do estudante:"))
                # print(estudantes) Retirado pois toda vez que incluia o nome printava todos os nomes incluidos.

            if opcao2 == 2:
                estudantes.sort()

                if estudantes:
                    print(f"Os estudantes cadastrados são: {estudantes}")

                else:
                    print("Nenhum estudante ainda foi cadastrado!")

            if opcao2 == 3:
                print("A opção ainda esta em desenvolvimento.")

            if opcao2 == 4:
                print("A opção ainda esta em desenvolvimento.")

    if opcao == 0:
        print("Saindo do menu...")
        break  # Sai do loop while quando a opção for escolhida.

    if opcao >= 2 and opcao <= 5:
        print(f"Você escolheu a opção {opcao}.")
        print("Essa opção ainda está em desenvolvimento.")
        continue

    else:
        print("Você escolheu uma opção inválida!")
        continue  # Caso seja escolhida uma opção invalida o loop para.
