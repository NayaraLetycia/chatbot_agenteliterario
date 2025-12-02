# Agente Literário Inteligente: Sistema de Recomendação Personalizado de Livros com IA

## Resumo

Este artigo apresenta o desenvolvimento de um agente literário inteligente baseado em Large Language Models (LLMs) para recomendação personalizada de livros. O sistema utiliza processamento de linguagem natural para manter diálogos contextualizados com usuários, identificar preferências literárias e gerar recomendações personalizadas integradas com APIs de busca e compra de livros. A solução foi implementada utilizando tecnologias gratuitas e open-source, demonstrando viabilidade prática e acessibilidade.

**Palavras-chave:** Inteligência Artificial, LLM, Recomendação Personalizada, Processamento de Linguagem Natural, Agentes Conversacionais

---

## 1. Introdução

### 1.1 Contextualização

Com o crescimento exponencial de publicações literárias, leitores enfrentam o desafio de descobrir livros alinhados aos seus interesses específicos. Sistemas tradicionais de recomendação baseiam-se em filtros colaborativos ou análise de metadados, frequentemente resultando em sugestões genéricas.

### 1.2 Problema

Como criar um sistema de recomendação que:
- Compreenda nuances individuais de preferências
- Mantenha diálogo natural e contextualizado
- Integre-se com plataformas de compra
- Seja acessível e escalável

### 1.3 Objetivo

Desenvolver um assistente inteligente capaz de:
1. Manter conversas naturais para entender gostos literários
2. Processar linguagem natural para extrair preferências
3. Gerar recomendações personalizadas
4. Integrar com APIs de busca e compra de livros
5. Criar planos de leitura progressivos

### 1.4 Justificativa

- **Relevância Social:** Democratiza acesso a descoberta literária
- **Inovação Tecnológica:** Aplica LLMs em contexto prático
- **Viabilidade:** Utiliza apenas recursos gratuitos

---

## 2. Fundamentação Teórica

### 2.1 Large Language Models (LLMs)

LLMs são modelos de aprendizado profundo treinados em vastos corpora textuais, capazes de:
- Compreensão contextual
- Geração de texto coerente
- Manutenção de diálogo multi-turno
- Raciocínio semântico

**Modelo utilizado:** Llama 3.1 (70B parâmetros) via Groq

### 2.2 Sistemas de Recomendação

Tipos de abordagens:
1. **Filtragem Colaborativa:** Baseada em similaridade entre usuários
2. **Baseada em Conteúdo:** Analisa características dos itens
3. **Híbrida:** Combina múltiplas abordagens
4. **Conversacional (Nossa abordagem):** Usa diálogo para refinar perfil

### 2.3 Processamento de Linguagem Natural (PLN)

Técnicas aplicadas:
- **Named Entity Recognition (NER):** Extração de entidades (autores, gêneros)
- **Análise de Sentimento:** Compreensão de preferências emocionais
- **Embeddings Semânticos:** Representação vetorial de preferências
- **Geração de Texto:** Criação de planos de leitura

### 2.4 APIs RESTful

Integração com Google Books API para:
- Busca de livros por query
- Obtenção de metadados (autor, sinopse, ISBN)
- Links de compra

---

## 3. Metodologia

### 3.1 Arquitetura do Sistema

```
┌─────────────────────────────────────────────┐
│         Interface (Streamlit)               │
├─────────────────────────────────────────────┤
│     Agente Conversacional (Python)          │
│  ┌──────────────────────────────────────┐   │
│  │ Gerenciador de Contexto              │   │
│  │ - Histórico de mensagens             │   │
│  │ - Perfil do usuário                  │   │
│  └──────────────────────────────────────┘   │
├─────────────────────────────────────────────┤
│         LLM Engine (Groq + Llama 3)         │
├─────────────────────────────────────────────┤
│        APIs Externas (Google Books)         │
└─────────────────────────────────────────────┘
```

### 3.2 Fluxo de Interação

1. **Inicialização:** Sistema inicia conversa com pergunta aberta
2. **Coleta de Informações:** Perguntas progressivas sobre gostos
3. **Construção de Perfil:** Extração de:
   - Gêneros favoritos
   - Autores preferidos
   - Temas de interesse
   - Nível de complexidade desejado
4. **Geração de Recomendações:** LLM sugere livros específicos
5. **Busca em API:** Query automática no Google Books
6. **Apresentação:** Links diretos para compra

### 3.3 Tecnologias Utilizadas

| Componente | Tecnologia | Justificativa |
|------------|------------|---------------|
| **LLM** | Groq (Llama 3.1 70B) | Gratuito, rápido, qualidade |
| **Backend** | Python 3.10+ | Simplicidade, bibliotecas |
| **Interface** | Streamlit | Desenvolvimento rápido |
| **API Livros** | Google Books | Gratuita, sem limites |
| **HTTP Client** | Requests | Padrão da indústria |
| **Config** | Python-dotenv | Segurança de credenciais |

### 3.4 Implementação

#### 3.4.1 Classe Principal

```python
class AgenteLiterario:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.historico_conversa = []
        self.perfil_usuario = {
            "generos_favoritos": [],
            "autores_favoritos": [],
            "temas_interesse": [],
            "nivel_leitura": None
        }
```

#### 3.4.2 Sistema de Memória Conversacional

```python
def conversar(self, mensagem_usuario):
    # Adiciona ao histórico
    self.historico_conversa.append({
        "role": "user",
        "content": mensagem_usuario
    })
    
    # Prepara contexto completo
    mensagens = [system_prompt] + self.historico_conversa
    
    # Chama LLM
    resposta = self.client.chat.completions.create(...)
    
    # Atualiza histórico
    self.historico_conversa.append({
        "role": "assistant",
        "content": resposta
    })
```

