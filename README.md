# ChatBot ArariTour

## Descrição do Projeto

O **ArariTour** é um chatbot interativo desenvolvido em Python usando a biblioteca **Gradio**. Ele fornece informações sobre a região do **Cariri**, incluindo pontos turísticos, hospedagem, gastronomia e eventos locais. Além disso, o chatbot possui três estilos de linguagem diferentes:

- **Regional:** linguagem típica da região, informal e acolhedora.
- **Formal:** respostas mais polidas e institucionais.
- **Engraçado:** tom divertido e descontraído, com emojis e expressões informais.

O usuário pode:

- Perguntar sobre turismo e cultura local.
- Ensinar novas respostas ao chatbot.
- Limpar o histórico de conversa e resetar contadores de interações.
- Sair da sessão e visualizar um resumo de interações.

O mascote do chatbot é **Araripinho**, uma representação divertida do “soldadinho do Araripe”.

---

## Funcionalidades

1. Chatbot com múltiplos estilos de linguagem.
2. Armazenamento de histórico de conversas (últimas 5 interações exibidas).
3. Aprendizado de novas respostas pelo usuário.
4. Contadores de interações e estilos usados.
5. Botão para limpar histórico e resetar contadores.
6. Resumo da sessão ao sair.

---

## Tecnologias Utilizadas

- Python 3.x
- Gradio
- Collections (Counter)
- Sistema de arquivos local para persistência (`.txt`)

---

## Estrutura de Arquivos

- `app.py` → Código principal do chatbot.
- `historico.txt` → Armazena as interações do usuário com o bot.
- `aprendizado.txt` → Armazena novas respostas aprendidas.
- `contador_estilos.txt` → Armazena o contador de uso dos estilos de linguagem.

---