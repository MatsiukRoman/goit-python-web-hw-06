import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql,[subj_id])
        return cur.fetchall()

subj_id = '1'
sql = """
SELECT s.student_id, s.student_name, sub.subject_name, ROUND(AVG(g.grade),2) AS AverageGrade
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
WHERE sub.subject_id = ?
GROUP BY s.student_id, s.student_name
ORDER BY AverageGrade DESC
LIMIT 1;
"""

print(execute_query(sql))
