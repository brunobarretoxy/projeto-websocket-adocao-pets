/**
 * Cliente WebSocket - Mural em Tempo Real
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
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const messagesList = document.getElementById('messagesList');
const connectionStatus = document.getElementById('connection-status');
const clientId = document.getElementById('client-id');


// ========== INICIALIZAÇÃO ==========
document.addEventListener('DOMContentLoaded', () => {
    console.log('🚀 Página carregada, conectando ao servidor WebSocket...');
    conectarWebSocket();
    
    // Event listeners
    sendButton.addEventListener('click', enviarMensagem);
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            enviarMensagem();
        }
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
    exibirMensagemSistema('🎉 Conectado ao servidor! Você pode enviar mensagens agora.');
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
        
        // Adicionar mensagem à lista
        adicionarMensagem(dados.content, dados.timestamp);
        
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
    exibirMensagemSistema('⚠️ Erro na conexão. Verifique se o servidor está rodando.');
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
    exibirMensagemSistema('🔴 Desconectado do servidor.');
    
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
    
    const texto = messageInput.value.trim();
    
    // Validar
    if (!texto) {
        console.warn('⚠️ Campo de mensagem vazio');
        return;
    }
    
    if (!ws || ws.readyState !== WebSocket.OPEN) {
        console.error('❌ WebSocket não está conectado');
        exibirMensagemSistema('❌ Não conectado ao servidor');
        return;
    }
    
    // Criar objeto de mensagem
    const mensagem = {
        type: 'message',
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
        exibirMensagemSistema('❌ Erro ao enviar mensagem');
    }
}


// ========== ATUALIZAÇÃO DA INTERFACE ==========

function adicionarMensagem(conteudo, timestamp) {
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
    const horaFormatada = data.toLocaleTimeString('pt-BR');
    
    // HTML da mensagem
    messageItem.innerHTML = `
        <div class="message-content">
            💬 ${conteudo}
        </div>
        <div class="message-time">
            ${horaFormatada}
        </div>
    `;
    
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
    messageItem.className = 'message-item';
    messageItem.style.borderLeftColor = '#f44336'; // Vermelho para sistema
    
    messageItem.innerHTML = `
        <div class="message-content" style="color: #f44336; font-weight: bold;">
            ${texto}
        </div>
        <div class="message-time">
            ${new Date().toLocaleTimeString('pt-BR')}
        </div>
    `;
    
    messagesList.appendChild(messageItem);
    messagesList.scrollTop = messagesList.scrollHeight;
}


function exibirStatus(conectado, texto) {
    /**
     * Atualiza o indicador de status da conexão
     */
    
    connectionStatus.textContent = (conectado ? '🟢 ' : '🔴 ') + texto;
    connectionStatus.className = conectado ? 'status-badge connected' : 'status-badge disconnected';
    
    console.log(`📊 Status: ${texto} (${conectado ? 'conectado' : 'desconectado'})`);
}


function limparMensagens() {
    /**
     * Limpa a lista de mensagens
     */
    messagesList.innerHTML = '<div class="empty-state">Nenhuma mensagem ainda. Envie a primeira!</div>';
}


// ========== LOGS E DEBUG ==========
console.log('%c🐾 MURAL EM TEMPO REAL - WebSocket', 'font-size: 18px; color: #667eea; font-weight: bold;');
console.log('%cProjeto de Adoção de Pets', 'font-size: 14px; color: #764ba2;');
console.log('%cConsole aberto - Você verá todos os eventos aqui!', 'color: #666;');
