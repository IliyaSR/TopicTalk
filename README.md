TopicTalk Forum Project
Overview

TopicTalk is a Django-based forum project that allows users to engage in discussions on various topics. This README provides instructions on setting up the project locally using Docker Desktop and connecting it to a PostgreSQL database.
Prerequisites

Make sure you have the following installed on your system:

    Docker Desktop
    Python (for managing dependencies)
    Git (optional)

Getting Started

    Clone the repository:

    bash

git clone https://github.com/IliyaSR/TopicTalk.git
cd TopicTalk

Create a virtual environment and install dependencies:

bash

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

Set up the PostgreSQL database:

Create a file named .env in the project root and add the following:

env

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

Replace your_db_name, your_db_user, and your_db_password with your desired database name, user, and password.

Build and run the Docker containers:

bash

docker-compose up -d --build

This command starts the Django web server and PostgreSQL database in separate containers.

Apply database migrations and create a superuser:

bash

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

Follow the prompts to create a superuser account.

Access the TopicTalk Forum:

Open your web browser and go to http://localhost:8000/. You can log in with the superuser account created in step 5.
