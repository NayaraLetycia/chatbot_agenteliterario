"""
Script de Teste - Verifica se tudo está configurado corretamente
Execute este arquivo para validar a instalação antes da apresentação!
"""

import sys
import os

def print_status(mensagem, sucesso=True):
    """Imprime status colorido"""
    simbolo = "✅" if sucesso else "❌"
    print(f"{simbolo} {mensagem}")

def testar_instalacao():
    """Testa todos os componentes do projeto"""
    print("=" * 70)
    print("🔍 TESTE DE INSTALAÇÃO - AGENTE LITERÁRIO")
    print("=" * 70)
    print()
    
    # 1. Testar Python
    print("1️⃣  Verificando Python...")
    versao = sys.version_info
    if versao.major >= 3 and versao.minor >= 10:
        print_status(f"Python {versao.major}.{versao.minor}.{versao.micro} instalado")
    else:
        print_status(f"Python {versao.major}.{versao.minor} - RECOMENDADO: 3.10+", False)
    print()
    
    # 2. Testar módulos
    print("2️⃣  Verificando dependências...")
    modulos = {
        "groq": "Groq (LLM)",
        "dotenv": "Python-dotenv (variáveis de ambiente)",
        "requests": "Requests (HTTP)",
        "streamlit": "Streamlit (interface web)"
    }
    
    modulos_faltando = []
    for modulo, nome in modulos.items():
        try:
            if modulo == "dotenv":
                __import__("dotenv")
            else:
                __import__(modulo)
            print_status(f"{nome} instalado")
        except ImportError:
            print_status(f"{nome} NÃO instalado", False)
            modulos_faltando.append(modulo)
    print()
    
    # 3. Testar .env
    print("3️⃣  Verificando configuração...")
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("GROQ_API_KEY")
    if api_key and api_key != "sua_chave_aqui":
        print_status("Arquivo .env configurado")
        print(f"   API Key: {api_key[:10]}...{api_key[-4:]}")
    else:
        print_status("Arquivo .env NÃO configurado ou chave inválida", False)
        print("   👉 Crie o arquivo .env e adicione: GROQ_API_KEY=sua_chave")
    print()
    
    # 4. Testar API Groq
    if api_key and api_key != "sua_chave_aqui":
        print("4️⃣  Testando conexão com Groq API...")
        try:
            from groq import Groq
            client = Groq(api_key=api_key)
            
            # Teste simples
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": "Diga apenas 'OK'"}],
                model="llama-3.1-70b-versatile",
                max_tokens=10
            )
            
            print_status("Groq API funcionando!")
            print(f"   Resposta: {response.choices[0].message.content}")
        except Exception as e:
            print_status(f"Erro ao conectar com Groq: {e}", False)
    else:
        print("4️⃣  Testando Groq API... PULADO (configure .env primeiro)")
    print()
    
    # 5. Testar Google Books
    print("5️⃣  Testando Google Books API...")
    try:
        import requests
        response = requests.get(
            "https://www.googleapis.com/books/v1/volumes",
            params={"q": "Harry Potter", "maxResults": 1},
            timeout=5
        )
        
        if response.status_code == 200:
            data = response.json()
            if "items" in data:
                livro = data["items"][0]["volumeInfo"]["title"]
                print_status("Google Books API funcionando!")
                print(f"   Teste: Encontrado '{livro}'")
            else:
                print_status("Google Books retornou vazio", False)
        else:
            print_status(f"Erro HTTP {response.status_code}", False)
    except Exception as e:
        print_status(f"Erro ao testar Google Books: {e}", False)
    print()
    
    # 6. Testar arquivos principais
    print("6️⃣  Verificando arquivos do projeto...")
    arquivos = [
        "agente_literario.py",
        "app_web.py",
        "requirements.txt",
        "exercicios/exercicio1_sentimentos.py",
        "exercicios/exercicio2_entidades.py",
        "exercicios/exercicio3_geracao_texto.py",
        "exercicios/exercicio4_resolucao_problemas.py",
        "exercicios/exercicio5_agente_virtual.py"
    ]
    
    for arquivo in arquivos:
        if os.path.exists(arquivo):
            print_status(f"{arquivo}")
        else:
            print_status(f"{arquivo} NÃO encontrado", False)
    print()
    
    # Resumo final
    print("=" * 70)
    print("📊 RESUMO")
    print("=" * 70)
    
    if modulos_faltando:
        print("\n❌ Ação necessária:")
        print(f"   Instale: pip install {' '.join(modulos_faltando)}")
    
    if not api_key or api_key == "sua_chave_aqui":
        print("\n❌ Ação necessária:")
        print("   1. Acesse: https://console.groq.com")
        print("   2. Crie conta gratuita")
        print("   3. Copie API Key")
        print("   4. Adicione ao arquivo .env")
    
    if not modulos_faltando and api_key and api_key != "sua_chave_aqui":
        print("\n✅ TUDO PRONTO PARA A APRESENTAÇÃO! 🎉")
        print("\n🚀 Próximos passos:")
        print("   - Versão terminal: python agente_literario.py")
        print("   - Versão web:      streamlit run app_web.py")
        print("   - Testar exercícios: python exercicios/exercicio1_sentimentos.py")
    
    print("\n" + "=" * 70)


if __name__ == "__main__":
    try:
        testar_instalacao()
    except KeyboardInterrupt:
        print("\n\n⚠️  Teste interrompido pelo usuário")
    except Exception as e:
        print(f"\n\n❌ Erro inesperado: {e}")
        print("Entre em contato com o time de desenvolvimento!")
