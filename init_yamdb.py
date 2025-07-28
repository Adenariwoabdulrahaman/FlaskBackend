import sqlite3

conn = sqlite3.connect('yamdb.sqlite3')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE diagnoses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    treatment TEXT
)
''')

cursor.execute('''
CREATE TABLE symptoms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE rules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptom_id INTEGER,
    diagnosis_id INTEGER,
    FOREIGN KEY (symptom_id) REFERENCES symptoms(id),
    FOREIGN KEY (diagnosis_id) REFERENCES diagnoses(id)
)
''')

conn.commit()
conn.close()
print("yamdb.sqlite3 and tables created.")
