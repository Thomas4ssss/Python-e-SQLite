import sqlite3

#=========================================================

banco = sqlite3.connect('banco_cadastro.db')
cursor = banco.cursor()
#cursor.execute("CREATE TABLE estoque (Produto text, Quantidade integer, Preço int)")

#=========================================================

contador = 0
while contador < 10:

    print("==========================================")
    print("OQUE DESEJA FAZER?")
    print("==========================================")
    print("ADICONAR UM ITEM------------------Digite 1\nVER ESTOQUES----------------------Digite 2\nREMOVER CADASTRO DE UM PRODUTO----Digite 3\nPARA ATUALIZAR UM CADASTRO--------DIGITE 4")
    print("==========================================")

    resposta = int(input("Escreva aqui o número...\n"))

#==================================================================================================================

    if resposta == 1:
        print("==========================================")
        print("Se deseja recomeçar digite 0 onde quiser.")
        print("==========================================")
        try:
            nome_prod = str(input("Escreva aqui o produto para adicionar...\n"))
            num_de_prod = input("Escreva aqui a quantidade deste produto...\n")
            prec_prod = input ("Digite o valor unitário do produto (no lugar onde haverá vírgula coloque ponto)...\n")
            if nome_prod == "0":
                print("Recomençando o sistema.")
                break
            else:
                if num_de_prod == 0:
                    break
                else:
                    nome_prod = nome_prod.upper()
                    cursor.execute("INSERT INTO estoque VALUES ('"+nome_prod+"', "+str(num_de_prod)+", "+str(prec_prod)+")")
                    banco.commit()
                    print("Os dados foram adicinados com sucesso!!!")
        except Exception as erro:
            print("Credenciais inválidas!")
            print(erro)

#==================================================================================================================

    if resposta == 2:
        cursor.execute("SELECT * FROM estoque")
        db = cursor.fetchall()
        for lista in db:
            print(lista)
        
#==================================================================================================================

    if resposta == 3:
        try:    
            print("==========================================")
            print("Se deseja recomeçar digite 0 na aba quantidade de produtos.")
            print("==========================================")
            nome_prod = str(input("Escreva aqui o produto para remover..."))
            if nome_prod == 0:
                break
            else:
                nome_prod = nome_prod.upper()
                cursor.execute("DELETE FROM estoque WHERE Produto = ('"+nome_prod+"')")
                banco.commit()  
                print("Os dados foram deletados com sucesso!!!")
            
        except sqlite3.Error as erro:
            print("Erro ao excluir o arquivo: ", erro)
            
#==================================================================================================================

    if resposta == 4:
        print("==========================================")
        print("SE DESEJA MUDAR O NOME------------DIGITE 1\nSE DESEJA MUDAR A QUANTIDADE------DIGITE 2\nSE DESEJA MUDAR O PREÇO-----------DIGITE 3")
        print("==========================================")
        print("Se deseja recomeçar digite 0.")
        print("==========================================")
        
        resposta_att = int(input("Digite aqui o número...\n"))
        if resposta_att == 0:
            break
        else:
            if resposta_att == 1:
                print("==========================================")
                print("Se deseja recomeçar digite 0 em qualquer aba.")
                print("==========================================")
                nome_prod_antigo = input("Escreva o nome registrado do produto que deseja mudar...")
                if nome_prod_antigo == 0:
                    break
                else:
                    nome_prod_novo = input("Escreva aqui o novo nome do produto para a substituição...")
                    if nome_prod_novo == 0:
                        break
                    else:
                        try:
                            nome_prod_antigo = nome_prod_antigo.upper()
                            nome_prod_novo = nome_prod_novo.upper()
                            cursor.execute("UPDATE estoque SET Produto = ('"+nome_prod_novo+"') WHERE Produto = ('"+nome_prod_antigo+"')")
                            banco.commit()
                            print("Os dados foram alterados com sucesso!!!")
                        except Exception as erro:
                            print("Credenciais inválidas!")
                            print(erro)

            if resposta_att == 2:
                print("==========================================")
                print("Se deseja recomeçar digite 0 em qualquer aba.")
                print("==========================================")
                qnt_prod_antigo = input("Escreva o nome registrado do produto para mudar a quantidade...\n")
                if qnt_prod_antigo == 0:
                    break
                else:
                    qnt_prod_novo = input("Escreva aqui a nova quantidade para o produto citado...\n")
                    if qnt_prod_novo == 0:
                        break
                    else:
                        try:
                            qnt_prod_antigo = qnt_prod_antigo.upper()
                            cursor.execute("UPDATE estoque SET Quantidade = ('"+qnt_prod_novo+"') WHERE Produto = ('"+qnt_prod_antigo+"')")
                            banco.commit()
                            print("Os dados foram alterados com sucesso!!!")
                        except Exception as erro:
                            print("Credenciais inválidas!")
                            print(erro)
            if resposta_att == 3:
                print("==========================================")
                print("Se deseja recomeçar digite 0 em qualquer aba.")
                print("==========================================")
                prec_prod_antigo = input("Escreva o nome registrado do produto para mudar a quantidade...\n")
                if prec_prod_antigo == 0:
                    break
                else:
                    prec_prod_novo = input("Escreva aqui a nova preçagem para o produto citado...\n")
                    if prec_prod_novo == 0:
                        break
                    else:
                        try:
                            prec_prod_antigo = prec_prod_antigo.upper()
                            cursor.execute("UPDATE estoque SET Preço = ('"+prec_prod_novo+"') WHERE Produto = ('"+prec_prod_antigo+"')")
                            banco.commit()
                            print("Os dados foram alterados com sucesso!!!")
                        except Exception as erro:
                            print("Credenciais inválidas!")
                            print(erro)

            else:
                print("Número Inválido!")
    