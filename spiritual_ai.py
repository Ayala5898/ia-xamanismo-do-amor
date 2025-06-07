def gerar_conteudo_espiritual(tema, opcao, canal, profundidade, usar_assinatura, tipo_ritual, outro_ritual_nome, estrategia_tipo):
    hashtags_fixas = "#XamanismoDoAmor #RituaisDeCura #FamíliaCósmica #Pertencimento #RitualDoAmor"

    assinatura = """
**Com amor e honra,**  
🌹 *Arlete Ayala Souza*  
*Xamã Ancestral do Amor – guiando por meio do amor à cura, à liberdade e ao voo sagrado da alma.*
    """ if usar_assinatura else ""

    if tipo_ritual == "Outro" and outro_ritual_nome.strip():
        ritual_nome = outro_ritual_nome.strip()
    else:
        ritual_nome = tipo_ritual

    # Estratégia ritualística de marketing
    if opcao == "Estratégia ritualística de marketing":
        resultado = f"""
🌕 **Estratégia ritualística de marketing**  
**Ritual / Jornada:** {ritual_nome}  
**Tema:** {tema}  
**Profundidade:** {profundidade}  
**Tipo de estratégia:** {estrategia_tipo}

✨ **Fio ritualístico da campanha:**  
“Há caminhos que pedem passagem. Há rezos que pedem palavra. Que este ciclo de {ritual_nome} se desenhe em presença e verdade.”

🌿 **Fases do ciclo ritualístico:**  
1️⃣ **Fase da Semente (Preparação do campo)**  
2️⃣ **Fase da Convocação (Chamada ritualística)**  
3️⃣ **Fase da Nutrição Cerimonial (Conteúdos que nutrem o campo)**  
4️⃣ **Fase da Conversão (Chamada com alma)**  
5️⃣ **Fase Pós-Ritual (Integração e continuidade do vínculo)**

🌀 **Arquétipos sugeridos por fase:**  
- Semente → A Tecelã do Destino, O Guardião do Silêncio  
- Convocação → A Voz da Mãe Ancestral, O Arauto da Verdade  
- Nutrição → A Guardiã do Fogo, A Mãe das Águas  
- Conversão → O Guerreiro de Luz, A Guardiã da Palavra  
- Pós-Ritual → A Anciã da Sabedoria, O Curador da Tradição

🕊️ **Tom de comunicação:**  
Profundo, cerimonial, sem urgência.  
Convite ao pertencimento, não à compra.  
Palavras que tocam a alma e despertam lembranças arquetípicas.

🎴 **Tipos de conteúdo por fase:**  
1️⃣ **Semente:**  
- Reels com histórias arquetípicas  
- Post sobre linhagem, pertencimento, rezo  
- Mensagem para grupo com pergunta ritualística

2️⃣ **Convocação:**  
- Sequência de Stories com frase âncora e caixa de resposta  
- Live com rezo e partilha  
- Post com mini-story ritualístico

3️⃣ **Nutrição Cerimonial:**  
- Email cerimonial com narrativa viva  
- Post sobre o ritual e seus símbolos  
- Bastidor ritualístico (foto do altar, frase cerimonial)  

4️⃣ **Conversão:**  
- Reels com depoimento de quem viveu o ritual  
- Chamada para grupo ou inscrição com frase ritualística  
- Live final com rezo de convocação

5️⃣ **Pós-Ritual:**  
- Email de integração com mensagem de rezo  
- Story com depoimento ou momento ritual  
- Post com convite para próximo ciclo

🌸 **Extras ritualísticos:**  
- Imagem de perfil sugerida: símbolo ritualístico com nome *{ritual_nome}*  
- Hashtags sugeridas:  
{hashtags_fixas}

{assinatura}
        """

    # Templates padrão para os outros tipos de conteúdo
    elif opcao == "Legenda mística para Instagram":
        resultado = f"""
✨ {tema}

Em cada palavra, um eco das memórias ancestrais. Que esta legenda sobre *{tema}* abra portais de presença e reverência.

{hashtags_fixas}
{assinatura}
        """

    elif opcao == "Roteiro de carrossel espiritual":
        resultado = f"""
**Slide 1:** Título profundo sobre *{tema}*  
**Slide 2:** Pergunta que abre o coração  
**Slide 3:** Ensinamento espiritual sobre *{tema}*  
**Slide 4:** Imagem ritualística ou símbolo  
**Slide 5:** Integração emocional e espiritual  
**Slide 6:** Rezo ou mantra final  
**Slide 7:** Chamada para ação / comunidade

{hashtags_fixas}
{assinatura}
        """

    elif opcao == "Frase cerimonial para Story":
        resultado = f"""
🕊️ *No silêncio de {tema}, tua alma escuta o que o tempo esqueceu de lembrar.* 🌹

{hashtags_fixas}
{assinatura}
        """

    elif opcao == "Chamada para live ritualística":
        resultado = f"""
🌙 **Live Ritualística: {tema}**  
Em teu coração, o que este {tema} desperta?  
Prepara teu altar. A chama já foi acesa.  
Te convido a atravessar este portal em comunidade.

{hashtags_fixas}
{assinatura}
        """

    elif opcao == "Meditação guiada completa":
        if profundidade == "Profundo":
            introducao = f"Hoje, serás conduzid@ por uma travessia ritual sobre o tema *{tema}*. Este não é um caminho comum — é um voo sagrado."
            visualizacao = f"Visualiza um grande círculo de luz, onde tua alma repousa em segurança. Ao centro, o tema *{tema}* se revela em símbolos, imagens e memórias."
            aprofundamento = f"Agora, permite que teu espírito atravesse as camadas ocultas do {tema}. Quais feridas emergem? Que bênçãos te aguardam no invisível?"
        elif profundidade == "Médio":
            introducao = f"Hoje, serás guiad@ a uma jornada suave sobre o tema *{tema}*."
            visualizacao = f"Visualiza um campo sereno onde o tema *{tema}* dança em tua frente."
            aprofundamento = f"Sente o que este {tema} toca em teu coração e corpo."
        else:  # Básico
            introducao = f"Iniciaremos uma meditação breve sobre *{tema}*."
            visualizacao = f"Visualiza uma luz suave envolvendo o tema *{tema}*."
            aprofundamento = f"Permite que um sentimento de paz surja ao contemplar este {tema}."

        resultado = f"""
🌬️ *Meditação Guiada: {tema}*

👁️ Introdução  
{introducao}

💨 Respiração  
Inspira profundamente... Segura... Expira... Três vezes.  
Sente teus pés, tuas mãos, tua respiração.

🌌 Visualização  
{visualizacao}

🕊️ Aprofundamento  
{aprofundamento}

🌿 Retorno suave  
Sente novamente teu corpo. Move os dedos, os ombros.  
Ao teu tempo, abre os olhos.

🌸 Bênção final  
Que este {tema} seja um portal de amor, clareza e reconexão.  
Tua alma ouviu. Teu corpo acolheu. Está feito.

{hashtags_fixas}
{assinatura}
        """

    else:
        resultado = "🌟 Opção não reconhecida."

    return resultado

