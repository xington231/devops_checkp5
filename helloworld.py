while True:
    name = input("Введите ваше имя: ").strip()
    if name:
        name = name.title()
        print(f"Привет, {name}!")
        break
    else:
        print("Имя не может быть пустым. Пожалуйста, введите имя.")
