Monitor de Latência de Sites
Este projeto monitora o tempo de resposta (latência) de sites, salva os resultados em um arquivo CSV e gera um gráfico de linha com o histórico de latência. As estatísticas (média, total de testes e falhas) são exibidas no console.
Funcionalidades

Mede a latência de URLs (em milissegundos) a cada 5 segundos.
Salva os dados em latencia_testes.csv.
Exibe no console: média de latência, total de testes e número de falhas.
Gera um gráfico de linha limpo em latencia_grafico.png.

Pré-requisitos

Python 3.6 ou superior
Bibliotecas: requests, pandas, matplotlib
Instale as dependências com: pip install -r requirements.txt



Como Usar

Clone o repositório:git clone https://github.com/SEU_USUARIO/monitor-latencia.git
cd monitor-latencia


Instale as dependências:pip install -r requirements.txt


Execute o programa:python monitor.py


Insira as URLs para testar (ex. https://www.google.com,https://www.example.com), separadas por vírgula.
Veja os resultados:
Console: Latências por teste e estatísticas (média, total de testes, falhas).
Arquivos:
latencia_testes.csv: Dados brutos (horário, URL, tempo, status HTTP).
latencia_grafico.png: Gráfico de linha com histórico de latência.





Estrutura do Projeto

monitor.py: Script principal que coordena o monitoramento, salvamento e geração de gráficos.
  modulos/
  medir_latencia.py: Mede o tempo de acesso às URLs.
  salvar_dados.py: Salva os dados no arquivo CSV.
  gerar_grafico.py: Gera o gráfico de linha e calcula estatísticas.



Configurações

Intervalo entre testes: 5 segundos
Número de testes por URL: 3
Saídas: latencia_testes.csv, latencia_grafico.png

Exemplo de Saída
Ao executar python monitor.py e inserir https://www.google.com:
Diretório de trabalho atual: C:\Users\verda\monitor-latencia
Digite as URLs para testar (separadas por vírgula): https://www.google.com
Monitorando 1 URLs a cada 5 segundos. Executando 3 testes.
[2025-07-13 20:01:00] https://www.google.com: Tempo de acesso: 538.63 ms | HTTP 200
[2025-07-13 20:01:05] https://www.google.com: Tempo de acesso: 407.16 ms | HTTP 200
[2025-07-13 20:01:10] https://www.google.com: Tempo de acesso: 377.50 ms | HTTP 200
Testes concluídos. Gerando gráfico...

Estatísticas dos testes:
https://www.google.com:
  Média (ms): 441.1
  Total de Testes: 3
  Falhas: 0

Gráfico salvo como: latencia_grafico.png
Dados salvos em: C:\Users\x\monitor-latencia\latencia_testes.csv