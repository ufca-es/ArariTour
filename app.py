import gradio as gr
import random
from collections import Counter

# --- Configuração inicial ---
total_interacoes = 0
contador_personalidade = Counter()
contador_perguntas = Counter()
ultima_resposta = None

# Respostas da Ararinha
respostas = {
    ("pontos turísticos", "atrações", "lugares para visitar", "locais", "roteiro"): [
        "🦜 Chapada do Araripe, Geopark e Museu dos Dinossauros são os mais visitados, cabra!",
        "🦜 Vai por mim: Chapada pra foto, Geopark pra aprender e museu pros bichim antigos! 🦖",
    ],
    ("hospedagem", "hotel", "hotéis", "pousada", "pousadas",
     "alojamento", "alojamentos", "acomodação", "acomodações", "estadia"): [
        "🦜 Em Juazeiro, Crato e Barbalha tem hotel e pousada arretada, pra todo bolso!",
        "🦜 Oxente, se quiser conforto tem hotel, se quiser aconchego tem pousada! 😴",
    ],
    ("eventos", "festas", "shows", "programação"): [
        "🦜 No Cariri o forró é garantido: Festa do Pau da Bandeira e Expocrato são os maiores!",
        "🦜 Pau da Bandeira é fé, Expocrato é música boa! 🎶",
    ]
}

# --- Função de resposta ---
def responder(mensagem, historico):
    global ultima_resposta, total_interacoes

    palavras_usuario = mensagem.lower().split()
    contador_perguntas[mensagem] += 1
    total_interacoes += 1

    for chaves in respostas:
        for palavra in palavras_usuario:
            if any(palavra in c.lower() for c in (chaves if isinstance(chaves, tuple) else (chaves,))):
                possiveis = respostas[chaves][:]
                if ultima_resposta in possiveis and len(possiveis) > 1:
                    possiveis.remove(ultima_resposta)
                resposta_bot = random.choice(possiveis)
                ultima_resposta = resposta_bot
                historico.append(("👤 " + mensagem, resposta_bot))
                return "", historico

    # Se não encontrou resposta
    resposta_bot = "🦜 Eita, não sei responder isso ainda... mas pode perguntar de pontos turísticos, hospedagem ou eventos!"
    historico.append(("👤 " + mensagem, resposta_bot))
    return "", historico

# --- Interface estilo smartphone ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 📱 Chat da Ararinha do Sertão")
    gr.Markdown("Simulação de conversa compacta, estilo smartphone")

    # Chatbot corrigido
    chatbot = gr.Chatbot(
        height=350,
        show_label=False,
        container=True,
        type="messages"
    )

    msg = gr.Textbox(
        label="Digite sua mensagem",
        placeholder="Escreva aqui...",
        scale=8
    )
    clear = gr.Button("🔄 Limpar conversa")

    # Primeira mensagem automática
    chatbot.value = [("🦜 Ararinha", "Oi cabra! O que você deseja saber sobre a região? 😉")]

    msg.submit(responder, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: [("🦜 Ararinha", "Oi cabra! O que você deseja saber sobre a região? 😉")], None, chatbot)

demo.launch(share=True)
