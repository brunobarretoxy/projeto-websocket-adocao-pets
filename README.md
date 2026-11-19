# 🐾 WebSocket — Mural de Adoções

Uma aplicação simples para compartilhar avisos sobre adoção de pets em tempo real. Quando uma pessoa publica um aviso, o servidor o retransmite para todos os clientes conectados, sem recarregar a página.

O projeto demonstra comunicação bidirecional com WebSocket, usando Python no servidor e HTML, CSS e JavaScript no navegador.

## Requisitos

- Python e `pip` instalados. O projeto foi testado com Python 3.14.
- Um navegador atualizado.
- As portas locais 8000 e 8001 disponíveis.

## Como executar

Abra um terminal **na pasta do projeto** e instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

### 1. Inicie o servidor WebSocket

No primeiro terminal, execute:

```powershell
python server.py
```

Mantenha esse terminal aberto. A saída deve incluir:

```text
[OK] Servidor iniciado em: ws://localhost:8000
```

### 2. Inicie o servidor HTTP

Abra um **segundo terminal**, também na pasta do projeto, e execute:

```powershell
python -m http.server 8001
```

Mantenha os dois terminais abertos. O servidor HTTP entrega a página e seus arquivos; o servidor WebSocket, na porta 8000, cuida das mensagens em tempo real.

### 3. Teste com dois clientes

1. Abra `http://localhost:8001` em duas abas ou janelas do navegador.
2. Confira se ambas mostram **Conectado**.
3. Na primeira aba, informe seu nome, escreva um aviso, como `Luna foi adotada!`, e clique em **Publicar aviso**.
4. Observe o nome e o aviso aparecerem nas duas abas sem atualizar a página.
5. Feche uma das abas e observe o registro de desconexão no terminal do servidor WebSocket.

Para encerrar cada servidor, pressione `Ctrl+C` no terminal correspondente.

## Como funciona

O navegador cria uma conexão explícita com o protocolo WebSocket:

```javascript
ws = new WebSocket("ws://localhost:8000");
```

O cliente envia o aviso em JSON. O servidor recebe a mensagem e a retransmite para todos os clientes conectados, incluindo quem enviou. A interface exibe o aviso e a hora. O servidor registra conexão, recebimento de mensagem e desconexão no console.

Exemplo de mensagem:

```json
{
  "type": "message",
  "author": "Bruno",
  "content": "Luna foi adotada!",
  "timestamp": "2026-11-15T17:40:30Z"
}
```

O servidor também envia mensagens JSON do tipo `connection_count` para atualizar o número de conexões na interface.

## Decisões técnicas

- **Identificação:** o servidor gera um UUID para cada conexão e o utiliza nos registros do console. O nome exibido no aviso é informado pela própria pessoa; não há cadastro nem verificação de identidade.
- **Armazenamento:** o dicionário `clients` mantém o objeto WebSocket como chave e os dados da conexão, incluindo UUID e horário, como valor.
- **Desconexão:** ao encerrar uma conexão, o servidor a remove do dicionário no bloco `finally` e atualiza a contagem dos clientes restantes.
- **Formato:** os avisos enviados pela interface são JSON, com tipo, nome, conteúdo e horário.

Com **polling**, cada cliente precisaria consultar o servidor periodicamente, inclusive quando não houvesse novidades; a atualização poderia demorar até a próxima consulta. O WebSocket mantém a conexão aberta e permite ao servidor enviar atualizações assim que elas acontecem. É útil para avisos, chats e monitoramento em tempo real; uma API REST é adequada para operações de requisição e resposta, como consultas ou cadastros.

## Arquivos principais

```text
server.py                  Servidor WebSocket
index.html                 Interface do mural
client.js                  Cliente WebSocket e interação com a página
style.css                  Estilos da interface
requirements.txt           Dependência Python
docs/DECISOES_TECNICAS.md  Explicações das decisões técnicas
docs/ARQUITETURA.md        Detalhes da arquitetura
docs/EXECUCAO_RAPIDA.md    Guia rápido de execução
docs/GUIA_SCREENSHOTS.md   Orientações para capturar as evidências
docs/CHECKLIST_APRESENTACAO.md  Checklist para apresentação
```

O endereço `ws://localhost:8000` aponta para a própria máquina de quem abre a página; a demonstração com duas abas deve ser feita no mesmo computador que executa o servidor.

## Solução de problemas

- **`No module named websockets`:** execute `python -m pip install -r requirements.txt` no mesmo ambiente Python usado para iniciar o servidor.
- **Porta 8000 ou 8001 em uso:** verifique se já existe um servidor do projeto em outro terminal. Encerre apenas o processo que você identificou e que deseja parar, ou libere a porta antes de iniciar novamente.
- **Interface desconectada:** confira se `server.py` está em execução e se a página foi aberta em `http://localhost:8001`.
- **Já estou na pasta do projeto:** execute os comandos diretamente, sem repetir `cd projeto-websocket-adocao-pets`.

## Entrega

Além do código-fonte, o professor solicita um único PDF com prints do servidor em execução, de dois clientes conectados e do recebimento de uma mensagem em tempo real. Inclua também as quatro respostas técnicas, com até cinco linhas por questão e no máximo uma página para as respostas descritivas. As orientações para as capturas estão no [guia de screenshots](docs/GUIA_SCREENSHOTS.md).

Tema: adoção de pets. Desenvolvedor: Bruno.
