import random
from collections import Counter

arquivo_aprendizado = "aprendizado.txt" #arquivo para implementação de novas perguntas
arquivo_historico   = "historico.txt"   # arquivo para registrar últimas 5 interações
arquivo_relatorio   = "relatorio.txt"   # arquivo para relatório final

# --- Estatísticas ---
total_interacoes = 0
contador_personalidade = Counter()
contador_perguntas = Counter()

# --- Dicionário de respostas ---
respostas = {
    "Formal": {
        ("pontos turísticos", "atrações", "lugares para visitar", "locais", "roteiro"): [
            "Os pontos turísticos mais conhecidos da região são: Chapada do Araripe, Geopark Araripe e Museu de Paleontologia em Santana do Cariri.",
            "Você pode visitar a Chapada do Araripe, um dos lugares mais icônicos, além do Geopark e o famoso Museu de Paleontologia.",
            "Destacam-se ainda as trilhas ecológicas da Chapada, os mirantes naturais e o Museu de Paleontologia de Santana do Cariri."
        ],
        ("hospedagem", "hotel", "hotéis", "pousada", "pousadas",
         "alojamento", "alojamentos", "acomodação", "acomodações",
         "estadia"): [
            "A maior quantidade de opções encontra-se nas cidades de Juazeiro do Norte, Barbalha e Crato, desde hotéis econômicos até pousadas familiares.",
            "Você encontrará hospedagem variada no Cariri, desde hotéis confortáveis até pousadas aconchegantes nas principais cidades.",
            "Existem opções de hospedagem próximas aos principais pontos turísticos, tanto para viagens de negócios quanto de lazer."
        ],
        ("eventos", "festas", "shows", "programação"): [
            "Dois eventos populares: Festival Expocrato e Festa do Pau da Bandeira.",
            "Entre os eventos mais tradicionais, destacam-se a Festa do Pau da Bandeira em Barbalha e o Festival Expocrato, referência musical da região.",
            "Eventos como o Festival Expocrato e a Festa do Pau da Bandeira atraem visitantes de várias partes do Brasil."
        ]
    },
    "Engraçado": {
        ("pontos turísticos", "atrações", "lugares para visitar", "locais", "roteiro"): [
            "Se liga! 📸 Chapada do Araripe, Geopark e Museu dos Dinossauros. Selfie garantida! 🦖😂",
            "Quer ver dinossauro de perto? Vai no museu! Quer uma vista de tirar o fôlego? Chapada do Araripe! 🌄",
            "Rolê garantido: Chapada pra foto, Geopark pra aventura e museu pra dar um 'oi' pros dinossauros! 🦕🎒"
        ],
        ("hospedagem", "hotel", "hotéis", "pousada", "pousadas",
         "alojamento", "alojamentos", "acomodação", "acomodações",
         "estadia"): [
            "Tem de tudo: hotel chique, pousada aconchegante... só não vale dormir na praça 😅",
            "Se quiser luxo, tem hotel. Se quiser economia, tem pousadinha. Só cuidado com as redes de dormir, que vicia! 🛏️😂",
            "Opção é o que não falta! Desde hotel cinco estrelas até aquele quartinho que parece casa da vó 👵✨"
        ],
        ("eventos", "festas", "shows", "programação"): [
            "Dois rolês que bombam: 🎉 Festival Expocrato e Festa do Pau da Bandeira. Forró, fé e alegria! 🍻",
            "Quer festa? Pau da Bandeira é fé e tradição. Quer música? Expocrato é o 'LollaPalooza' do Cariri! 🎶😂",
            "No Cariri a galera não brinca: Expocrato e Pau da Bandeira são praticamente feriado extra! 🎊"
        ]
    },
    "Regional": {
        ("pontos turísticos", "atrações", "lugares para visitar", "locais", "roteiro"): [
            "Ôxente, cabra! Tu tem que conhecer a Chapada do Araripe, o Geopark e o Museu dos Dinossauros. É de encher os olhos, visse?",
            "Na Chapada do Araripe tu vê a natureza bonita, no Geopark tu aprende e no museu tu encontra os bichim antigos! 🦖",
            "Ave Maria! Chapada, Geopark e Museu dos Dinossauros são a cara do Cariri. Tem que ir, homi!"
        ],
        ("hospedagem", "hotel", "hotéis", "pousada", "pousadas",
         "alojamento", "alojamentos", "acomodação", "acomodações",
         "estadia"): [
            "Tem opção pra todo bolso, meu rei! Em Juazeiro, Crato e Barbalha tem hotel e pousada que é um aconchego só.",
            "Se quiser ficar bem hospedado, vá pra Juazeiro, Crato ou Barbalha, que lá tem cama boa até demais. 😴",
            "Oxente, aqui é assim: tem hospedagem pra quem vem só passear e até pra quem quer morar uns dias no Cariri!"
        ],
        ("eventos", "festas", "shows", "programação"): [
            "Dois dos festejos mais arretados: Festival Expocrato e Festa do Pau da Bandeira. É forró e alegria que só a moléstia!",
            "Na Festa do Pau da Bandeira o povo vai na fé, e no Expocrato vai no forró. É alegria garantida, cabra!",
            "Visse? O Cariri ferve na época do Pau da Bandeira e do Expocrato. O povo não perde por nada!"
        ]
    }
}

