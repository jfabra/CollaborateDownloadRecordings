import csv
import os

def sum_storage_usage(directory):
    total_storage = 0
    total_rows = 0
    all_rows = []

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        total_storage += float(row["StorageUsageGigabytes"])
                        total_rows += 1
                        all_rows.append(row)
                    except ValueError:
                        continue

    return total_rows, total_storage, all_rows

def split_and_save_rows(rows, output_directory, limit_gb):
    os.makedirs(output_directory, exist_ok=True)
    file_counter = 1
    current_gb = 0
    current_rows = []

    for row in rows:
        row_gb = float(row["StorageUsageGigabytes"])
        if current_gb + row_gb > limit_gb:
            save_rows_to_csv(current_rows, output_directory, file_counter)
            file_counter += 1
            current_gb = 0
            current_rows = []
        
        current_gb += row_gb
        current_rows.append(row)

    if current_rows:  # save remaining rows
        save_rows_to_csv(current_rows, output_directory, file_counter)

def save_rows_to_csv(rows, directory, counter):
    with open(os.path.join(directory, f'log_{counter}.csv'), 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        entry_count = 0
        total_gb = 0.0

        for row in reader:
            try:
                entry_count += 1
                total_gb += float(row["StorageUsageGigabytes"])
            except ValueError:
                continue

    return entry_count, total_gb

def analyze_directory(directory):
    results = []

    total_entries = 0
    total_gb = 0.0

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            entries, gb = analyze_file(file_path)
            total_entries += entries
            total_gb += gb
            results.append({
                'Filename': filename,
                'Entries': entries,
                'GB Total': gb
            })

    results.append({
        'Filename': 'TOTAL',
        'Entries': total_entries,
        'GB Total': total_gb
    })

    return results

def display_results(results):
    print("{:<30} {:<10} {:<15}".format('Filename', 'Entries', 'GB Total'))
    print('-' * 55)
    for result in results:
        print("{:<30} {:<10} {:<15.2f}".format(result['Filename'], result['Entries'], result['GB Total']))


rows_count, storage_sum, all_rows = sum_storage_usage('recording-logs')
print(f"Total rows processed: {rows_count}")
print(f"Total storage used (in gigabytes): {storage_sum:.2f} GB")

split_and_save_rows(all_rows, 'split-logs', 9)

results = analyze_directory('split-logs')
display_results(results)
