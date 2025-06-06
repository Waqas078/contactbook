# ContactBook

## Project Description
ContactBook is a web application designed to manage and store contacts. Users can add, edit, view, and delete contact information. This project uses Django and Django Rest Framework, offering a user-friendly interface and backend API for CRUD operations on contacts.

---

## Setup Instructions

Follow these steps to set up and run the project locally.

### 1. **Create a Virtual Environment**
   - Create a virtual environment to isolate the project dependencies:

     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\venv\Scripts\activate
       ```
     - On macos/Linux:
       ```bash
       source venv/bin/activate
       ```

### 2. **Install Dependencies**
   - Install the required dependencies by running:

     ```bash
     pip install -r requirements.txt
     ```

### 3. **Set Up the Database**
   - Run the following command to apply database migrations:

     ```bash
     python manage.py migrate
     ```

### 4. **Run the Development Server**
   - Start the Django development server:

     ```bash
     python manage.py runserver
     ```

   - The application should now be accessible at `http://127.0.0.1:8000/`.

---

## Creating a Superuser or Logging In

### 1. **Create a Superuser**
   - To create a superuser (admin) account, run the following command:

     ```bash
     python manage.py createsuperuser
     ```

   - Follow the prompts to set the username, email, and password.

### 2. **Login**
   - Use the superuser credentials to log in and manage the contacts.
   - can also create a register on the page and log in directly from the web instead of the admin

---

## Optional Features Added

- **Contact Search**: Implemented a search feature to filter contacts based on name, phone number, or email.
- **API Endpoints**: Developed API endpoints using Django Rest Framework for CRUD op
