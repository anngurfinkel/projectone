import json
import logging
import os
from pathlib import Path
import time

# int(time.time()) UNIX-час

# Унікальне імя лог-файлу для os
os_log_file = f'json/json_instructor_os_{int(time.time())}.log'


# Налаштування логера для os
logging.basicConfig(
    filename=os_log_file,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
os_logger = logging.getLogger("os_logger")

# Перевірка валідності JSON-файлів за допомогою os
json_folder = "json"  # Папка з JSON-файлами
for filename in os.listdir(json_folder):
    if filename.endswith(".json"):
        filepath = os.path.join(json_folder, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as json_file:
                json.load(json_file)  # Спроба завантажити JSON
        except json.JSONDecodeError as e:
            os_logger.error(f"Файл {filename} не є валідним JSON: {e}")

time.sleep(1)

# Унікальне імя лог-файлу для os і pathlib
pathlib_log_file = f'json/json_instructor_pathlib_{int(time.time())}.log'

# Налаштування логера для pathlib
logging.basicConfig(
    filename=pathlib_log_file,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
pathlib_logger = logging.getLogger("pathlib_logger")

# Перевірка валідності JSON-файлів за допомогою pathlib
json_folder_path = Path(json_folder)
for file in json_folder_path.glob("*.json"):
    try:
        with file.open('r', encoding='utf-8') as json_file:
            json.load(json_file)  # Спроба завантажити JSON
    except json.JSONDecodeError as e:
        pathlib_logger.error(f"Файл {file.name} не є валідним JSON: {e}")

print(f"Перевірка завершена. Результати для os у файлі {os_log_file}, для pathlib у файлі {pathlib_log_file}.")
