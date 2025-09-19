import gradio as gr
import random
import os
from collections import Counter
import unicodedata

# ================================================================
# >>> CONFIGURAÇÕES INICIAIS
# ================================================================


# ---------- Arquivos ----------
ARQ_HISTORICO = "historico.txt"
ARQ_APRENDIZADO = "aprendizado.txt"
CONTADOR_ESTILOS_ARQ = "contador_estilos.txt"

# ---------- Dados iniciais ----------
total_interacoes = 0
contador_perguntas = Counter()
ultima_resposta = None
contador_estilos = Counter()

# ================================================================
# >>> FUNÇÕES PARA GERENCIAR O CONTADOR DE ESTILOS
# ================================================================

def carregar_contador_estilos():
    global contador_estilos
    if os.path.exists(CONTADOR_ESTILOS_ARQ):
        with open(CONTADOR_ESTILOS_ARQ, "r", encoding="utf-8") as arq:
            for linha in arq:
                est, val = linha.strip().split("|")
                contador_estilos[est] = int(val)

def salvar_contador_estilos():
    with open(CONTADOR_ESTILOS_ARQ, "w", encoding="utf-8") as arq:
        for est, val in contador_estilos.items():
            arq.write(f"{est}|{val}\n")

carregar_contador_estilos()

# ================================================================
# >>> LIMPAR HISTÓRICO
# ================================================================

def limpar_historico():
    global total_interacoes, contador_perguntas, contador_estilos

    # Apaga o arquivo de histórico
    if os.path.exists(ARQ_HISTORICO):
        os.remove(ARQ_HISTORICO)

    # Reseta variáveis da sessão
    total_interacoes = 0
    contador_perguntas = Counter()
    contador_estilos = Counter()
    salvar_contador_estilos()

    # Retorna mensagem inicial no chatbot e contador zerado
    contador_html = f"""
    <b>Estilos usados:</b><br>
    Regional: 0<br>
    Formal: 0<br>
    Engraçado: 0
    """
    return [{"role": "assistant", "content": "Histórico e contadores limpos! Comece a conversa novamente 😉"}], contador_html

# ================================================================
# >>> DICIONÁRIO BASE DE RESPOSTAS
# ================================================================

