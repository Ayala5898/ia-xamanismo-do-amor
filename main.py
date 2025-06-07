import streamlit as st
from spiritual_ai import gerar_conteudo_espiritual

# 🌿 Carrega o estilo ritualístico EXTERNO (aqui que corrige!)
with open("ritual_style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# 🌿 Título e introdução
st.markdown("""
# 🌿 <span style="color: #d4af37;">Painel de Criação Espiritual – Xamanismo do Amor</span> 🌿

Crie conteúdos profundos e cerimoniais com um clique ✨

<span style="color:#e75480;">🌸 Como usar a Estratégia ritualística de marketing:</span>  
Escolha abaixo da estratégia ritualística desejada.  
A IA gerará um plano completo com fases do ciclo ritualístico, arquétipos, fio ritualístico, tom de comunicação e tipos de conteúdo sugeridos.  

Este plano te ajudará a estruturar campanhas cerimoniais, jornadas de conversão com alma e lançamentos com coerência ritual.

⚠️ *Importante:* Esta IA não gera marketing comum — ela convoca, nutre e converte através do campo ritualístico, respeitando o caminho da alma e do pertencimento.  

🌞 *Use com presença, intenção e beleza ritualística.*
""", unsafe_allow_html=True)

# 🌿 Seletor de tipo de conteúdo
opcao = st.selectbox("O que você deseja criar agora?", [
    "Legenda mística para Instagram",
    "Texto ritualístico para Reels",
    "Texto para carrossel cerimonial",
    "Mensagem para grupo de WhatsApp",
    "Texto para email cerimonial",
    "Estratégia ritualística de marketing"
])

# 🌿 Seletor de tipo de ritual
ritual_nome = st.selectbox("Tipo de Ritual / Jornada:", [
    "Ritual com Ayahuasca",
    "Ritual de Solstício",
    "Ritual de Lua Cheia",
    "Ritual de Maria Madalena",
    "Ritual das Águas Sagradas",
    "Ritual de Equ
