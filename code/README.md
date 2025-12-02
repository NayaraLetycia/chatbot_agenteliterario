# 📚 Agente Literário Inteligente

Sistema de recomendação de livros usando IA, totalmente gratuito.

## 🚀 Tecnologias Usadas
- Python 3.10+
- Groq API (LLM gratuito - Llama 3)
- Google Books API (gratuita)
- Streamlit (interface web gratuita)

## 📦 Instalação

```bash
pip install -r requirements.txt
```

## 🔑 Configuração

1. Crie uma conta gratuita em: https://console.groq.com
2. Copie sua API key
3. Crie o arquivo `.env`:

```
GROQ_API_KEY=sua_chave_aqui
```

## ▶️ Como Usar

```bash
# Versão terminal
python agente_literario.py

# Versão web (interface bonita)
streamlit run app_web.py
```

## 📋 Funcionalidades

✅ Conversa natural com o usuário
✅ Entende gostos e preferências
✅ Busca livros reais via Google Books API
✅ Gera planos de leitura personalizados
✅ Interface web amigável
✅ 100% gratuito!
