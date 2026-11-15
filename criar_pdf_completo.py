#!/usr/bin/env python3
"""
Script para gerar PDF completo com respostas técnicas.
Passo 1: Gera o PDF com as respostas
Passo 2: Você adiciona os screenshots manualmente (GUIA_SCREENSHOTS.md)
Passo 3: Resultado final é o PDF entregável
"""

import os
from pathlib import Path
from datetime import datetime

try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
except ImportError:
    print("[*] Instalando reportlab...")
    import subprocess
    subprocess.check_call(["pip", "install", "reportlab"])
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT

# Cores do projeto
COR_PRINCIPAL = colors.HexColor('#1e40af')
COR_SECUNDARIA = colors.HexColor('#7c3aed')
COR_SUCESSO = colors.HexColor('#059669')
COR_TEXTO = colors.HexColor('#1f2937')

def criar_estilos():
    """Cria estilos personalizados para o PDF"""
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=26,
        textColor=COR_PRINCIPAL,
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=COR_SECUNDARIA,
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=colors.white,
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold',
        backColor=COR_PRINCIPAL,
        leftIndent=6,
        rightIndent=6,
        topPadding=4,
        bottomPadding=4
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
        leading=14,
        textColor=COR_TEXTO
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontSize=8,
        fontName='Courier',
        textColor=colors.HexColor('#374151'),
        backColor=colors.HexColor('#f3f4f6'),
        leftIndent=12,
        rightIndent=12,
        topPadding=6,
        bottomPadding=6
    )
    
    info_style = ParagraphStyle(
        'Info',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#6b7280'),
        alignment=TA_CENTER
    )
    
    return {
        'title': title_style,
        'subtitle': subtitle_style,
        'heading': heading_style,
        'body': body_style,
        'code': code_style,
        'info': info_style
    }

