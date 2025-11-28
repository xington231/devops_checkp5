import re
def is_valid_name(name):
    pattern = r"^[A-Za-zА-Яа-яЁёs'-]+$"
    return bool(re.match(pattern, name))
def normalize_name(name):
    name = re.sub(r's+', ' ', name.strip())
    def capitalize_part(part):
        return part[0].upper() + part[1:].lower() if part else ''

    words = []
    for word in name.split(' '):
        parts = re.split("([-'])", word)
        parts = [capitalize_part(part) if i % 2 == 0 else part for i, part in enumerate(parts)]
        words.append(''.join(parts))
    return ' '.join(words)
while True:
    try:
        name = input("Введите ваше имя: ")
        if not name.strip():
            print("Имя не может быть пустым. Пожалуйста, введите имя.")
            continue

        if len(name.strip()) < 2:
            print("Имя слишком короткое. Попробуйте снова.")
            continue

        if len(name.strip()) > 50:
            print("Имя слишком длинное. Попробуйте снова.")
            continue

        if not is_valid_name(name):
            print("Имя должно содержать только буквы, пробелы, дефисы или апострофы. Попробуйте снова.")
            continue

        name = normalize_name(name)
        print(f"Привет, {name}!")
        break
    except KeyboardInterrupt:
        print("\nВыход из программы.")
        break
