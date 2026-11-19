/**
 * Cliente WebSocket - Mural de Adoções
 * 
 * IMPORTANTE: O protocolo WebSocket é EXPLÍCITO neste código:
 * const ws = new WebSocket("ws://localhost:8000");
 * 
 * Responsabilidades:
 * - Conectar ao servidor WebSocket
 * - Enviar mensagens
 * - Receber mensagens do servidor
 * - Atualizar interface em tempo real
 * - Registrar eventos no console
 */

// ========== VARIÁVEIS GLOBAIS ==========
let ws;
const nameInput = document.getElementById('nameInput');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const messageForm = document.getElementById('messageForm');
const messagesList = document.getElementById('messagesList');
const connectionStatus = document.getElementById('connection-status');
const statusText = document.getElementById('status-text');
const onlineCount = document.getElementById('online-count');


// ========== INICIALIZAÇÃO ==========
document.addEventListener('DOMContentLoaded', () => {
    console.log('🚀 Página carregada, conectando ao servidor WebSocket...');
    conectarWebSocket();
    
    // Event listeners
    messageForm.addEventListener('submit', (e) => {
        e.preventDefault();
        enviarMensagem();
    });
    [nameInput, messageInput].forEach((input) => {
        input.addEventListener('input', () => input.setCustomValidity(''));
    });
});


// ========== CONEXÃO WEBSOCKET ==========
function conectarWebSocket() {
    /**
     * ⭐ CRÍTICO: URL com ws:// EXPLÍCITO
     * Não usar bibliotecas que abstraem o protocolo (como Socket.IO)
     * O professor quer ver claramente: ws://localhost:8000
     */
    
    try {
        // Conectar ao servidor
        ws = new WebSocket("ws://localhost:8000");
        
        console.log('📡 Tentando conectar a ws://localhost:8000...');
        
        // Eventos do WebSocket
        ws.onopen = handleConnectionOpen;
        ws.onmessage = handleMessageReceived;
        ws.onerror = handleError;
        ws.onclose = handleConnectionClose;
        
    } catch (error) {
        console.error('❌ Erro ao criar WebSocket:', error);
        exibirStatus(false, 'Erro ao conectar');
    }
}


// ========== HANDLERS DO WEBSOCKET ==========

function handleConnectionOpen(event) {
    /**
     * Chamado quando a conexão é estabelecida com sucesso
     */
    console.log('✅ Conectado ao servidor WebSocket!');
    console.log('   Protocolo: WebSocket (ws://)');
    console.log('   Servidor: localhost:8000');
    
    // Atualizar interface
    exibirStatus(true, 'Conectado');
    messageInput.disabled = false;
    sendButton.disabled = false;
    
    // Limpar mensagens anteriores
    limparMensagens();
}


function handleMessageReceived(event) {
    /**
     * Chamado quando o servidor envia uma mensagem
     * 
     * A mensagem pode ser:
     * - Uma mensagem de outro cliente (broadcast)
     * - Uma mensagem de sistema
     */
    
    console.log('📨 Mensagem recebida do servidor:', event.data);
    
    try {
        // Tentar fazer parse como JSON
        let dados;
        try {
            dados = JSON.parse(event.data);
        } catch (e) {
            // Se não for JSON, tratar como texto simples
            dados = {
                type: 'message',
                content: event.data,
                timestamp: new Date().toISOString()
            };
        }
        
        // Verificar tipo de mensagem
        if (dados.type === 'connection_count') {
            // Atualizar contador de clientes
            atualizarContadorClientes(dados.count);
        } else {
            // Adicionar mensagem à lista
            adicionarMensagem(dados.content, dados.timestamp, dados.author);
        }
        
    } catch (error) {
        console.error('❌ Erro ao processar mensagem:', error);
    }
}


function handleError(event) {
    /**
     * Chamado quando ocorre um erro na conexão WebSocket
     */
    console.error('❌ Erro na conexão WebSocket:', event);
    exibirStatus(false, 'Erro na conexão');
    exibirMensagemSistema('Erro na conexão. Verifique se o servidor está rodando.');
}


function handleConnectionClose(event) {
    /**
     * Chamado quando a conexão é fechada
     */
    console.log('🔌 Desconectado do servidor');
    console.log('   Código:', event.code);
    console.log('   Razão:', event.reason);
    
    // Atualizar interface
    exibirStatus(false, 'Desconectado');
    messageInput.disabled = true;
    sendButton.disabled = true;
    atualizarContadorClientes('—');
    exibirMensagemSistema('Desconectado do servidor.');
    
    // Tentar reconectar após 3 segundos
    console.log('⏳ Tentando reconectar em 3 segundos...');
    setTimeout(() => {
        console.log('🔄 Reconectando...');
        conectarWebSocket();
    }, 3000);
}


// ========== ENVIO DE MENSAGENS ==========

