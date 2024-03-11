import csv
import os

def process_csv(file_path):
    total_storage = 0
    row_count = 0

    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                total_storage += float(row["StorageUsageGigabytes"])
                row_count += 1
            except ValueError:  # En caso de que no pueda convertir el valor a float
                print(f"Warning: Found an invalid value in file {file_path}. Skipping...")
                continue

    return total_storage, row_count

def main():
    directory = "recording-logs"
    total_storage_global = 0
    total_rows_global = 0

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            total_storage, total_rows = process_csv(file_path)
            total_storage_global += total_storage
            total_rows_global += total_rows

    print(f"Total rows processed: {total_rows_global}")
    print(f"Total storage (in GB): {total_storage_global:.2f}")

if __name__ == "__main__":
    main()


