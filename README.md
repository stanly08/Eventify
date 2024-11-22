**Eventify**
Eventify is a web application built using Python and Flask that allows users to manage and attend events seamlessly. It provides a platform for administrators to create and manage events, and for users to register and pay for attending events. The application integrates with the M-Pesa payment gateway for secure and convenient payments.
**Features**
1.User Authentication: Secure sign-up and login for both users and administrators.

2.Admin Dashboard: Administrators can create, update, and delete events. They can also view and manage user registrations.

3.User Dashboard: Users can view available events, register for events, and manage their event registrations.

4.Event Registration: Users can register for events and view event details.

5.Payment Integration: Integration with M-Pesa for secure payments during event registration.

**Project Structure**
```
Eventify/
├── app/
│   ├── __init__.py          # Initialize Flask app, SQLAlchemy, and other extensions
│   ├── models.py            # Define User, Admin, Event models
│   ├── routes.py            # Define routes for User and Admin functionalities
│   ├── admin_routes.py      # Admin-specific routes (event management)
│   ├── user_routes.py       # User-specific routes (event registration, viewing events)
│   ├── mpesa.py             # M-Pesa payment integration
│   ├── forms.py             # Define Flask-WTF forms for user inputs
│   ├── static/              # Static files (CSS, images, etc.)
│   ├── templates/
│   │   ├── base.html        # Base template with common layout
│   │   ├── signup.html      # Common sign-up form (admin/user role selection)
│   │   ├── login.html       # Login form for both users and admins
│   │   ├── admin_dashboard.html  # Admin dashboard for managing events
│   │   ├── user_dashboard.html   # User dashboard to view and register for events
│   │   ├── event_list.html  # List of events for users to register
│   │   ├── event_detail.html  # Event details page
│   └── events.db            # SQLite database to store users, admins, and events
│
├── config.py                # Configuration settings
├── requirements.txt         # Project dependencies
├── run.py                   # Entry point to start the Flask app
└── README.md                # Documentation
```

**Getting Started**
**Prerequisites**
1.Python 3.x

2.Flask

3.M-Pesa API credentials (for payment integration)

**Installation**
1. Clone the repository:
  ```
  git clone https://github.com/yourusername/eventify.git
  cd eventify
  ```
2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
    ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
    ```
4.Set up environment variables:
  Create a .env file and add your environment variables (e.g., M-Pesa API credentials).
5.Initialize the database:
  ```
  flask db init
  flask db migrate -m "Initial migration."
  flask db upgrade
  ```
6.Run the application:
  ```
  flask run
  ```

**Usage**
Admin: Log in to the admin dashboard to manage events.

User: Register and log in to view and sign up for events.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.











   




