def adicionar_contatos(agenda):
    nome = input("Digite um nome: ")
    twitter = input("Digite a conta do Twitter:  ")
    facebook = input("Digite a sua conta do facebook:  ")
    instagram = input("Digite a conta do Instagram: ")
    telefone = input("Digite o número de telefone: ")
    email = input("Digite um e-mail válido para fazer o seu login : ")
    agenda[nome] = {"telefone": telefone, "email": email, "twitter": twitter, "instagram": instagram, "facebook": facebook}
    print(f"Contato {nome} adicionado.")

def procurar_contatos(agenda):
    nome = input("Digite o nome do contato que deseja consultar: ")
    
    if nome in agenda:
        print(f"Contato {nome}:")
        print(f"facebook: {agenda[nome]['facebook']}")
        print(f"Telefone: {agenda[nome]['telefone']}")
        print(f"E-mail: {agenda[nome]['email']}")
        print(f"Twitter: {agenda[nome]['twitter']}")
        print(f"Instagram: {agenda[nome]['instagram']}")
    else:
        print(f" não foi possível encontrar o Contato {nome} .")

def remover_contatos(agenda):
    nome = input("Digite o nome do contato que você quer remover: ")
    
    if nome in agenda:
        del agenda[nome]
        print(f" seu Contato {nome} foi excluido com sucesso.")
    
    else:
        print(f" seu Contato {nome} não encontrado.")

def atualizar_contato(agenda):
    nome_de_usuario = input("Digite o nome do contato que você quer alterar : ")
   
   
    if nome_de_usuario in agenda:
        telefone = input("Digite o novo número de telefone: ")
        email = input("Digite o novo e-mail: ")
        twitter = input("Digite a nova conta do Twitter: ")
        instagram = input("Digite a nova conta do Instagram: ")
        facebook = input("Digite sua nova conta do facebook")
        
        agenda[nome_de_usuario] = {"telefone": telefone, "email": email, "twitter": twitter, "instagram": instagram, "facebook": facebook}
        print(f"Contato {nome_de_usuario} alterado.")
    
    else:
        print(f" seu Contato {nome_de_usuario} não encontrado.")

def adicionar_varios_contatos(agenda):
    contatos2 = int(input("Quantos contatos você quer adicionar? "))
    
    for i in range(contatos2):
        nome = input(f"Digite o nome do contato {i+1}: ")
        twitter = input(f"Digite a conta do Twitter do contato {i+1}: ")
        instagram = input(f"Digite a conta do Instagram do contato {i+1}: ")
        telefone = input(f"Digite o número de telefone do contato {i+1}: ")
        email = input(f"Digite um e-mail válido para fazer o login do contato {i+1}: ")
        facebook = input(f"Digite a conta do facebook do contato {i+1}: ")
        
        agenda[nome] = {"telefone": telefone, "email": email, "twitter": twitter, "instagram": instagram, "facebook": facebook}
    
    print(f"{contatos2} contatos adicionados.")

def gerar_relatorio(agenda):
    print("Nro Nome e-mail Twitter Facebook")
    for i, (nome, contato) in enumerate(agenda.items()):
        print(f"{i+1} {nome} {contato['email']} {contato['twitter']} {contato['facebook']}")

def main():
    agenda = {}

    while True:
        print("olá esse é o menu, selecione algo:")
        print("1- deseja Inserir um novo contato ? ")
        print("2- deseja fazer a consulta de um contato ?")
        print('3- deseja remover um contato ? ')
        print('4- deseja alterar um contato ? ')
        print('5- deseja inserir vários contatos ? ')
        print('6- deseja gerar um relatório ? ')
        print('7- deseja sair? selecione esse alternativa')
        break

if __name__ == '__main__':
    main()
