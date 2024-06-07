import snowflake.connector

# Configure Snowflake connection
SNOWFLAKE_CONNECTOR = snowflake.connector.connect(
    user='Meghana',
    password='Maggi@3107',
    account='zsmhnub-ir98847',
    database='cms',  # Set the database to 'cms'
    schema='public'  # Assuming 'public' schema, adjust if needed
)

def create_courses_table():
    create_table_query = """
    CREATE OR REPLACE TABLE cms.public.courses (
        course_id INT AUTOINCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT NOT NULL,
        instructor VARCHAR(255) NOT NULL,
        duration VARCHAR(50) NOT NULL
    );
    """
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute(create_table_query)
    cur.close()
    print("Courses table created successfully.")

def insert_sample_data():
    insert_data_query = """
    INSERT INTO cms.public.courses (course_id, name, description, instructor, duration) VALUES
    (1, 'Python Programming Fundamentals', 'Learn the basics of programming using Python.', 'Guido van Rossum', '4 weeks'),
    (2, 'Sample Course', 'Description for sample course.', 'Sample Instructor', '4 weeks'),
    (3, 'Python Web Development', 'Developing web applications using Python and Django framework.', 'Django Reinhardt', '8 weeks'),
    (4, 'Java Mobile App Development', 'Building mobile applications for Android platform using Java.', 'Android Andy', '6 weeks'),
    (5, 'Python Data Analysis', 'Analyzing data using Python libraries such as Pandas and NumPy.', 'Data Science Diana', '5 weeks'),
    (6, 'Java GUI Programming', 'Creating graphical user interfaces (GUIs) using Java and Swing library.', 'Swingin\\Sammy', '4 weeks'),
    (7, 'Python Machine Learning', 'Introduction to machine learning concepts and algorithms using Python.', 'ML Mike', '11 weeks'),
    (8, 'Java Database Programming', 'Working with databases in Java applications using JDBC.', 'Database Dan', '6 weeks'),
    (9, 'Python Game Development', 'Creating games using Python and Pygame library.', 'Game Dev Gary', '8 weeks'),
    (10, 'Java Enterprise Development', 'Java Enterprise Development is the field of building scalable enterprise applications using Java', 'Henry''s', '11 weeks');
    """
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute(insert_data_query)
    SNOWFLAKE_CONNECTOR.commit()
    cur.close()
    print("Sample data inserted successfully.")

# Create table and insert sample data
create_courses_table()
insert_sample_data()

def create_course_content_table():
    create_table_query = """
    CREATE OR REPLACE TABLE cms.public.course_content (
        id INT AUTOINCREMENT PRIMARY KEY,
        course_content_id INT,
        title VARCHAR(255),
        description TEXT,
        duration VARCHAR(50),
        FOREIGN KEY (course_content_id) REFERENCES cms.public.courses (course_id)
    );
    """
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute(create_table_query)
    cur.close()
    print("course_content table created successfully.")

