import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql,[stud_id,teach_id])
        return cur.fetchall()

stud_id = '2'
teach_id = '5'
sql = """
SELECT g.student_id, t.teacher_name, sub.subject_name, ROUND(AVG(g.grade),2) AS AverageGrade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.subject_id 
JOIN teachers t ON sub.teacher_id = t.teacher_id 
WHERE g.student_id = ? AND t.teacher_id = ?;
"""

print(execute_query(sql))
