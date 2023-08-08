# django-rest-framework-todo-app

This is a simple application that uses the Django Rest Framework and JavaScript API calls to produce a dynamic ToDo App.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

The Django To-Do App is a web-based task management application that allows users to create, edit, and delete tasks. The frontend is built using JavaScript, HTML,and CSS (styled with Bootstrap). The backend is powered by Django and Django REST Framework, Python web frameworks. The app utilizes AJAX with the Fetch API to provide a seamless user experience by dynamically updating the task list without requiring a full page refresh.

## Features

- Create new tasks with a title.
- Edit existing tasks.
- Mark tasks as completed or incomplete.
- Delete tasks.
- Stylish and responsive interface.
- Utilizes Django's CSRF protection for security.
- Fetches task data using AJAX for real-time updates.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/django-todo-app.git
    ```
   
2. Navigate to the project directory
   ```bash
    cd django-todo-app
    ```
3. Create and activate a virtual environment (optional but recommended):
   ```bash
    python3 -m venv venv
   source venv/bin/activate
    ```
4. Install the project dependencies using pip:
   ```bash
    pip instll -r requirements.txt
    ```
5. Apply the database migrations:
   ```bash
    python manage.py migrate
    ```
   
## Usage

1. Run the development server:
```bash
python manage.py runserver
```

2. Open your web browser and go to `http://127.0.0.1:8000` to access the To-Do app.

3. Use the interface to add, edit, complete, and delete tasks. The app will use AJAX to update the task list dynamically.

## Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
