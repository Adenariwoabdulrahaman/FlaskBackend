import sqlite3

conn = sqlite3.connect('yamdb.sqlite3')
cursor = conn.cursor()

# Insert diagnoses
diagnoses = [
    ('Yam Beetles', 'Pest', 'Crop rotation, early harvesting, use of resistant varieties, and soil treatment.'),
    ('Mealy Bugs', 'Pest', 'Use of insecticidal soap, beneficial insects, and field hygiene.'),
    ('Nematodes', 'Pest', 'Use nematode-free planting material, crop rotation, and proper curing of tubers.'),
    ('Termites', 'Pest', 'Destroy termite nests, apply wood ash or neem powder, avoid storing yam near infested soil.'),
    ('Anthracnose', 'Disease', 'Use resistant yam varieties, crop rotation, fungicide, and sanitation.'),
    ('Yam Mosaic Virus', 'Disease', 'Use virus-free planting material, control aphids, monitor field regularly.'),
    ('Dry Rot', 'Disease', 'Cure tubers before storage, avoid injuries, store in dry conditions.')
]
cursor.executemany("INSERT INTO diagnoses (name, type, treatment) VALUES (?, ?, ?)", diagnoses)

# Insert symptoms
symptoms = [
    ('boreholes',),
    ('wilting vines',),
    ('white cottony mass',),
    ('leaf yellowing',),
    ('stunted growth',),
    ('sooty mold',),
    ('cracks on tuber',),
    ('internal browning',),
    ('dry rot',),
    ('termite mounds',),
    ('holes in tuber',),
    ('dark brown spots',),
    ('leaf blight',),
    ('dieback of vines',),
    ('mosaic pattern',),
    ('leaf distortion',),
    ('small tubers',)
]
cursor.executemany("INSERT INTO symptoms (name) VALUES (?)", symptoms)

# Insert rules (symptom_id, diagnosis_id)
rules = [
    (1, 1), (2, 1),
    (3, 2), (4, 2), (5, 2), (6, 2),
    (7, 3), (8, 3), (9, 3),
    (10, 4), (11, 4),
    (12, 5), (13, 5), (14, 5),
    (15, 6), (16, 6), (17, 6)
]
cursor.executemany("INSERT INTO rules (symptom_id, diagnosis_id) VALUES (?, ?)", rules)

conn.commit()
conn.close()
print("All data inserted successfully into yamdb.sqlite3")