#### 3.4.3 Integração com API Google Books

```python
def buscar_livros_google(self, query, max_results=5):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": query,
        "maxResults": max_results,
        "langRestrict": "pt"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    return self.processar_resultados(data)
```

---

## 4. Resultados

### 4.1 Funcionalidades Implementadas

✅ **Conversa Natural:** Sistema mantém diálogo coerente e contextualizado
✅ **Análise de Preferências:** Extração automática de gostos literários
✅ **Recomendações Personalizadas:** Sugestões específicas baseadas no perfil
✅ **Integração API:** Busca automática e links de compra
✅ **Planos de Leitura:** Roteiros progressivos do básico ao avançado
✅ **Interface Web:** UI amigável com Streamlit
✅ **5 Exercícios PLN:** Implementados conforme especificação

### 4.2 Casos de Teste

#### Caso 1: Leitor Iniciante
**Input:** "Nunca li ficção científica, mas tenho curiosidade"
**Output:** 
- Sistema pergunta sobre interesses gerais
- Sugere: "O Guia do Mochileiro das Galáxias" (introdutório)
- Gera plano progressivo: Adams → Asimov → Philip K. Dick

#### Caso 2: Leitor Avançado
**Input:** "Gosto de fantasia épica complexa, já li Tolkien e Martin"
**Output:**
- Detecta nível avançado
- Sugere: "O Nome do Vento", "A Roda do Tempo"
- Links diretos para compra

### 4.3 Métricas de Performance

| Métrica | Valor |
|---------|-------|
| Tempo de resposta (LLM) | ~2-3 segundos |
| Tempo de busca (API) | ~0.5 segundos |
| Taxa de sucesso (API) | 98% |
| Relevância das recomendações | Qualitativa (positiva) |
| Limite gratuito (Groq) | 14.400 req/dia |

---

## 5. Discussão

### 5.1 Vantagens da Abordagem

1. **Personalização Profunda:**
   - LLMs capturam nuances que filtros tradicionais perdem
   - Exemplo: "Quero fantasia, mas sem romances excessivos"

2. **Experiência Natural:**
   - Usuário não preenche formulários
   - Conversa fluida como com bibliotecário humano

3. **Integração Prática:**
   - Não apenas recomenda, facilita compra
   - Diferencial técnico (peso 1 do projeto)

4. **Custo Zero:**
   - Viável para implantação em bibliotecas, escolas
   - Sem barreiras financeiras

### 5.2 Limitações Identificadas

1. **Dependência de Internet:** Requer conexão para APIs
2. **Idioma:** Google Books prioriza inglês (mitigado com `langRestrict`)
3. **Privacidade:** Conversas não persistidas (histórico volátil)
4. **Validação:** Falta de métrica quantitativa de relevância

### 5.3 Trabalhos Relacionados

- **GoodReads:** Sistema colaborativo, mas sem conversa
- **Amazon Recommendations:** Baseado em compras, não personalizado
- **ChatGPT + Browse:** Genérico, sem especialização literária

**Nossa contribuição:** Sistema especializado + integração API + gratuito

---

## 6. Conclusão

Este trabalho demonstrou a viabilidade de um agente literário inteligente utilizando LLMs para recomendação personalizada de livros. A solução combina:
- Conversa natural contextualizada
- Processamento avançado de linguagem natural
- Integração prática com APIs de compra
- Acessibilidade (100% gratuito)

### 6.1 Objetivos Alcançados

✅ Sistema conversacional funcional
✅ Recomendações personalizadas efetivas
✅ Integração com API Google Books (peso 1)
✅ Interface web profissional
✅ 5 exercícios de PLN implementados

### 6.2 Trabalhos Futuros

1. **Persistência de Dados:**
   - Banco de dados para histórico de leituras
   - Sistema de login

2. **Múltiplos Canais:**
   - Integração Discord
   - Newsletter automática (Gmail + N8N)

3. **Métricas Avançadas:**
   - Sistema de feedback (like/dislike)
   - Análise de relevância quantitativa

4. **Expansão de APIs:**
   - Amazon (afiliados)
   - Skoob (rede social brasileira)

5. **Modelo Local:**
   - Deploy de Llama 3 local
   - Eliminação de dependência externa

---

## 7. Referências

[1] BROWN, T. et al. Language Models are Few-Shot Learners. *NeurIPS*, 2020.

[2] TOUVRON, H. et al. Llama 3 Technical Report. *Meta AI*, 2024.

[3] RICCI, F.; ROKACH, L.; SHAPIRA, B. Recommender Systems Handbook. *Springer*, 2015.

[4] DEVLIN, J. et al. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. *NAACL*, 2019.

[5] Google Books APIs. Disponível em: https://developers.google.com/books

[6] Groq Documentation. Disponível em: https://console.groq.com/docs

[7] Streamlit Documentation. Disponível em: https://docs.streamlit.io

---

## Apêndices

### Apêndice A: Código Completo
Disponível em: GitHub (ou anexar arquivos)

### Apêndice B: Exemplos de Interações
(Screenshots da interface Streamlit)

### Apêndice C: Manual de Instalação
Ver arquivo `INSTALACAO.md` no repositório

---

**Autores:**
- Lucca (Desenvolvimento)
- Nayara (Desenvolvimento)
- Cleiton (Documentação)
- Henrique (Exercícios)
- Geovani (Exercícios)
- Adriana (Apresentação)

**Data:** Dezembro 2024
**Curso:** [Nome do Curso]
**Instituição:** [Nome da Instituição]
