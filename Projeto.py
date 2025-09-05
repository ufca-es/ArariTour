while True:
    print("Saudações, sou o Soldadinho-do-Araripe, guardião do Cariri")
    entrada = input("Digite o número da forma que deseja que eu me comunique com você!! 1 - Formal, 2 - Engraçado, 3 - Regional(Cariri), digite '0' para encerrar a conversa: ")
    
    if not entrada.isdigit():
        print("Por favor, digite apenas números!")
        continue
    
    digito = int(entrada)

    if digito == 0:
        print("Encerrando a conversa. Até logo!")
        break
    elif digito in [1, 2, 3]:
        print("Ótimo, como posso ajudar em sua descoberta da região?")
    else:
        print("Opção inválida, tente novamente!")
        continue

    interacao = input("Digite o número das opções: 1 - pontos turísticos, 2 - hospedagem, 3 - eventos: ")

    if not interacao.isdigit():
        print("Por favor, digite apenas números!")
        continue

    interacao1 = int(interacao)

    if digito == 1:  
        if interacao1 == 1:
            print("Os pontos turísticos mais conhecidos da região são: Chapada do Araripe, o Geopark Araripe e o Museu de Paleontologia em Santana do Cariri.")
        elif interacao1 == 2:
            print("A maior quantidade de opções encontra-se nas cidades de Juazeiro do Norte, Barbalha e Crato, desde hotéis econômicos até pousadas familiares.")
        elif interacao1 == 3:
            print("Dois dos eventos mais populares são: O Festival Expocrato, que ocorre no mês de Julho na cidade de Crato e a Festa do Pau da Bandeira de Santo Antônio em Barbalha, que ocorre no mês de Junho.")

    elif digito == 2: 
        if interacao1 == 1:
            print("Se liga! 📸 Chapada do Araripe, Geopark e Museu dos Dinossauros. Vai querer selfie até com os fósseis! 🦖😂")
        elif interacao1 == 2:
            print("Tem de tudo: hotel chique, pousada aconchegante... Só não vale dormir na praça, beleza? 😅")
        elif interacao1 == 3:
            print("Dois rolês que bombam por aqui são: 🎉 o Festival Expocrato (em julho, lá no Crato 🤠) e a lendária Festa do Pau da Bandeira de Santo Antônio 🌳💪 (em junho, na Barbalha)! Bora se preparar que esses eventos são de perder o fôlego... e o rumo também 😂🍻.")

    elif digito == 3: 
        if interacao1 == 1:
            print("Ôxente, cabra! Tu tem que conhecer a Chapada do Araripe, o Geopark e o Museu dos Dinossauros. É de encher os olhos, visse?")
        elif interacao1 == 2:
            print("Tem opção pra todo bolso, meu rei! Em Juazeiro, Crato e Barbalha tem hotel e pousada que é um aconchego só.")
        elif interacao1 == 3:
            print("Dois dos festejos mais arretados que tem por essas banda é o Festival Expocrato, que acontece em julho lá no Crato, e a famosa Festa do Pau da Bandeira de Santo Antônio, que rola em junho lá na Barbalha. É forró, é fé e é alegria que só a moléstia!")

