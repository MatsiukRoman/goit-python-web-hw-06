import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql,[gr_id, sb_id])
        return cur.fetchall()

gr_id = '3'
sb_id = '2'
sql = """
SELECT s.student_id , s.student_name, sb.subject_name , grd.grade 
FROM students s
JOIN groups g ON s.group_id = g.group_id
JOIN grades grd ON s.student_id = grd.student_id
JOIN subjects sb ON sb.subject_id = grd.subject_id 
WHERE g.group_id = ? AND sb.subject_id = ?
GROUP BY s.student_id, s.student_name, sb.subject_name;
"""

print(execute_query(sql))
