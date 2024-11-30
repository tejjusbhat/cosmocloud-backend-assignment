# Cosmocloud Backend Assignment by Tejjus S. Bhat

Welcome to the Cosmocloud Backend Assignment repository! This project implements a **Student Management System** using **FastAPI** and **MongoDB**. Below is the guide to set up and run the project on your local machine.


## Prerequisites

Before setting up the project, make sure you have the following software installed:

- **Python 3.8+**: The backend is built using Python, so make sure you have a compatible version of Python installed.
- **MongoDB**: You'll need a MongoDB instance running locally or access to a MongoDB Atlas cluster for the database.
- **pip**: Python package manager to install dependencies.
- **Git**: Version control system to clone the repository.
- **Docker** (for containerized deployment)


## Setup Instructions

Follow the steps below to set up the project on your local machine:

### 1. Clone the Repository
Start by cloning the repository to your local machine using the following command:

```
git clone https://github.com/tejjusbhat/cosmocloud-backend-assignment.git
```

### 2. Create a Virtual Environment
Navigate to the project directory and create a virtual environment:

```
cd cosmocloud-backend-assignment
python3 -m venv env
```

### 3. Activate the Virtual Environment
- For **Linux/MacOS**:
    ```
    source env/bin/activate
    ```

- For **Windows**:
    ```
    .\env\Scripts\activate
    ```

### 4. Install Dependencies
Once the virtual environment is activated, install the project dependencies using pip:

```
pip install -r requirements.txt
```

This will install all the necessary Python packages for the project.

### 5. Configure MongoDB
Make sure you have access to a MongoDB instance. If you're using MongoDB Atlas, you can find the connection string in your Atlas account.

- Open `db/mongodb.py` and update the `MONGO_URI` variable with your MongoDB connection string.

```
MONGO_URI = "your_mongodb_connection_string"
```

### 6. Run the Application
To start the FastAPI application, use the following command:

```
uvicorn app.main:app --reload
```

The server will start running at `http://127.0.0.1:8000`. You can access the FastAPI documentation by visiting `http://127.0.0.1:8000/docs`.


## API Endpoints

This project exposes several RESTful API endpoints for managing student data. Below are the available endpoints:

### 1. Create a Student

- **URL:** `/students`
- **Method:** `POST`
- **Request Body:** A JSON object containing student details.
  
    Example request body:
    ```json
    {
        "name": "John Doe",
        "age": 25,
        "address": {
            "country": "India",
            "city": "New Delhi"
        }
    }
    ```

- **Response:**
    - Status Code: `201 Created`
    - Response Body:
    ```json
    {
        "id": "student_id",
        "name": "John Doe",
        "age": 25,
        "address": {
            "country": "India",
            "city": "New Delhi"
        }
    }
    ```

### 2. List Students

- **URL:** `/students`
- **Method:** `GET`
- **Query Parameters:**
    - `country`: (Optional) Filter students by country.
    - `age`: (Optional) Filter students by age (age greater than or equal to the specified value).
  
    Example request:
    ```bash
    GET /students?country=India&age=20
    ```

- **Response:**
    - Status Code: `200 OK`
    - Response Body:
    ```json
    {
        "data": [
            {
                "id": "student_id",
                "name": "John Doe",
                "age": 25,
                "address": {
                    "country": "India",
                    "city": "New Delhi"
                }
            }
        ]
    }
    ```

### 3. Fetch Single Student by ID

- **URL:** `/students/{id}`
- **Method:** `GET`
- **Parameters:**
    - `id`: (Required) The unique ID of the student.

- **Response:**
    - Status Code: `200 OK`
    - Response Body:
    ```json
    {
        "id": "student_id",
        "name": "John Doe",
        "age": 25,
        "address": {
            "country": "India",
            "city": "New Delhi"
        }
    }
    ```

### 4. Update Student by ID

- **URL:** `/students/{id}`
- **Method:** `PATCH`
- **Parameters:**
    - `id`: (Required) The unique ID of the student to be updated.
- **Request Body:** A JSON object with the fields you want to update.
  
    Example request body:
    ```json
    {
        "age": 26
    }
    ```

- **Response:**
    - Status Code: `204 No Content`
    - No response body is returned.

### 5. Delete Student by ID

- **URL:** `/students/{id}`
- **Method:** `DELETE`
- **Parameters:**
    - `id`: (Required) The unique ID of the student to be deleted.

- **Response:**
    - Status Code: `200 OK`
    - Response Body:
    ```json
    {
        "message": "Student deleted successfully"
    }
    ```
