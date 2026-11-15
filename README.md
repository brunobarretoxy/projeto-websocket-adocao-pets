# 🐾 WebSocket - Mural em Tempo Real (Adoção de Pets)

## 📋 Descrição do Projeto

Uma aplicação de comunicação em tempo real usando **WebSocket** que demonstra avisos instantâneos de adoção de pets. Quando um cliente envia uma mensagem (ex: "Luna foi adotada!"), o servidor retransmite para **todos os clientes conectados simultaneamente**.

O projeto evidencia a **diferença entre HTTP tradicional (requisição-resposta) e WebSocket (comunicação bidirecional contínua)**.

---

## 🎯 Objetivo Educacional

Ao final do projeto, demonstramos:

✅ **Conexão WebSocket:** `ws://localhost:8000` (explícito no código)  
✅ **Envio/Recebimento:** Cliente envia mensagem → Servidor retransmite  
✅ **Broadcast:** Todos os clientes recebem simultaneamente  
✅ **Ciclo de vida:** Abertura → Envio → Recebimento → Encerramento  
✅ **Múltiplos clientes:** Teste em 2+ abas do navegador  
✅ **Registro em console:** Logs de conexão/desconexão/mensagens  

---

## 🚀 Execução Rápida

### 1️⃣ Pré-requisitos
```bash
# Python 3.8+
python --version

# Instalar dependências
pip install websockets
```

### 2️⃣ Iniciar o Servidor
```bash
python server.py
```

**Esperado:**
```
Server started on ws://localhost:8000
Waiting for connections...
```

### 3️⃣ Abrir a Interface
```
Abra 2 abas do navegador:
http://localhost:8000
http://localhost:8000
```

### 4️⃣ Testar
- Na **aba 1**: Digite "Luna foi adotada!" no input
- Clique "Enviar"
- **Ambas as abas** mostram a mensagem em tempo real ✨

---

## 📂 Estrutura do Projeto

```
projeto-websocket-adocao-pets/
├── README.md                    # Este arquivo
├── server.py                    # Servidor WebSocket (Python)
├── index.html                   # Interface web
├── style.css                    # Estilos CSS
├── client.js                    # Cliente JavaScript (nativo)
└── docs/
    ├── DECISOES_TECNICAS.md     # Respostas técnicas para o professor
    └── ARQUITETURA.md           # Detalhes de implementação
```

---

## 🔌 Arquitetura

### Fluxo de Comunicação

```
┌─────────────────────────────────────────────────────────┐
│ CLIENTE 1 (Aba 1)                                       │
│ const ws = new WebSocket("ws://localhost:8000")        │
└─────────────────────────────────────────────────────────┘
                          │
                          │ 1. Envia mensagem
                          │    ws.send(JSON.stringify({...}))
                          ▼
┌─────────────────────────────────────────────────────────┐
│ SERVIDOR (Python)                                       │
│ async def handle_client(websocket, path):              │
│   - Registra cliente                                   │
│   - Recebe mensagem                                    │
│   - Retransmite para TODOS                             │
└─────────────────────────────────────────────────────────┘
                          │
          ┌───────────────┴────────────────┐
          │                                │ 2. Broadcast
          ▼                                ▼
    ┌─────────────┐              ┌─────────────┐
    │ CLIENTE 1   │              │ CLIENTE 2   │
    │ (recebe)    │              │ (recebe)    │
    └─────────────┘              └─────────────┘
```

### Identificação de Clientes

Cada cliente recebe um **ID único** gerado pelo servidor:
```python
client_id = str(uuid.uuid4())  # Ex: "a1b2c3d4-e5f6-g7h8..."
clients[websocket] = {
    "id": client_id,
    "connected_at": datetime.now()
}
```

### Armazenamento de Conexões

```python
# Dicionário de clientes conectados
clients = {
    websocket_object: {
        "id": "uuid-123",
        "connected_at": "2026-11-15 17:40:00"
    },
    websocket_object_2: {
        "id": "uuid-456",
        "connected_at": "2026-11-15 17:41:00"
    }
}
```

---

## 📝 Formato de Mensagem (JSON)

```json
{
  "type": "message",
  "client_id": "a1b2c3d4-e5f6-g7h8",
  "content": "Luna foi adotada!",
  "timestamp": "2026-11-15T17:40:30Z"
}
```

---

## 🖥️ Tecnologias Utilizadas

| Camada | Tecnologia | Por quê |
|--------|-----------|---------|
| **Servidor** | Python + `websockets` | Simples, assíncrona, mostra `ws://` explícito |
| **Cliente** | JavaScript nativo + WebSocket API | Sem dependências, protocolo `ws://` visível |
| **Interface** | HTML5 + CSS3 | Minimalista, foco no WebSocket |
| **Protocolo** | WebSocket (`ws://`) | Requisito obrigatório, bidirecional, em tempo real |

---

## ⚙️ Como Funciona o Código

### Servidor (Python)

```python
# 1. Define conexões ativas
clients = {}

# 2. Quando cliente conecta
async def handle_client(websocket, path):
    client_id = str(uuid.uuid4())
    clients[websocket] = {"id": client_id}
    print(f"Client {client_id} connected")  # Log obrigatório
    
    # 3. Fica escutando mensagens
    try:
        async for message in websocket:
            print(f"Message from {client_id}: {message}")  # Log
            
            # 4. Retransmite para todos
            for client_ws in clients:
                await client_ws.send(message)
    
    # 5. Quando desconecta
    finally:
        del clients[websocket]
        print(f"Client {client_id} disconnected")  # Log

# 6. Inicia servidor em ws://localhost:8000
start_server = websockets.serve(handle_client, "localhost", 8000)
```

