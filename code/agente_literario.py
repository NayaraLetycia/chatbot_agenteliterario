"""
Agente Literário Inteligente - Versão Terminal
Sistema de recomendação de livros usando IA
"""

import os
import json
import requests
from groq import Groq
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

class AgenteLiterario:
    def __init__(self):
        """Inicializa o agente com LLM e APIs"""
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.historico_conversa = []
        self.perfil_usuario = {
            "generos_favoritos": [],
            "autores_favoritos": [],
            "temas_interesse": [],
            "nivel_leitura": None
        }
        
    def buscar_livros_google(self, query, max_results=5):
        """Busca livros na API gratuita do Google Books"""
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": query,
            "maxResults": max_results,
            "langRestrict": "pt",  
            "orderBy": "relevance"
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            livros = []
            for item in data.get("items", []):
                info = item.get("volumeInfo", {})
                livros.append({
                    "titulo": info.get("title", "Título desconhecido"),
                    "autores": ", ".join(info.get("authors", ["Autor desconhecido"])),
                    "descricao": info.get("description", "Sem descrição")[:200] + "...",
                    "link": info.get("infoLink", "#"),
                    "imagem": info.get("imageLinks", {}).get("thumbnail", "")
                })
            return livros
        except Exception as e:
            print(f"Erro ao buscar livros: {e}")
            return []
    
    def conversar(self, mensagem_usuario):
        """Mantém conversa com o usuário usando LLM"""
        
        self.historico_conversa.append({
            "role": "user",
            "content": mensagem_usuario
        })
        
       
        system_prompt = """Você é um agente literário especialista em recomendar livros.
        
Seu objetivo é:
1. Fazer perguntas para entender os gostos do usuário
2. Identificar gêneros, autores e temas de interesse
3. Recomendar livros específicos baseado nas preferências
4. Criar planos de leitura progressivos

Seja conversacional, amigável e faça perguntas específicas.
Quando tiver informações suficientes, sugira livros reais e populares.

Use este formato quando for recomendar:
RECOMENDAÇÃO: [nome do livro] por [autor]"""

        
        mensagens = [
            {"role": "system", "content": system_prompt}
        ] + self.historico_conversa
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=mensagens,
                model="llama-3.3-70b-versatile", 
                temperature=0.7,
                max_tokens=1000
            )
            
            resposta = chat_completion.choices[0].message.content
            
            self.historico_conversa.append({
                "role": "assistant",
                "content": resposta
            })
            
            return resposta
            
        except Exception as e:
            return f"Erro ao processar: {e}"
    
    def extrair_recomendacoes(self, texto):
        """Extrai nomes de livros do texto da conversa"""
        livros_mencionados = []
        linhas = texto.split('\n')
        
        for linha in linhas:
            if 'RECOMENDAÇÃO:' in linha or 'recomendo' in linha.lower():
                # Tenta extrair título e autor
                livros_mencionados.append(linha)
        
        return livros_mencionados
    
    def gerar_plano_leitura(self):
        """Gera um plano de leitura baseado no histórico"""
        prompt = f"""Baseado na nossa conversa, crie um plano de leitura progressivo 
        com 5 livros específicos (títulos e autores reais), do mais fácil ao mais complexo.
        
        Formato:
        1. [Título] - [Autor] - [Motivo]
        2. [Título] - [Autor] - [Motivo]
        ..."""
        
        return self.conversar(prompt)


def main():
    """Função principal - Interface de terminal"""
    print("=" * 60)
    print("📚 AGENTE LITERÁRIO INTELIGENTE")
    print("=" * 60)
    print("\nOlá! Sou seu assistente de recomendação de livros.")
    print("Vou fazer algumas perguntas para conhecer seus gostos.\n")
    print("Digite 'sair' para encerrar")
    print("Digite 'buscar: [termo]' para buscar livros no Google Books")
    print("Digite 'plano' para gerar um plano de leitura completo")
    print("-" * 60)
    
    agente = AgenteLiterario()
    
    
    resposta_inicial = agente.conversar("Olá! Quero recomendações de livros.")
    print(f"\n🤖 Agente: {resposta_inicial}\n")
    
    while True:
        
        entrada = input("👤 Você: ").strip()
        
        if not entrada:
            continue
            
        if entrada.lower() == 'sair':
            print("\n👋 Até logo! Boas leituras!\n")
            break
        
       
        if entrada.lower().startswith('buscar:'):
            termo = entrada.split(':', 1)[1].strip()
            print(f"\n🔍 Buscando '{termo}' no Google Books...\n")
            livros = agente.buscar_livros_google(termo)
            
            if livros:
                for i, livro in enumerate(livros, 1):
                    print(f"{i}. {livro['titulo']}")
                    print(f"   Autor(es): {livro['autores']}")
                    print(f"   Link: {livro['link']}")
                    print()
            else:
                print("Nenhum livro encontrado.\n")
            continue
        
        
        if entrada.lower() == 'plano':
            print("\n📋 Gerando seu plano de leitura personalizado...\n")
            plano = agente.gerar_plano_leitura()
            print(f"🤖 Agente:\n{plano}\n")
            continue
        
        
        resposta = agente.conversar(entrada)
        print(f"\n🤖 Agente: {resposta}\n")
        
        
        if 'RECOMENDAÇÃO:' in resposta or 'recomendo' in resposta.lower():
            recomendacoes = agente.extrair_recomendacoes(resposta)
            if recomendacoes:
                print("📖 Buscando links de compra...\n")
               
                primeiro_livro = recomendacoes[0].split('RECOMENDAÇÃO:')[-1].strip()
                livros = agente.buscar_livros_google(primeiro_livro, max_results=3)
                
                if livros:
                    print("🔗 Onde comprar:")
                    for livro in livros[:3]:
                        print(f"   • {livro['titulo']} - {livro['link']}")
                    print()


if __name__ == "__main__":
    main()


