import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql,[stud_id])
        return cur.fetchall()

stud_id = '5'
sql = """
SELECT s.student_id, s.student_name, sb.subject_name 
FROM students s 
JOIN grades g ON s.student_id = g.student_id 
JOIN subjects sb ON sb.subject_id = g.subject_id
WHERE s.student_id = ?
GROUP BY s.student_id, s.student_name, sb.subject_name;
"""

print(execute_query(sql))
