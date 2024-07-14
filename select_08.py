import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT t.teacher_id , t.teacher_name , s.subject_name , ROUND(AVG(g.grade),2) AS AverageGrade
FROM teachers t 
JOIN subjects s ON t.teacher_id = s.teacher_id 
JOIN grades g ON s.subject_id = g.subject_id 
GROUP BY t.teacher_id , t.teacher_name, s.subject_name 
ORDER BY AverageGrade DESC;
"""

print(execute_query(sql))
