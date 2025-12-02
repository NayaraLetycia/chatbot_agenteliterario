# 🚀 Guia de Instalação Completo

## Pré-requisitos
- Python 3.10 ou superior
- Conexão com internet

## Passo a Passo

### 1️⃣ Instalar Dependências

Abra o PowerShell nesta pasta e execute:

```powershell
pip install -r requirements.txt
```

### 2️⃣ Obter API Key Gratuita (Groq)

1. Acesse: https://console.groq.com
2. Crie uma conta gratuita (pode usar Google/GitHub)
3. Vá em "API Keys"
4. Clique em "Create API Key"
5. Copie a chave gerada

**Limites gratuitos do Groq:**
- 30 requisições/minuto
- 14.400 requisições/dia
- Totalmente suficiente para o projeto! 🎉

### 3️⃣ Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```powershell
Copy-Item .env.example .env
notepad .env
```

Cole sua API key no arquivo:
```
GROQ_API_KEY=gsk_sua_chave_aqui
```

Salve e feche o arquivo.

### 4️⃣ Testar Instalação

Execute um exercício de teste:

```powershell
python exercicios/exercicio1_sentimentos.py
```

Se aparecer uma análise de sentimento, está funcionando! ✅

## 🎯 Como Usar

### Versão Terminal (Simples)
```powershell
python agente_literario.py
```

### Versão Web (Interface Bonita)
```powershell
streamlit run app_web.py
```

O navegador abrirá automaticamente em `http://localhost:8501`

## 📋 Testar Exercícios

```powershell
# Exercício 1 - Análise de Sentimentos
python exercicios/exercicio1_sentimentos.py

# Exercício 2 - Identificação de Entidades
python exercicios/exercicio2_entidades.py

# Exercício 3 - Geração de Texto
python exercicios/exercicio3_geracao_texto.py

# Exercício 4 - Resolução de Problemas
python exercicios/exercicio4_resolucao_problemas.py

# Exercício 5 - Agente Virtual
python exercicios/exercicio5_agente_virtual.py
```

## 🔧 Solução de Problemas

### Erro: "No module named 'groq'"
```powershell
pip install groq
```

### Erro: "API key not found"
Verifique se o arquivo `.env` existe e tem a chave correta.

### Erro: "Rate limit exceeded"
Aguarde 1 minuto. O limite gratuito é de 30 req/min.

### Streamlit não abre no navegador
Abra manualmente: http://localhost:8501

## 📚 Estrutura do Projeto

```
Agente Literario/
├── agente_literario.py      # Versão terminal
├── app_web.py               # Versão web (Streamlit)
├── requirements.txt         # Dependências
├── .env                     # Suas chaves (NÃO commitar!)
├── .env.example            # Exemplo de .env
├── README.md               # Documentação
├── INSTALACAO.md           # Este arquivo
└── exercicios/             # 5 exercícios do curso
    ├── exercicio1_sentimentos.py
    ├── exercicio2_entidades.py
    ├── exercicio3_geracao_texto.py
    ├── exercicio4_resolucao_problemas.py
    └── exercicio5_agente_virtual.py
```

## 🎓 Para a Apresentação

1. **Demonstre a versão web** (mais visual)
2. **Mostre um caso real de uso**
3. **Explique as APIs gratuitas usadas**
4. **Execute um dos exercícios**

## 💡 Dicas

- A versão web (Streamlit) é mais impressionante visualmente
- Prepare exemplos de perguntas para demonstração
- Teste antes da apresentação!
- O Google Books API não precisa de chave (mais fácil)

## ✅ Checklist Final

- [ ] Python instalado
- [ ] Dependências instaladas (`pip install -r requirements.txt`)
- [ ] API Key do Groq obtida
- [ ] Arquivo `.env` configurado
- [ ] Testado versão terminal
- [ ] Testado versão web
- [ ] Todos os 5 exercícios funcionando

---
**Dúvidas?** Leia o README.md ou teste os exemplos!
