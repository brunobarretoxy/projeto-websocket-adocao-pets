# ✅ Checklist de Apresentação para o Professor

Use este checklist para garantir que tudo está pronto para apresentar o projeto ao professor.

---

## 📋 PRÉ-APRESENTAÇÃO (Verificar Tudo)

### Requisitos Técnicos

- [ ] Python 3.8+ instalado
  ```bash
  python --version
  ```

- [ ] websockets instalado
  ```bash
  pip install websockets
  ```

- [ ] Arquivo `server.py` pronto
  
- [ ] Arquivo `index.html` pronto
  
- [ ] Arquivo `client.js` pronto
  
- [ ] Arquivo `style.css` pronto

### Documentação

- [ ] `README.md` completo
  
- [ ] `docs/DECISOES_TECNICAS.md` completo (respostas do professor)
  
- [ ] `docs/ARQUITETURA.md` completo (diagrama e fluxo)
  
- [ ] `requirements.txt` com dependências

### Código Obrigatório

- [ ] ✅ `ws://localhost:8000` **EXPLÍCITO** em `client.js`
  ```javascript
  const ws = new WebSocket("ws://localhost:8000");
  ```

- [ ] ✅ Servidor WebSocket em `server.py`

- [ ] ✅ Logs de conexão no console do servidor

- [ ] ✅ Interface HTML com input e lista de mensagens

---

## 🎯 DURANTE A APRESENTAÇÃO

### Passo 1: Iniciar o Servidor (Terminal 1)

```bash
cd projeto-websocket-adocao-pets
python server.py
```

**Verificar:**
- [ ] Servidor respondeu com: `✅ Servidor iniciado em: ws://localhost:8000`
- [ ] Aguardando conexões

### Passo 2: Iniciar Servidor HTTP (Terminal 2)

```bash
cd projeto-websocket-adocao-pets
python -m http.server 8001
```

**Verificar:**
- [ ] Servidor HTTP respondeu
- [ ] Porta 8001 disponível

### Passo 3: Abrir 2 Abas do Navegador

- [ ] Aba 1: `http://localhost:8001`
- [ ] Aba 2: `http://localhost:8001`

**Verificar:**
- [ ] Ambas carregaram com sucesso
- [ ] Status mostra "🟢 Conectado"
- [ ] Podem digitar no input

### Passo 4: Observar Logs do Servidor

No Terminal 1, você deve ver:

```
✅ [CONEXÃO] Cliente a1b2c3d4-... conectado
   Total de clientes: 1
✅ [CONEXÃO] Cliente e5f6g7h8-... conectado
   Total de clientes: 2
```

**Verificar:**
- [ ] 2 clientes conectados foram registrados
- [ ] IDs únicos (UUID) aparecem para cada cliente

### Passo 5: Enviar Mensagem (Aba 1)

- [ ] Digitar: "Luna foi adotada! 🎉"
- [ ] Clicar em "📤 Enviar"

**Verificar nos Logs do Terminal 1:**
```
📨 [MENSAGEM] Do cliente a1b2c3d4-...:
   Conteúdo: {"type":"message","content":"Luna foi adotada!..."}
   Retransmitindo para 2 cliente(s)...
   ✓ Broadcast concluído
```

- [ ] Mensagem foi recebida
- [ ] Broadcast aconteceu para 2 clientes

### Passo 6: Verificar Recebimento Simultâneo

- [ ] **Aba 1:** Mensagem apareceu na lista
- [ ] **Aba 2:** Mensagem apareceu INSTANTANEAMENTE (sem refresh!)

**Este é o ponto crítico da demonstração!**

- [ ] Reforçar: "Veja, não fiz refresh. Comunicação em tempo real!"

### Passo 7: Testar Novamente

- [ ] Enviar outra mensagem da Aba 2
- [ ] Verificar que aparece em Aba 1 também
- [ ] Confirmar que a comunicação é bidirecional

### Passo 8: Demonstrar Logs

- [ ] Fechar uma aba
- [ ] Terminal mostra:
  ```
  ❌ [DESCONEXÃO] Cliente e5f6g7h8-... desconectado
     Total de clientes: 1
  ```
- [ ] [ ] Explicar que o servidor rastreia ciclo de vida completo

---

## 💬 FALA SUGERIDA PARA O PROFESSOR

> "Projeto WebSocket - Mural em Tempo Real.
> 
> Nós implementamos um servidor em Python com protocolo **WebSocket explícito em `ws://localhost:8000`**, 
> e uma interface web em HTML + JavaScript usando a **WebSocket API nativa do navegador**.
> 
> Quando alguém envia uma mensagem, como 'Luna foi adotada!', o servidor retransmite 
> **instantaneamente para todos os clientes conectados**, que recebem e atualizam a interface 
> **sem fazer refresh da página**.
> 
> Vejam aqui: tenho 2 abas abertas (Cliente 1 e Cliente 2). Vou enviar na Aba 1...
> 
> Pronto! Apareceu na Aba 2 também, em tempo real! E aqui no terminal do servidor 
> (aponte para os logs), vocês veem que ele registra **quando clientes conectam, quando 
> mensagens chegam, e quando desconectam**. 
> 
> Isso é **WebSocket** - uma conexão bidirecional contínua, muito mais eficiente que 
> fazer polling com requisições HTTP periódicas para perguntar 'tem mensagem nova?'"

