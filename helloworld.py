while True:
    try:
        name = input("Введите ваше имя: ").strip()
        if name:
            name = name.title()
            print(f"Привет, {name}!")
            break
        else:
            print("Имя не может быть пустым. Пожалуйста, введите имя.")
    except KeyboardInterrupt:
        print("\nВыход из программы.")
        break
