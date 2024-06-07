from flask import Flask
from config import SNOWFLAKE_CONNECTOR, SECRET_KEY
from app.views.course_view import course_view_api
from app.views.course_content_view import course_content_api

cms = Flask(__name__)
cms.config['SECRET_KEY'] = SECRET_KEY
cms.register_blueprint(course_view_api)
cms.register_blueprint(course_content_api)

conn = SNOWFLAKE_CONNECTOR

if __name__ == '__main__':
    cms.run(debug=True)
