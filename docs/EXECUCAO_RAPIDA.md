# 🚀 GUIA RÁPIDO DE EXECUÇÃO

Execute os comandos abaixo na pasta raiz do projeto.

## Servidor WebSocket e interface

### Terminal 1 - Inicia o Servidor WebSocket

```bash
python server.py
```

**Esperado:**
```
════════════════════════════════════════════════════
🚀 SERVIDOR WEBSOCKET - MURAL EM TEMPO REAL
════════════════════════════════════════════════════

⏳ Iniciando servidor...
✅ Servidor iniciado em: ws://localhost:8000

📝 Logs de Eventos:
────────────────────────────────────────────────────
```

### Terminal 2 - Inicia um Servidor HTTP (para servir HTML)

```bash
python -m http.server 8001
```

**Esperado:**
```
Serving HTTP on 0.0.0.0 port 8001 (http://0.0.0.0:8001/)
```

### Browser

Abra em 2 abas:
```
http://localhost:8001
http://localhost:8001
```

---

## ✅ Teste Completo

1. **Terminal:** `python server.py`
2. **Outro Terminal:** `python -m http.server 8001`
3. **Browser - Aba 1:** http://localhost:8001
4. **Browser - Aba 2:** http://localhost:8001
5. **Aba 1:** Digitar "Luna foi adotada!" → Clicar Enviar
6. **Aba 2:** Mensagem aparece automaticamente! ✨
7. **Terminal 1:** Ver logs de conexão e broadcast

---

## 📊 O Que Você Vai Ver

### No Terminal (Logs do Servidor)

```
✅ [CONEXÃO] Cliente a1b2c3d4-... conectado
   Total de clientes: 1
✅ [CONEXÃO] Cliente e5f6g7h8-... conectado
   Total de clientes: 2
📨 [MENSAGEM] Do cliente a1b2c3d4-...:
   Conteúdo: {"type":"message","content":"Luna foi adotada!","timestamp":"2026-11-15T17:40:45Z"}
   Retransmitindo para 2 cliente(s)...
   ✓ Broadcast concluído
❌ [DESCONEXÃO] Cliente e5f6g7h8-... desconectado
   Total de clientes: 1
```

### No Browser (Aba 1 e Aba 2)

```
🐾 Mural em Tempo Real

Status: 🟢 Conectado
ID: a1b2c3d4-e5f6-g7h8-i9j0k1l2m3n4

💬 Mensagens em Tempo Real
- Luna foi adotada! 🎉
  17:40:45

🔌 Protocolo: ws://localhost:8000
```

### No Console do Navegador (F12)

```
🐾 MURAL EM TEMPO REAL - WebSocket
Projeto de Adoção de Pets
Console aberto - Você verá todos os eventos aqui!
📡 Tentando conectar a ws://localhost:8000...
✅ Conectado ao servidor WebSocket!
   Protocolo: WebSocket (ws://)
   Servidor: localhost:8000
📤 Enviando mensagem: {type: "message", content: "Luna foi adotada!", timestamp: "..."}
✅ Mensagem enviada com sucesso
📨 Mensagem recebida do servidor: {"type":"message",...}
📝 Mensagem adicionada à interface
```

---

## 🔧 Troubleshooting

### "Erro: Módulo websockets não encontrado"

```bash
pip install websockets
```

### "Porta 8000 já em uso"

```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux
lsof -i :8000
kill -9 <PID>
```

### "Não consegue conectar ao servidor"

Verificar:
1. ✅ `python server.py` está rodando?
2. ✅ `python -m http.server 8001` está rodando?
3. ✅ Navegador aberto em `http://localhost:8001`?
4. ✅ Firewall permite porta 8000?

---

## 🎯 Para a Apresentação ao Professor

1. Abra **2 terminais**
2. Terminal 1: `python server.py`
3. Terminal 2: `python -m http.server 8001`
4. Abra navegador em **2 abas**: `http://localhost:8001`
5. Na Aba 1, envie: "Luna foi adotada!"
6. Mostre que aparece instantaneamente em **Aba 1 E Aba 2**
7. Mostre os **logs no terminal** (conexão, mensagem, desconexão)
8. Mencione que usa **`ws://localhost:8000`** explícito no código

---

**Projeto:** WebSocket - Mural em Tempo Real 🐾  
**Data:** 15/11/2026
