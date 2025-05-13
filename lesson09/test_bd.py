from sqlalchemy import create_engine,inspect
from sqlalchemy import text

db=create_engine("postgresql://postgres:1@localhost:5432/Homework3.1")

subject_title = "Testedit1"
subject_id = "17"


def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names == ['users', 'subject', 'student', 'group_student', 'teacher']


def test_add_new_student():
    with db.connect() as connect:
        connect.execute(
            text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"),
            {"id": subject_id, "title": subject_title}
        )
        result = connect.execute(
            text("SELECT * FROM subject WHERE subject_id = :id"),
            {"id": subject_id}
        )
        assert result.rowcount == 1
        connect.execute(
            text("DELETE FROM subject WHERE subject_id = :id"),
            {"id": subject_id}
        )

def test_edit():
    with db.connect() as connect:
        connect.execute(
            text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"),
            {"id": subject_id, "title": subject_title})
        connect.execute(
            text("UPDATE subject SET subject_title = :title WHERE subject_id = :id"),
            {"title": subject_title, "id": subject_id})
        result = connect.execute(
            text("SELECT subject_title FROM subject WHERE subject_id = :id"),
            {"id": subject_id}).fetchall()
        assert result[0][0] == subject_title
        connect.execute(
            text("DELETE FROM subject WHERE subject_id = :id"),
            {"id": subject_id})


def test_delete():
    with db.connect() as connect:
        connect.execute(
            text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)"),
            {"id": subject_id, "title": subject_title}
        )
        result = connect.execute(
            text("SELECT * FROM subject WHERE subject_id = :id"),
            {"id": subject_id}
        )
        assert result.rowcount == 1
        connect.execute(
            text("DELETE FROM subject WHERE subject_id = :id"),
            {"id": subject_id}
        )
        result = connect.execute(
            text("SELECT * FROM subject WHERE subject_id = :id"),
            {"id": subject_id}
        )
        assert result.rowcount == 0