import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql,[gr_id])
        return cur.fetchall()

gr_id = '3'
sql = """
SELECT s.student_id , s.student_name
FROM students s
JOIN groups g ON s.group_id = g.group_id 
WHERE g.group_id = ?;
"""

print(execute_query(sql))
