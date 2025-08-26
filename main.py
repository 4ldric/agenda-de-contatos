# Modulos
from sys import exception

# Funções
def adicionar_contato(contatos, nome, telefone, email):
    contato = {"contato": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f'{nome} adicionado com sucesso.')
    return

# Menu
contatos = []
while True:
    print("=== ☏ Contatos ===")
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
            pass
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
            print("Opção invalida.")
    except exception:
        print("Comando invalido..")