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
        print("Pressione [0] para voltar ao menu.")

def detalhes_contato(indice):
    if indice > 0:
        indice -= 1
        nome_contato = contatos[indice]["contato"]
        telefone = contatos[indice]["telefone"]
        email = contatos[indice]["email"]
        favorito = "⭐" if contatos[indice]["favorito"] else " "
        print("== 📞 Detalhes do Contato ==")
        print(f"""
Nome: {nome_contato} {favorito}
Telefone: {telefone}
E-mail: {email}""")
    elif indice == 0:
        print("Retornando ao menu...")
    else:
        print("Digito invalido..")


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
            pass
        elif comando == 4:
            pass
        elif comando == 5:
            pass
        elif comando == 6:
            pass
        elif comando == 7:
            print("Saindo...")
            break
        else:
            print("⚠️ Opção invalida..")
    except exception:
        print("⚠️ Comando invalido..")
