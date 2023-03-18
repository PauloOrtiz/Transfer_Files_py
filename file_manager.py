import glob
import shutil
import logging
import os
from datetime import datetime 

class FileTransfer:
    def __init__(self, source_path, destination_path, file_type, message):
        self._source_path = source_path
        self._destination_path = destination_path
        self._file_type = file_type
        self._message = message

        current_date = datetime.now().strftime("%Y-%m-%d")
        logging.basicConfig(filename= current_date, level=logging.INFO,
                            format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S')

        self.validate_paths()
        self.validate_file_type()

    def validate_paths(self):
        if not os.path.exists(self._source_path) or not os.path.isdir(self._source_path):
            raise ValueError(f"Caminho de origem inválido: {self._source_path}")

        if not os.path.exists(self._destination_path) or not os.path.isdir(self._destination_path):
            raise ValueError(f"Caminho de destino inválido: {self._destination_path}")

    def validate_file_type(self):
        if not self._file_type.startswith('.'):
            raise ValueError(f"Tipo de arquivo inválido: {self._file_type}")

    def find_files(self):
        search_pattern = os.path.join(self._source_path, self._file_type)
        return glob.glob(search_pattern)

    def transfer_files(self):
        try:
            list_files = self.find_files()

            for file in list_files:
                destination_file = os.path.join(self._destination_path, os.path.basename(file))
                shutil.move(file, destination_file)

                if os.path.exists(destination_file):
                    self.create_log(file, destination_file, self._message)
                else:
                    logging.error(f"Falha ao mover o arquivo {file} para {destination_file}")

        except Exception as e:
            logging.error(str(e))
            raise


    def create_log(self, file, destination, message):
        log_message = "Transferencia realizada do arquivo {} para {} referente a ".format(file, destination)
        logging.info(log_message)

    

