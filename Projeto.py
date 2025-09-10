arquivo = open("respostas.txt", "w", encoding="utf-8")
arquivo.write("Testando código\n")

# Arquivos
arquivo_aprendizado = "aprendizado.txt"
arquivo_historico = "historico.txt"

# Arquivos
# "

# Dicionário inicial com palavras-chave
respostas = {
    "Formal": {
        "pontos turísticos": "Os pontos turísticos mais conhecidos da região são: Chapada do Araripe, Geopark Araripe e Museu de Paleontologia em Santana do Cariri.",
        "hospedagem": "A maior quantidade de opções encontra-se nas cidades de Juazeiro do Norte, Barbalha e Crato, desde hotéis econômicos até pousadas familiares.",
        "eventos": "Dois eventos populares: Festival Expocrato e Festa do Pau da Bandeira de Santo Antônio de Barbalha."
    },
    "Engraçado": {
        "pontos turísticos": "Se liga! 📸 Chapada do Araripe, Geopark e Museu dos Dinossauros. Selfie garantida! 🦖😂",
        "hospedagem": "Tem de tudo: hotel chique, pousada aconchegante... só não vale dormir na praça 😅",
        "eventos": "Dois rolês que bombam: 🎉 Festival Expocrato e Festa do Pau da Bandeira. Forró, fé e alegria! 🍻"
    },
    "Regional": {
        "pontos turísticos": "Ôxente, cabra! Tu tem que conhecer a Chapada do Araripe, o Geopark e o Museu dos Dinossauros. É de encher os olhos, visse?",
        "hospedagem": "Tem opção pra todo bolso, meu rei! Em Juazeiro, Crato e Barbalha tem hotel e pousada que é um aconchego só.",
        "eventos": "Dois dos festejos mais arretados: Festival Expocrato e Festa do Pau da Bandeira. É forró e alegria que só a moléstia!"
    }
}

# Mapear estilos
personalidades = {
    1: "Formal",
    2: "Engraçado",
    3: "Regional"
}

# Funções de arquivos
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

# Garante que os arquivos existem
arquivo = open(arquivo_aprendizado, "a", encoding="utf-8")
arquivo.close()
arquivo = open(arquivo_historico, "a", encoding="utf-8")
arquivo.close()

# Carregar aprendizado
arquivo = open(arquivo_aprendizado, "r", encoding="utf-8")
for linha in arquivo:
    partes = linha.strip().split("|")
    if len(partes) == 3:
        estilo, palavra_chave, resposta = partes
        if estilo in respostas:
            respostas[estilo][palavra_chave] = resposta
        else:
            respostas[estilo] = {palavra_chave: resposta}
arquivo.close()

# Exibir últimas 5 interações anteriores
arquivo = open(arquivo_historico, "r", encoding="utf-8")
linhas = arquivo.readlines()
arquivo.close()
if linhas:
    print("\nÚltimas 5 interações anteriores:")
    for l in linhas[-5:]:
        print(l.strip())
    print("-" * 40)

# Loop principal
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

    # Buscar palavra-chave no dicionário
    achou = False
    for chave in respostas[estilo]:
        if chave in pergunta_usuario:
            resposta_bot = respostas[estilo][chave]
            print(resposta_bot)
            salvar_historico(pergunta_usuario, resposta_bot)
            achou = True

    if not achou:
        print("Ainda não sei responder isso. 😢")
        nova_resposta = input("Você pode me ensinar? Digite uma resposta apropriada: ").strip()
        respostas[estilo][pergunta_usuario] = nova_resposta
        salvar_aprendizado(estilo, pergunta_usuario, nova_resposta)
        salvar_historico(pergunta_usuario, nova_resposta)
        print("Obrigado! Aprendi algo novo e salvei no arquivo aprendizado.txt ✅")

