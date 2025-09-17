# chatbot.py

import random
from collections import Counter

# Arquivos de armazenamento
arquivo_aprendizado = "aprendizado.txt"
arquivo_historico = "historico.txt"
arquivo_relatorio = "relatorio.txt"

# Estatísticas
total_interacoes = 0
contador_personalidade = Counter()
contador_perguntas = Counter()
ultima_resposta = None

# Personalidades disponíveis
personalidades = {1: "Formal", 2: "Engraçado", 3: "Regional"}

# Dicionário de respostas
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

# --- Funções principais do chatbot para uso na interface ---

def responder(pergunta_usuario, estilo):
    global ultima_resposta, total_interacoes

    palavras_usuario = pergunta_usuario.lower().split()
    contador_perguntas[pergunta_usuario] += 1
    contador_personalidade[estilo] += 1
    total_interacoes += 1

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
                salvar_historico(pergunta_usuario, resposta_bot)
                return resposta_bot

    return None  # Não encontrou resposta

def ensinar(estilo, pergunta_usuario, nova_resposta):
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

# --- Funções de suporte (salvamento de dados) ---

def salvar_aprendizado(estilo, palavra_chave, resposta):
    with open(arquivo_aprendizado, "a", encoding="utf-8") as arq:
        arq.write(f"{estilo}|{palavra_chave}|{resposta}\n")

def salvar_historico(pergunta, resposta):
    with open(arquivo_historico, "a", encoding="utf-8") as arq:
        arq.write(f"Pergunta: {pergunta} | Resposta: {resposta}\n")
