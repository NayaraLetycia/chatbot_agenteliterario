# 🎤 Roteiro de Apresentação

## ⏱️ Tempo: 15-25 minutos

---

## 1️⃣ Introdução (2 min)
**[Adriana]**

> "Olá! Nosso grupo desenvolveu um **Agente Literário Inteligente** que resolve um problema real: **como descobrir livros que realmente combinam com você?**"

### Problema que resolvemos:
- Milhares de livros disponíveis
- Difícil escolher o próximo livro
- Recomendações genéricas de sites
- Falta de personalização

### Nossa solução:
- Conversa natural com IA
- Entende seus gostos específicos
- Busca livros reais
- Gera planos de leitura

---

## 2️⃣ Arquitetura e Tecnologias (3 min)
**[Lucca]**

### Tecnologias Escolhidas (100% GRATUITAS! 🎉)

```
┌─────────────────────────────────────┐
│  Interface (Streamlit)              │
├─────────────────────────────────────┤
│  Agente IA (Groq + Llama 3)        │
├─────────────────────────────────────┤
│  API Google Books (busca livros)    │
└─────────────────────────────────────┘
```

**Por que essas escolhas?**
- **Groq**: LLM gratuito, rápido (30 req/min)
- **Google Books API**: Gratuita, sem limite
- **Streamlit**: Interface web em minutos
- **Python**: Simplicidade e poder

---

## 3️⃣ Demonstração ao Vivo (8-10 min)
**[Nayara]**

### 🎬 Cenário Real

**Execute:**
```powershell
streamlit run app_web.py
```

### Script de Demonstração:

1. **Primeira pergunta do agente:**
   - Mostra que ele inicia a conversa

2. **Responda como usuário:**
   > "Gosto de fantasia medieval, já li Harry Potter e Senhor dos Anéis"

3. **Agente pergunta mais:**
   - Mostra que ele aprofunda para entender

4. **Continue:**
   > "Prefiro histórias com sistemas de magia complexos"

5. **Recomendação:**
   - Agente sugere livros específicos
   - **DEMONSTRE:** Links aparecem automaticamente!

6. **Plano de Leitura:**
   - Clique em "Gerar Plano de Leitura"
   - Mostra progressão do mais fácil ao mais complexo

7. **Busca Manual:**
   - Use sidebar: buscar "Brandon Sanderson"
   - Mostra integração com Google Books

---

## 4️⃣ Código Fonte - Explicação (5 min)
**[Lucca e Nayara]**

### Arquivos Principais:

#### `agente_literario.py` - O Cérebro
```python
class AgenteLiterario:
    def conversar(self, mensagem):
        # 1. Mantém histórico da conversa
        self.historico_conversa.append(mensagem)
        
        # 2. Envia para LLM com contexto
        resposta = self.client.chat.completions.create(...)
        
        # 3. Retorna resposta contextualizada
        return resposta
```

**Destaque:** Sistema de memória conversacional

#### Busca de Livros
```python
def buscar_livros_google(self, query):
    # Chama API do Google Books
    response = requests.get(
        "https://www.googleapis.com/books/v1/volumes",
        params={"q": query}
    )
    # Extrai informações relevantes
    return livros_formatados
```

**Destaque:** Integração API para compra (requisito peso 1)

---

## 5️⃣ Diferenciais Técnicos (3 min)
**[Henrique/Geovani]**

### ✨ Peso 9: Sistema de Recomendação

1. **Conversa Natural:**
   - Não é formulário, é diálogo
   - LLM entende contexto e nuances

2. **Perfil Progressivo:**
   - Aprende com cada resposta
   - Refina recomendações continuamente

3. **Planos de Leitura:**
   - Não só recomenda, cria jornada
   - Do iniciante ao avançado

### 💎 Peso 1: API de Compra

- Processamento NLP → Busca automática
- Links diretos para Google Books
- Cada recomendação vira link clicável

---

## 6️⃣ Exercícios Implementados (2 min)
**[Henrique/Geovani]**

### Demonstração Rápida de 1 Exercício:

```powershell
python exercicios/exercicio5_agente_virtual.py
```

**Fale:** "Implementamos os 5 exercícios solicitados:"

1. ✅ Análise de Sentimentos - avalia se resenha é positiva/negativa
2. ✅ Identificação de Entidades - extrai nomes, lugares
3. ✅ Geração de Texto - cria sinopses, resenhas
4. ✅ Resolução de Problemas - responde perguntas sobre livros
5. ✅ Agente Virtual - conversa com contexto (base do projeto)

---

## 7️⃣ Casos de Uso Reais (2 min)
**[Adriana]**

### Quem pode usar?

1. **Leitores iniciantes:**
   - Não sabem por onde começar
   - Agente guia do básico ao avançado

2. **Clubes de leitura:**
   - Sugestões para próxima reunião
   - Considera preferências do grupo

3. **Estudantes:**
   - Busca livros por tema acadêmico
   - Relaciona com área de estudo

4. **Bibliotecas:**
   - Atendimento automatizado
   - Disponível 24/7

---

## 8️⃣ Conclusão e Melhorias Futuras (2 min)
**[Todos]**

### O que conseguimos:
✅ Sistema funcional e prático
✅ 100% gratuito
✅ Interface web profissional
✅ Integração com APIs reais
✅ Todos os exercícios implementados

### Possíveis expansões:
- 📧 Newsletter automática (Gmail/N8N)
- 💬 Integração Discord
- 📊 Dashboard de leituras
- 🤝 Compartilhamento social
- 📱 App mobile

---

## 9️⃣ Sabatina - Perguntas Esperadas

**P: Por que não usaram ChatGPT?**
> R: Groq é gratuito sem limites restritivos, ideal para desenvolvimento e demonstração.

**P: Como funciona a memória do agente?**
> R: Mantemos histórico de mensagens e passamos para o LLM a cada interação, criando contexto contínuo.

**P: E se a API cair?**
> R: Google Books é extremamente estável. Groq tem fallback automático entre modelos.

**P: Quanto custaria em produção?**
> R: Groq gratuito até 14.400 req/dia. Para escala, migrar para OpenAI (~$0.002/req) ou auto-hospedar Llama.

**P: Como validam as recomendações?**
> R: LLM treinado em vasta literatura. Busca confirma existência do livro via Google Books.

---

## 📋 Checklist Antes da Apresentação

- [ ] Teste completo da demo 3x
- [ ] API Key funcionando
- [ ] Internet estável
- [ ] Streamlit abre no navegador
- [ ] Prepare 2-3 cenários de demonstração
- [ ] Todos sabem sua parte
- [ ] Cronometraram? (15-25min)
- [ ] Documento/artigo entregue

---

## 🎯 Dica Final

**Grave um vídeo de backup da demonstração!**
Se a internet falhar, você tem o vídeo.

**Boa sorte! 🚀📚**
