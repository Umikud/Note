from sqlalchemy import select, delete
from db.database import get_session
from db.tables.note_table import Note

async def create_note(header: int, desc: str):
    """
    Создает новую заметку с указанным заголовком и описанием.
    """
    async with get_session() as session:
        obj = Note(
            header=header, 
            desc=desc
        )
        session.add(obj)
        await session.commit()

async def get_all_notes():
    """
    Возвращает список всех заметок.
    """
    async with get_session() as session:
        sql = select(
            Note
        )
        result = await session.execute(sql)
        return result.scalars().all()

async def select_note(id: int):
    """
    Возвращает заметку по указанному ID.
    """
    async with get_session() as session:
        sql = select(
            Note
        ).where(
            Note.id == id
        )
        result = await session.execute(sql)
        return result.scalar()

async def search_notes(keyword: str):
    """
    Возвращает список заметок, содержащих указанное ключевое слово в заголовке или описании.
    """
    async with get_session() as session:
        sql = select(
            Note
        ).where(
            Note.header.contains(keyword) | Note.desc.contains(keyword)
        )
        result = await session.execute(sql)
        return result.scalars().all()

async def delete_note(note_id: int):
    """
    Удаляет заметку с указанным ID.
    """
    async with get_session() as session:
        sql = delete(Note).where(Note.id == note_id)
        await session.execute(sql)
        await session.commit()


            
        

