# ✅ CHECKLIST DE ENTREGA - WebSocket Projeto

Use este checklist para garantir que você entrega tudo que o professor pediu.

---

## 📋 ARQUIVOS DE CÓDIGO

- [ ] **server.py** - Servidor WebSocket com protocolo `ws://localhost:8000` explícito
- [ ] **client.js** - Cliente JavaScript com `new WebSocket("ws://localhost:8000")`
- [ ] **index.html** - Interface web com campo de input e lista de mensagens
- [ ] **style.css** - Estilos da interface
- [ ] **requirements.txt** - Dependências (websockets>=10.0)
- [ ] **.gitignore** - Configuração Git

**Validação:** Todos 6 arquivos estão presentes? ☐

---

## 📚 DOCUMENTAÇÃO OBRIGATÓRIA

- [ ] **README.md** - Documentação do projeto
- [ ] **DECISOES_TECNICAS.md** - Respostas às 4 questões do professor (a/b/c/d)

**Validação:** Ambos os arquivos contêm respostas claras e concisas? ☐

---

## 📸 EVIDÊNCIAS - PDF

- [ ] **EVIDENCIAS_WEBSOCKET.pdf** com:
  - [ ] Capa com informações do projeto
  - [ ] Resposta à pergunta A (Como armazenar conexões)
  - [ ] Resposta à pergunta B (Como identificar clientes)
  - [ ] Resposta à pergunta C (E se usasse polling?)
  - [ ] Resposta à pergunta D (Cenários WebSocket vs REST)

**Validação:** PDF existe e tem todas as 4 respostas? ☐

---

## 📸 SCREENSHOTS (opcional mas recomendado)

Se você quiser adicionar screenshots ao PDF:

- [ ] Screenshot 1: Servidor WebSocket em execução (ws://localhost:8000)
- [ ] Screenshot 2: 2 clientes conectados simultaneamente
- [ ] Screenshot 3: Mensagem recebida em tempo real (broadcast)
- [ ] Screenshot 4: Logs no servidor mostrando conexão/mensagem/desconexão

**Como capturar:** Siga o arquivo `GUIA_SCREENSHOTS.md`

**Validação:** Todos 4 screenshots estão no PDF? ☐

---

## ✅ TESTES FUNCIONAIS

Antes de entregar, teste:

- [ ] Servidor inicia corretamente: `python server.py`
- [ ] HTTP server inicia: `python -m http.server 8001`
- [ ] Página carrega em: `http://localhost:8001`
- [ ] 2 abas conseguem conectar simultaneamente
- [ ] Mensagem enviada em uma aba aparece na outra
- [ ] **SEM REFRESH** necessário (prova WebSocket)
- [ ] Logs mostram: CONEXAO, MENSAGEM, DESCONEXAO

**Validação:** Todos os testes passaram? ☐

---

## 🎯 REQUISITOS DO PROFESSOR

Marque cada requisito confirmando que foi atendido:

### Escopo da Atividade

- [ ] Um servidor WebSocket
- [ ] Uma interface web simples (HTML + JavaScript)
- [ ] Um mecanismo para envio de atualizações
- [ ] Atualização automática da interface dos clientes conectados

### Requisitos Mínimos Obrigatórios

- [ ] Utilizar protocolo WebSocket (ws://) - **NÃO** Socket.IO
- [ ] 2+ clientes conectados simultaneamente
- [ ] Permitir envio de mensagens do cliente para o servidor
- [ ] Permitir broadcast (servidor para todos os clientes)
- [ ] Exibir visualmente as mensagens recebidas
- [ ] Registrar no console do servidor:
  - [ ] Abertura de conexão
  - [ ] Recebimento de mensagem
  - [ ] Encerramento de conexão

### Tomada de Decisão Obrigatória (documentada)

- [ ] Como identificar os clientes conectados? → `DECISOES_TECNICAS.md` pergunta B
- [ ] Como armazenar as conexões ativas? → `DECISOES_TECNICAS.md` pergunta A
- [ ] Como tratar clientes desconectados? → `README.md` + `server.py`
- [ ] Qual formato de mensagem será utilizado? → JSON (respondido em docs)

**Validação:** Todos os requisitos foram atendidos? ☐

---

## 📦 FORMATO DE ENTREGA

O professor pediu **Link do repositório Git OU Arquivo compactado (.zip)**

### Opção 1: Git + GitHub

- [ ] Repositório criado e públicono GitHub
- [ ] Todos os arquivos commitados
- [ ] URL fornecida ao professor

**Git commit sugerido:**
```bash
git add .
git commit -m "feat: websocket mural em tempo real com broadcast"
git push origin main
```

### Opção 2: Arquivo ZIP

- [ ] Arquivo `projeto-websocket-adocao-pets.zip` criado
- [ ] Contém todos os arquivos:
  - ✓ server.py
  - ✓ client.js
  - ✓ index.html
  - ✓ style.css
  - ✓ requirements.txt
  - ✓ README.md
  - ✓ DECISOES_TECNICAS.md
  - ✓ EVIDENCIAS_WEBSOCKET.pdf
  - ✓ .gitignore

**Validação:** Arquivo ZIP está pronto para entregar? ☐

---

## 📋 DOCUMENTO PDF FINAL

Deve conter:

- [ ] Prints do servidor em execução
- [ ] Prints de dois clientes conectados simultaneamente
- [ ] Prints demonstrando recebimento de mensagem em tempo real
- [ ] Resposta à pergunta A (max 5 linhas)
- [ ] Resposta à pergunta B (max 5 linhas)
- [ ] Resposta à pergunta C (max 5 linhas)
- [ ] Resposta à pergunta D (max 5 linhas)
- [ ] **Limite:** Máximo 1 página de respostas descritivas

**Validação:** PDF tem tudo isso? ☐

---

## 🎓 APRESENTAÇÃO EM SALA

Se você vai apresentar:

- [ ] Terminal com servidor rodando visível
- [ ] Navegador com 2 abas abertas
- [ ] Enviar mensagem e mostrar que aparece nas 2 abas
- [ ] Mostrar os logs no terminal
- [ ] Duração: 3-5 minutos
- [ ] Ter a fala pronta (vide `RESUMO_EXECUTIVO.txt`)

**Validação:** Você está pronto para apresentar? ☐

---

## 🏆 CHECKLIST FINAL

- [ ] Código funciona 100%
- [ ] Documentação está completa
- [ ] PDF de evidências foi gerado
- [ ] Todos os arquivos estão prontos
- [ ] Teste funcional passou
- [ ] Formato de entrega está certo (Git ou ZIP)
- [ ] Você releu o rubric e atendeu tudo

---

## 📝 NOTAS IMPORTANTES

1. **ws:// explícito:** O professor DEVE VER `ws://localhost:8000` no código
2. **Sem Socket.IO:** Apenas WebSocket nativo
3. **Broadcast obrigatório:** Mensagem deve chegar em todos os clientes
4. **Logs obrigatórios:** Console do servidor deve registrar conexão/msg/desconexão
5. **Respostas técnicas:** Máximo 5 linhas por pergunta
6. **PDF:** Máximo 1 página de respostas (screenshots extras OK)

---

## ✨ PONTOS EXTRAS (opcional)

Se quiser se destacar:

- [ ] Interface com animações suaves
- [ ] Indicador visual de quantos clientes estão conectados
- [ ] Timestamps nas mensagens
- [ ] Tratamento de reconexão automática
- [ ] Nomes personalizados para clientes
- [ ] Chat persistente (armazena histórico)
- [ ] Diferentes tipos de mensagem (info, alerta, etc)

---

## 🎉 CONCLUSÃO

Quando todos os checkboxes estiverem marcados, você está **100% pronto** para:
1. ✅ Entregar ao professor
2. ✅ Apresentar em sala
3. ✅ Obter nota máxima

---

**Data de conclusão:** ________________  
**Assinado:** ________________________

---

*Bom trabalho! Você conseguiu! 🚀*
