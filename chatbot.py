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
        # ---- SAUDAÇÕES ----
        ("oi", "olá", "bom dia", "boa tarde", "boa noite"): [
            "Olá, como posso ajudá-lo hoje?",
            "Saudações! Estou à disposição para lhe orientar sobre o Cariri.",
            "Bem-vindo! Deseja informações sobre turismo, hospedagem ou eventos?"
        ],
        ("tchau", "até logo", "adeus", "encerrar"): [
            "Até breve! Foi um prazer ajudá-lo.",
            "Encerrando nossa conversa. Volte sempre!",
            "Obrigado pelo contato. Estarei disponível quando precisar."
        ],
        ("pare", "para", "chega"): [
            "Tudo bem, vou me calar agora.",
            "Certo, encerrando a conversa.",
            "De acordo, estarei em silêncio."
        ],

        # ---- TURISMO ----
        ("pontos turísticos", "atrações", "lugares para visitar", "locais", "roteiro"): [
            "Os principais pontos turísticos são: Chapada do Araripe, Geopark Araripe, Museu de Paleontologia de Santana do Cariri e a estátua de Padre Cícero em Juazeiro do Norte.",
            "Vale a pena conhecer a Chapada do Araripe, os mirantes naturais, o Geopark e o Museu de Paleontologia.",
            "Você pode visitar a Colina do Horto, onde está a estátua de Padre Cícero, além da Chapada do Araripe e os museus da região."
        ],

        # ---- HOSPEDAGEM ----
        ("hospedagem", "hotel", "pousada", "acomodação", "estadia"): [
            "Em Juazeiro do Norte, há o Iuá Hotel (a partir de R$ 250 por noite) e o Verdes Vales Hotel (a partir de R$ 300).",
            "No Crato, você pode se hospedar no Hotel Encosta da Serra (a partir de R$ 200) ou em pousadas locais mais econômicas (em torno de R$ 100 a R$ 150).",
            "Em Barbalha, opções incluem o Imperial Palace Hotel (a partir de R$ 180) e pousadas aconchegantes no centro da cidade."
        ],

        # ---- RESTAURANTES ----
        ("comida", "restaurante", "gastronomia", "onde comer"): [
            "Em Juazeiro, o Restaurante Cheiro Verde é muito conhecido pela comida regional. Pratos a partir de R$ 25.",
            "No Crato, recomendo o Espetinho do Gordo, famoso pelos churrascos. Preços médios de R$ 20 a R$ 40.",
            "Em Barbalha, a Pizzaria Água na Boca é bastante frequentada. Pizzas entre R$ 40 e R$ 60."
        ],

        # ---- EVENTOS ----
        ("eventos", "festas", "shows", "programação"): [
            "Dois eventos populares são o Festival Expocrato (em julho) e a Festa do Pau da Bandeira (em junho, em Barbalha).",
            "Entre os eventos mais tradicionais: a Festa do Pau da Bandeira, que abre os festejos juninos, e o Festival Expocrato, um dos maiores do Nordeste.",
            "Eventos como o Festival Expocrato e a Festa do Pau da Bandeira atraem milhares de visitantes todos os anos."
        ]
    },

    "Engraçado": {
        ("oi", "olá", "bom dia", "boa tarde", "boa noite"): [
            "E aí! 👋 Preparado pro rolê no Cariri?",
            "Fala, turista raiz! Bora descobrir uns lugares top?",
            "Oi sumido(a)! Bora pro forró? 🎶😂"
        ],
        ("tchau", "até logo", "adeus", "encerrar"): [
            "Falou, meu consagrado! Volta logo que o Cariri não para! 🚀",
            "Tchau! Vai mas volta, senão o Padre Cícero fica de mal! 🙃",
            "Encerrando... mas já tô com saudade 😢"
        ],
        ("pare", "para", "chega"): [
            "Opa! Quieto feito múmia agora 🤐",
            "Beleza, vou desligar o modo falador 📴",
            "Tranquilo, vou dar um tempo 😅"
        ],

        ("pontos turísticos", "atrações", "lugares para visitar", "locais", "roteiro"): [
            "Quer selfie? Vai na Chapada! Quer aventura? Geopark! Quer ver dino? Museu! 🦖📸",
            "Rolê certo: Chapada do Araripe + Museu dos Dinossauros + Colina do Horto (tem até vista panorâmica top!)",
            "Se liga: Chapada pra foto, Geopark pra aprender e Expocrato pra dançar! 🎉"
        ],
        ("hospedagem", "hotel", "pousada", "acomodação", "estadia"): [
            "Tem de tudo: hotel chique 💎, pousadinha aconchegante 🏡, só não vale dormir na praça! 😂",
            "Juazeiro tem hotel de luxo, Crato tem pousada raiz... escolha seu estilo!",
            "Se não achar hospedagem, sempre tem a rede de dormir da vó! 🛏️😂"
        ],
        ("comida", "restaurante", "gastronomia", "onde comer"): [
            "Quer rango bom e barato? Vai no Cheiro Verde 🍲",
            "Cariri é raiz até na comida: baião, carne de sol e macaxeira! 😋",
            "Restaurante top mesmo é o da vó... mas enquanto isso, tem as pizzarias e churrascarias da região! 🍕🥩"
        ],
        ("eventos", "festas", "shows", "programação"): [
            "Dois rolês que bombam: 🎉 Expocrato e Pau da Bandeira!",
            "Quer forró? Vai no Expocrato! Quer tradição? Pau da Bandeira!",
            "Cariri = festa todo mês. Expocrato é o Lollapalooza daqui 😂"
        ]
    },

    "Regional": {
        ("oi", "olá", "bom dia", "boa tarde", "boa noite"): [
            "Ôxente! Bem-vindo, cabra bom!",
            "Eita, como vai você, visse?",
            "Oi, meu rei! Bora conversar sobre o Cariri?"
        ],
        ("tchau", "até logo", "adeus", "encerrar"): [
            "Até mais, meu fi! Vá com Deus!",
            "Tchauzinho, cabra arretado!",
            "Encerrando a prosa, mas volte logo!"
        ],
        ("pare", "para", "chega"): [
            "Oxente, tá certo, vou calar a boca 😅",
            "Tá bom, homi, fico caladinho agora!",
            "Paro já, visse?"
        ],

        ("pontos turísticos", "atrações", "lugares para visitar", "locais", "roteiro"): [
            "Ave Maria! Chapada do Araripe, Geopark e Museu dos Dinossauros é visita obrigatória!",
            "Tem a Colina do Horto com a estátua do Padim Ciço, eita lugar bonito demais!",
            "Quer aventura? Vai pras trilhas da Chapada, cabra!"
        ],
        ("hospedagem", "hotel", "pousada", "acomodação", "estadia"): [
            "Juazeiro tem hotel chique que só, como o Iuá Hotel. Preço? Uns R$ 250 a diária.",
            "No Crato tem o Hotel Encosta da Serra, arretado! A diária sai por uns R$ 200.",
            "Se quiser mais baratinho, tem pousada em Barbalha a partir de R$ 100."
        ],
        ("comida", "restaurante", "gastronomia", "onde comer"): [
            "Bora comer baião de dois no Cheiro Verde em Juazeiro! É bom que só! 🍲",
            "No Crato tem churrasco do Espetinho do Gordo, famoso demais! 🥩",
            "Em Barbalha, a Pizzaria Água na Boca mata a fome da galera! 🍕"
        ],
        ("eventos", "festas", "shows", "programação"): [
            "No Cariri, o Pau da Bandeira em Barbalha é fé e festa, e o Expocrato é música até o sol nascer! 🎶",
            "Aqui a gente não perde o Pau da Bandeira nem o Expocrato. É tradição!",
            "Forró, fé e alegria: assim é a festa no Cariri, cabra!"
        ]
    }
}

# --- Funções principais do chatbot ---

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

    return "Desculpe, não entendi sua pergunta. Pode reformular?"

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

# --- Funções de suporte ---

def salvar_aprendizado(estilo, palavra_chave, resposta):
    with open(arquivo_aprendizado, "a", encoding="utf-8") as arq:
        arq.write(f"{estilo}|{palavra_chave}|{resposta}\n")

def salvar_historico(pergunta, resposta):
    with open(arquivo_historico, "a", encoding="utf-8") as arq:
        arq.write(f"Pergunta: {pergunta} | Resposta: {resposta}\n")
