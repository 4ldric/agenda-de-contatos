# Modulos
from time import sleep
# Funções

def adicionar_contato(contatos, nome, telefone, email):
    contato = {"contato": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"✅ {nome} adicionado com sucesso. Retornando ao menu..")
    sleep(1.1)
    return

def lista_contatos(contatos):
    print("\n== 👤 Lista de contatos ==")
    if not contatos:
        print("\nVocê não possui contatos no momento.")
    else:
        for indice, contato in enumerate(contatos, start = 1):
            status = "⭐" if contato["favorito"] else " "
            nome_contato = contato["contato"]
            print(f"» {indice}. [{status}] {nome_contato}")

def detalhes_contato(indice):
    indice_revisado = indice - 1
    if indice > 0 and indice_revisado in range(len(contatos)):
        nome_contato = contatos[indice_revisado]["contato"]
        telefone = contatos[indice_revisado]["telefone"]
        email = contatos[indice_revisado]["email"]
        favorito = "⭐" if contatos[indice_revisado]["favorito"] else " "
        print("== 📞 Detalhes do Contato ==")
        print(f"""
Nome: {nome_contato} {favorito}
Telefone: {telefone}
E-mail: {email}
""")
    elif indice == 0:
        print("Retornando ao menu...")
        sleep(1.3)
    else:
        print("Digito invalido..")
        sleep(1.3)

def detalhes_favorito(indice):
    indice_revisado = indice - 1
    if indice == 0:
        print("Retornando ao menu...")
        sleep(1.1)
    elif not contatos[indice_revisado]["favorito"]:
        print("\nContato não favoritado ou não existe. Retornando ao menu...")
        sleep(1.1)
    else:
        favorito = "⭐" if contatos[indice_revisado]["favorito"] else " "
        print("== 📞 Detalhes do Contato ==")
        print(f"""
Nome: {contatos[indice_revisado]["contato"]} {favorito}
Telefone: {contatos[indice_revisado]["telefone"]}
E-mail: {contatos[indice_revisado]['email']}""")


def editar_contato(indice):
    print(
        """
» [1]. Nome
» [2]. Telefone
» [3]. E-mail
"""
    )
    editor = int(input("\nDigite a opção que deseja editar: "))
    indice -= 1
    if editor == 1:
        novo_nome = input("Digite o nome atualizado: ")
        contatos[indice]["contato"] = novo_nome
        print("\nNome do contato atualizado com sucesso")
    elif editor == 2:
        novo_telefone = input("Digite o telefone atualizado: ")
        contatos[indice]["telefone"] = novo_telefone
        print("\nTelefone do contato atualizado com sucesso")
    elif editor == 3:
        novo_email = input("Digite o email atualizado: ")
        contatos[indice]["email"] = novo_email
        print("\nE-mail do contato atualizado com sucesso")
    else:
        print("Opção invalida.")
    sleep(1.3)

def favoritar_contato(contatos,indice):
    indice -= 1
    contato = contatos[indice]["contato"]
    if contatos[indice]["favorito"]:
        contatos[indice]["favorito"] = False
        print(f"{contato} removido dos favoritos.")
    else:
        contatos[indice]["favorito"] = True
        print(f"{contato} adicionado aos favoritos.")
        sleep(1.3)

def lista_favoritos(contatos):
    for indice, contato in enumerate(contatos, start = 1):
        if contato['favorito']:
            status =  contato["status"] = "⭐"
            print(f'» {indice}. [{status}] {contato["contato"]}')

def excluir_contato(contatos, indice):
    indice -= 1
    if indice in range(len((contatos))):
        nome = contatos[indice]["contato"]
        del contatos[indice]
        print(f"♻️ {nome} excluido da lista de contatos. Retornando ao menu...")
    elif indice <= 0:
        print("Retornando ao menu...")

    else:
        print("⚠️ Opção invalida ou contato não existe. Retornando ao menu...")
    sleep(1.3)


# Menu
contatos = []
while True:
    print("\n=== ☎️  Menu principal ===")
    print("""
» [1]. Adicionar contato.
» [2]. Visualizar contatos.
» [3]. Editar contato
» [4]. Marcar/desmarcar favorito.
» [5]. Visualizar contatos favoritos.
» [6]. Excluir contato
» [7]. Sair
""")
    try:
        comando = int(input("\nDigite uma opção: "))
        if comando == 1:
            nome = input("digite o nome do contato: ")
            telefone = input("Digite o numero de telefone: ")
            email = input("Digite o email: ")
            adicionar_contato(contatos, nome, telefone, email)
            sleep(1.1)
        elif comando == 2:
            if not contatos:
                print("\nVocê não possui contatos no momento. Retornando ao menu...")
                sleep(1.3)
            else:
                lista_contatos(contatos)
                try:
                    indice = int(input("\ndigite o contato que queira visualizar: "))
                    detalhes_contato(indice)
                    input("\nPressione [0] para voltar ao menu: ")
                except(ValueError, IndexError):
                    print("⚠️  Comando invalido..")
        elif comando == 3:
            if not contatos:
                print("\nVocê não possui contatos no momento. Retornando ao menu...")
                sleep(1.3)
            else:
                lista_contatos(contatos)
                try:
                    indice = int(input("digite o contato que queira editar: "))
                    editar_contato(indice)
                except (ValueError, IndexError):
                    print("⚠️  Comando invalido..")
        elif comando == 4:
            if not contatos:
                print("\nVocê não possui contatos no momento. Retornando ao menu...")
                sleep(1.3)
            else:
                lista_contatos(contatos)
                try:
                    indice = int(input("\nDigite o contato que queira adicionar ou remover dos favoritos: "))
                    favoritar_contato(contatos,indice)
                except(ValueError, IndexError):
                    print("⚠️  Comando invalido..")
        elif comando == 5:
            if not contatos:
                print("\nVocê não possui contatos no momento. Retornando ao menu...")
                sleep(1.3)
            else:
                try:
                    lista_favoritos(contatos)
                    indice = int(input("\nDigite o contato que queira visualizar ou pressione [0] para retornar ao menu: "))
                    detalhes_favorito(indice)
                    input("pressione [0] para retornar ao menu: ")
                    sleep(1)
                except (ValueError, IndexError):
                    print(
                        "\n⚠️ Contato não favoritado ou não existe. Retornando ao menu..."
                    )
        elif comando == 6:
            if not contatos:
                print("\n⚠️ Comando invalido. Retornando ao menu...")
                sleep(1)
            else:
                lista_contatos(contatos)
                try:
                    indice = int(input("\nDigite o contato que queira excluir: "))
                    excluir_contato(contatos, indice)
                except (ValueError,IndexError):
                    print("⚠️  Comando invalido..")
        elif comando == 7:
            print("Saindo...")
            sleep(0.5)
            break
        else:
            print("⚠️ Opção invalida..")
            sleep(0.7)
    except ValueError:
        print("⚠️  Comando invalido..")
        sleep(0.7)
