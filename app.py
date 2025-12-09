import requests # Importa a biblioteca para fazer pedidos na internet
import json     

def buscar_conselho():
    """
    Função que conecta na API e retorna um conselho aleatório.
    """
    # Endereço da API pública de conselhos
    url = "https://api.adviceslip.com/advice"

    try:
        # Faz o pedido para a URL como se fosse abrir um site
        resposta = requests.get(url)

        # Verifica se deu certo, o código 200 significa OK
        if resposta.status_code == 200:
            # Transforma o texto recebido em um dicionário Python
            dados = resposta.json()
            # Pega só a parte do conselho que está dentro de 'slip' -> 'advice'
            conselho = dados["slip"]["advice"]
            return conselho
        else:
            return "Ops, não consegui pegar um conselho agora."

    except Exception as erro:
        # Se acontecer qualquer outro erro, como sem internet, etc.
        return f"Erro na conexão: {erro}"

# --- INÍCIO DO PROGRAMA ---
if __name__ == "__main__":
    print("--- Gerador de Conselhos Aleatórios ---")
    print("Buscando um conselho para você...")
    print("---------------------------------------")

    # Chama a função e guarda o resultado
    conselho_do_dia = buscar_conselho()

    # Mostra o resultado na tela
    print(f"\n💡 Conselho: \"{conselho_do_dia}\"\n")
    print("---------------------------------------")
