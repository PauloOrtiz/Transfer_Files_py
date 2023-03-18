# File Transfer Automator

File Transfer Automator é um projeto Python desenvolvido para automatizar a transferência de arquivos entre diretórios com base em parâmetros fornecidos através de um arquivo CSV.

## Características

- Transfere arquivos com base nos parâmetros fornecidos em um arquivo CSV
- Validação de caminhos e tipos de arquivos
- Registra as transferências de arquivos com sucesso e erros em arquivos de log diários
- Pode ser agendado para executar automaticamente no Windows usando o Agendador de Tarefas

## Requisitos

- Python 3.x

## Como usar

1. Clone este repositório ou faça o download dos arquivos do projeto.
2. Crie um arquivo CSV seguindo o formato de exemplo `transfer_params.csv`:
    ```
    origem,destino,tipo,message
    C:\caminho\para\pasta\origem,C:\caminho\para\pasta\destino,.txt,Transferência de arquivos de texto
    ```
3. Execute o script `main.py` com o caminho do arquivo CSV como argumento:
    ```
    python main.py transfer_params.csv
    ```
4. Verifique os arquivos de log na mesma pasta do script para obter informações sobre as transferências de arquivos.

## Agendando a execução no Windows

Para agendar a execução do script no Windows, siga estas etapas:

1. Crie um arquivo `.bat` para executar o script Python (consulte as instruções na seção de respostas acima).
2. Configure uma nova tarefa no Agendador de Tarefas do Windows para executar o arquivo `.bat` de acordo com o cronograma desejado.

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e correções de bugs. Todas as contribuições são bem-vindas!

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).