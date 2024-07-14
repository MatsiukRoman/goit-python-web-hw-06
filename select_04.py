import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT ROUND(AVG(grade),2) AS AverageGrade
FROM grades;
"""

print(execute_query(sql))
