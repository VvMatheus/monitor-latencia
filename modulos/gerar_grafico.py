import pandas as pd
import matplotlib.pyplot as plt

def calcular_estatisticas(df):

    #Calcula estatísticas por URL

    estatisticas = {}
    urls = df['URL'].unique()

    for url in urls:
        dados_url = df[df['URL'] == url]
        total_falhas = dados_url[dados_url['Tempo_ms'] == "Erro"]
        dados_validos = dados_url[dados_url['Tempo_ms'] != "Erro"]

        if not dados_validos.empty:
            tempo_float = dados_validos['Tempo_ms'].astype(float)
            media = round(tempo_float.mean(), 2)
        else:
            media = "N/A"

        estatisticas[url] = {
            'Média (ms)': media,
            'Total de Testes': len(dados_url),
            'Falhas': len(total_falhas)
        }

    return estatisticas

def plotar_grafico(df, arquivo_csv):
    
    #Gera e exibe um gráfico de linha com a latência por URL ao longo do tempo.
    
    try:
        #apenas dados válidos (sem erro)
        df_valido = df[df['Tempo_ms'] != "Erro"].copy()
        df_valido['Tempo_ms'] = df_valido['Tempo_ms'].astype(float)

        if df_valido.empty:
            print("Nenhum dado válido no CSV para gerar o gráfico.")
            return

        #dados por horário para garantir gráfico correto
        df_valido = df_valido.sort_values("Horario")

        #gráfico
        plt.figure(figsize=(10, 6))
        for url in df_valido['URL'].unique():
            dados_url = df_valido[df_valido['URL'] == url]
            plt.plot(dados_url['Horario'], dados_url['Tempo_ms'], label=url, marker='o')

        plt.xlabel("Horário")
        plt.ylabel("Latência (ms)")
        plt.title("Histórico de Latência dos Sites")
        plt.legend(loc='upper right')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.margins(y=0.2)
        plt.tight_layout()
        plt.savefig("latencia_grafico.png")
        plt.show()
        print("Gráfico salvo como: latencia_grafico.png")

    except Exception as e:
        print(f"Erro ao gerar o gráfico: {e}")
