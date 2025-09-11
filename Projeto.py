import random

arquivo = open("respostas.txt", "w", encoding="utf-8")
arquivo.write("Testando código\n")

arquivo_aprendizado = "aprendizado.txt"
arquivo_historico = "historico.txt"

respostas = {
    "Formal": {
        "pontos turísticos": [
            "Os pontos turísticos mais conhecidos da região são: Chapada do Araripe, Geopark Araripe e Museu de Paleontologia em Santana do Cariri.",
            "Você pode visitar a Chapada do Araripe, um dos lugares mais icônicos, além do Geopark e o famoso Museu de Paleontologia.",
            "Destacam-se ainda as trilhas ecológicas da Chapada, os mirantes naturais e o Museu de Paleontologia de Santana do Cariri."
        ],
        "hospedagem": [
            "A maior quantidade de opções encontra-se nas cidades de Juazeiro do Norte, Barbalha e Crato, desde hotéis econômicos até pousadas familiares.",
            "Você encontrará hospedagem variada no Cariri, desde hotéis confortáveis até pousadas aconchegantes nas principais cidades.",
            "Existem opções de hospedagem próximas aos principais pontos turísticos, tanto para viagens de negócios quanto de lazer."
        ],
        "eventos": [
            "Dois eventos populares: Festival Expocrato e Festa do Pau da Bandeira.",
            "Entre os eventos mais tradicionais, destacam-se a Festa do Pau da Bandeira em Barbalha e o Festival Expocrato, referência musical da região.",
            "Eventos como o Festival Expocrato e a Festa do Pau da Bandeira atraem visitantes de várias partes do Brasil."
        ]
    },
    "Engraçado": {
        "pontos turísticos": [
            "Se liga! 📸 Chapada do Araripe, Geopark e Museu dos Dinossauros. Selfie garantida! 🦖😂",
            "Quer ver dinossauro de perto? Vai no museu! Quer uma vista de tirar o fôlego? Chapada do Araripe! 🌄",
            "Rolê garantido: Chapada pra foto, Geopark pra aventura e museu pra dar um 'oi' pros dinossauros! 🦕🎒"
        ],
        "hospedagem": [
            "Tem de tudo: hotel chique, pousada aconchegante... só não vale dormir na praça 😅",
            "Se quiser luxo, tem hotel. Se quiser economia, tem pousadinha. Só cuidado com as redes de dormir, que vicia! 🛏️😂",
            "Opção é o que não falta! Desde hotel cinco estrelas até aquele quartinho que parece casa da vó 👵✨"
        ],
        "eventos": [
            "Dois rolês que bombam: 🎉 Festival Expocrato e Festa do Pau da Bandeira. Forró, fé e alegria! 🍻",
            "Quer festa? Pau da Bandeira é fé e tradição. Quer música? Expocrato é o 'LollaPalooza' do Cariri! 🎶😂",
            "No Cariri a galera não brinca: Expocrato e Pau da Bandeira são praticamente feriado extra! 🎊"
        ]
    },
    "Regional": {
        "pontos turísticos": [
            "Ôxente, cabra! Tu tem que conhecer a Chapada do Araripe, o Geopark e o Museu dos Dinossauros. É de encher os olhos, visse?",
            "Na Chapada do Araripe tu vê a natureza bonita, no Geopark tu aprende e no museu tu encontra os bichim antigos! 🦖",
            "Ave Maria! Chapada, Geopark e Museu dos Dinossauros são a cara do Cariri. Tem que ir, homi!"
        ],
        "hospedagem": [
            "Tem opção pra todo bolso, meu rei! Em Juazeiro, Crato e Barbalha tem hotel e pousada que é um aconchego só.",
            "Se quiser ficar bem hospedado, vá pra Juazeiro, Crato ou Barbalha, que lá tem cama boa até demais. 😴",
            "Oxente, aqui é assim: tem hospedagem pra quem vem só passear e até pra quem quer morar uns dias no Cariri!"
        ],
        "eventos": [
            "Dois dos festejos mais arretados: Festival Expocrato e Festa do Pau da Bandeira. É forró e alegria que só a moléstia!",
            "Na Festa do Pau da Bandeira o povo vai na fé, e no Expocrato vai no forró. É alegria garantida, cabra!",
            "Visse? O Cariri ferve na época do Pau da Bandeira e do Expocrato. O povo não perde por nada!"
        ]
    }
}

