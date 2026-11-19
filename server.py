#!/usr/bin/env python3
"""
Servidor WebSocket - Mural em Tempo Real (Adoção de Pets)

Este servidor:
1. Aceita conexões WebSocket em ws://localhost:8000
2. Mantém registro de clientes conectados
3. Recebe mensagens de clientes
4. Retransmite mensagens para todos os clientes (broadcast)
5. Registra em console: conexão, mensagem, desconexão
"""

import asyncio
import websockets
import json
import uuid
from datetime import datetime

# Dicionário de clientes conectados
# Chave: objeto websocket
# Valor: dict com id, timestamp de conexão
clients = {}


async def handle_client(websocket):
    """
    Gerencia a conexão de um cliente WebSocket.
    
    Responsabilidades:
    - Registrar cliente ao conectar
    - Receber mensagens
    - Fazer broadcast para todos
    - Remover cliente ao desconectar
    """
    
    # Gerar ID único para este cliente
    client_id = str(uuid.uuid4())
    
    # Armazenar cliente
    clients[websocket] = {
        "id": client_id,
        "connected_at": datetime.now().isoformat()
    }
    
    # ========== OBRIGATÓRIO: LOG DE CONEXÃO ==========
    print(f"\n[CONEXAO] Cliente {client_id} conectado")
    print(f"   Total de clientes: {len(clients)}")
    
    # Enviar contagem de clientes para todos
    await notificar_contagem_clientes()
    
    try:
        # Fica escutando mensagens do cliente
        async for message in websocket:
            # ========== OBRIGATÓRIO: LOG DE RECEBIMENTO ==========
            print(f"\n[MENSAGEM] Do cliente {client_id}:")
            print(f"   Conteudo: {message}")
            
            # Fazer broadcast: enviar para TODOS os clientes
            print(f"   Retransmitindo para {len(clients)} cliente(s)...")
            
            # Iterar sobre todos os clientes conectados
            for client_ws in clients:
                try:
                    await client_ws.send(message)
                except Exception as e:
                    print(f"   [ERRO] Falha ao enviar para cliente: {e}")
            
            print(f"   [OK] Broadcast concluido")
    
    except websockets.exceptions.ConnectionClosed:
        pass
    
    finally:
        # ========== OBRIGATÓRIO: LOG DE DESCONEXÃO ==========
        if websocket in clients:
            del clients[websocket]
        
        print(f"\n[DESCONEXAO] Cliente {client_id} desconectado")
        print(f"   Total de clientes: {len(clients)}")
        
        # Atualizar contagem para clientes restantes
        await notificar_contagem_clientes()


async def notificar_contagem_clientes():
    """Envia a contagem de clientes conectados para todos."""
    contagem = {
        "type": "connection_count",
        "count": len(clients)
    }
    
    for client_ws in clients:
        try:
            await client_ws.send(json.dumps(contagem))
        except Exception as e:
            print(f"[ERRO] Falha ao enviar contagem: {e}")


async def main():
    """Inicia o servidor WebSocket."""
    
    print("\n" + "="*60)
    print("[*] SERVIDOR WEBSOCKET - MURAL EM TEMPO REAL")
    print("="*60)
    print(f"\n[*] Iniciando servidor...")
    
    # Criar servidor WebSocket
    # IMPORTANTE: ws://localhost:8000 é EXPLÍCITO no código
    async with websockets.serve(handle_client, "localhost", 8000):
        print(f"[OK] Servidor iniciado em: ws://localhost:8000")
        print(f"\n[*] Logs de Eventos:")
        print("-"*60)
        
        # Manter o servidor rodando
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    # Executar servidor
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n[!] Servidor encerrado pelo usuário")
