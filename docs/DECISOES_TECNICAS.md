# 📋 Decisões Técnicas - WebSocket Mural em Tempo Real

Este documento responde as questões obrigatórias do professor sobre as decisões arquiteturais do projeto.

---

## a) Como as conexões dos clientes foram armazenadas?

### Implementação
```python
clients = {}

# Quando cliente conecta:
clients[websocket] = {
    "id": str(uuid.uuid4()),
    "connected_at": datetime.now().isoformat()
}

# Quando cliente desconecta:
del clients[websocket]
```

### Detalhes
- **Estrutura:** Dicionário Python onde a chave é o objeto `websocket` e o valor é um dict com metadados
- **Identificação:** Cada cliente recebe um UUID único (ex: `a1b2c3d4-e5f6-g7h8-i9j0k1l2m3n4`)
- **Timestamp:** Registramos quando o cliente conectou para auditoria
- **Remoção:** Ao desconectar, removemos da lista automaticamente (no bloco `finally`)

### Vantagens
- ✅ Simples e eficiente
- ✅ Identifica clientes de forma única
- ✅ Automático cleanup ao desconectar
- ✅ O objeto `websocket` é imutável, ideal como chave

---

## b) Como o sistema identifica um cliente conectado?

### Identificação Única
Cada cliente recebe um **UUID v4** na conexão:
```python
client_id = str(uuid.uuid4())
# Exemplo: "a1b2c3d4-e5f6-g7h8-i9j0k1l2m3n4"
```

### Métodos de Identificação

| Método | Onde | Como |
|--------|------|------|
| **UUID** | Servidor (Python) | Gerado na conexão, armazenado em `clients[websocket]["id"]` |
| **Objeto WebSocket** | Servidor (Python) | Chave do dicionário `clients` |
| **Ordem de Conexão** | Cliente (HTML/JS) | Visualmente como "Cliente 1", "Cliente 2", etc |

### No Código
```python
# Servidor identifica por UUID
client_id = str(uuid.uuid4())
clients[websocket] = {"id": client_id}

# E também por objeto websocket
for client_ws in clients:  # client_ws é a chave (objeto)
    await client_ws.send(message)
```

### Justificativa
- UUIDs garantem **zero colisões** (probabilidade: 1 em 5.3 × 10³⁶)
- Objeto `websocket` é garantido ser único por conexão
- Simples de implementar, sem complexidade desnecessária

---

## c) O que aconteceria se a mesma funcionalidade fosse implementada usando polling?

### Polling (HTTP Tradicional)

```javascript
// Cliente faz requisições periódicas
setInterval(() => {
    fetch('http://localhost:8000/messages')
        .then(r => r.json())
        .then(data => {
            // Processar mensagens
        });
}, 1000);  // A cada 1 segundo
```

### Problemas do Polling

| Problema | Impacto |
|----------|---------|
| **Latência alta** | Delay de até 1000ms para receber mensagem |
| **Requisições vazias** | 99% das requisições retornam "sem novidades" |
| **Overhead de rede** | Protocolo HTTP completo a cada requisição |
| **Uso de bandwidth** | 50-100x mais dados trafegando |
| **Escalabilidade ruim** | 100 clientes = 100 req/segundo sempre |

### Conclusão: Polling é INEFICIENTE para tempo real ❌

---

## d) Em quais cenários o WebSocket é mais adequado que uma API REST tradicional?

### WebSocket é IDEAL para:

✅ Chat em tempo real (este projeto!)  
✅ Notificações push instantâneas  
✅ Jogos multiplayer  
✅ Monitoramento de sistemas (alertas vivos)  
✅ Dashboards com dados atualizando continuamente  
✅ Colaboração simultânea (múltiplos editores)  

### REST é IDEAL para:

✅ Dados estáticos (GET /products)  
✅ CRUD operações (POST, PUT, DELETE)  
✅ Download de arquivos  
✅ Cache de dados  

### Comparação Rápida

| Cenário | WebSocket | REST |
|---------|-----------|------|
| Chat tempo real | ⭐⭐⭐⭐⭐ | ⭐ |
| Notificações push | ⭐⭐⭐⭐⭐ | ⭐ |
| Fetch dados estáticos | ⭐ | ⭐⭐⭐⭐⭐ |
| CRUD operações | ⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 📊 Resumo das Decisões

| Decisão | Escolha | Razão |
|---------|---------|-------|
| Protocolo | `ws://localhost:8000` | Obrigatório, tempo real |
| Servidor | Python + websockets | Simples, mostra ws:// explícito |
| Cliente | JS nativo | Sem dependências, protocolo visível |
| Armazenamento | Dict + UUID | Eficiente, único, cleanup automático |
| Formato | JSON | Estruturado, parseável |

---

**Projeto:** WebSocket - Mural em Tempo Real 🐾  
**Data:** 15/11/2026