personalidades = {1: "Formal", 2: "Engraçado", 3: "Regional"}
ultima_resposta = None

# --- Funções auxiliares ---
def salvar_aprendizado(estilo, palavra_chave, resposta):
    with open(arquivo_aprendizado, "a", encoding="utf-8") as arq:
        arq.write(f"{estilo}|{palavra_chave}|{resposta}\n")

def salvar_historico(pergunta, resposta):
    with open(arquivo_historico, "a", encoding="utf-8") as arq:
        arq.write(f"Pergunta: {pergunta} | Resposta: {resposta}\n")

def limpar_historico():
    open(arquivo_historico, "w", encoding="utf-8").close()
    print("Histórico limpo com sucesso! ✅")

# --- gerar relatório ---
def gerar_relatorio():
    mais_perg = contador_perguntas.most_common(1)
    pergunta_top = mais_perg[0][0] if mais_perg else "Nenhuma"
    with open(arquivo_relatorio, "w", encoding="utf-8") as arq:
        arq.write("=== Relatório de Interações ===\n")
        arq.write(f"Total de interações: {total_interacoes}\n")
        arq.write(f"Pergunta mais feita: {pergunta_top}\n")
        arq.write("Uso de personalidades:\n")
        for p, c in contador_personalidade.items():
            arq.write(f"  {p}: {c}\n")
    print("Relatório gerado em", arquivo_relatorio)

def mostrar_sugestoes():
    print("\nSugestões de perguntas mais frequentes:")
    for p, _ in contador_perguntas.most_common(5):
        print(" -", p)

# --- Carrega histórico prévio ---
for nome in [arquivo_aprendizado, arquivo_historico]:
    try:
        with open(nome, "r", encoding="utf-8") as arq:
            linhas = arq.readlines()
    except FileNotFoundError:
        linhas = []

if linhas:
    print("\nÚltimas 5 interações anteriores:")
    for l in linhas[-5:]:
        print(l.strip())
    print("-" * 40)

# --- Loop principal ---
while True:
    print("\nSaudações, sou o Soldadinho-do-Araripe, guardião do Cariri")
    print("[1] - Formal\n[2] - Engraçado\n[3] - Regional(Cariri)")
    print("[4] - Limpar histórico\n[5] - Sugestões\n[6] - Relatório\n[0] - Encerrar")
    entrada = input("Escolha uma opção: ")

    if not entrada.isdigit():
        print("Por favor, digite apenas números!")
        continue
    digito = int(entrada)

    if digito == 0:
        gerar_relatorio()
        print("Encerrando a conversa. Até logo!")
        break
    elif digito == 4:
        limpar_historico()
        continue
    elif digito == 5:
        mostrar_sugestoes()
        continue
    elif digito == 6:
        gerar_relatorio()
        continue
    elif digito not in personalidades:
        print("Opção inválida, tente novamente!")
        continue

    estilo = personalidades[digito]
    contador_personalidade[estilo] += 1
    print(f"Você escolheu o estilo: {estilo}")

    # --- Pergunta  ---
    pergunta_usuario = input("Sobre o que você quer saber? (ex: pontos turísticos, hospedagem, eventos) ").strip()
    palavras_usuario = pergunta_usuario.lower().split()
    contador_perguntas[pergunta_usuario] += 1
    total_interacoes += 1

    achou = False
    for chaves in respostas[estilo]:
        for palavra in palavras_usuario:
            if any(palavra in c.lower() for c in (chaves if isinstance(chaves, tuple) else (chaves,))):
                valor = respostas[estilo][chaves]
                if not isinstance(valor, list):
                    valor = [valor]
                    respostas[estilo][chaves] = valor
                possiveis = valor[:]
                if ultima_resposta in possiveis and len(possiveis) > 1:
                    possiveis.remove(ultima_resposta)
                resposta_bot = random.choice(possiveis)
                ultima_resposta = resposta_bot
                print(resposta_bot)
                salvar_historico(pergunta_usuario, resposta_bot)
                achou = True
                break
        if achou:
            break

    if not achou:
        print("Ainda não sei responder isso. 😢")
        nova_resposta = input("Você pode me ensinar? Digite uma resposta apropriada: ").strip()
        if pergunta_usuario in respostas[estilo]:
            if isinstance(respostas[estilo][pergunta_usuario], list):
                respostas[estilo][pergunta_usuario].append(nova_resposta)
            else:
                respostas[estilo][pergunta_usuario] = [
                    respostas[estilo][pergunta_usuario],
                    nova_resposta
                ]
        else:
            respostas[estilo][pergunta_usuario] = [nova_resposta]

        salvar_aprendizado(estilo, pergunta_usuario, nova_resposta)
        salvar_historico(pergunta_usuario, nova_resposta)
        print("Obrigado! Aprendi algo novo e salvei no arquivo aprendizado.txt ✅")
