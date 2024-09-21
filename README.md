Eventify is a web application that allows;
1. Users
  To register for upcoming events.

2. Admins
  To plan and list events so that the users can sign up for them.

Technologies
a) For my Event Registration System project, here are the key technologies I used:

Frontend Technologies:
HTML5:

Used for creating the structure of the web pages (signup, login, event listing, etc.).
CSS3:

Used for styling the pages, ensuring responsiveness and layout design. Since you're using Bootstrap, you can also integrate custom styles.
Bootstrap 5:

A frontend framework to help you design responsive, modern, and mobile-friendly user interfaces. It will speed up the design process for forms, buttons, tables, and overall layout.

Backend Technologies:
Python:

The core programming language for handling the backend logic, data manipulation, and server-side scripting.
Flask Framework:

Flask is a lightweight, yet powerful Python web framework. It will handle the creation of routes (URLs) for your pages, handle form submissions, manage sessions, and direct users to different parts of the application (admin vs user).
Flask-Login:

For handling user sessions, ensuring proper user authentication, and restricting access to admin-specific features.
Flask-WTF:

Flask-WTF is an extension of Flask that simplifies the process of building forms. You can use it for handling form validation and CSRF protection.
Database:
SQLite:

A relational database that stores the data for users, admins, and events. Since it’s lightweight and doesn’t require a separate server, it’s perfect for small to medium-sized applications.
SQLAlchemy:

An ORM (Object Relational Mapper) that simplifies database interaction by mapping database tables to Python classes. It helps manage the creation of models (User, Event) and their relationships.
Additional Tools:
Jinja2 (Included in Flask):

A templating engine that allows you to dynamically render HTML pages and inject data from the backend into the frontend.
Flask-Migrate:

To manage database migrations easily as you update and modify your database schema.
SQLite Studio (Optional):

A GUI tool for managing and inspecting your SQLite database, making it easier to track changes in your data.


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
