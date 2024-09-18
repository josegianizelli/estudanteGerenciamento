import json


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


def processarMenuOperacao(opcao, arquivo):
    if opcao == 1:
        novoCadastro(arquivo)
    elif opcao == 2:
        listarCadastros(arquivo)
    elif opcao == 3:
        editarCadastro(arquivo)
    elif opcao == 4:
        removerCadastro(arquivo)
    elif opcao == 0:
        print("Voltando ao menu principal!")
        return False
    else:
        print("Opção inválida. Tente novamente.")

    return True


# Funções para todas as entidades (estudantes, professores, disciplinas, turmas, matrículas)
def novoCadastro(arquivo):
    registros = lerArquivo(arquivo)
    cadastro = {
        "nome": input("Digite o nome: "),
        "codigo": int(input("Digite o codigo: "))
    }
    registros.append(cadastro)
    salvarArquivo(registros, arquivo)
    print(f"{cadastro['nome']} cadastrado com sucesso!")


def listarCadastros(arquivo):
    registros = lerArquivo(arquivo)
    if registros:
        print("Os registros cadastrados são:")
        for registro in registros:
            print(f"Nome: {registro['nome']}, Código: {registro['codigo']}")
    else:
        print("Nenhum registro ainda foi cadastrado!")


def editarCadastro(arquivo):
    registros = lerArquivo(arquivo)
    codigoEdit = int(input("Digite o código que você deseja editar: "))
    registroEdit = next(
        (r for r in registros if r["codigo"] == codigoEdit), None)

    if registroEdit is None:
        print(f"Não encontrei o registro com o código {codigoEdit}.")
    else:
        registroEdit["nome"] = input("Digite o novo nome: ")
        registroEdit["codigo"] = int(input("Digite o novo código: "))
        salvarArquivo(registros, arquivo)
        print("Registro atualizado com sucesso.")


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


def salvarArquivo(dados, nomeArquivo):
    with open(nomeArquivo, "w", encoding='utf-8') as arquivoAberto:
        json.dump(dados, arquivoAberto, ensure_ascii=False)


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
            if not processarMenuOperacao(opcao_operacao, arquivo_estudante):
                break

    elif opcao_menu == 2:
        # Gerenciar professores
        while True:
            opcao_operacao = menuOperacoes()
            if not processarMenuOperacao(opcao_operacao, arquivo_professor):
                break

    elif opcao_menu == 3:
        # Gerenciar disciplinas
        while True:
            opcao_operacao = menuOperacoes()
            if not processarMenuOperacao(opcao_operacao, arquivo_disciplina):
                break

    elif opcao_menu == 4:
        # Gerenciar turmas
        while True:
            opcao_operacao = menuOperacoes()
            if not processarMenuOperacao(opcao_operacao, arquivo_turma):
                break

    elif opcao_menu == 5:
        # Gerenciar matrículas
        while True:
            opcao_operacao = menuOperacoes()
            if not processarMenuOperacao(opcao_operacao, arquivo_matricula):
                break

    elif opcao_menu == 0:
        print("Saindo do programa.")
        break
