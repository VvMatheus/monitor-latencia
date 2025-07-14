#📡 Monitor de Latência de Sites
Este projeto mede quanto tempo (latência) um site demora para responder.  
Ele salva esses tempos em um arquivo e também cria um gráfico mostrando essa informação ao longo do tempo.  
Além disso, mostra no console estatísticas como a média da latência, quantos testes foram feitos e quantos falharam.

##Ajuda a responder perguntas como:
"Meu site está respondendo rápido?"
"A latência da minha internet está estável?"
"Alguma URL está fora do ar ou demorando para responder?"
"Qual serviço tem melhor desempenho: Google, Bing ou DuckDuckGo?"


#Funcionalidades
- Mede o tempo de resposta das URLs que você escolher a cada 5 segundos.
- Salva os resultados em um arquivo chamado 'latencia_testes.csv'.
- Mostra no console:
  - A média dos tempos medidos.
  - Quantos testes foram feitos.
  - Quantos testes deram erro.
- Cria um gráfico ('latencia_grafico.png') mostrando a latência ao longo do tempo.

#Pré-requisitos
Para rodar o programa, você precisa ter:
- Python 3.6 ou superior instalado.
- As bibliotecas: requests, pandas, matplotlib

#Como Usar
##1.Baixe ou clone o projeto do GitHub.
##2.Entre na pasta do projeto:
  cd monitor-latencia
##3.Instale as dependências:
  pip install -r requirements.txt
##4.Execute o programa:
  python monitor.py
##5.Digite as URLs separadas por vírgula quando o programa pedir.

#Saídas do Programa
Console: tempo de resposta e estatísticas (média, total de testes, falhas).
latencia_testes.csv: dados brutos (horário, URL, tempo, status).
latencia_grafico.png: gráfico de linha mostrando a latência ao longo do tempo.

#Estrutura do Projeto
  monitor-latencia/
  monitor.py               # Script principal
  requirements.txt         # Bibliotecas necessárias
  README.md                # Instruções e documentação
  .gitignore               # Arquivos ignorados pelo Git
  modulos/                 # Módulos do projeto
    medir_latencia.py    # Mede o tempo de acesso às URLs
    salvar_dados.py      # Salva os dados no CSV
    gerar_grafico.py     # Gera o gráfico e estatísticas

#Configurações
Intervalo entre testes: 5 segundos
Número de testes por URL: 3
Arquivos gerados: latencia_testes.csv e latencia_grafico.png

#🧪 Exemplo de Saída
    [2025-07-10 20:01:00] https://www.google.com: Tempo de acesso: 538.63 ms | HTTP 200
    [2025-07-10 20:01:05] https://www.google.com: Tempo de acesso: 407.16 ms | HTTP 200
    [2025-07-10 20:01:10] https://www.google.com: Tempo de acesso: 377.50 ms | HTTP 200
    
    Estatísticas dos testes:
    https://www.google.com:
      Média (ms): 441.1
      Total de Testes: 3
      Falhas: 0
      
    Gráfico salvo como: latencia_grafico.png

#Dica
Se quiser apagar os dados e começar do zero, exclua os arquivos:
  latencia_testes.csv
  latencia_grafico.png

