#!/usr/bin/env python3
"""
Script para gerar PDF com respostas técnicas e instruções de screenshots
"""

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
    from datetime import datetime
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    print("[!] Instalando reportlab...")
    import subprocess
    subprocess.check_call(["pip", "install", "reportlab"])
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
    from datetime import datetime

# Criar PDF
pdf_path = "EVIDENCIAS_WEBSOCKET.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)

# Estilos
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1e40af'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.HexColor('#1e40af'),
    spaceAfter=8,
    spaceBefore=8,
    fontName='Helvetica-Bold'
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['Normal'],
    fontSize=10,
    alignment=TA_JUSTIFY,
    spaceAfter=6
)

# Conteúdo
content = []

# ===== PÁGINA 1: TÍTULO E SCREENSHOTS =====
content.append(Spacer(1, 0.3*inch))

content.append(Paragraph("WebSocket: Mural em Tempo Real", title_style))
content.append(Paragraph("Adoção de Pets - Projeto WebSocket", styles['Normal']))

content.append(Spacer(1, 0.2*inch))

content.append(Paragraph("<b>EVIDÊNCIAS DE FUNCIONAMENTO</b>", heading_style))

content.append(Spacer(1, 0.1*inch))

# Instruções de screenshots
evidencias_text = """
<b>1. PRINT DO SERVIDOR EM EXECUÇÃO</b><br/>
Mostrar terminal com:<br/>
- &quot;[*] SERVIDOR WEBSOCKET - MURAL EM TEMPO REAL&quot;<br/>
- &quot;[OK] Servidor iniciado em: ws://localhost:8000&quot;

<br/><b>2. PRINT DE DOIS CLIENTES CONECTADOS</b><br/>
Mostrar 2 abas do navegador lado a lado:<br/>
- Ambas em http://localhost:8001<br/>
- Status verde "Conectado" em ambas<br/>
- Campo de input visível

<br/><b>3. PRINT DA MENSAGEM EM TEMPO REAL</b><br/>
Após enviar mensagem como &quot;Luna foi adotada!&quot;:<br/>
- Mensagem aparecendo em ambas as abas<br/>
- Timestamp das mensagens visível<br/>
- Sem refresh necessário

<br/><b>4. PRINT DOS LOGS DO SERVIDOR</b><br/>
Terminal mostrando:<br/>
- &quot;[CONEXAO] Cliente xxx conectado&quot;<br/>
- &quot;[MENSAGEM] Do cliente xxx: Luna foi adotada!&quot;<br/>
- &quot;[OK] Broadcast concluido&quot;<br/>
- &quot;Total de clientes: 2&quot;
"""

content.append(Paragraph(evidencias_text, body_style))

content.append(PageBreak())

# ===== PÁGINA 2: RESPOSTAS TÉCNICAS =====
content.append(Spacer(1, 0.2*inch))

content.append(Paragraph("RESPOSTAS ÀS QUESTÕES TÉCNICAS", title_style))

content.append(Spacer(1, 0.15*inch))

# Pergunta A
content.append(Paragraph("<b>a) Como as conexões dos clientes foram armazenadas?</b>", heading_style))

resposta_a = """
Utilizamos um <b>dicionário Python</b> onde:<br/>
• <b>Chave:</b> objeto WebSocket (único por conexão)<br/>
• <b>Valor:</b> dict com {id: UUID, connected_at: timestamp}<br/>
<br/>
<font face="Courier" size="9">
clients = {}<br/>
clients[websocket] = {"id": uuid.uuid4(), "connected_at": datetime.now()}
</font><br/>
<br/>
Vantagem: Simples, eficiente e cleanup automático ao desconectar (del clients[websocket]).
"""

content.append(Paragraph(resposta_a, body_style))

content.append(Spacer(1, 0.1*inch))

# Pergunta B
content.append(Paragraph("<b>b) Como o sistema identifica um cliente conectado?</b>", heading_style))

resposta_b = """
Cada cliente recebe um <b>UUID v4 único</b> na conexão:<br/>
<br/>
<font face="Courier" size="9">
client_id = str(uuid.uuid4())<br/>
# Exemplo: "a1b2c3d4-e5f6-g7h8-i9j0k1l2m3n4"
</font><br/>
<br/>
Identificação por: (1) UUID (zero colisões), (2) Objeto WebSocket (chave do dict), (3) Ordem de conexão (visualmente).
"""

content.append(Paragraph(resposta_b, body_style))

content.append(PageBreak())

# Pergunta C
content.append(Spacer(1, 0.2*inch))

content.append(Paragraph("<b>c) O que aconteceria com polling?</b>", heading_style))

resposta_c = """
<b>Problemas do Polling HTTP:</b><br/>
• Latência alta (até 1000ms de delay)<br/>
• Requisições vazias (99% sem novidades)<br/>
• Overhead: protocolo HTTP completo a cada requisição<br/>
• Bandwidth 50-100x maior que WebSocket<br/>
• Escalabilidade ruim (100 clientes = 100 req/segundo)<br/>
<br/>
<b>Conclusão:</b> Polling é ineficiente para tempo real. WebSocket mantém conexão aberta e envia instantaneamente.
"""

content.append(Paragraph(resposta_c, body_style))

content.append(Spacer(1, 0.1*inch))

# Pergunta D
content.append(Paragraph("<b>d) Em quais cenários WebSocket é melhor que REST?</b>", heading_style))

resposta_d = """
<b>WebSocket é IDEAL para:</b> Chat tempo real, notificações push, jogos multiplayer, monitoramento de sistemas, dashboards vivos, colaboração simultânea.<br/>
<br/>
<b>REST é IDEAL para:</b> Dados estáticos (GET), CRUD, download de arquivos, cache.<br/>
<br/>
<b>Este projeto demonstra:</b> Chat/Mural em tempo real com múltiplos clientes recebendo atualizações instantaneamente, algo impossível de forma eficiente com REST/polling.
"""

content.append(Paragraph(resposta_d, body_style))

content.append(Spacer(1, 0.2*inch))

# Informações do projeto
info_style = ParagraphStyle(
    'Info',
    parent=styles['Normal'],
    fontSize=9,
    textColor=colors.HexColor('#666666'),
    alignment=TA_CENTER
)

content.append(Paragraph(
    f"Projeto WebSocket - Mural em Tempo Real | Data: {datetime.now().strftime('%d/%m/%Y')} | Python 3.14 + websockets",
    info_style
))

# Gerar PDF
doc.build(content)

print(f"\n✅ PDF gerado com sucesso: {pdf_path}")
print(f"📄 Localização: c:\\Users\\bruno\\Documents\\GITHUB\\projeto-websocket-adocao-pets\\{pdf_path}")
