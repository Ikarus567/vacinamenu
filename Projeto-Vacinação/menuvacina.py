from sistemamenu import SistemaVacinacao

sistema = SistemaVacinacao() #cria o sistema

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar pessoa")
    print("2 - Imprimir Pessoas da Fila")
    print("3 - Imprimir quantas doses tem disponíveis")
    print("4 - Vacinar uma pessoa")
    print("5 - Exibir total de pessoas vacinadas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        cpf = input("CPF: ")
        print(sistema.adicionar_pessoa(nome, cpf))

    elif opcao == "2":
        sistema.imprimir_fila()

    elif opcao == "3":
        print(f"\nDoses disponíveis: {sistema.doses_restantes()}")

    elif opcao == "4":
        print(sistema.vacinar_pessoa())

    elif opcao == "5":
        print(f"\nTotal de vacinados: {sistema.total_vacinados()}")

    elif opcao == "0":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida!")
