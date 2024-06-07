# Import necessary modules
from flask import jsonify, request
from main.models.course_content import add_course_content, update_course_content, delete_course_content, get_course_content,get_single_course_content
from flask import Blueprint


# Create a blueprint for course content management
course_content_api = Blueprint('course_content_api', __name__)

# Define routes and controller functions for course content management

# Add course content
@course_content_api.route('/api/courses/<int:course_id>/content', methods=['POST'])
def add_course_content_route(course_id):
    # Get data from the request
    data = request.json
    if not data:
        return jsonify({'error': 'No JSON data received'}), 400

    # Check if all required keys are present
    required_keys = ['title', 'description', 'duration']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Missing required keys in JSON data'}), 400

    # Extract data from JSON
    title = data['title']
    description = data['description']
    duration = data['duration']
    if not isinstance(title, str) or not title.strip():
        return jsonify({'error': 'Invalid value for name'}), 400
    if not isinstance(description, str) or not description.strip():
        return jsonify({'error': 'Invalid value for description'}), 400
    if not isinstance(duration, str) or not duration.strip():  # Assuming duration should be a string
        return jsonify({'error': 'Invalid value for duration'}), 400
 

    # Add course content
    add_course_content(course_id, title, description, duration)
    return jsonify({'message': 'Course content created successfully'}), 201

# Update course content
@course_content_api.route('/api/courses/<int:course_id>/content/<int:content_id>', methods=['PUT'])
def update_course_content_route(course_id, content_id):
    # Get data from the request
    data = request.json

    # Check if all required keys are present
    required_keys = ['title', 'description', 'duration']
    if not all(key in data for key in required_keys):
        return jsonify({'error': 'Missing required keys in JSON data'}), 400

    # Extract data from JSON
    title = data['title']
    description = data['description']
    duration = data['duration']

    if not isinstance(title, str) or not title.strip():
        return jsonify({'error': 'Invalid value for name'}), 400
    if not isinstance(description, str) or not description.strip():
        return jsonify({'error': 'Invalid value for description'}), 400
    if not isinstance(duration, str) or not duration.strip():  # Assuming duration should be a string
        return jsonify({'error': 'Invalid value for duration'}), 400

    # Update course content
    update_course_content(course_id, content_id, title, description, duration)
    return jsonify({'message': 'Course content updated successfully'}), 200


# Delete course content
@course_content_api.route('/api/courses/<int:course_id>/content/<int:content_id>', methods=['DELETE'])
def delete_course_content_route(course_id, content_id):
    # Delete course content
    delete_course_content(course_id, content_id)
    return jsonify({'message': 'Course content deleted successfully'}), 200

# View course content
@course_content_api.route('/api/courses/<int:course_id>/content', methods=['GET'])
def get_course_content_route(course_id):
    # Get course content
    content = get_course_content(course_id)
    return jsonify(content)

@course_content_api.route('/api/courses/<int:course_id>/content/<int:course_content_id>', methods=['GET'])
def get_single_course_content_route(course_id, course_content_id):
    # Get single course content
    content = get_single_course_content(course_id, course_content_id)
    if content:
        return jsonify(content)
    else:
        return jsonify({'error': 'Missing course content'}), 400
    
    
