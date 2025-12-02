# 📂 Estrutura do Projeto Agente Literário

```
Agente Literario/
│
├── 📄 README.md                      # Visão geral do projeto
├── ⚡ INICIO_RAPIDO.md              # Guia de 5 minutos
├── 📖 INSTALACAO.md                 # Instalação detalhada
├── 🎤 ROTEIRO_APRESENTACAO.md       # Roteiro completo (15-25min)
├── 📝 ARTIGO_BASE.md                # Estrutura do artigo acadêmico
│
├── 🔧 ARQUIVOS DE CONFIGURAÇÃO
│   ├── requirements.txt             # Dependências Python
│   ├── .env.example                 # Modelo de configuração
│   ├── .gitignore                   # Arquivos ignorados no Git
│   └── [.env]                       # SEU arquivo (não commitar!)
│
├── 🚀 APLICAÇÃO PRINCIPAL
│   ├── agente_literario.py          # Versão terminal (CLI)
│   ├── app_web.py                   # Versão web (Streamlit)
│   └── testar_instalacao.py         # Script de validação
│
└── 📚 EXERCÍCIOS (5 obrigatórios)
    └── exercicios/
        ├── exercicio1_sentimentos.py       # Análise de sentimentos
        ├── exercicio2_entidades.py         # NER (entidades)
        ├── exercicio3_geracao_texto.py     # Geração criativa
        ├── exercicio4_resolucao_problemas.py  # Q&A
        └── exercicio5_agente_virtual.py    # Conversação

```

---

## 🎯 Arquivos por Responsabilidade

### 👨‍💻 Lucca e Nayara (Desenvolvimento)
- `agente_literario.py` - Lógica principal
- `app_web.py` - Interface web
- `testar_instalacao.py` - Testes

### 📝 Cleiton (Documentação)
- `ARTIGO_BASE.md` - Base para artigo final
- Pode editar/expandir README.md

### 🧪 Henrique e Geovani (Exercícios)
- `exercicios/exercicio1_sentimentos.py`
- `exercicios/exercicio2_entidades.py`
- `exercicios/exercicio3_geracao_texto.py`
- `exercicios/exercicio4_resolucao_problemas.py`
- `exercicios/exercicio5_agente_virtual.py`

### 🎤 Adriana (Apresentação)
- `ROTEIRO_APRESENTACAO.md` - Roteiro completo
- Preparar slides baseado no roteiro
- Coordenar ensaio

---

## 🔑 Arquivos Essenciais para Executar

### Mínimo necessário:
1. ✅ `requirements.txt` - Instalar dependências
2. ✅ `.env` - API key do Groq
3. ✅ `agente_literario.py` - Aplicação principal
4. ✅ `app_web.py` - Interface web

### Para apresentação completa:
5. ✅ Todos os 5 exercícios em `exercicios/`
6. ✅ `ROTEIRO_APRESENTACAO.md`
7. ✅ `ARTIGO_BASE.md` (entregar no dia)

---

## 📊 Tecnologias por Arquivo

| Arquivo | Tecnologias |
|---------|-------------|
| `agente_literario.py` | Python, Groq, Google Books API, dotenv |
| `app_web.py` | Python, Streamlit, Groq, Google Books API |
| `exercicio*.py` | Python, Groq, PLN |
| `testar_instalacao.py` | Python, requests, dotenv |

---

## 🎨 Fluxo de Uso

```
1. INSTALAÇÃO
   └─> pip install -r requirements.txt
   └─> Configurar .env

2. TESTE
   └─> python testar_instalacao.py

3. EXECUÇÃO
   ├─> streamlit run app_web.py    (Interface web)
   └─> python agente_literario.py  (Terminal)

4. DEMONSTRAÇÃO
   └─> Seguir ROTEIRO_APRESENTACAO.md
```

---

## 📦 Dependências (requirements.txt)

```
groq==0.9.0              # LLM (Llama 3) - IA conversacional
python-dotenv==1.0.0     # Gerenciar variáveis de ambiente
requests==2.31.0         # HTTP client (Google Books API)
streamlit==1.28.0        # Interface web
```

**Total:** 4 pacotes (todos gratuitos!)

---

## 🔐 Segurança

**NUNCA commitar:**
- `.env` (tem sua API key)
- `__pycache__/` (cache Python)

**Pode commitar:**
- `.env.example` (modelo sem chaves)
- Todo o resto

---

## 🎓 Para Entrega

### Documento obrigatório:
- Artigo baseado em `ARTIGO_BASE.md`
- Entregar no início da aula 07 (03/dez)

### Apresentação (15-25 min):
- Seguir `ROTEIRO_APRESENTACAO.md`
- Todos devem apresentar uma parte

### Código:
- Todo o repositório (exceto .env)
- Todos os 5 exercícios funcionando

---

## 💡 Dicas de Organização

1. **Testar HOJE:** `python testar_instalacao.py`
2. **Dividir tarefas:** Ver "Funções" no projeto
3. **Ensaiar apresentação:** Pelo menos 1x antes
4. **Backup:** Gravar vídeo da demo funcionando
5. **Artigo:** Começar pelo `ARTIGO_BASE.md`

---

## 🆘 Suporte

**Problemas técnicos:**
- Ler `INSTALACAO.md` (guia detalhado)
- Executar `testar_instalacao.py`
- Verificar `.env` configurado

**Dúvidas conceituais:**
- Ler `README.md` (visão geral)
- Ler `ARTIGO_BASE.md` (fundamentos)

**Apresentação:**
- Seguir `ROTEIRO_APRESENTACAO.md`
- Praticar com o grupo

---

**Criado com ❤️ para o projeto Agente Literário**
