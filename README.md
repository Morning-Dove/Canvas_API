# Assignment Submitter API

## Overview
This API allows you to submit assignments to Canvas. It provides routes to retrieve courses, get assignments for a specific course, and submit assignments.

## Requirements
The API includes the following routes:

* /courses: Retrieves a list of all courses.
* /courses/{course_id}/assignments: Retrieves a list of all assignments for a specific course.
* /courses/{course_id}/assignments/{assignment_id}/submit: Submits an assignment for a specific course.

## API Endpoints

1. Get All Courses
Endpoint: /courses
Method: GET
Description: Retrieves a list of all courses.

2. Get Assignments for a Specific Course
Endpoint: /courses/{course_id}/assignments
Method: GET
Description: Retrieves a list of all assignments for a specific course.
Path Parameters:
course_id: The ID of the course.

3. Submit an Assignment for a Specific Course
Endpoint: /courses/{course_id}/assignments/{assignment_id}/submit
Method: POST
Description: Submits an assignment for a specific course.
Path Parameters:
course_id: The ID of the course.
assignment_id: The ID of the assignment.

## Installation and Setup

#### Clone the repository:
    git clone https://github.com/yourusername/assignment-submitter-api.git
    cd assignment-submitter-api

#### Install dependencies:

    pip install -r requirements.txt
    uvicorn main:app --reload

#### API will be accessible at:
http://127.0.0.1:8000

### Usage
Use a tool like Postman or cURL to interact with the API endpoints. Make sure to replace {course_id} and {assignment_id} with actual IDs when making requests.