def criar_pdf():
    """Gera o PDF completo"""
    
    pdf_path = "EVIDENCIAS_WEBSOCKET.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        topMargin=0.6*inch,
        bottomMargin=0.6*inch,
        leftMargin=0.6*inch,
        rightMargin=0.6*inch
    )
    
    styles = criar_estilos()
    content = []
    
    # ===== PÁGINA 1: CAPA =====
    content.append(Spacer(1, 0.5*inch))
    
    content.append(Paragraph(
        "WebSocket<br/>Mural em Tempo Real",
        styles['title']
    ))
    
    content.append(Paragraph(
        "Adoção de Pets 🐾",
        styles['subtitle']
    ))
    
    content.append(Spacer(1, 0.3*inch))
    
    content.append(Paragraph(
        "<b>PROJETO WEBSOCKET</b>",
        styles['heading']
    ))
    
    content.append(Spacer(1, 0.2*inch))
    
    info_text = """
    <b>Disciplina:</b> Desenvolvimento Web Avançado<br/>
    <b>Tipo:</b> Projeto de Comunicação em Tempo Real<br/>
    <b>Tema:</b> WebSocket vs HTTP/Polling<br/>
    <b>Data:</b> {}<br/>
    <b>Linguagem:</b> Python 3.14 + JavaScript<br/>
    <b>Protocolo:</b> ws://localhost:8000
    """.format(datetime.now().strftime('%d/%m/%Y'))
    
    content.append(Paragraph(info_text, styles['body']))
    
    content.append(PageBreak())
    
    # ===== PÁGINA 2: INSTRUÇÕES DE SCREENSHOTS =====
    content.append(Spacer(1, 0.2*inch))
    
    content.append(Paragraph(
        "EVIDÊNCIAS DE FUNCIONAMENTO",
        styles['heading']
    ))
    
    content.append(Spacer(1, 0.1*inch))
    
    screenshot_guide = """
    <b>Importante:</b> Para complementar este PDF com os screenshots, siga os passos em GUIA_SCREENSHOTS.md<br/>
    <br/>
    <b>Screenshots Necessários:</b><br/>
    1. Servidor WebSocket em execução (ws://localhost:8000)<br/>
    2. Dois clientes conectados simultaneamente<br/>
    3. Mensagem recebida em tempo real (broadcast)<br/>
    4. Logs no servidor mostrando: conexão, mensagem, desconexão<br/>
    """
    
    content.append(Paragraph(screenshot_guide, styles['body']))
    
    content.append(PageBreak())
    
    # ===== PÁGINA 3-4: RESPOSTAS TÉCNICAS =====
    content.append(Spacer(1, 0.2*inch))
    
    content.append(Paragraph(
        "RESPOSTAS ÀS QUESTÕES OBRIGATÓRIAS",
        styles['heading']
    ))
    
    content.append(Spacer(1, 0.15*inch))
    
    # Pergunta A
    content.append(Paragraph(
        "a) Como as conexões dos clientes foram armazenadas?",
        ParagraphStyle('Q', parent=styles['body'], fontSize=11, fontName='Helvetica-Bold', textColor=COR_PRINCIPAL)
    ))
    
    resposta_a = """
    <b>Implementação:</b> Dicionário Python onde a chave é o objeto WebSocket e o valor é um dict com metadados.<br/>
    <br/>
    <u>Código:</u><br/>
    """
    content.append(Paragraph(resposta_a, styles['body']))
    
    code_a = """clients = {}
clients[websocket] = {
    "id": str(uuid.uuid4()),
    "connected_at": datetime.now().isoformat()
}
del clients[websocket]  # ao desconectar"""
    
    content.append(Paragraph(code_a, styles['code']))
    
    resposta_a_final = """
    <br/>
    <b>Detalhes:</b> Cada cliente recebe um UUID único (ex: a1b2c3d4-e5f6-g7h8). O objeto WebSocket é imutável e garante identificação única. Remoção automática ao desconectar (bloco <font face="Courier">finally</font>).
    """
    content.append(Paragraph(resposta_a_final, styles['body']))
    
    content.append(Spacer(1, 0.2*inch))
    
    # Pergunta B
    content.append(Paragraph(
        "b) Como o sistema identifica um cliente conectado?",
        ParagraphStyle('Q', parent=styles['body'], fontSize=11, fontName='Helvetica-Bold', textColor=COR_PRINCIPAL)
    ))
    
    resposta_b = """
    <b>Três métodos:</b><br/>
    • <b>UUID v4:</b> Único por conexão (zero colisões, probabilidade 1 em 5.3×10³⁶)<br/>
    • <b>Objeto WebSocket:</b> Chave do dicionário, garantido único<br/>
    • <b>Visualmente:</b> Ordem de conexão (Cliente 1, Cliente 2, etc)<br/>
    <br/>
    <b>Justificativa:</b> UUIDs garantem identificação segura e única. Simples de implementar sem complexidade desnecessária.
    """
    content.append(Paragraph(resposta_b, styles['body']))
    
    content.append(Spacer(1, 0.2*inch))
    
    # Pergunta C
    content.append(Paragraph(
        "c) O que aconteceria se implementado com polling?",
        ParagraphStyle('Q', parent=styles['body'], fontSize=11, fontName='Helvetica-Bold', textColor=COR_PRINCIPAL)
    ))
    
    resposta_c = """
    <b>Problemas do Polling HTTP:</b><br/>
    ✗ Latência alta (delay até 1000ms)<br/>
    ✗ Requisições vazias (99% sem novidades)<br/>
    ✗ Overhead: protocolo HTTP completo a cada requisição<br/>
    ✗ Bandwidth 50-100x maior que WebSocket<br/>
    ✗ Escalabilidade ruim (100 clientes = 100 req/segundo sempre)<br/>
    <br/>
    <b>WebSocket é MELHOR porque:</b> Mantém conexão aberta. Envio instantâneo. Bidirecional. Eficiente em recursos. Ideal para tempo real.
    """
    content.append(Paragraph(resposta_c, styles['body']))
    
    content.append(PageBreak())
    
    # Pergunta D
    content.append(Spacer(1, 0.2*inch))
    
    content.append(Paragraph(
        "d) Em quais cenários WebSocket é melhor que REST?",
        ParagraphStyle('Q', parent=styles['body'], fontSize=11, fontName='Helvetica-Bold', textColor=COR_PRINCIPAL)
    ))
    
    resposta_d = """
    <b>WebSocket é IDEAL para:</b><br/>
    ✓ Chat em tempo real (este projeto!)<br/>
    ✓ Notificações push instantâneas<br/>
    ✓ Jogos multiplayer<br/>
    ✓ Monitoramento de sistemas com alertas vivos<br/>
    ✓ Dashboards com dados atualizando continuamente<br/>
    ✓ Colaboração simultânea (múltiplos editores)<br/>
    <br/>
    <b>REST é IDEAL para:</b><br/>
    ✓ Dados estáticos (GET /products)<br/>
    ✓ CRUD operações (POST, PUT, DELETE)<br/>
    ✓ Download de arquivos<br/>
    ✓ Cache de dados<br/>
    <br/>
    <b>Este Projeto Demonstra:</b> Mural/Chat em tempo real onde múltiplos clientes recebem atualizações instantaneamente. Algo impossível de forma eficiente com REST/polling.
    """
    content.append(Paragraph(resposta_d, styles['body']))
    
    content.append(Spacer(1, 0.3*inch))
    
    # Resumo técnico
    content.append(Paragraph("RESUMO DAS DECISÕES TÉCNICAS", styles['heading']))
    
    content.append(Spacer(1, 0.1*inch))
    
    # Tabela
    table_data = [
        ['Decisão', 'Escolha', 'Razão'],
        ['Protocolo', 'ws://localhost:8000', 'Obrigatório, tempo real'],
        ['Servidor', 'Python + websockets', 'Simples, ws:// explícito'],
        ['Cliente', 'JavaScript nativo', 'Sem dependências, protocolo visível'],
        ['Armazenamento', 'Dict + UUID', 'Eficiente, único, cleanup automático'],
        ['Formato', 'JSON', 'Estruturado, parseável, padrão web'],
        ['Broadcast', 'Loop sobre clientes', 'Direto, sem intermediários']
    ]
    
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COR_PRINCIPAL),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f9fafb')),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#e5e7eb')),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f3f4f6')])
    ])
    
    table = Table(table_data, colWidths=[1.8*inch, 1.8*inch, 1.8*inch])
    table.setStyle(table_style)
    content.append(table)
    
    content.append(Spacer(1, 0.3*inch))
    
    # Rodapé
    footer_text = f"""
    <b>Projeto WebSocket - Mural em Tempo Real</b><br/>
    Adoção de Pets | {datetime.now().strftime('%d/%m/%Y')}<br/>
    Python 3.14 + websockets | JavaScript + HTML5<br/>
    <font size=8>Protocolo: ws://localhost:8000</font>
    """
    
    content.append(Paragraph(footer_text, styles['info']))
    
    # Gerar PDF
    doc.build(content)
    
    return pdf_path

if __name__ == "__main__":
    print("\n" + "="*70)
    print("GERANDO PDF COM RESPOSTAS TÉCNICAS")
    print("="*70 + "\n")
    
    try:
        pdf_path = criar_pdf()
        
        # Verificar tamanho
        file_size = os.path.getsize(pdf_path)
        
        print(f"[OK] PDF criado com sucesso!")
        print(f"[OK] Arquivo: {pdf_path}")
        print(f"[OK] Tamanho: {file_size:,} bytes")
        print(f"[OK] Localização: {os.path.abspath(pdf_path)}")
        
        print("\n" + "="*70)
        print("PROXIMOS PASSOS:")
        print("="*70)
        print("1. Leia GUIA_SCREENSHOTS.md para capturar os 4 screenshots")
        print("2. Adicione os screenshots ao PDF ou crie um PDF novo com eles")
        print("3. Entregue EVIDENCIAS_WEBSOCKET.pdf + código + README.md")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"[ERRO] Falha ao gerar PDF: {e}")
        import traceback
        traceback.print_exc()
