# 📸 Guia de Captura de Screenshots para o PDF

Siga este guia passo a passo para capturar os 4 screenshots obrigatórios.

---

## ✅ PRÉ-REQUISITOS

Certifique-se de que:
- ✅ Terminal 1: `python server.py` rodando
- ✅ Terminal 2: `python -m http.server 8001` rodando
- ✅ Navegador: 2 abas abertas em `http://localhost:8001`
- ✅ Ambas as abas mostram "Conectado" (verde)

---

## 📸 SCREENSHOT 1: SERVIDOR WEBSOCKET EM EXECUÇÃO

**O que capturar:**
- Terminal onde o servidor Python está rodando
- Mostrar as linhas:
  ```
  ============================================================
  [*] SERVIDOR WEBSOCKET - MURAL EM TEMPO REAL
  ============================================================
  [*] Iniciando servidor...
  [OK] Servidor iniciado em: ws://localhost:8000
  ```

**Passo a passo:**
1. Clique no terminal do servidor
2. Pressione `Print Screen` (ou `Alt + Print Screen` para apenas a janela)
3. Cole em um editor de imagens (Paint, Word, etc)
4. Corte para mostrar apenas o servidor
5. Salve como `01-servidor.png`

---

## 📸 SCREENSHOT 2: DOIS CLIENTES CONECTADOS

**O que capturar:**
- 2 abas do navegador lado a lado
- Ambas em `http://localhost:8001`
- Status verde "Conectado" visível
- Campo de input visível
- Isso prova que temos 2 clientes conectados simultaneamente

**Passo a passo:**
1. Redimensione o navegador para caber 2 abas na tela (ou use `Win + Seta Esquerda` + `Win + Seta Direita`)
2. Abra a Aba 1 em http://localhost:8001
3. Abra a Aba 2 em http://localhost:8001 (em outra janela ou lado a lado)
4. Verifique que ambas mostram "Conectado" em verde
5. Pressione `Print Screen`
6. Cole e corte para mostrar as 2 abas
7. Salve como `02-dois-clientes.png`

---

## 📸 SCREENSHOT 3: MENSAGEM ENVIADA E RECEBIDA (BROADCAST)

**O que capturar:**
- Aba 1 com a mensagem que você digitou e enviou
- Aba 2 com a mesma mensagem recebida
- Ambas devem mostrar a mesma mensagem
- Sem refresh! Apareceu instantaneamente.

**Passo a passo:**
1. Na **Aba 1**, no campo de input (onde diz "Digite uma mensagem..."), escreva:
   ```
   Luna foi adotada!
   ```

2. Pressione `Enter` ou clique no botão "Enviar"

3. **Imediatamente**, observe a **Aba 2** - a mensagem deve aparecer lá também!

4. Pronto! Isso é a prova de broadcast. Agora capture:
   - Aba 1: mostrando a mensagem na lista
   - Aba 2: mostrando a MESMA mensagem na lista
   - Sem refresh necessário

5. Pressione `Print Screen`

6. Cole e corte para mostrar as 2 abas com a mensagem

7. Salve como `03-broadcast.png`

---

## 📸 SCREENSHOT 4: LOGS DO SERVIDOR

**O que capturar:**
- Terminal do servidor
- Mostrar as linhas de log que comprovam:
  - Conexão dos clientes
  - Recebimento da mensagem
  - Broadcast concluído

**Passo a passo:**
1. Clique no terminal do servidor (aquele que está rodando `python server.py`)

2. Você deve ver algo como:
   ```
   [CONEXAO] Cliente a1b2c3d4... conectado
      Total de clientes: 1

   [CONEXAO] Cliente e5f6g7h8... conectado
      Total de clientes: 2

   [MENSAGEM] Do cliente a1b2c3d4...:
      Conteudo: Luna foi adotada!
      Retransmitindo para 2 cliente(s)...
      [OK] Broadcast concluido
   ```

3. Pressione `Print Screen` ou `Alt + Print Screen`

4. Cole e corte para mostrar apenas os logs relevantes

5. Salve como `04-logs.png`

---

## 📋 CHECKLIST FINAL

Você deve ter 4 imagens:
- ✅ `01-servidor.png` - Servidor rodando
- ✅ `02-dois-clientes.png` - 2 abas conectadas
- ✅ `03-broadcast.png` - Mensagem recebida em ambas as abas
- ✅ `04-logs.png` - Logs no servidor mostrando conexão, mensagem, broadcast

---

## 🎓 O QUE VOCÊ ESTÁ PROVANDO

Com esses 4 screenshots, você prova para o professor:

| Screenshot | Prova |
|------------|-------|
| 1 | ✅ Servidor WebSocket está rodando em `ws://localhost:8000` |
| 2 | ✅ 2+ clientes conectados SIMULTANEAMENTE |
| 3 | ✅ Broadcast funcionando (mensagem enviada e recebida por outro cliente) |
| 4 | ✅ Logs obrigatórios: conexão, mensagem, desconexão |

---

## 💡 DICAS

- **Emojis no terminal:** Se não aparecerem emojis, tudo bem! Os logs mostram `[CONEXAO]`, `[MENSAGEM]`, `[DESCONEXAO]` que é tudo que o professor precisa.

- **Redimensionar navegador:** Use `F12` para abrir devtools, depois clique na aba e vá pra tela cheia. Ou abra 2 navegadores lado a lado.

- **Screenshot de qualidade:** Prefira capturar a janela inteira. Não recorte demais - deixe margens para ficar claro.

- **Timestamp:** As mensagens mostram timestamp automático. Isso é bom! Prova que está funcionando em tempo real.

---

## 🎬 DEPOIS DOS SCREENSHOTS

1. Crie um PDF combinando as imagens com as respostas técnicas.
2. Limite as respostas a cinco linhas por questão e a uma página no total.
3. Entregue o PDF junto com o código.

---

**Pronto! Você está pronto para demonstrar ao professor! 🚀**
