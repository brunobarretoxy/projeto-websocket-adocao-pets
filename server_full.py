#!/usr/bin/env python3
"""
Servidor WebSocket + HTTP para servir a interface

Este servidor combina:
1. Servidor WebSocket (ws://localhost:8000) - comunicação em tempo real
2. Servidor HTTP básico - serve index.html e assets
"""

import asyncio
import websockets
import json
import uuid
import mimetypes
from datetime import datetime
from pathlib import Path

# Dicionário de clientes WebSocket
clients = {}

# Diretório do projeto
PROJECT_DIR = Path(__file__).parent


async def handle_http(path, request_headers):
    """Trata requisições HTTP simples (serve arquivos estáticos)."""
    
    if path == "/" or path == "/index.html":
        file_path = PROJECT_DIR / "index.html"
    elif path == "/style.css":
        file_path = PROJECT_DIR / "style.css"
    elif path == "/client.js":
        file_path = PROJECT_DIR / "client.js"
    else:
        return [("404", [])], b"Not Found"
    
    if file_path.exists():
        with open(file_path, "rb") as f:
            content = f.read()
        mime_type, _ = mimetypes.guess_type(str(file_path))
        headers = [("Content-Type", mime_type or "text/plain")]
        return [("200", headers)], content
    else:
        return [("404", [])], b"Not Found"


async def handle_websocket(websocket, path):
    """Gerencia conexões WebSocket."""
    
    # Gerar ID único para este cliente
    client_id = str(uuid.uuid4())
    
    # Armazenar cliente
    clients[websocket] = {
        "id": client_id,
        "connected_at": datetime.now().isoformat()
    }
    
    # ========== LOG DE CONEXÃO ==========
    print(f"\n✅ [CONEXÃO] Cliente {client_id} conectado")
    print(f"   Total de clientes: {len(clients)}")
    
    try:
        # Fica escutando mensagens do cliente
        async for message in websocket:
            # ========== LOG DE RECEBIMENTO ==========
            print(f"\n📨 [MENSAGEM] Do cliente {client_id}:")
            print(f"   Conteúdo: {message}")
            
            # Fazer broadcast: enviar para TODOS os clientes
            print(f"   Retransmitindo para {len(clients)} cliente(s)...")
            
            # Iterar sobre todos os clientes conectados
            for client_ws in clients:
                try:
                    await client_ws.send(message)
                except Exception as e:
                    print(f"   ⚠️  Erro ao enviar para cliente: {e}")
            
            print(f"   ✓ Broadcast concluído")
    
    except websockets.exceptions.ConnectionClosed:
        pass
    
    finally:
        # ========== LOG DE DESCONEXÃO ==========
        if websocket in clients:
            del clients[websocket]
        
        print(f"\n❌ [DESCONEXÃO] Cliente {client_id} desconectado")
        print(f"   Total de clientes: {len(clients)}")


async def main():
    """Inicia o servidor combinado WebSocket + HTTP."""
    
    print("\n" + "="*60)
    print("🚀 SERVIDOR WEBSOCKET + HTTP - MURAL EM TEMPO REAL")
    print("="*60)
    print(f"\n⏳ Iniciando servidor...")
    
    # Criar servidor WebSocket com suporte a HTTP upgrade
    async with websockets.serve(
        handle_websocket,
        "localhost",
        8000,
        process_request=handle_http  # Trata requisições HTTP
    ):
        print(f"✅ Servidor iniciado em: ws://localhost:8000")
        print(f"✅ Acesse em: http://localhost:8000")
        print(f"\n📝 Logs de Eventos:")
        print("-"*60)
        
        # Manter o servidor rodando
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n⛔ Servidor encerrado pelo usuário")
