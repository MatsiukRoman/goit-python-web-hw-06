import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql,[teach_id])
        return cur.fetchall()

teach_id = '5'
sql = """
SELECT sub.subject_id , sub.subject_name , t.teacher_name
FROM subjects sub
JOIN teachers t ON sub.teacher_id = t.teacher_id 
WHERE t.teacher_id = ?;
"""

print(execute_query(sql))