personalidades = {
    1: "Formal",
    2: "Engraçado",
    3: "Regional"
}

def salvar_aprendizado(estilo, palavra_chave, resposta):
    arquivo = open(arquivo_aprendizado, "a", encoding="utf-8")
    arquivo.write(f"{estilo}|{palavra_chave}|{resposta}\n")
    arquivo.close()

def salvar_historico(pergunta, resposta):
    arquivo = open(arquivo_historico, "a", encoding="utf-8")
    arquivo.write(f"Pergunta: {pergunta} | Resposta: {resposta}\n")
    arquivo.close()

def limpar_historico():
    arquivo = open(arquivo_historico, "w", encoding="utf-8")
    arquivo.close()
    print("Histórico limpo com sucesso! ✅")

arquivo = open(arquivo_aprendizado, "a", encoding="utf-8")
arquivo.close()
arquivo = open(arquivo_historico, "a", encoding="utf-8")
arquivo.close()

arquivo = open(arquivo_aprendizado, "r", encoding="utf-8")
for linha in arquivo:
    partes = linha.strip().split("|")
    if len(partes) == 3:
        estilo, palavra_chave, resposta = partes
        if estilo in respostas:
            if palavra_chave in respostas[estilo]:
                if isinstance(respostas[estilo][palavra_chave], list):
                    respostas[estilo][palavra_chave].append(resposta)
                else:
                    respostas[estilo][palavra_chave] = [respostas[estilo][palavra_chave], resposta]
            else:
                respostas[estilo][palavra_chave] = [resposta]
        else:
            respostas[estilo] = {palavra_chave: [resposta]}
arquivo.close()

arquivo = open(arquivo_historico, "r", encoding="utf-8")
linhas = arquivo.readlines()
arquivo.close()
if linhas:
    print("\nÚltimas 5 interações anteriores:")
    for l in linhas[-5:]:
        print(l.strip())
    print("-" * 40)

ultima_resposta = None

while True:
    print("\nSaudações, sou o Soldadinho-do-Araripe, guardião do Cariri")
    print("[1] - Formal\n[2] - Engraçado\n[3] - Regional(Cariri)\n[4] - Limpar histórico\n[0] - Encerrar")
    entrada = input("Escolha uma opção: ")

    if not entrada.isdigit():
        print("Por favor, digite apenas números!")
        continue

    digito = int(entrada)

    if digito == 0:
        print("Encerrando a conversa. Até logo!")
        break
    elif digito == 4:
        limpar_historico()
        continue
    elif digito not in personalidades:
        print("Opção inválida, tente novamente!")
        continue

    estilo = personalidades[digito]
    print(f"Você escolheu o estilo: {estilo}")

    pergunta_usuario = input("Sobre o que você quer saber? (ex: pontos turísticos, hospedagem, eventos) ").strip()

    achou = False
    for chave in respostas[estilo]:
        if chave in pergunta_usuario:
            valor = respostas[estilo][chave]
            if not isinstance(valor, list):
                valor = [valor]
                respostas[estilo][chave] = valor

            possiveis = valor[:]
            if ultima_resposta in possiveis and len(possiveis) > 1:
                possiveis.remove(ultima_resposta)

            resposta_bot = random.choice(possiveis)
            ultima_resposta = resposta_bot

            print(resposta_bot)
            salvar_historico(pergunta_usuario, resposta_bot)
            achou = True

    if not achou:
        print("Ainda não sei responder isso. 😢")
        nova_resposta = input("Você pode me ensinar? Digite uma resposta apropriada: ").strip()

        if pergunta_usuario in respostas[estilo]:
            if isinstance(respostas[estilo][pergunta_usuario], list):
                respostas[estilo][pergunta_usuario].append(nova_resposta)
            else:
                respostas[estilo][pergunta_usuario] = [respostas[estilo][pergunta_usuario], nova_resposta]
        else:
            respostas[estilo][pergunta_usuario] = [nova_resposta]

        salvar_aprendizado(estilo, pergunta_usuario, nova_resposta)
        salvar_historico(pergunta_usuario, nova_resposta)
        print("Obrigado! Aprendi algo novo e salvei no arquivo aprendizado.txt ✅")
