import streamlit as st
from spiritual_ai import gerar_conteudo_espiritual
from fpdf import FPDF
import base64
import urllib.parse

st.set_page_config(page_title="IA Cerimonial da Ayala", layout="centered")
st.title("🌿 Painel de Criação Espiritual – Xamanismo do Amor")
st.markdown("Crie conteúdos com apenas um clique ✨")

opcao = st.selectbox("O que você deseja criar agora?", [
    "Legenda mística para Instagram",
    "Roteiro de carrossel espiritual",
    "Frase cerimonial para Story",
    "Chamada para live ritualística",
    "Conteúdo viral com campanha",
    "Meditação guiada completa"
])

tema = st.text_input("Qual é o tema ou intenção do conteúdo?")

if st.button("Gerar Conteúdo"):
    if not tema:
        st.warning("Por favor, insira um tema para gerar o conteúdo.")
    else:
        resultado = gerar_conteudo_espiritual(tema, opcao)
        st.success("✨ Conteúdo gerado com sucesso!")
        st.text_area("📝 Resultado", resultado, height=300)

        # Copiar conteúdo
        st.code(resultado, language="markdown")

        # Botão de download PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in resultado.split('\n'):
            pdf.multi_cell(0, 10, line)
        pdf_file = "conteudo_espiritual.pdf"
        pdf.output(pdf_file)

        with open(pdf_file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_download_link = f'<a href="data:application/pdf;base64,{base64_pdf}" download="{pdf_file}">📥 Baixar como PDF</a>'
            st.markdown(pdf_download_link, unsafe_allow_html=True)

        # Botão de envio via WhatsApp
        mensagem = urllib.parse.quote(f"Conteúdo gerado pela IA Cerimonial da Ayala:\n\n{resultado}")
        whatsapp_link = f"https://wa.me/5531971252848?text={mensagem}"
        st.markdown(f"[📲 Enviar pelo WhatsApp](%s)" % whatsapp_link)
