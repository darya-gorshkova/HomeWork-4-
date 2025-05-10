from sqlalchemy import create_engine,inspect


db=create_engine("postgresql://postgres:1@localhost:5432/Homework3.1")


def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names == ['users', 'subject', 'student', 'group_student', 'teacher']


def test_add_new_student():
    connect = db.connect()
    connect.execute("INSERT INTO subject (subject_id, subject_title) values (17, 'Testsubject')")
    result = connect.execute("SELECT * FROM subject WHERE subject_id = 17")
    assert result.rowcount == 1
    connect.execute('delete from subject WHERE subject_id = 17')


def test_edit():
    connect = db.connect()
    connect.execute("INSERT INTO subject (subject_id, subject_title) values (17, 'Testedit')")
    connect.execute("UPDATE subject SET subject_title = 'Testedit1' WHERE subject_id = 17")

    result = connect.execute("SELECT subject_title FROM subject WHERE subject_id = 17").fetchall()
    assert result[0][0] == 'Testedit1'
    connect.execute('delete from subject WHERE subject_id = 17')

def test_delete():
    connect = db.connect()
    connect.execute("INSERT INTO subject (subject_id, subject_title) values (17, 'Testdelete')")
    result = connect.execute("SELECT * FROM subject WHERE subject_id = 17")
    assert result.rowcount == 1
    connect.execute('delete from subject WHERE subject_id = 17')
    result = connect.execute("SELECT * FROM subject WHERE subject_id = 17")
    assert result.rowcount == 0