import argparse
from file_manager import FileTransfer
from transfer_params import read_transfer_params

import argparse
from file_manager import FileTransfer
from transfer_params import read_transfer_params

def main(params_file):
    transfer_params_list = read_transfer_params(params_file)

    for params in transfer_params_list:
        source_path = params['origem']
        destination_path = params['destino']
        file_type = params['tipo']
        message = params['message']

        file_transfer = FileTransfer(source_path, destination_path, file_type, message)
        file_transfer.transfer_files()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script de transferência de arquivos com base em parâmetros do arquivo CSV")
    parser.add_argument("csv_path", help="Caminho para o arquivo CSV contendo os parâmetros de transferência")

    args = parser.parse_args()
    main(args.csv_path)


