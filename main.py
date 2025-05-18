import json
contacts = []


def add_contacts(contacts):
    '''
    Добавляет новый контакт с именем, телефоном и email.
    Имя не пустое и телефон состоит только из цифр.
    '''
    name = input("Имя: ").strip()
    phone = input("Телефон: ").strip()
    email = input("Email: ").strip()
    if not name:
        print("Имя не может быть пустым")
        return
    elif not phone.isdigit():
        print("Телефон должен состоять только из цифр")
        return
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print(f"Контакт добавлен:\n"
          f"Имя: {contact['name']}\n"
          f"Телефон: {contact['phone']}\n"
          f"Email: {contact['email']}")


def delete_contacts(contacts):
    '''
    Удаляет контакт из списка по имени.
    Если контакт не найден - выводится сообщение об ошибке
    '''
    if not contacts:
        print("Список пуст")
        return
    name = input("Введите имя контакта, которого хотите удалить: ").strip()
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print(f"Контакт {contact['name']} удален")
            return
    print(f"Контакт {name} не найден")


def update_contacts(contacts):
    '''
    Обновляет телефон и email по имени контакта.
    '''
    name = input("Введите имя контакта, у которого хотите обновить телефон и email: ").strip()
    for contact in contacts:
        if contact["name"] == name:
            new_phone = input("Введите новый номер телефона: ").strip()
            if not new_phone.isdigit():
                print("Телефон должен состоять только из цифр")
                return
            contact["phone"] = new_phone
            contact["email"] = input("Введите новый email: ").strip()
            print(f"Контакт обновлен:\n"
                  f"Имя: {contact['name']}\n"
                  f"Телефон: {contact['phone']}\n"
                  f"Email: {contact['email']}")
            return
    print(f"Контакт {name} не найден")


def search_contacts(contacts):
    '''
    Посик контакта по имени, номеру или email.
    Также находит частичное совпадение (например, по части имени
    или номера).
    '''
    query = input("Введите имя, телефон или email для поиска: ").strip().lower()
    for contact in contacts:
        name = contact["name"].lower()
        phone = contact["phone"]
        email = contact["email"].lower()
        if query in name or query in email or query in phone:
            print(f"Контакт найден:\n"
                  f"Имя: {contact['name']}\n"
                  f"Телефон: {contact['phone']}\n"
                  f"Email: {contact['email']}")
            return
    print(f"Контакт {query} не найден")


def show_contacts(contacts):
    '''
    Просмотр всех контактов, отсортированных по имени.
    '''
    if not contacts:
        print("Контактов нет")
        return
    for contact in sorted(contacts, key=lambda x: x["name"]):
        print(f"Имя: {contact['name']}\n"
              f"Телефон: {contact['phone']}\n"
              f"Email: {contact['email']}")


def save_contacts(contacts, filename="contacts.json"):
    '''
    Сохраняет список контактов в указанный файл в формате JSON.
    '''
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)
        print("Контакты сохранены")


def load_contacts(filename="contacts.json"):
    '''
    Загружает список контактов из указанного JSON-файла.
    '''
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def main():
    '''
    Позволяет пользователю выбрать действия из меню:
    1. Добавить контакт
    2. Удалить контакт
    3. Обновить контакт
    4. Найти контакт
    5. Показать все контакты
    6. Сохранить контакты в файл
    7. Загрузить контакты из файла
    0. Выйти
    '''
    global contacts
    contacts = load_contacts()
    menu = '''
    Выберите действие:
    1. Добавить контакт
    2. Удалить контакт
    3. Обновить контакт
    4. Найти контакт
    5. Показать все контакты
    6. Сохранить контакты в файл
    7. Загрузить контакты из файла
    0. Выйти
    '''
    while True:
        print(menu)
        choice = input("Введите номер действия: ").strip()

        if choice == '1':
            add_contacts(contacts)
        elif choice == '2':
            delete_contacts(contacts)
        elif choice == '3':
            update_contacts(contacts)
        elif choice == '4':
            search_contacts(contacts)
        elif choice == '5':
            show_contacts(contacts)
        elif choice == '6':
            save_contacts(contacts)
        elif choice == '7':
            contacts[:] = load_contacts()
            print('Контакты загружены из файла')
        elif choice == '0':
            print("До свидания.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
