import sqlite3
DB_name = "students.db"
def get_connection():
    return sqlite3.connect(DB_name)
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        create table if not exists students(
            id integer primary key,
            name text not null,
            age integer,
            grade text,
            email text
        )
    """)
    conn.commit()
    conn.close()