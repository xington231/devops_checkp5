import re
def is_valid_name(name):
    pattern = r"^[A-Za-zА-Яа-яЁёs-]+$"
    return bool(re.match(pattern, name))
while True:
    try:
        name = input("Введите ваше имя: ").strip()
        if not name:
            print("Имя не может быть пустым. Пожалуйста, введите имя.")
            continue
        if not is_valid_name(name):
            print("Имя должно содержать только буквы, пробелы или дефисы. Попробуйте снова.")
            continue

        name = ' '.join(word.capitalize() for word in name.split())
        print(f"Привет, {name}!")
        break
    except KeyboardInterrupt:
        print("\nВыход из программы.")
        break
