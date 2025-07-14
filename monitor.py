import time
import os
import pandas as pd
from modulos.medir_latencia import medir_tempo_acesso
from modulos.salvar_dados import salvar_dados
from modulos.gerar_grafico import plotar_grafico, calcular_estatisticas

# Configurações
INTERVALO = 5  # Intervalo entre testes (segundos)
ARQUIVO_CSV = "latencia_testes.csv"  # Nome do arquivo CSV
NUM_TESTES = 3  # Número de testes por URL

def monitorar_acessos():
    
    #Monitora o tempo de acesso a URLs fornecidas, registra os dados em um CSV,
    #calcula estatísticas e gera um gráfico com os resultados.
    print(f"Diretório de trabalho atual: {os.getcwd()}")
    urls = input("Digite as URLs para testar (separadas por vírgula): ").split(",")
    urls = [url.strip() for url in urls if url.strip()]

    if not urls:
        print("Nenhuma URL fornecida. Encerrando.")
        return

    print(f"\nMonitorando {len(urls)} URLs a cada {INTERVALO} segundos. Executando {NUM_TESTES} testes...\n")

    dados_totais = []

    try:
        for _ in range(NUM_TESTES):
            for url in urls:
                tempo, status = medir_tempo_acesso(url)
                horario = time.strftime("%Y-%m-%d %H:%M:%S")
                msg = f"[{horario}] {url}: "
                msg += f"Tempo de acesso: {tempo:.2f} ms | HTTP {status}" if tempo is not None else "Erro ao acessar o site."
                print(msg)
                dados_totais.append({
                    "horario": horario,
                    "url": url,
                    "tempo": tempo,
                    "status": status
                })
            time.sleep(INTERVALO)

        # Salva todos os dados de uma vez
        salvar_dados(dados_totais, ARQUIVO_CSV)
        print("\nTestes concluídos. Gerando gráfico e estatísticas...\n")

    except KeyboardInterrupt:
        print("\nMonitoramento interrompido pelo usuário.")
        return

    # Verifica se o arquivo foi salvo e gera estatísticas
    if not os.path.exists(ARQUIVO_CSV):
        print("Nenhum dado foi salvo. Finalizando.")
        return

    try:
        df = pd.read_csv(ARQUIVO_CSV, encoding='utf-8')

        estatisticas = calcular_estatisticas(df)
        print("Estatísticas dos testes:")
        for url, stats in estatisticas.items():
            print(f"\n{url}:")
            print(f"  Média (ms): {stats['Média (ms)']}")
            print(f"  Total de Testes: {stats['Total de Testes']}")
            print(f"  Falhas: {stats['Falhas']}")

        plotar_grafico(df, ARQUIVO_CSV)
        print(f"\nDados salvos em: {os.path.abspath(ARQUIVO_CSV)}")

    except Exception as e:
        print(f"Erro ao processar os dados: {e}")

if __name__ == "__main__":
    monitorar_acessos()
