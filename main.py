from db.commands.note_commands import (
    create_note,
    get_all_notes,
    select_note,
    search_notes,
    delete_note
)
from db.tables.note_table import Note
from db.database import create_base

from typing import List
import asyncio


async def create_note_action():
    """
    Функция добавления заметки
    """
    header = input('Введите заголовок заметки: ')
    desc = input('Введите описание заметки: ')

    await create_note(header=header, desc=desc)
    print('Заметка была создана!')


async def see_all_notes_action():
    """
    Функция просмотра всех заметок
    """
    notes: List[Note] = await get_all_notes()

    for row in notes:
        print(f'#{row.id} | {row.header}\n')


async def see_note_action():
    """
    Функция просмотра конкретной заметки по номеру
    """
    notes: List[Note] = await get_all_notes()

    for row in notes:
        print(f'#{row.id} | {row.header}\n')

    number = input('Введите номер заметки для получения данных о ней: ')

    if not number.isdigit():
        print('\nВы ввели не номер!\n')
        return

    note: Note = await select_note(number)

    if not note:
        print(f'Заметки #{number} не существует!\n')
        return

    print(f'Название: {note.header}\nОписание: {note.desc}')


async def _find_note():
    """
    Функция для поиска заметок по ключевому слову
    """
    word = input('Найдите заметку по ключевому слову:')

    notes: Note = await search_notes(word)

    if not notes:
        print('Нет заметок по данному ключевому слову')

    for row in notes:
        print(f'#{row.id} | {row.header}\n')


async def _delete_note():
    """
    Функция удаления заметки
    """
    notes: List[Note] = await get_all_notes()

    for row in notes:
        print(f'#{row.id} | {row.header}\n')

    number = input('Введите номер заметки для ее удаления: ')

    if not number.isdigit():
        print('\nВы ввели не номер!\n')
        return
    
    note: Note = await select_note(number)

    if not note:
        print(f'Заметки #{number} не существует!\n')
        return

    await delete_note(number)
    
    print('Заметка успешно удалена')


async def main():
    """
    Основная функция запущенная в бесконечном цикле
    """
    await create_base()

    while True:
        print(
            'Выберите действие\n'
            '1. Добавить заметку\n'
            '2. Просмотреть все заметки\n'
            '3. Просмотреть заметку\n'
            '4. Найти заметку\n'
            '5. Удалить заметку'
        )
        number = input('Выберите вариант: ')

        if not number.isdigit():
            print('\nВведите корректный вариант!\n')
            continue

        option_actions = {
            1: create_note_action,
            2: see_all_notes_action,
            3: see_note_action,
            4: _find_note,
            5: _delete_note
        }

        action = option_actions.get(int(number))
        if action is None:
            print('\nТакого варианта нет!\n')
            continue

        await action()
        

if __name__ == '__main__':
    asyncio.run(main())
