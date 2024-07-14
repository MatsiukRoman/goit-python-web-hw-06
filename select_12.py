import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql,[grp_id,sub_id])
        return cur.fetchall()

grp_id = '1'
sub_id = '5'
sql = """
SELECT grp.group_name , s.student_id, s.student_name, sub.subject_name ,g.grade, g.date_of 
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN subjects sub ON g.subject_id = sub.subject_id
JOIN groups grp ON s.group_id = grp.group_id
WHERE grp.group_id = ? AND sub.subject_id = ?
AND g.date_of = (
    SELECT MAX(g2.date_of)
    FROM grades g2
    JOIN students s2 ON g2.student_id = s2.student_id
    WHERE s2.group_id = grp.group_id AND g2.subject_id = sub.subject_id
)
ORDER BY s.student_name;
"""

print(execute_query(sql))
