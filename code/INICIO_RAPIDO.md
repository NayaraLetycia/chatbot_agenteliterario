# ⚡ INÍCIO RÁPIDO - 5 MINUTOS

## 📥 1. Instalar Dependências

```powershell
pip install -r requirements.txt
```

## 🔑 2. Configurar API Key (GRÁTIS!)

### Obter chave Groq (30 segundos):
1. Acesse: https://console.groq.com
2. Clique "Sign Up" (pode usar Google)
3. Vá em "API Keys" → "Create API Key"
4. Copie a chave

### Configurar no projeto:
```powershell
# Copiar arquivo de exemplo
Copy-Item .env.example .env

# Editar arquivo
notepad .env
```

Cole sua chave:
```
GROQ_API_KEY=gsk_sua_chave_aqui
```

Salve e feche.

## ✅ 3. Testar Instalação

```powershell
python testar_instalacao.py
```

Se aparecer ✅ tudo verde, está pronto!

## 🚀 4. Executar

### Opção 1: Interface Web (RECOMENDADO)
```powershell
streamlit run app_web.py
```

Abre automaticamente no navegador: http://localhost:8501

### Opção 2: Terminal
```powershell
python agente_literario.py
```

## 🧪 5. Testar Exercícios

```powershell
# Exercício 1 - Análise de Sentimentos
python exercicios/exercicio1_sentimentos.py

# Exercício 5 - Agente Virtual
python exercicios/exercicio5_agente_virtual.py
```

## 📋 Demonstração Rápida

No Streamlit:
1. Digite: "Gosto de fantasia medieval"
2. Responda as perguntas do agente
3. Veja as recomendações aparecerem
4. Clique "Gerar Plano de Leitura"

## ❓ Problemas?

**Erro: "No module named 'groq'"**
```powershell
pip install groq
```

**Erro: "API key not found"**
- Verifique se arquivo `.env` existe
- Confira se a chave está correta

**Streamlit não abre**
- Abra manualmente: http://localhost:8501
- Ou use: `python agente_literario.py`

## 📚 Próximos Passos

- Leia `ROTEIRO_APRESENTACAO.md` para preparar apresentação
- `ARTIGO_BASE.md` tem estrutura completa do artigo
- `INSTALACAO.md` tem guia detalhado

## 🎯 Para Apresentação

1. Execute `streamlit run app_web.py`
2. Prepare 2-3 cenários de teste
3. Teste antes! (evita surpresas)

**Pronto! Você tem um agente literário funcionando! 🎉**
