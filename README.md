# 🤖 ChatBot ArariTour

## 📌 Descrição do Projeto
O **ArariTour** é um chatbot interativo desenvolvido em **Python** com a biblioteca **Gradio**, que fornece informações sobre a região do **Cariri**.  
Ele ajuda turistas e moradores a conhecerem **pontos turísticos**, **hospedagem**, **gastronomia** e **eventos locais**, oferecendo uma experiência divertida e personalizada.

O chatbot possui **três estilos de linguagem**:
- 🏡 **Regional**: linguagem típica da região, informal e acolhedora.  
- 🏛️ **Formal**: respostas polidas e institucionais.  
- 😂 **Engraçado**: tom descontraído, com emojis e expressões divertidas.  

Recursos principais:
- Perguntar sobre turismo e cultura local.  
- Ensinar **novas respostas** ao chatbot (aprendizado dinâmico).  
- Limpar o **histórico de conversa** e resetar os contadores de interação.  
- Visualizar um **resumo da sessão** ao encerrar.  

Mascote: **Araripinho** — representação divertida do *soldadinho-do-Araripe*.

---

## 🚀 Como Executar

### 1️⃣ Pré-requisitos
- **Python 3.x** instalado  
- Biblioteca: `gradio`

Instale a dependência:
    pip install gradio

### 2️⃣ Clonar o repositório
    git clone https://github.com/seu-usuario/ArariTour.git
    cd ArariTour

### 3️⃣ Executar o chatbot
    python app.py

O Gradio exibirá um link local no terminal (ex.: http://localhost:7860). Abra-o no navegador para interagir com o chatbot.

---

## 👥 Integrantes e Funções
| Integrante         | Função no Projeto                                      |
|--------------------|--------------------------------------------------------|
| André Wesley       | 🧑‍💻 Desenvolvedor Principal – programação e integração com Gradio |
| Pedro Kauan        | 🎨 Design de Interface – layout e imagens              |
| Ramona Vitória     | 📚 Conteúdo e Pesquisa – informações turísticas e textos|
| Renan Munhoz       | 🧪 Testes e Qualidade – QA e validação de respostas    |

---

## 🖼️ Demonstrações
### Prints
![Imagem 1] (Imagens/Foto_1Arari.jpeg)
![Imagem 2] (Imagens/Foto_2Arari.jpeg)

### Vídeo
  [▶️ Vídeo de demonstração](Video/8d5430df-8430-4e1a-963f-206d9057f3ca.mp4)

---

## 🗂️ Estrutura de Arquivos

📁 ArariTour  
├─ 📄 app.py                # Código principal do chatbot  
├─ 📄 README.md             # Documento de apresentação do projeto  
├─ 📄 requirements.txt      # Dependências do Python  
├─ 📁 data                  # Arquivos de dados  
│   ├─ 📄 historico.txt     # Histórico de interações  
│   ├─ 📄 aprendizado.txt   # Respostas aprendidas  
│   └─ 📄 contador_estilos.txt  # Contador de estilos de linguagem  
├─ 📁 docs                  # Arquivos de demonstração  
│   ├─ 🖼️ print1.png        # Captura de tela da interface  
│   └─ 🖼️ print2.png        # Exemplo de conversa  
└─ 📁 assets                # (Opcional) Ícones, mascote, imagens extras  
    └─ 🖼️ araripinho.png

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.13** linguagem utilizada 
- **Gradio** (interface web)  
- **collections.Counter** para contagem de estilos/interações  
- **Arquivos .txt** para persistência simples
- **ChatGPT** para construção do código
- **VSCode** para testes e modificações do código principal

---

### 📜 Licença
Projeto para fins educacionais e demonstrativos. Contribuições são bem-vindas! 🚀
