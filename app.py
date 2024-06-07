from flask import Flask, jsonify
from config import SNOWFLAKE_CONNECTOR, SECRET_KEY
# from app.views.course_view import course_view_api
# from app.views.course_content_view import course_content_api
from main.views.course_view import course_view_api
from main.views.course_content_view import course_content_api

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint(course_view_api)
app.register_blueprint(course_content_api)

conn = SNOWFLAKE_CONNECTOR

@app.route('/')
def index():
    return jsonify({"status": "Ok", "message":"rock it"})

if __name__ == '__main__':
    app.run(debug=True)
