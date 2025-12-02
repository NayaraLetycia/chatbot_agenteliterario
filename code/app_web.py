"""
Agente Literário Inteligente - Interface Web com Streamlit
Versão com interface gráfica amigável
"""

import streamlit as st
import os
from dotenv import load_dotenv
from agente_literario import AgenteLiterario

# Configuração da página
st.set_page_config(
    page_title="Agente Literário IA",
    page_icon="📚",
    layout="wide"
)

# Carregar variáveis de ambiente
load_dotenv()

# CSS customizado
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
    }
    .agent-message {
        background-color: #f5f5f5;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.title("📚 Agente Literário Inteligente")
st.markdown("*Seu assistente pessoal de recomendações de livros usando IA*")
st.divider()

# Inicializar session state
if 'agente' not in st.session_state:
    st.session_state.agente = AgenteLiterario()
    st.session_state.mensagens = []
    # Mensagem inicial
    resposta_inicial = st.session_state.agente.conversar("Olá! Quero recomendações de livros.")
    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta_inicial
    })

# Sidebar com informações
with st.sidebar:
    st.header("ℹ️ Como usar")
    st.markdown("""
    1. **Converse naturalmente** com o agente
    2. Responda as perguntas sobre seus gostos
    3. Receba **recomendações personalizadas**
    4. Use os botões para ações rápidas
    """)
    
    st.divider()
    
    st.header("🎯 Ações Rápidas")
    
    if st.button("📋 Gerar Plano de Leitura", use_container_width=True):
        with st.spinner("Criando plano personalizado..."):
            plano = st.session_state.agente.gerar_plano_leitura()
            st.session_state.mensagens.append({
                "role": "assistant",
                "content": f"**📋 Seu Plano de Leitura:**\n\n{plano}"
            })
            st.rerun()
    
    st.divider()
    
    # Busca no Google Books
    st.header("🔍 Buscar Livros")
    termo_busca = st.text_input("Digite o título ou autor:", key="busca")
    
    if st.button("Buscar", use_container_width=True) and termo_busca:
        with st.spinner(f"Buscando '{termo_busca}'..."):
            livros = st.session_state.agente.buscar_livros_google(termo_busca)
            
            if livros:
                resultado = f"**🔍 Resultados para '{termo_busca}':**\n\n"
                for i, livro in enumerate(livros, 1):
                    resultado += f"{i}. **{livro['titulo']}**\n"
                    resultado += f"   📝 {livro['autores']}\n"
                    resultado += f"   🔗 [Ver no Google Books]({livro['link']})\n\n"
                
                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": resultado
                })
                st.rerun()
            else:
                st.error("Nenhum livro encontrado.")
    
    st.divider()
    
    if st.button("🔄 Nova Conversa", use_container_width=True):
        st.session_state.agente = AgenteLiterario()
        st.session_state.mensagens = []
        resposta_inicial = st.session_state.agente.conversar("Olá! Quero recomendações de livros.")
        st.session_state.mensagens.append({
            "role": "assistant",
            "content": resposta_inicial
        })
        st.rerun()

# Área de chat
st.header("💬 Conversa")

# Exibir mensagens
chat_container = st.container()
with chat_container:
    for msg in st.session_state.mensagens:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>👤 Você:</strong><br>
                {msg["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message agent-message">
                <strong>🤖 Agente:</strong><br>
                {msg["content"]}
            </div>
            """, unsafe_allow_html=True)

# Input do usuário
st.divider()
col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.text_input(
        "Digite sua mensagem:",
        key="user_input",
        label_visibility="collapsed",
        placeholder="Ex: Gosto de fantasia medieval..."
    )

with col2:
    enviar = st.button("Enviar", use_container_width=True, type="primary")

# Processar entrada
if enviar and user_input:
    # Adiciona mensagem do usuário
    st.session_state.mensagens.append({
        "role": "user",
        "content": user_input
    })
    
    # Obtém resposta do agente
    with st.spinner("Pensando..."):
        resposta = st.session_state.agente.conversar(user_input)
    
    # Adiciona resposta do agente
    st.session_state.mensagens.append({
        "role": "assistant",
        "content": resposta
    })
    
    # Se houver recomendação, busca automaticamente
    if 'RECOMENDAÇÃO:' in resposta or 'recomendo' in resposta.lower():
        # Extrai recomendações
        recomendacoes = st.session_state.agente.extrair_recomendacoes(resposta)
        if recomendacoes:
            primeiro_livro = recomendacoes[0].split('RECOMENDAÇÃO:')[-1].strip()
            livros = st.session_state.agente.buscar_livros_google(primeiro_livro, max_results=3)
            
            if livros:
                links = "\n\n**🔗 Onde encontrar:**\n\n"
                for livro in livros[:3]:
                    links += f"• [{livro['titulo']}]({livro['link']})\n"
                
                st.session_state.mensagens.append({
                    "role": "assistant",
                    "content": links
                })
    
    st.rerun()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    Desenvolvido com ❤️ usando Python + Groq + Google Books API<br>
    100% Gratuito | Código aberto
</div>
""", unsafe_allow_html=True)