function enviarMensagem() {
    /**
     * Envia uma mensagem do cliente para o servidor
     * O servidor faz broadcast para todos os clientes
     */
    
    const nome = nameInput.value.trim();
    const texto = messageInput.value.trim();
    
    // Validar
    if (!nome) {
        nameInput.setCustomValidity('Informe seu nome.');
        nameInput.reportValidity();
        return;
    }
    if (!texto) {
        messageInput.setCustomValidity('Escreva um aviso.');
        messageInput.reportValidity();
        return;
    }
    
    if (!ws || ws.readyState !== WebSocket.OPEN) {
        console.error('❌ WebSocket não está conectado');
        exibirMensagemSistema('Não conectado ao servidor');
        return;
    }
    
    // Criar objeto de mensagem
    const mensagem = {
        type: 'message',
        author: nome,
        content: texto,
        timestamp: new Date().toISOString()
    };
    
    // Converter para JSON
    const mensagemJson = JSON.stringify(mensagem);
    
    console.log('📤 Enviando mensagem:', mensagem);
    
    try {
        // Enviar ao servidor
        ws.send(mensagemJson);
        
        console.log('✅ Mensagem enviada com sucesso');
        
        // Limpar input
        messageInput.value = '';
        messageInput.focus();
        
    } catch (error) {
        console.error('❌ Erro ao enviar mensagem:', error);
        exibirMensagemSistema('Erro ao enviar mensagem');
    }
}


// ========== ATUALIZAÇÃO DA INTERFACE ==========

function adicionarMensagem(conteudo, timestamp, autor) {
    /**
     * Adiciona uma mensagem à lista visual
     */
    
    // Remover estado vazio se existir
    const emptyState = messagesList.querySelector('.empty-state');
    if (emptyState) {
        emptyState.remove();
    }
    
    // Criar elemento de mensagem
    const messageItem = document.createElement('div');
    messageItem.className = 'message-item';
    
    // Formatar timestamp
    const data = new Date(timestamp);
    const horaFormatada = data.toLocaleTimeString('pt-BR', {
        hour: '2-digit',
        minute: '2-digit'
    });
    
    const messageMeta = document.createElement('div');
    messageMeta.className = 'message-meta';
    const messageAuthor = document.createElement('span');
    messageAuthor.className = 'message-author';
    messageAuthor.textContent = typeof autor === 'string' && autor.trim() ? autor.trim() : 'Sem nome';
    const messageTime = document.createElement('span');
    messageTime.textContent = `· ${horaFormatada}`;
    messageMeta.append(messageAuthor, messageTime);
    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';
    messageContent.textContent = conteudo;
    messageItem.append(messageMeta, messageContent);
    
    // Adicionar à lista
    messagesList.appendChild(messageItem);
    
    // Scroll automático para a última mensagem
    messagesList.scrollTop = messagesList.scrollHeight;
    
    console.log('📝 Mensagem adicionada à interface');
}


function exibirMensagemSistema(texto) {
    /**
     * Adiciona uma mensagem de sistema (informação, alerta, etc)
     */
    
    // Remover estado vazio se existir
    const emptyState = messagesList.querySelector('.empty-state');
    if (emptyState) {
        emptyState.remove();
    }
    
    // Criar elemento
    const messageItem = document.createElement('div');
    messageItem.className = 'message-item system';
    
    messageItem.innerHTML = `
        <div class="message-content">
            ${texto}
        </div>
        <div class="message-time">
            ${new Date().toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })}
        </div>
    `;
    
    messagesList.appendChild(messageItem);
    messagesList.scrollTop = messagesList.scrollHeight;
}


function exibirStatus(conectado, texto) {
    /**
     * Atualiza o indicador de status da conexão
     */
    
    statusText.textContent = texto;
    
    if (conectado) {
        connectionStatus.classList.add('connected');
        connectionStatus.classList.remove('disconnected');
    } else {
        connectionStatus.classList.remove('connected');
        connectionStatus.classList.add('disconnected');
    }
    
    console.log(`📊 Status: ${texto} (${conectado ? 'conectado' : 'desconectado'})`);
}


function atualizarContadorClientes(count) {
    /**
     * Atualiza o contador de clientes conectados
     */
    onlineCount.textContent = count;
    console.log(`👥 Clientes conectados: ${count}`);
}


function limparMensagens() {
    /**
     * Limpa a lista de mensagens
     */
    messagesList.innerHTML = `
        <div class="empty-state">
            <span class="empty-icon" aria-hidden="true">✉</span>
            <p>O mural está esperando por uma história.</p>
            <small>Que tal compartilhar a primeira novidade?</small>
        </div>
    `;
}


// ========== LOGS E DEBUG ==========
console.log('%c🐾 MURAL DE ADOÇÕES — WebSocket', 'font-size: 18px; color: #d96c4e; font-weight: bold;');
console.log('%cComunicação em Tempo Real', 'font-size: 14px; color: #748087;');
console.log('%c⭐ Protocolo: ws://localhost:8000 (EXPLÍCITO no código)', 'color: #d96c4e; font-weight: bold;');
console.log('%cConsole aberto - Você verá todos os eventos aqui!', 'color: #748087;');
