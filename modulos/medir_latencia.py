import requests
import time

def medir_tempo_acesso(url):
    
    #Mede o tempo de resposta de uma URL em milissegundos.

    try:
        inicio = time.perf_counter()
        resposta = requests.get(url, timeout=10)
        fim = time.perf_counter()
        tempo_ms = (fim - inicio) * 1000  # Converte para milissegundos
        return tempo_ms, resposta.status_code
    except requests.RequestException:
        return None, None
