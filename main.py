from file_manager import FileTransfer

origem = origem = "C:\\Users\\porti\\OneDrive\\Documentos\\Estudo\\Python\\transfer Files Python\\Transfer_Files_py\\Origem\\"
tipoDeArquivo = "*.txt"
destino = "C:\\Users\\porti\\OneDrive\\Documentos\\Estudo\Python\\transfer Files Python\\Transfer_Files_py\\Destino\\"

newFile = FileTransfer(origem, destino, tipoDeArquivo)

newFile.transfer_files()

