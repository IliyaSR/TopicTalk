# TopicTalk - Django Forum Project

Welcome to TopicTalk, a Django-based forum project designed for discussions on various topics. This project is connected to a PostgreSQL database and can be easily set up using Docker Desktop for local development.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Docker Desktop](https://www.docker.com/products/docker-desktop)

### Setting Up the Project

1. Clone the repository:

    ```bash
    git clone https://github.com/IliyaSR/TopicTalk.git
    cd TopicTalk
    ```

2. Create a `.env` file in the project root and configure your Django settings:

    ```env
    # .env file
    DEBUG=True
    SECRET_KEY=your_secret_key
    DB_NAME=topic_talk_db
    DB_USER=topic_talk_user
    DB_PASSWORD=your_db_password
    DB_HOST=db
    DB_PORT=5432
    ```

    Replace `your_secret_key` and `your_db_password` with your preferred values.

3. Build and run the Docker containers:

    ```bash
    docker-compose up -d --build
    ```

    (If using Docker Desktop, you can also use the Docker Desktop interface to manage containers.)

4. Apply database migrations:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

5. Create a superuser for admin access:

    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

6. Access the forum at [http://localhost:8000/](http://localhost:8000/) and the admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) using the superuser credentials.

## Development Workflow

- Start the development server:

    ```bash
    docker-compose up
    ```

    (Or use Docker Desktop to manage containers.)

- Access the Django shell:

    ```bash
    docker-compose exec web python manage.py shell
    ```

- Run tests:

    ```bash
    docker-compose exec web python manage.py test
    ```

## Stopping the Containers

To stop the Docker containers (if using `docker-compose`):

```bash
docker-compose down
