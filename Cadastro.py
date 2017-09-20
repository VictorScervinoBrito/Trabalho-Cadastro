listaNome = []
listaRua = []
listaCep = []
listaBairro = []
listaEstado = []
listaTelefone = []
cont = 0

i = 0
u = 1
while i < u:
    print("Deseja inserir novos dados? ")
    consulta1 = str(input("S = Sim N = Não\n"))
    if consulta1 == 'S' or consulta1 == 's':
        listaNome.append(str(input("Digite seu nome: ")))
        nome = listaNome[cont]
        print("Digite seu endereço: ")
        listaRua.append(str(input("Rua: ")))
        rua = listaRua[cont]
        listaCep.append(str(input("CEP: ")))
        cep = listaCep[cont]
        listaBairro.append(str(input("Bairro: ")))
        bairro = listaBairro[cont]
        listaEstado.append(str(input("Estado: ")))
        estado = listaEstado[cont]
        listaTelefone.append(str(input("Telefone: ")))
        telefone = listaTelefone[cont]       
        cont += 1
        with open("cadastro.txt", "a") as arq:
            arq.write(" ========== ========== ")
            arq.write("\n")
            arq.write("Nome: ")
            arq.write(nome)
            arq.write("\n")
            arq.write("Endereço: ")
            arq.write("\n")
            arq.write("Rua: ")
            arq.write(rua)
            arq.write("\n")
            arq.write("CEP: ")
            arq.write(cep)
            arq.write("\n")
            arq.write("Bairro: ")
            arq.write(bairro)
            arq.write("\n")
            arq.write("Estado: ")
            arq.write(estado)
            arq.write("\n")
            arq.write("Telefone: ")
            arq.write(telefone)
            arq.write("\n")
            arq.write(" ========== ========== ")
            arq.write("\n")
            arq.close()     
    else:
        i = 1

x = 0
y = 1
while x < y:
    print("Deseja consultar os dados? ")
    consulta = str(input("S = Sim N = Não\n"))
    if consulta == 'S' or consulta == 's':        
        print("Quem deseja consultar? ")
        procura = str(input("Digite o nome da pessoa: "))
        for x in range(len(listaNome)):
            if procura == listaNome[x]:
                print("Seu Nome: ", listaNome[x])
                print("Seu Rua: ", listaRua[x])
                print("Seu CEP: ", listaCep[x])
                print("Seu Bairro: ", listaBairro[x])
                print("Seu Estado: ", listaEstado[x])
                print("Telefone: : ", listaTelefone[x])
            else:
                print("O nome não esta na lista! ")
    else:
        print("Trabalho finalizado!")
        x = 1

