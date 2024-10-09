import pandas as pd
import os
import random
from tqdm import tqdm


# Створення папки для збереження файлів
file_name = 'baza_gen_phone'
os.makedirs(file_name, exist_ok=True)


# Функція для генерації всіх можливих комбінацій номерів телефонів для заданого префіксу
def generate_all_phone_numbers(prefix):
    numbers = [f"+{prefix}{str(num).zfill(7)}" for num in tqdm(range(10000000), desc=f"Генерація для {prefix}")]
    return numbers

# Вхідні дані
prefixes = ['38067', '38096', '38097', '38098', '38050', '38099']

# Генерація і перемішування номерів
all_numbers = []
total_numbers = len(prefixes) * 10000000
with tqdm(total=total_numbers, desc="Прогрес генерації номерів") as pbar:
    for prefix in prefixes:
        numbers = generate_all_phone_numbers(prefix)
        all_numbers.extend(numbers)
        pbar.update(len(numbers))

print(f"Перемішування номерів...")
random.shuffle(all_numbers)

print(f"Збереження всіх номерів в один текстовий файл для історії...")
history_txt_file = f'{file_name}/{file_name}_history.txt'
with open(history_txt_file, 'w', encoding='utf-8') as file:
    for number in all_numbers:
        file.write(number + '\n')

print(f"Всі номери збережено в {history_txt_file} ({total_numbers}шт)")

# Розбивка на частини по 1 мільйону і збереження в окремі текстові файли
max_rows_per_patch = 1000000
chunks = [all_numbers[i:i + max_rows_per_patch] for i in range(0, len(all_numbers), max_rows_per_patch)]


# Максимальна кількість рядків на один файл
max_rows_per_file = 100000

# Збереження частин у текстові файли
for i, chunk in enumerate(tqdm(chunks, desc="Збереження частин у текстові файли")):
    chunk_txt_patch = f'{file_name}/{file_name}_{i + 1}'
    
    os.makedirs(chunk_txt_patch, exist_ok=True)
        
    # Розбивка даних на частини по max_rows_per_file рядків
    chunksX = [chunk[j:j + max_rows_per_file] for j in range(0, len(chunk), max_rows_per_file)]

    # Збереження кожного чанка в окремий файл
    for j, chunkX in enumerate(chunksX):
        chunk_txt_file = f'{chunk_txt_patch}/{file_name}_{j + 1}.txt'
        with open(chunk_txt_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(number for number in chunkX if number.strip()))
