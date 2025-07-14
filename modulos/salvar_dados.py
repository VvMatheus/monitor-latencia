import os
import csv

def salvar_dados(dados, arquivo_csv):
    # se o arquivo nao existir, crie e escreva o cabecalho
    if not os.path.isfile(arquivo_csv):
        with open(arquivo_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Horario", "URL", "Tempo_ms", "Status_HTTP"])

    # abra para acrescentar os dados
    with open(arquivo_csv, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for dado in dados:
            horario = dado.get("horario", "N/A")
            url = dado.get("url", "N/A")
            tempo = dado.get("tempo", "Erro") if dado.get("tempo") is not None else "Erro"
            status = dado.get("status", "Erro") if dado.get("status") is not None else "Erro"

            writer.writerow([horario, url, tempo, status])
