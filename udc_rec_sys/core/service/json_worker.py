import json

# NOTE
# dump - записывает Python-объекты в файл JSON
# dumps - Сохраняет объект в виде строки с нотацией JSON
# load - Прочитывает файл JSON и возвращает его в виде объекта
# loads - Преобразует строку с нотацией JSON в объект


def get_object_from_json_file(*, json_file: str) -> dict:
    with open(json_file, 'r', encoding='utf-8') as f:
        json_dict = json.load(f)

    return json_dict


def get_json_object_as_string(*, json_object: dict) -> str:
    return json.dumps(json_object)


def get_json_string_as_object(*, json_string: str) -> dict:
    return json.loads(json_string)


def save_json_object_to_file(*, json_data: dict, file_path: str) -> None:
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)
