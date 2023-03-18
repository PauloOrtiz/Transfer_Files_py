import csv

def read_transfer_params(file_path):
    transfer_params = []

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            transfer_params.append(row)

    return transfer_params