respostas = {
    "Formal": {
        ("oi", "ola", "bom dia", "boa tarde", "boa noite"): [
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
        ("pontos turísticos", "atrações", "lugares para visitar", "locais", "roteiro"): [
            "Os principais pontos turísticos são: Chapada do Araripe, Geopark Araripe, Museu de Paleontologia de Santana do Cariri e a estátua de Padre Cícero em Juazeiro do Norte.",
            "Vale a pena conhecer a Chapada do Araripe, os mirantes naturais, o Geopark e o Museu de Paleontologia.",
            "Você pode visitar a Colina do Horto, onde está a estátua de Padre Cícero, além da Chapada do Araripe e os museus da região."
        ],
        ("hospedagem", "hospedagens", "hotel", "hoteis", "pousada", "pousadas", "acomodacao", "acomodacoes", "estadia", "estadias"): [
            "Em Juazeiro do Norte, há o Iuá Hotel (a partir de R$ 250 por noite) e o Verdes Vales Hotel (a partir de R$ 300).",
            "No Crato, você pode se hospedar no Hotel Encosta da Serra (a partir de R$ 200) ou em pousadas locais mais econômicas (em torno de R$ 100 a R$ 150).",
            "Em Barbalha, opções incluem o Imperial Palace Hotel (a partir de R$ 180) e pousadas aconchegantes no centro da cidade."
        ],
        ("comida", "restaurante", "gastronomia", "onde comer"): [
            "Em Juazeiro, o Restaurante Cheiro Verde é muito conhecido pela comida regional. Pratos a partir de R$ 25.",
            "No Crato, recomendo o Espetinho do Gordo, famoso pelos churrascos. Preços médios de R$ 20 a R$ 40.",
            "Em Barbalha, a Pizzaria Água na Boca é bastante frequentada. Pizzas entre R$ 40 e R$ 60."
        ],
        ("eventos", "festas", "shows", "programação"): [
            "Dois eventos populares são o Festival Expocrato (em julho) e a Festa do Pau da Bandeira (em junho, em Barbalha).",
            "Entre os eventos mais tradicionais: a Festa do Pau da Bandeira, que abre os festejos juninos, e o Festival Expocrato, um dos maiores do Nordeste.",
            "Eventos como o Festival Expocrato e a Festa do Pau da Bandeira atraem milhares de visitantes todos os anos."
        ],
        ("mais opções", "outras opções", "outras respostas", "mais respostas", "outras alternativas", "mais alternativas"): [
    "Desculpe, não tenho mais opções por enquanto 😅"
]
    },
    "Engraçado": {
        ("oi", "ola", "bom dia", "boa tarde", "boa noite"): [
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
        ("hospedagem", "hospedagens", "hotel", "hoteis", "pousada", "pousadas", "acomodacao", "acomodacoes", "estadia", "estadias"): [
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
        ],
        ("mais opções", "outras opções", "outras respostas", "mais respostas", "outras alternativas", "mais alternativas"): [
    "Desculpe, não tenho mais opções por enquanto 😅"
]
    },
    "Regional": {
        ("oi", "ola", "bom dia", "boa tarde", "boa noite"): [
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
        ("hospedagem", "hospedagens", "hotel", "hoteis", "pousada", "pousadas", "acomodacao", "acomodacoes", "estadia", "estadias"): [
            "Juazeiro tem hotel chique que só, como o Iuá Hotel. Preço? Uns R$ 250 a diária.",
            "No Crato tem o Hotel Encosta da Serra, arretado! A diária sai por uns R$ 200.",
            "Se quiser mais baratinho, tem pousada em Barbalha a partir de R$ 100."
        ],
        ("comida","comidas", "restaurante", "gastronomia", "onde comer"): [
            "Bora comer baião de dois no Cheiro Verde em Juazeiro! É bom que só! 🍲",
            "No Crato tem churrasco do Espetinho do Gordo, famoso demais! 🥩",
            "Em Barbalha, a Pizzaria Água na Boca mata a fome da galera! 🍕"
        ],
        ("eventos", "festas", "shows", "programação"): [
            "No Cariri, o Pau da Bandeira em Barbalha é fé e festa, e o Expocrato é música até o sol nascer! 🎶",
            "Aqui a gente não perde o Pau da Bandeira nem o Expocrato. É tradição!",
            "Forró, fé e alegria: assim é a festa no Cariri, cabra!"
        ],
        ("mais opções", "outras opções", "outras respostas", "mais respostas", "outras alternativas", "mais alternativas"): [
    "Desculpe, não tenho mais opções por enquanto 😅"
]
    }
}

# ---------- Funções de arquivo ----------
def salvar_interacao(pergunta, resposta):
    with open(ARQ_HISTORICO, "a", encoding="utf-8") as arq:
        arq.write(f"User: {pergunta}\nBot: {resposta}\n---\n")

def remover_acentos(texto):

    # Remove acentos e cedilha para facilitar comparação de palavras-chave independente de acentuação.

    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ).replace('ç', 'c').replace('Ç','C').lower()


def ultimas_interacoes():

    # Retorna as últimas 5 interações salvas, para exibir quando a interface iniciar.

    if not os.path.exists(ARQ_HISTORICO):
        return []
    with open(ARQ_HISTORICO, "r", encoding="utf-8") as arq:
        blocos = arq.read().strip().split("---\n")
    blocos = [b.strip() for b in blocos if b.strip()]
    ultimos = blocos[-5:]
    historico = []
    for bloco in ultimos:
        linhas = bloco.split("\n")
        if len(linhas) >= 2:
            pergunta = linhas[0].replace("User: ", "")
            resposta = linhas[1].replace("Bot: ", "")
            historico.append({"role": "user", "content": pergunta})
            historico.append({"role": "assistant", "content": resposta})
    return historico

def salvar_aprendizado(estilo, chave, resposta):

    # Adiciona nova pergunta/resposta ensinada pelo usuário ao arquivo.

    with open(ARQ_APRENDIZADO, "a", encoding="utf-8") as arq:
        arq.write(f"{estilo}|{chave}|{resposta}\n")

def carregar_aprendizado():

    # Lê o arquivo de aprendizados e adiciona as respostas ensinadas ao dicionário principal.

    if not os.path.exists(ARQ_APRENDIZADO):
        return
    with open(ARQ_APRENDIZADO, "r", encoding="utf-8") as arq:
        for linha in arq:
            est, chave, resp = linha.strip().split("|", 2)
            chave = chave.lower()
            if est in respostas:
                respostas[est].setdefault(chave, []).append(resp)

carregar_aprendizado()

# ================================================================
# >>> FUNÇÕES PRINCIPAIS DO CHATBOT
# ================================================================

def responder_interface(mensagem, historico, estilo):

    """
    Função principal chamada quando o usuário envia uma mensagem.
    - Normaliza a mensagem
    - Busca resposta de acordo com o estilo e palavras-chave
    - Atualiza contadores e histórico
    """

    global ultima_resposta, total_interacoes, contador_perguntas
    total_interacoes += 1


    # Incrementa o contador do estilo selecionado
    contador_estilos[estilo] += 1
    contador_perguntas[mensagem.lower()] += 1
    salvar_contador_estilos()

    msg_normalizada = remover_acentos(mensagem)

    # --- Checa se o usuário quer "mais opções" ---
    mais_opcoes_chaves = [
        "mais opcoes", "outras opcoes", "outras respostas", "mais respostas",
        "outras alternativas", "mais alternativas"
    ]
    if any(p in msg_normalizada for p in mais_opcoes_chaves):
        resposta_bot = "Desculpe, não tenho mais opções por enquanto 😅"
    else:
        resposta_bot = "🤔 Não entendi. Pergunte ou ensine uma nova resposta."

        # percorre todas as chaves do estilo
        for chaves, lista in respostas[estilo].items():
            if isinstance(chaves, tuple):
                palavras_chave = [remover_acentos(p) for p in chaves]
            else:
                palavras_chave = [remover_acentos(chaves)]

            if any(p in msg_normalizada for p in palavras_chave):
                possiveis = lista[:]
                if ultima_resposta in possiveis and len(possiveis) > 1:
                    possiveis.remove(ultima_resposta)
                resposta_bot = random.choice(possiveis)
                break

     # Salva interação e atualiza histórico

    salvar_interacao(mensagem, resposta_bot)
    historico.append({"role": "user", "content": mensagem})
    historico.append({"role": "assistant", "content": resposta_bot})
    ultima_resposta = resposta_bot

     # Atualiza HTML com contagem de estilos
    contador_html = f"""
    <b>Estilos usados:</b><br>
    Regional: {contador_estilos['Regional']}<br>
    Formal: {contador_estilos['Formal']}<br>
    Engraçado: {contador_estilos['Engraçado']}
    """
    return "", historico, contador_html




def ensinar_interface(estilo, pergunta, nova_resp):

# Permite ao usuário ensinar novas respostas: - adiciona ao dicionário em tempo real - salva em arquivo para persistência
    
    if not pergunta or not nova_resp:
        return "<span style='color:red;'>❌ Preencha os dois campos para ensinar.</span>"
    chave = pergunta.lower()
    respostas[estilo].setdefault(chave, []).append(nova_resp)
    salvar_aprendizado(estilo, chave, nova_resp)
    return f"<span style='color:green;font-weight:bold;'>✅ Aprendido!</span><br><em>{pergunta}</em> → {nova_resp} (estilo {estilo})"

# ---------- Função de saída ----------
def sair_sessao():

 # Gera um resumo da sessão: - total de interações - pergunta mais frequente - Depois zera os contadores de sessão.

    global total_interacoes, contador_perguntas
    if total_interacoes == 0:
        return "<b>Nenhuma interação nesta sessão.</b>"
    
    mais_frequente = contador_perguntas.most_common(1)[0][0] if contador_perguntas else "N/A"
    
    resumo = f"""
    <b>Resumo da sessão:</b><br>
    Número total de interações: {total_interacoes}<br>
    Pergunta mais frequente: {mais_frequente}<br>
    """
    
    # Resetar contadores da sessão
    total_interacoes = 0
    contador_perguntas = Counter()
    
    return resumo

# ================================================================
# >>> INTERFACE GRADIO
# ================================================================

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("<h2 style='text-align:center; color:#2E8B57;'>ChatBot - ArariTour</h2>")
    gr.HTML("""
        <div style="width:100%; display:flex; justify-content:center; margin-bottom:15px;">
            <div style="text-align:center;">
                <img src="https://i.imgur.com/59ADZSc.png"
                     style="width:150px;height:150px;border-radius:50%; border:3px solid #2E8B57; box-shadow:2px 2px 15px rgba(0,0,0,0.3);" />
                <br>
                <span style="font-weight:bold; color:#2E8B57; font-size:18px;">Araripinho</span>
            </div>
        </div>
    """)
    gr.Markdown("As últimas 5 interações anteriores aparecem abaixo (se existirem).")

    # Dropdown para selecionar o estilo de linguagem

    estilo_select = gr.Dropdown(
        choices=["Regional", "Formal", "Engraçado"],
        label="Estilo da linguagem",
        value="Regional"
    )

    # Contador de estilos em tempo real

    estilo_contador_html = gr.HTML(
        value=f"""
        <b>Estilos usados:</b><br>
        Regional: {contador_estilos['Regional']}<br>
        Formal: {contador_estilos['Formal']}<br>
        Engraçado: {contador_estilos['Engraçado']}
        """
    )

     # Área principal do chat

    chatbot = gr.Chatbot(
        value=ultimas_interacoes() or [{"role": "assistant", "content": "Olá! Escolha um estilo e pergunte sobre o Cariri 😉"}],
        height=400,
        type="messages"
    )

    # Caixa de texto para o usuário digitar
    
    msg = gr.Textbox(label="Digite sua mensagem", placeholder="Escreva aqui...", lines=1)
    

    msg.submit(responder_interface, [msg, chatbot, estilo_select], [msg, chatbot, estilo_contador_html])

    # --- Seção de Ensino ---
    with gr.Accordion("📝 Ensinar uma nova pergunta/resposta", open=False):
        gr.Markdown(
            "Aqui você pode **ensinar a Ararinha** a responder algo novo. "
            "Escreva a **palavra-chave ou frase** e a resposta desejada. "
            "Quando alguém mencionar qualquer palavra dessa frase, a Ararinha lembrará!"
        )
        with gr.Row():
            nova_pergunta = gr.Textbox(
                label="Palavra-chave ou frase",
                placeholder="Ex: restaurante, onde posso comer tapioca..."
            )
            nova_resposta = gr.Textbox(
                label="Resposta da Ararinha",
                placeholder="Ex: Você pode experimentar a tapioca na Expocrato!"
            )
        ensinar_btn = gr.Button("✅ Ensinar agora")
        saida_ensinar = gr.HTML()
        ensinar_btn.click(
            ensinar_interface,
            [estilo_select, nova_pergunta, nova_resposta],
            saida_ensinar
        )

    # Botão para limpar apenas a conversa da interface

    clear = gr.Button("🔄 Limpar conversa")
    clear.click(lambda: ultimas_interacoes() or [{"role":"assistant","content":"Oi cabra! Escolha um estilo e pergunte sobre o Cariri 😉"}],
                None,
                chatbot)
    
     
     # Botão para limpar histórico de arquivo e contadores

    clear_historico = gr.Button("🗑️ Limpar histórico")
    clear_historico.click(
    limpar_historico,
    None,
    [chatbot, estilo_contador_html]
)

    # --- Botão Sair ---
    sair_btn = gr.Button("🚪 Sair")
    saida_sair = gr.HTML()
    sair_btn.click(sair_sessao, None, saida_sair)


# Lança a aplicação
demo.launch(share=True)
