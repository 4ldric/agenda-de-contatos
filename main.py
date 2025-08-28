# Modulos
from sys import exception

# Funções
def adicionar_contato(contatos, nome, telefone, email):
    contato = {"contato": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"✅ {nome} adicionado com sucesso.")
    return

def lista_contatos(contatos):
    print("\n== 👤 Lista de contatos ==")
    for indice, contato in enumerate(contatos, start = 1):
        status = "⭐" if contato["favorito"] else " "
        nome_contato = contato["contato"]
        print(f"» {indice}. [{status}] {nome_contato}")
    print("\nPressione [0] para voltar ao menu.")

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
E-mail: {email}""")
    elif indice == 0:
        print("Retornando ao menu...")
    else:
        print("Digito invalido..")

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

def favoritar_contato(contatos,indice):
    indice -= 1
    contato = contatos[indice]["contato"]
    if contatos[indice]["favorito"]:
        contatos[indice]["favorito"] = False
        print(f"{contato} removido dos favoritos.")
    else:
        contatos[indice]["favorito"] = True
        print(f"{contato} adicionado aos favoritos.")

def lista_favoritos(contatos):
    for indice, contato in enumerate(contatos, start = 1):
        if contato['favorito']:
            status =  contato["status"] = "⭐"
            print(f'» {indice}. [{status}] {contato["contato"]}')
    print("retornando ao menu..")

def excluir_contato(contatos, indice):
    indice -= 1
    if indice in range(len((contatos))):
        nome = contatos[indice]["contato"]
        del contatos[indice]
        print(f"{nome} excluido da lista de contatos.")
    else:
        print("Opção invalida, ou contato não existe.")

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
    comando = int(input("\nDigite uma opção: "))
    try:
        if comando == 1:
            nome = input("digite o nome do contato: ")
            telefone = int(input("Digite o numero de telefone: "))
            email = input("Digite o email: ")
            adicionar_contato(contatos, nome, telefone, email)
        elif comando == 2:
            lista_contatos(contatos)
            indice = int(input("digite o contato que queira visualizar: "))
            detalhes_contato(indice)
        elif comando == 3:
            lista_contatos(contatos)
            indice = int(input("digite o contato que queira editar: "))
            editar_contato(indice)
        elif comando == 4:
            lista_contatos(contatos)
            indice = int(input("Digite o contato que queira adicionar ou remover dos favoritos: "))
            favoritar_contato(contatos,indice)
        elif comando == 5:
            lista_favoritos(contatos)
        elif comando == 6:
            lista_contatos(contatos)
            indice = int(input("Digite o contato que queira excluir: "))
            excluir_contato(contatos,indice)
        elif comando == 7:
            print("Saindo...")
            break
        else:
            print("⚠️ Opção invalida..")
    except exception:
        print("⚠️ Comando invalido..")
