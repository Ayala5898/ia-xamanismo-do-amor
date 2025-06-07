import streamlit as st
from spiritual_ai import gerar_conteudo_espiritual

# 🌿 Carrega o estilo ritualístico EXTERNO (temporariamente comentado para evitar bug do Streamlit)
# with open("ritual_style.css") as f:
#     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🌿 Título e introdução
st.markdown("""
# 🌿 <span style="color: #d4af37;">Painel de Criação Espiritual – Xamanismo do Amor</span> 🌿

Crie conteúdos profundos e cerimoniais com um clique ✨

<span style="color:#e75480;">🌸 Como usar a Estratégia ritualística de marketing:</span>  
Escolha abaixo da estratégia ritualística desejada.  
A IA gerará um plano completo com fases do ciclo ritualístico, arquétipos, fio ritualístico, tom de comunicação e tipos de conteúdo sugeridos.  

Este plano te ajudará a estruturar campanhas cerimoniais, jornadas de conversão com alma e lançamentos com coerência ritual.

⚠️ Importante: Esta IA não gera marketing comum — ela convoca, nutre e converte através do campo ritualístico, respeitando o caminho da alma e do pertencimento.  

🌞 Use com presença, intenção e beleza ritualística.
""", unsafe_allow_html=True)

# 🌿 Seletor de tipo de conteúdo
opcao = st.selectbox("O que você deseja criar agora?", [
    "Legenda mística para Instagram",
    "Texto ritualístico para Reels",
    "Texto para carrossel cerimonial",
    "Mensagem para grupo de WhatsApp",
    "Texto para email cerimonial",
    "Estratégia ritualística de marketing",  # botão especial que abre o plano completo
    "Me entrega uma mandala de conteúdo para meu produto",
    "Preciso de uma copy xamânica que convida sem pressionar",
    "Quero um planejamento místico-estratégico com base nos arquétipos",
    "Desenha um lançamento com estrutura de rito de passagem",
    "Cria uma sequência de conteúdo cerimonial com ativação emocional e venda sutil",
    "Preciso de uma jornada de conversão com alma",
    "Quero um plano ritualístico de marketing com poder de conversão"
])

# 🌿 Seletor de tipo de ritual
ritual_nome = st.selectbox("Tipo de Ritual / Jornada:", [
    "Ritual com Ayahuasca",
    "Ritual de Solstício",
    "Ritual de Lua Cheia",
    "Ritual de Maria Madalena",
    "Ritual das Águas Sagradas",
    "Ritual de Equinócio",
    "Outro Ritual"
])

# 🌿 Seletor de canal
canal = st.selectbox("Para qual canal você quer criar?", [
    "Feed do Instagram",
    "Stories do Instagram",
    "Grupo de WhatsApp",
    "Email",
    "Página de vendas",
    "Outro canal"
])

# 🌿 Seletor de profundidade
profundidade = st.selectbox("Qual nível de profundidade?", [
    "Básico",
    "Médio",
    "Avançado",
    "Profundo"
])

# 🌿 Campo de texto para tema ou intenção
tema = st.text_input("Qual é o tema ou intenção do conteúdo?")

# 🌿 Botão para gerar o conteúdo
if st.button("✨ Gerar conteúdo ritualístico"):
    with st.spinner("Gerando conteúdo cerimonial... ✨"):
        resultado = gerar_conteudo_espiritual(tema, opcao, canal, profundidade, usar_assinatura=True, tipo_ritual=ritual_nome, outro_ritual_nome="", estrategia_tipo="")

    st.markdown("### 🌸 Conteúdo gerado:")
    st.markdown(resultado)

    # 🌹 Assinatura padrão
    assinatura = """
Com amor e honra,  
🌹 Arlete Ayala Souza  
Xamã Ancestral do Amor – guiando por meio do amor à cura, à liberdade e ao voo sagrado da alma.
    """
    st.markdown(assinatura)
