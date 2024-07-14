import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql,[stud_id,teach_id])
        return cur.fetchall()

stud_id = '1'
teach_id = '3'
sql = """
SELECT s.student_id, s.student_name, sb.subject_name , t.teacher_name 
FROM students s 
JOIN grades g ON s.student_id = g.student_id 
JOIN subjects sb ON sb.subject_id = g.subject_id
JOIN teachers t ON t.teacher_id = sb.teacher_id 
WHERE s.student_id = ? AND t.teacher_id = ?
GROUP BY s.student_id, s.student_name, sb.subject_name;
"""

print(execute_query(sql))
