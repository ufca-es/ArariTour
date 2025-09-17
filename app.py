# app.py
import streamlit as st
import random

# Seu dicionário de respostas e personalidades (reduzi para deixar enxuto, mas você pode colocar o seu completo)
respostas = {
    "Formal": {
        ("pontos turísticos", "atrações", "lugares para visitar"): [
            "Os pontos turísticos mais conhecidos são: Chapada do Araripe, Geopark e Museu de Paleontologia.",
            "Você pode visitar a Chapada do Araripe, Geopark e Museu de Paleontologia em Santana do Cariri."
        ],
        ("hospedagem", "hotel", "pousada"): [
            "A maior quantidade de opções está em Juazeiro do Norte, Barbalha e Crato.",
            "Existem hotéis econômicos e pousadas aconchegantes nas principais cidades."
        ],
    },
    "Engraçado": {
        ("pontos turísticos", "atrações", "lugares para visitar"): [
            "Quer selfie com dinossauro? Museu dos Dinossauros! 🦖😂",
            "Chapada do Araripe é o lugar para vistas de tirar o fôlego! 🌄"
        ],
        ("hospedagem", "hotel", "pousada"): [
            "Tem hotel chique e pousada aconchegante... só não durma na praça! 😅",
            "Opções não faltam: do luxo ao simples, tem pra todo gosto!"
        ],
    }
}

personalidades = {1: "Formal", 2: "Engraçado"}

# Inicializa o estado da sessão
if "fase" not in st.session_state:
    st.session_state.fase = "inicio"  # fases: inicio, escolha_personalidade, pergunta, resposta
if "estilo" not in st.session_state:
    st.session_state.estilo = None
if "pergunta" not in st.session_state:
    st.session_state.pergunta = ""
if "resposta" not in st.session_state:
    st.session_state.resposta = ""

st.title("Soldadinho-do-Araripe Chatbot")

def escolher_personalidade():
    st.write("Escolha o estilo de resposta:")
    for k, v in personalidades.items():
        if st.button(f"{k} - {v}"):
            st.session_state.estilo = v
            st.session_state.fase = "pergunta"
            st.session_state.resposta = ""
            st.session_state.pergunta = ""

def perguntar_tema():
    st.write(f"Você escolheu o estilo: **{st.session_state.estilo}**")
    pergunta = st.text_input("Sobre o que você quer saber? (ex: pontos turísticos, hospedagem, eventos)", value=st.session_state.pergunta)
    if st.button("Enviar"):
        if pergunta.strip() == "":
            st.warning("Por favor, digite algo!")
            return
        st.session_state.pergunta = pergunta
        # Procura resposta
        estilo = st.session_state.estilo
        palavras_usuario = pergunta.lower().split()
        resposta_bot = "Ainda não sei responder isso. 😢"
        achou = False
        for chaves in respostas.get(estilo, {}):
            if any(palavra in chaves for palavra in palavras_usuario):
                valor = respostas[estilo][chaves]
                resposta_bot = random.choice(valor)
                achou = True
                break
        st.session_state.resposta = resposta_bot
        st.session_state.fase = "resposta"

def mostrar_resposta():
    st.write(f"**Você perguntou:** {st.session_state.pergunta}")
    st.write(f"**Resposta:** {st.session_state.resposta}")
    if st.button("Fazer outra pergunta"):
        st.session_state.fase = "pergunta"
        st.session_state.pergunta = ""
        st.session_state.resposta = ""
    if st.button("Voltar para escolha de estilo"):
        st.session_state.fase = "inicio"
        st.session_state.estilo = None
        st.session_state.pergunta = ""
        st.session_state.resposta = ""

# Fluxo
if st.session_state.fase == "inicio":
    escolher_personalidade()
elif st.session_state.fase == "pergunta":
    perguntar_tema()
elif st.session_state.fase == "resposta":
    mostrar_resposta()
