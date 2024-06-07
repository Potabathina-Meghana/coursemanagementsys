from config import SNOWFLAKE_CONNECTOR
from db import SNOWFLAKE_CONNECTOR

def add_course_content(course_id, title, description, duration):
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute("INSERT INTO course_content (course_content_id, title, description, duration) VALUES (%s, %s, %s, %s)",
                (course_id, title, description, duration))
    SNOWFLAKE_CONNECTOR.commit()
    cur.close()

def update_course_content(course_id, content_id, title, description, duration):
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute("UPDATE course_content SET title=%s, description=%s, duration=%s WHERE id=%s AND course_content_id=%s",
                (title, description, duration, content_id, course_id))
    SNOWFLAKE_CONNECTOR.commit()
    cur.close()

def delete_course_content(course_id, content_id):
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute("DELETE FROM course_content WHERE id=%s AND course_content_id=%s", (content_id, course_id))
    SNOWFLAKE_CONNECTOR.commit()
    cur.close()

def get_course_content(course_id):
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute("SELECT * FROM course_content WHERE course_content_id = %s", (course_id,))
    content = cur.fetchall()
    cur.close()
    return content

def get_single_course_content(course_id, content_id):
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute("SELECT * FROM course_content WHERE course_content_id = %s AND id = %s", (course_id, content_id))
    content = cur.fetchone()
    cur.close()
    return content

