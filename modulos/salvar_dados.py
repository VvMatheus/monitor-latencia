import os
import csv

def salvar_dados(dados, arquivo_csv):
    
    #Salva os dados de monitoramento no arquivo CSV.

    arquivo_existe = os.path.isfile(arquivo_csv)

    with open(arquivo_csv, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Escreve o cabeçalho apenas se o arquivo ainda não existe
        if not arquivo_existe:
            writer.writerow(["Horario", "URL", "Tempo_ms", "Status_HTTP"])

        # Escreve os dados
        for dado in dados:
            horario = dado.get("horario", "N/A")
            url = dado.get("url", "N/A")
            tempo = dado.get("tempo", "Erro") if dado.get("tempo") is not None else "Erro"
            status = dado.get("status", "Erro") if dado.get("status") is not None else "Erro"

            writer.writerow([horario, url, tempo, status])
