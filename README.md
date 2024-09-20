Eventify is a web application that allows;
1. Users
  To register for upcoming events.

2. Admins
  To plan and list events so that the users can sign up for them.

Technologies
a) 


Below is a comprehensive structure of the project:
```
Eventify/
│
├── app/
│   ├── __init__.py          # Initialize Flask app, SQLAlchemy, and other extensions
│   ├── models.py            # Define User, Admin, Event models
│   ├── routes.py            # Define routes for User and Admin functionalities
│   ├── admin_routes.py      # Admin-specific routes (event management)
│   ├── user_routes.py       # User-specific routes (event registration, viewing events)
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