def insert_course_content_data():
    insert_query_data = """
    INSERT INTO cms.public.course_content (course_content_id, title, description, duration) VALUES 
    (1, 'Variables and Data Types', 'Introduction to variables and data types in Python.', '2 hours'),
    (1, 'Control Flow', 'Learn about conditional statements and loops in Python.', '3 hours'),
    (1, 'Functions', 'Understanding how to define and use functions in Python.', '4 hours'),
    (1, 'Lists and Tuples', 'Exploring lists and tuples data structures in Python.', '3.5 hours'),
    (1, 'Dictionaries and Sets', 'Working with dictionaries and sets in Python.', '2.5 hours'),
    (1, 'File Handling', 'Learn how to read from and write to files in Python.', '3 hours'),
    (1, 'Exception Handling', 'Handling errors and exceptions in Python.', '2 hours'),
    (1, 'Modules and Packages', 'Understanding how to organize code into modules and packages.', '4 hours'),
    (1, 'Object-Oriented Programming', 'Introduction to object-oriented programming (OOP) concepts in Python.', '5 hours'),
    (1, 'Introduction to Libraries', 'Exploring popular Python libraries for various tasks.', '3.5 hours'),

    (2, 'Introduction to Java Syntax', 'Learn the basic syntax of the Java programming language.', '2 hours'),
    (2, 'Object-Oriented Programming in Java', 'Understanding the principles of object-oriented programming in Java.', '3.5 hours'),
    (2, 'Collections Framework', 'Exploring the Java Collections Framework.', '3 hours'),
    (2, 'Exception Handling in Java', 'Handling exceptions in Java programs.', '2.5 hours'),
    (2, 'File Handling in Java', 'Working with files in Java programs.', '2.5 hours'),
    (2, 'Multithreading', 'Understanding multithreading concepts in Java.', '3 hours'),
    (2, 'Networking in Java', 'Networking concepts and APIs in Java.', '2.5 hours'),
    (2, 'Database Access with JDBC', 'Working with databases using JDBC in Java.', '3.5 hours'),
    (2, 'GUI Programming with Swing', 'Creating graphical user interfaces using Swing library in Java.', '4 hours'),
    (2, 'Introduction to JavaFX', 'An introduction to JavaFX for building modern UI applications.', '3 hours'),

    (3, 'Introduction to Web Development', 'An overview of web development concepts and technologies.', '2.5 hours'),
    (3, 'Setting Up Python Environment', 'Learn how to set up Python environment for web development.', '3 hours'),
    (3, 'Introduction to Django Framework', 'An introduction to Django framework for building web applications.', '4 hours'),
    (3, 'Models and Database Integration', 'Working with models and integrating databases in Django.', '3.5 hours'),
    (3, 'Views and Templates', 'Understanding views and templates in Django for rendering web pages.', '2.5 hours'),
    (3, 'Forms and Form Handling', 'Working with forms and form handling in Django.', '3 hours'),
    (3, 'Authentication and Authorization', 'Implementing authentication and authorization in Django applications.', '2 hours'),
    (3, 'RESTful APIs with Django Rest Framework', 'Building RESTful APIs using Django Rest Framework.', '4 hours'),
    (3, 'Deployment and Hosting', 'Deploying Django applications and hosting options.', '3.5 hours'),
    (3, 'Advanced Django Concepts', 'Exploring advanced concepts and techniques in Django.', '4 hours'),

    (4, 'Introduction to Mobile App Development', 'An overview of mobile app development concepts and platforms.', '2.5 hours'),
    (4, 'Setting Up Java Environment for Android', 'Setting up Java environment for Android app development.', '3 hours'),
    (4, 'Introduction to Android Studio', 'An introduction to Android Studio IDE for Android development.', '3.5 hours'),
    (4, 'User Interface Design', 'Designing user interfaces for Android apps using XML layouts.', '2.5 hours'),
    (4, 'Activity and Fragment Lifecycle', 'Understanding the lifecycle of activities and fragments in Android.', '3 hours'),
    (4, 'Working with Intents', 'Using intents for communication between components in Android apps.', '2.5 hours'),
    (4, 'Data Persistence', 'Implementing data persistence in Android apps using SQLite database.', '3.5 hours'),
    (4, 'Networking and Web Services', 'Working with networking and web services in Android apps.', '3 hours'),
    (4, 'Testing and Debugging', 'Testing and debugging Android applications.', '2 hours'),
    (4, 'Publishing Android Apps', 'Publishing Android apps to the Google Play Store.', '4 hours'),

    (5, 'Introduction to Data Analysis', 'An introduction to data analysis and its importance.', '2.5 hours'),
    (5, 'Setting Up Data Analysis Environment', 'Setting up Python environment for data analysis.', '3 hours'),
    (5, 'Data Import and Cleaning', 'Importing data into Python and cleaning data for analysis.', '3.5 hours'),
    (5, 'Exploratory Data Analysis', 'Conducting exploratory data analysis using Pandas library.', '2.5 hours'),
    (5, 'Data Visualization with Matplotlib', 'Visualizing data using Matplotlib library in Python.', '3 hours'),
    (5, 'Statistical Analysis', 'Performing statistical analysis on data using NumPy library.', '2.5 hours'),
    (5, 'Introduction to Machine Learning', 'An introduction to machine learning concepts and algorithms.', '3.5 hours'),
    (5, 'Supervised Learning', 'Understanding supervised learning algorithms.', '3 hours'),
    (5, 'Unsupervised Learning', 'Exploring unsupervised learning techniques.', '3 hours'),
    (5, 'Data Analysis Project', 'Applying data analysis techniques to a real-world project.', '4 hours'),

    (6, 'Introduction to GUI Programming', 'An introduction to GUI programming concepts.', '2 hours'),
    (6, 'Setting Up Java Environment for GUI Development', 'Setting up Java environment for GUI development.', '3 hours'),
    (6, 'Creating Windows and Dialogs', 'Creating windows and dialogs using Swing library.', '3.5 hours'),
    (6, 'Handling User Input', 'Handling user input through various GUI components.', '2.5 hours'),
    (6, 'Event Handling', 'Understanding event handling mechanisms in Java Swing.', '3 hours'),
    (6, 'Layouts and Containers', 'Working with layouts and containers in Swing applications.', '3.5 hours'),
    (6, 'Customizing Look and Feel', 'Customizing the look and feel of Swing applications.', '2.5 hours'),
    (6, 'Working with Menus and Toolbars', 'Creating menus and toolbars in Swing applications.', '3 hours'),
    (6, 'Using Swing Components', 'Using various Swing components for building GUI.', '2.5 hours'),
    (6, 'Advanced Swing Techniques', 'Exploring advanced techniques in Java Swing programming.', '4 hours'),

    (7, 'Introduction to Machine Learning', 'An overview of machine learning concepts and applications.', '2 hours'),
    (7, 'Setting Up Python Environment for Machine Learning', 'Setting up Python environment for machine learning.', '3 hours'),
    (7, 'Data Preprocessing', 'Preparing data for machine learning tasks.', '3.5 hours'),
    (7, 'Supervised Learning Algorithms', 'Understanding supervised learning algorithms and their applications.', '3 hours'),
    (7, 'Unsupervised Learning Algorithms', 'Exploring unsupervised learning techniques and algorithms.', '3 hours'),
    (7, 'Model Evaluation and Validation', 'Evaluating and validating machine learning models.', '3.5 hours'),
    (7, 'Feature Engineering', 'Engineering features for machine learning models.', '2.5 hours'),
    (7, 'Ensemble Methods', 'Using ensemble methods to improve model performance.', '3 hours'),
    (7, 'Neural Networks and Deep Learning', 'An introduction to neural networks and deep learning concepts.', '3 hours'),
    (7, 'Deploying Machine Learning Models', 'Deploying machine learning models to production environments.', '4 hours'),

    (8, 'Introduction to Database Programming', 'An overview of database programming concepts and techniques.', '2 hours'),
    (8, 'Setting Up Java Environment for Database Programming', 'Setting up Java environment for database programming.', '3 hours'),
    (8, 'JDBC Basics', 'Understanding the basics of Java Database Connectivity (JDBC).', '3 hours'),
    (8, 'Connecting to Databases', 'Connecting to various databases using JDBC.', '2.5 hours'),
    (8, 'Executing SQL Queries', 'Executing SQL queries through JDBC in Java.', '3.5 hours'),
    (8, 'Handling Result Sets', 'Handling result sets returned from database queries.', '3 hours'),
    (8, 'Transaction Management', 'Managing transactions in JDBC applications.', '3 hours'),
    (8, 'Using Prepared Statements', 'Using prepared statements for efficient database operations.', '2.5 hours'),
    (8, 'Database Connection Pooling', 'Implementing database connection pooling in Java applications.', '3.5 hours'),
    (8, 'Advanced JDBC Techniques', 'Exploring advanced techniques in JDBC programming.', '4 hours'),

    (9, 'Introduction to Game Development', 'An introduction to game development concepts and techniques.', '2 hours'),
    (9, 'Setting Up Python Environment for Game Development', 'Setting up Python environment for game development.', '3 hours'),
    (9, 'Introduction to Pygame Library', 'An introduction to Pygame library for game development.', '3.5 hours'),
    (9, 'Creating Game Window', 'Creating a game window using Pygame.', '2.5 hours'),
    (9, 'Handling User Input in Games', 'Handling user input in Pygame-based games.', '3 hours'),
    (9, 'Game Loop and Updates', 'Implementing game loop and updating game state.', '3.5 hours'),
    (9, 'Drawing Graphics', 'Drawing graphics and animations in Pygame.', '3 hours'),
    (9, 'Working with Sprites', 'Using sprites for game objects in Pygame.', '2.5 hours'),
    (9, 'Collision Detection', 'Implementing collision detection in games.', '3 hours'),
    (9, 'Game Development Project', 'Applying game development techniques to a real-world project.', '4 hours'),

    (10, 'Introduction to Java Enterprise Development', 'An overview of Java enterprise development concepts and technologies.', '2 hours'),
    (10, 'Setting Up Java Environment for Enterprise Development', 'Setting up Java environment for enterprise development.', '3 hours'),
    (10, 'Introduction to Java EE Platform', 'An introduction to Java EE platform and its components.', '3.5 hours'),
    (10, 'Enterprise JavaBeans (EJB)', 'Understanding Enterprise JavaBeans (EJB) and their use cases.', '2.5 hours'),
    (10, 'Java Persistence API (JPA)', 'Working with Java Persistence API (JPA) for database operations.', '3 hours'),
    (10, 'Web Services with JAX-WS', 'Developing web services using JAX-WS API in Java.', '3.5 hours'),
    (10, 'RESTful Web Services with JAX-RS', 'Building RESTful web services using JAX-RS API.', '3 hours'),
    (10, 'Java Message Service (JMS)', 'Using Java Message Service (JMS) for messaging.', '2.5 hours'),
    (10, 'Security in Java EE Applications', 'Implementing security features in Java EE applications.', '3.5 hours'),
    (10, 'Deploying Java EE Applications', 'Deploying Java EE applications to application servers.', '4 hours');
    """
    cur = SNOWFLAKE_CONNECTOR.cursor()
    cur.execute(insert_query_data)
    SNOWFLAKE_CONNECTOR.commit()
    cur.close()
    print("Course content data inserted successfully.")

create_course_content_table()
insert_course_content_data()
