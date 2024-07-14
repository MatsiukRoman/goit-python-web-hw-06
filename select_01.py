import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.student_id , s.student_name, ROUND(AVG(g.grade),2) AS AverageGrade
FROM students s
JOIN grades g ON s.student_id = g.student_id
GROUP BY s.student_id, s.student_name
ORDER BY AverageGrade DESC
LIMIT 5;
"""

print(execute_query(sql))
