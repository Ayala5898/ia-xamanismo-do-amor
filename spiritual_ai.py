def gerar_conteudo_espiritual(tema, opcao, canal, profundidade, usar_assinatura, tipo_ritual, outro_ritual_nome, estrategia_tipo):
    hashtags_fixas = "#XamanismoDoAmor #RituaisDeCura #FamíliaCósmica #Pertencimento #RitualDoAmor"

    assinatura = """
*Com amor e honra,*  
🌹 Arlete Ayala Souza  
Xamã Ancestral do Amor – guiando por meio do amor à cura, à liberdade e ao voo sagrado da alma.
    """ if usar_assinatura else ""

    if tipo_ritual == "Outro Ritual" and outro_ritual_nome.strip():
        ritual_nome = outro_ritual_nome.strip()
    else:
        ritual_nome = tipo_ritual

    # Estratégia ritualística de marketing
    if opcao == "Estratégia ritualística de marketing":
        resultado = f"""
🌕 *Estratégia ritualística de marketing*  
*Ritual / Jornada:* {ritual_nome}  
*Tema:* {tema}  
*Profundidade:* {profundidade}  
*Tipo de estratégia:* {estrategia_tipo}

✨ *Fio ritualístico da campanha:*  
“Há caminhos que pedem passagem. Há rezos que pedem palavra. Que este ciclo de {ritual_nome} se desenhe em presença e verdade.”

🌿 *Fases do ciclo ritualístico:*  
1️⃣ *Fase da Semente (Preparação do campo)*  
2️⃣ *Fase da Convocação (Chamada ritualística)*  
3️⃣ *Fase da Nutrição Cerimonial (Conteúdos que nutrem o campo)*  
4️⃣ *Fase da Conversão (Chamada com alma)*  
5️⃣ *Fase Pós-Ritual (Integração e continuidade do vínculo)*

🌀 *Arquétipos sugeridos por fase:*  
- Semente → A Tecelã do Destino, O Guardião do Silêncio  
- Convocação → A Voz da Mãe Ancestral, O Arauto da Verdade  
- Nutrição → A Guardiã do Fogo, A Mãe das Águas  
- Conversão → O Guerreiro de Luz, A Guardiã da Palavra  
- Pós-Ritual → A Anciã da Sabedoria, O Curador da Tradição

🕊️ *Tom de comunicação:*  
Profundo, cerimonial, sem urgência.  
Convite ao pertencimento, não à compra.  
Palavras que tocam a alma e despertam lembranças arquetípicas.

🎴 *Tipos de conteúdo por fase:*  
1️⃣ *Semente:*  
- Reels com histórias arquetípicas  
- Post sobre linhagem, pertencimento, rezo  
- Mensagem para grupo com pergunta ritualística

2️⃣ *Convocação:*  
- Sequência de Stories com frase âncora e caixa de resposta  
- Live com rezo e partilha  
- Post com mini-story ritualístico

3️⃣ *Nutrição Cerimonial:*  
- Email cerimonial com narrativa viva  
- Post sobre o ritual e seus símbolos  
- Bastidor ritualístico (foto do altar, frase cerimonial)  

4️⃣ *Conversão:*  
- Reels com depoimento de quem viveu o ritual  
- Chamada para grupo ou inscrição com frase ritualística  
- Live final com rezo de convocação

5️⃣ *Pós-Ritual:*  
- Email de integração com mensagem de rezo  
- Story com depoimento ou momento ritual  
- Post com convite para próximo ciclo

🌸 *Extras ritualísticos:*  
- Imagem de perfil sugerida: símbolo ritualístico com nome {ritual_nome}  
- Hashtags sugeridas:  
{hashtags_fixas}

{assinatura}
        """

    # Templates padrão para os outros tipos de conteúdo
    elif opcao == "Legenda mística para Instagram":
        resultado = f"""
✨ {tema}

Em cada palavra, um eco das memórias ancestrais. Que esta legenda sobre {tema} abra portais de presença e reverência.

{hashtags_fixas}
{assinatura}
        """

    elif opcao == "Texto ritualístico para Reels":
        resultado = f"""
🎥 *Roteiro para Reels Ritualístico:*  
*Tema:* {tema}  
*Canal:* {canal}  
*Profundidade:* {profundidade}

👉 Começa com uma imagem simbólica forte relacionada a {tema}.  
👉 Insere um rezo ou frase de poder.  
👉 Mostra um gesto ritual (mãos, vela, água, natureza).  
👉 Finaliza com uma chamada sutil ao pertencimento.

{hashtags_fixas}
{assinatura}
        """

    elif opcao == "Texto para carrossel cerimonial":
        resultado = f"""
*Slide 1:* Título profundo sobre {tema}  
*Slide 2:* Pergunta que abre o coração  
*Slide 3:* Ensinamento espiritual sobre {tema}  
*Slide 4:* Imagem ritualística ou símbolo  
*Slide 5:* Integração emocional e espiritual  
*Slide 6:* Rezo ou mantra final  
*Slide 7:* Chamada para ação / comunidade

{hashtags_fixas}
{assinatura}
        """

    elif opcao == "Mensagem para grupo de WhatsApp":
        resultado = f"""
🌸 Mensagem Cerimonial para Grupo 🌸

Hoje, nos reunimos no campo sagrado do {ritual_nome}.  
Que esta mensagem sobre {tema} ative em ti memórias antigas e a força do pertencimento.

*Rezo:*  
“Que cada palavra seja um fio de luz em tua jornada.”

{hashtags_fixas}
{assinatura}
        """

    elif opcao == "Texto para email cerimonial":
        resultado = f"""
🌸 *Email Cerimonial:* {tema}

Querida alma,  

Hoje compartilho contigo um rezo profundo: {tema}.  
Que este email seja um fio de presença e de nutrição espiritual.

🌿 *Mensagem:*  
[Escreve aqui o desenvolvimento da mensagem sobre o tema.]

🌕 Que tua jornada se ilumine.  

{hashtags_fixas}
{assinatura}
        """

    else:
        resultado = "🌟 Opção não reconhecida."

    return resultado