---

## 🎓 QUESTÕES QUE O PROFESSOR PODE FAZER

### P: "Por que WebSocket e não REST?"

✅ **Resposta:**
- REST exigiria polling (requisições periódicas)
- Cada requisição HTTP tem overhead de headers
- WebSocket é conexão contínua, mais eficiente
- Latência muito menor (<100ms vs 1000ms+)

### P: "Como identifica os clientes?"

✅ **Resposta:**
- Cada cliente recebe um UUID único na conexão
- Armazenamos em dicionário Python
- Quando desconecta, removemos automaticamente

### P: "E se houvesse 1000 clientes?"

✅ **Resposta:**
- WebSocket: cada conexão ativa usa pouca memória
- Broadcast: ~1MB por cliente
- Com polling: seria insustentável (1000 requisições/segundo vazias)

### P: "Cadê o `ws://` no código?"

✅ **Resposta:**
- (Abrir client.js em editor)
- Mostrar: `const ws = new WebSocket("ws://localhost:8000");`
- Explicar: não usamos Socket.IO ou lib que abstrai, é WebSocket puro

### P: "E se perder a conexão?"

✅ **Resposta:**
- client.js detecta `onclose`
- Tenta reconectar a cada 3 segundos automaticamente
- Servidor remove cliente se desconectar

---

## 📸 EVIDÊNCIAS PARA DOCUMENTO PDF

Prepare prints para entregar:

- [ ] **Print 1:** Terminal mostrando servidor rodando em `ws://localhost:8000`
- [ ] **Print 2:** 2 abas do navegador abertas (ambas conectadas)
- [ ] **Print 3:** Mensagem enviada em Aba 1, recebida em Aba 2
- [ ] **Print 4:** Terminal mostrando logs (conexão, mensagem, broadcast)
- [ ] **Print 5:** client.js aberto, mostrando `ws://localhost:8000` explícito

---

## ⚡ TROUBLESHOOTING RÁPIDO

Se algo der errado:

### "Erro: WebSocket não conecta"
- [ ] Servidor Python rodando? (`python server.py`)
- [ ] Porta 8000 está livre? (`netstat -ano | findstr :8000`)
- [ ] Firewall bloqueando?

### "Mensagem não aparece na outra aba"
- [ ] Ambas abas conectadas? (Verificar status verde)
- [ ] Console do navegador mostra erro? (F12)
- [ ] Servidor recebeu a mensagem? (Ver terminal)

### "Não consegue acessar http://localhost:8001"
- [ ] HTTP server rodando? (`python -m http.server 8001`)
- [ ] Porta 8001 está livre?
- [ ] Browser carregando? (Verificar reload)

---

## 🏁 CHECKLIST FINAL

Antes de apresentar, confirme:

- [ ] Arquivos do projeto incluídos
- [ ] `ws://localhost:8000` EXPLÍCITO em `client.js`
- [ ] Servidor Python testado e rodando
- [ ] 2 abas do navegador conectadas
- [ ] Broadcast funcionando
- [ ] Logs aparecem no terminal
- [ ] Documentação completa (`README.md`, `DECISOES_TECNICAS.md`)
- [ ] Respostas do professor preparadas
- [ ] Fala ensaiada (30-60 segundos)
- [ ] Prints coletados para PDF

---

## 📁 ARQUIVOS PARA ENVIAR

Ao professor, entregar:

1. **Link do repositório Git** (GitHub) OU
2. **Arquivo `.zip`** contendo:
   ```
   projeto-websocket-adocao-pets/
   ├── server.py
   ├── client.js
   ├── index.html
   ├── style.css
   ├── README.md
   ├── requirements.txt
   ├── .gitignore
   └── docs/
       ├── DECISOES_TECNICAS.md
       ├── ARQUITETURA.md
       ├── EXECUCAO_RAPIDA.md
       ├── GUIA_SCREENSHOTS.md
       └── CHECKLIST_APRESENTACAO.md
   ```

3. **PDF com evidências:**
   - 5 prints (servidor, 2 clientes, mensagem, logs)
   - Respostas (a, b, c, d) - máximo 5 linhas cada

---

**Projeto:** WebSocket - Mural em Tempo Real 🐾  
**Data:** 15/11/2026  
**Desenvolvedor:** Bruno  
**Status:** ✅ PRONTO PARA APRESENTAÇÃO
