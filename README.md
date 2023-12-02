# SEMA-MAMA-APP
# SEMA-MAMA Django App

## Overview

SEMA-MAMA is a mental health support app designed to address postpartum depression among young mothers and adolescent girls in the Kenyan healthcare system. This README provides step-by-step instructions on how to set up and run the SEMA-MAMA Django app locally.

## Prerequisites

Before you begin, ensure that you have the following installed:

- [Python](https://www.python.org/) (version 3.11.4)
- [pip](https://pip.pypa.io/) (Python package installer)
- [Django](https://www.djangoproject.com/) (version 4.2.7)
## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/sema-mama-django.git
    cd sema-mama-django
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure Environment Variables:**

    Create a `.env` file in the root directory and add the following:

    ```plaintext
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=mongodb://localhost:27017/sema-mama-db
    ```

    Replace `your_secret_key` with a secure secret key for Django.

6. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Create Superuser (for Admin Access):**

    ```bash
    python manage.py createsuperuser
    ```

    Follow the prompts to create an admin user.

8. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

    The app will be accessible at `http://127.0.0.1:8000`.

9. **Access the Admin Panel:**

    Visit `http://127.0.0.1:8000/admin` in your web browser and log in with the superuser credentials.

## Usage

- Visit `http://127.0.0.1:8000` in your web browser to access the SEMA-MAMA Django app.

## Contributing

If you would like to contribute to SEMA-MAMA, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
