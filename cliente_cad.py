import sqlite3

#=========================================================

banco = sqlite3.connect('banco_cadastro.db')
cursor = banco.cursor()
#cursor.execute("CREATE TABLE clientes (nome text, idade integer, email text)")

#=========================================================

contador = 0
while contador < 10:

    print("============================")
    print("OQUE DESEJA FAZER?")
    print("============================")
    print("ADICIONAR CLIENTE---Digite 1\nATUALIZAR CLIENTES--Digite 2\nREMOVER CLIENTE-----Digite 3\nVER CLIENTES--------Digite 4")
    print("============================")
    resposta_principal = input("Insira aqui o número...")

    if resposta_principal == "1":
        resposta_nome = input("Escreva aqui o nome e sobrenome do cliente...")
        resposta_idade = input("Escreva aqui a idade do cliente...")
        resposta_email = input("Escreva aqui o email do cliente...")
    
    #==================================================================================================================

        cursor.execute("INSERT INTO clientes VALUES ('"+resposta_nome+"', "+str(resposta_idade)+", '"+resposta_email+"')")
        banco.commit()
        print("Os dados foram adicinados com sucesso!!!")
    
    #==================================================================================================================

    if resposta_principal == "2":
        print("============================")
        print("SE DESEJA ALTERAR O NOME - DIGITE 1\n SE DESEJA ALTERAR A IDADE - digite 2\n deseja alterar o email digite 3")
        print("============================")

        resposta_1 = input("Escreva aqui oque deseja fazer...")

        if resposta_1 == "1":
            nome_cliente_antigo = input("Escreva o nome registrado que deseja mudar...")
            nome_cliente_novo = input("Escreva aqui o novo nome que deseja substituir...")
            try:
                cursor.execute("UPDATE clientes SET nome = ('"+nome_cliente_novo+"') WHERE nome = ('"+nome_cliente_antigo+"')")
                banco.commit()
                print("Os dados foram alterados com sucesso!!!")
            except Exception as erro:
                print("Não existe esse usuário")
                print(erro)


        if resposta_1 == "2":
            idade_antiga = input("Escreva a idade registrado que deseja mudar...")
            idade_nova = input("Escreva aqui a nova idade que deseja substituir...")
            try:
                cursor.execute("UPDATE clientes SET idade = ('"+idade_nova+"') WHERE idade = ('"+idade_antiga+"')")
                banco.commit()
                print("Os dados foram alterados com sucesso!!!")
            except Exception as erro:
                print("Não existe esse usuário")
                print(erro)


        if resposta_1 == "3":
            email_antigo = input("Escreva o email registrado que deseja mudar...")
            email_novo = input("Escreva aqui o novo email que deseja substituir...")
            try:
                cursor.execute("UPDATE clientes SET email = ('"+email_novo+"') WHERE email = ('"+email_antigo+"')")
                banco.commit()
                print("Os dados foram alterados com sucesso!!!")
            except Exception as erro:
                print("Não existe esse usuário")
                print(erro)


        else:
            print("Número INVÁLIDO")


    if resposta_principal == "3":
        resposta_rem = input("Insira o nome completo do cliente que deseja remover...")

        try:
            cursor.execute("DELETE FROM clientes WHERE nome = ('"+resposta_rem+"')")
            banco.commit()  
            print("Os dados foram deletados com sucesso!!!")

        except sqlite3.Error as erro:
            print("Erro ao excluir o arquivo: ", erro)