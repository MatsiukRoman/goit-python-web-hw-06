import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql,[subj_id])
        return cur.fetchall()

subj_id = '3'
sql = """
SELECT grp.group_id, grp.group_name , sub.subject_name, ROUND(AVG(gr.grade),2) AS AverageGrade
FROM students s
JOIN grades gr ON s.student_id = gr.student_id 
JOIN subjects sub ON gr.subject_id = sub.subject_id 
JOIN Groups grp ON s.group_id = grp.group_id
WHERE sub.subject_id = ?
GROUP BY grp.group_id, grp.group_name, sub.subject_name;
"""

print(execute_query(sql))
