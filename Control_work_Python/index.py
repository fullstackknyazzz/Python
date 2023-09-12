import json
import os
from datetime import datetime

# Путь к файлу, в котором будут храниться заметки
NOTES_FILE = "notes.json"

# Создание файла для заметок, если его нет
if not os.path.exists(NOTES_FILE):
    with open(NOTES_FILE, "w") as file:
        json.dump([], file)

def load_notes():
    with open(NOTES_FILE, "r") as file:
        return json.load(file)

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(title, message):
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": str(datetime.now())
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка добавлена успешно.")

def list_notes():
    notes = load_notes()
    for note in notes:
        print(f"ID: {note['id']}")
        print(f"Заголовок: {note['title']}")
        print(f"Сообщение: {note['message']}")
        print(f"Дата/время: {note['timestamp']}")
        print("")

def edit_note(note_id, title, message):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["message"] = message
            note["timestamp"] = str(datetime.now())
            save_notes(notes)
            print("Заметка отредактирована успешно.")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка удалена успешно.")
            return
    print("Заметка с указанным ID не найдена.")

if __name__ == "__main__":
    while True:
        print("\nВыберите действие:")
        print("1. Добавить заметку")
        print("2. Просмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        
        choice = input("Введите номер действия: ")
        
        if choice == "1":
            title = input("Введите заголовок заметки: ")
            message = input("Введите текст заметки: ")
            add_note(title, message)
        elif choice == "2":
            list_notes()
        elif choice == "3":
            note_id = int(input("Введите ID заметки, которую хотите отредактировать: "))
            title = input("Введите новый заголовок заметки: ")
            message = input("Введите новый текст заметки: ")
            edit_note(note_id, title, message)
        elif choice == "4":
            note_id = int(input("Введите ID заметки, которую хотите удалить: "))
            delete_note(note_id)
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
