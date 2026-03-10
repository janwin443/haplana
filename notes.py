import sqlite3


def connect(database):
    # Wir geben beides zurück, um commit() und close() nutzen zu können
    con = sqlite3.connect(database)
    return con, con.cursor()


def add_note(title, content):
    con, cur = connect("notes.db")

    # IF NOT EXISTS verhindert den OperationalError beim zweiten Start
    cur.execute("CREATE TABLE IF NOT EXISTS notes (title TEXT PRIMARY KEY, content TEXT NOT NULL)")

    # Ein einzelnes Statement mit Platzhaltern
    cur.execute("INSERT OR REPLACE INTO notes (title, content) VALUES (?, ?)", (title, content))

    con.commit()
    con.close()


def read_note(title):
    con, cur = connect("notes.db")
    # Suche gezielt nach dem Titel
    cur.execute("SELECT content FROM notes WHERE title = ?", (title,))
    result = cur.fetchone()
    con.close()

    if result:
        return result[0]  # Gibt nur den String des Contents zurück
    return "Note nicht gefunden."