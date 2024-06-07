from config import SNOWFLAKE_CONNECTOR

from db import SNOWFLAKE_CONNECTOR


def get_courses():
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute("SELECT * FROM courses")
    courses = cur.fetchall()
    cur.close()
    return courses
 
def get_course_by_name(name):
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute("SELECT * FROM courses WHERE name = %s", (name,))
    course = cur.fetchone()
    cur.close()
    return course
 
def add_course(name, description, instructor, duration):
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute("INSERT INTO courses (name, description, instructor, duration) VALUES (%s, %s, %s, %s)",
                (name, description, instructor, duration))
    SNOWFLAKE_CONNECTOR.commit()
    cur.close()
 
def update_course_in_database(course_id, name, description, instructor, duration):
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute("UPDATE courses SET description=%s, instructor=%s, duration=%s, name=%s WHERE course_id=%s",
                (description, instructor, duration, name, course_id))
    SNOWFLAKE_CONNECTOR.commit()
    cur.close()


 
def course_exists(name):
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute("SELECT COUNT(*) FROM courses WHERE name = %s", (name,))
    result = cur.fetchone()[0]
    cur.close()
    return result > 0


def delete_course(name):
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute("DELETE FROM courses WHERE name = %s", (name,))
    SNOWFLAKE_CONNECTOR.commit()
    cur.close()