### Cliente (JavaScript)

```javascript
// 1. Conecta ao servidor (ws:// EXPLÍCITO!)
const ws = new WebSocket("ws://localhost:8000");

// 2. Quando conecta
ws.onopen = () => {
    console.log("Connected to WebSocket server");
};

// 3. Quando recebe mensagem
ws.onmessage = (event) => {
    const msg = JSON.parse(event.data);
    exibir_mensagem(msg.content);  // Mostra na interface
};

// 4. Quando envia (botão "Enviar")
function enviar_mensagem() {
    const texto = input.value;
    const msg = JSON.stringify({
        type: "message",
        content: texto,
        timestamp: new Date().toISOString()
    });
    ws.send(msg);  // Envia ao servidor
}

// 5. Quando desconecta
ws.onclose = () => {
    console.log("Disconnected from server");
};
```

---

## 🧪 Testes Esperados

### Teste 1: Conexão Inicial
- Abrir navegador em `http://localhost:8000`
- **Esperado:** Console mostra "Client [ID] connected"

### Teste 2: Dois Clientes Simultâneos
- Abrir 2 abas do navegador
- Ambas devem conectar
- **Esperado:** Console mostra 2 logs de conexão

### Teste 3: Envio de Mensagem
- Aba 1: Digitar "Luna foi adotada!"
- Aba 1: Clicar "Enviar"
- **Esperado:** Mensagem aparece em Aba 1 E Aba 2 instantaneamente

### Teste 4: Desconexão
- Fechar uma aba
- **Esperado:** Console mostra "Client [ID] disconnected"

---

## ❓ Respostas Técnicas para Apresentação

### a) Como as conexões dos clientes foram armazenadas?

Dicionário Python com websocket como chave:
```python
clients = {
    websocket_obj: {"id": "uuid-123", "connected_at": datetime}
}
```
Cada cliente recebe ID único (UUID). Ao desconectar, removemos do dicionário.

### b) Como o sistema identifica um cliente conectado?

Cada cliente gera um **UUID único** na conexão e envia em cada mensagem. O servidor usa o objeto `websocket` como chave para armazenar. No frontend, o cliente é identificado pela ordem de conexão (Cliente 1, Cliente 2...).

### c) O que aconteceria com polling?

Com polling (requisições HTTP periódicas):
- Cliente faria GET a cada 1-2 segundos: "Tem mensagem nova?"
- Servidor processaria centenas de requisições vazias
- Latência: múltiplos ms por requisição
- Muito ineficiente para tempo real

**WebSocket evita isso:** conexão contínua, mensagem dispara instantaneamente.

### d) Em quais cenários WebSocket é melhor que REST?

1. **Chat em tempo real** (este projeto)
2. **Notificações instantâneas** (novo pedido, novo aluno conectado)
3. **Colaboração em tempo real** (compartilhamento de documento)
4. **Monitoramento de sistemas** (alertas, status vivo)
5. **Jogos multiplayer** (movimento instantâneo)

REST é melhor para: dados estáticos, CRUD simples, cache.

---

## 📊 Demonstração ao Professor

### Passo a Passo

1. **Abra terminal:** Execute `python server.py`
2. **Abra navegador (Aba 1):** `http://localhost:8000`
3. **Abra navegador (Aba 2):** `http://localhost:8000` (mesma URL)
4. **Terminal mostra:**
   ```
   Client a1b2c3d4-... connected
   Client e5f6g7h8-... connected
   ```
5. **Aba 1:** Digite "Luna foi adotada!" → Clique Enviar
6. **Ambas abas mostram:** "Luna foi adotada!" em tempo real
7. **Terminal mostra:**
   ```
   Message from a1b2c3d4-...: {"type": "message", "content": "Luna foi adotada!", ...}
   ```
8. **Feche Aba 2** → Terminal mostra:
   ```
   Client e5f6g7h8-... disconnected
   ```

---

## 📦 Dependências

```txt
websockets>=10.0
```

Instalar:
```bash
pip install websockets
```

---

## 🎓 Conceitos Demonstrados

✅ **Protocolo WebSocket:** Comunicação bidirecional em tempo real  
✅ **Cliente-Servidor:** Arquitetura cliente-servidor  
✅ **Broadcast:** Retransmissão para múltiplos clientes  
✅ **Identificação:** Clientes com UUID  
✅ **Ciclo de vida:** Conexão → Mensagens → Desconexão  
✅ **JSON:** Formato de mensagem estruturado  
✅ **Assincronismo:** Python asyncio no servidor  

---

## 🚨 Requisitos Atendidos

| Requisito | Status | Local |
|-----------|--------|-------|
| Servidor WebSocket | ✅ | `server.py` |
| Interface web (HTML + JS) | ✅ | `index.html` + `client.js` |
| 2+ clientes simultâneos | ✅ | 2 abas do navegador |
| Envio cliente → servidor | ✅ | Campo input + botão |
| Broadcast servidor → clientes | ✅ | `for client_ws in clients: await client_ws.send()` |
| Exibição visual | ✅ | Lista de mensagens em HTML |
| Logs em console | ✅ | `print()` no servidor |
| Protocolo `ws://` explícito | ✅ | `new WebSocket("ws://localhost:8000")` |
| Decisões técnicas documentadas | ✅ | `docs/DECISOES_TECNICAS.md` |

---

## 📌 Autor

**Bruno** - Desenvolvedor do projeto WebSocket  
Tema: Adoção de Pets  
Data: 15/11/2026

---

**Projeto concluído e pronto para apresentação! 🎉**
