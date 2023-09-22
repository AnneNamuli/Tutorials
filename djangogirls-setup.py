# Setup: python3 -m pip install --upgrade pip

"""
    pip is a package manager for Python packages, or modules if you like.
    pip is already installed if you're using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org
    pip is included by default with the Python binary installers.
    pip is a command line program.
    pip is used to install and manage software packages written in Python.
    Packages are modules that can be installed.
    Packages are libraries that you can include in your project.
    Packages are code libraries that extend the functionality of Python.
"""

# For this tutorial we will be using a new directory djangogirls from your home directory:
# Setup: mkdir djangogirls
# Setup: cd djangogirls
# Setup: pip3 install --user virtualenv


# create a virtual environment
"""
    virtual environment is a self-contained directory tree that contains a Python installation 
    for a particular version of Python, plus a number of additional packages.
    virtual environment doesn't copy Python binaries
    virtual environment is just a directory that contains a few scripts

"""
# Setup: python3 -m venv myvenv

# activate the virtual environment
"""
    activate the virtual environment before you start working on your project

        On macOS and Linux:
            source myvenv/bin/activate
        On Windows:
            myvenv\Scripts\activate

    If you want to deactivate your virtual environment, 
        type deactivate on macOS
        and Linux or myvenv\Scripts\deactivate on Windows.

"""

# Setup: install Django using a requirements.txt file
"""
    First create a requirements.txt file inside of the djangogirls/ folder, using the code editor 
    that you installed earlier. You do this by opening a new file in the code editor and then 
    saving it as requirements.txt in the djangogirls/ folder. Your directory will look like this:

    djangogirls
    ├── myvenv
    │   └── ...
    └───requirements.txt
"""
# Setup: In your djangogirls/requirements.txt file you should add the following text: Django~=4.0
# Setup: pip install -r requirements.txt

# Setup: django-admin startproject mysite . for macOS and Linux
# Setup: django-admin.exe startproject mysite . for Windows

# Django-admin will create the skeleton of a Django project for you with this output:
"""
    djangogirls
    ├───manage.py
    ├───mysite
    │   ├───__init__.py
    │   ├───settings.py
    │   ├───urls.py
    │   └───wsgi.py
    └───requirements.txt
"""

# mysite/ is your project directory
# manage.py is a script that helps with management of the site
# mysite/__init__.py is an empty file that tells Python that this directory should be considered a Python package
# mysite/settings.py is a file that contains the configuration of your website
# mysite/urls.py is a file that contains a list of patterns used by urlresolver
# mysite/wsgi.py is an entry-point for WSGI-compatible web servers to serve your project

# changing the settings.py file

"""
    By default, Django is configured to use SQLite -- a lightweight database engine stored in a single file.
    This is the easiest to use choice for beginners.
    SQLite is included in Python, so you won't need to install anything else to support your database.
    However, for real projects you should use a more scalable database, like PostgreSQL or MySQL.
    These database engines are also supported by Django.
    If you wish to use one of these you will need to install additional software onto your computer.
    For PostgreSQL you will need to install psycopg2.
    For MySQL you will need to install mysqlclient.
    We don't cover these databases in this tutorial.

"""

#changing the time zone
    
"""
    Visit http://en.wikipedia.org/wiki/List_of_tz_zones_by_name to get your time zone.
    In settings.py find the line that contains TIME_ZONE and modify it to choose your own time zone.
""" 

# add path for static files
"""
    Static files are all of your CSS and images.
    Django will place them in a folder called static in your project directory.
    This is nice and tidy.
    To do this, add the following line at the end of the file, just after the STATIC_URL entry:
"""
# Setup: STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# allowed hosts
"""
    ALLOWED_HOSTS is a security measure to prevent HTTP Host header attacks, 
    which are possible even under many seemingly-safe web server configurations.
    By validating the Host header, you can be sure your Django site is not responding to a request 
    intended for another site.
    This is especially important if your site is accessible on the Internet.
    You can read more about this in the Django documentation.
    For now, just add your domain name or IP address like this:
"""
# Setup: ALLOWED_HOSTS = ['localhost', '127.0.0.1"]


# database setup

"""
    If you're using SQLite -- which is included in Python -- your database will be a file on your computer.
    This is simple and convenient, but a little bit slower than other types of databases.
    If you want to use another database, install the right Python library (a "database adapter") and change
    a few settings.
    The Django documentation has more information about it.
    If you're using SQLite and you're seeing a warning like this:
"""

# Setup: run python manage.py migrate to create your site's database tables

"""
    sample output
    (myvenv) ~/djangogirls$ python manage.py migrate
    Operations to perform:
    Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    ...
"""


# Setup: run python manage.py runserver to start the web server

#  If you are on Windows and this fails with UnicodeDecodeError, use this command instead:
# Setup: python manage.py runserver 0:8000
# Go to http://127.0.0.1:8000/ with your Web browser. You'll see a "Welcome to Django" page.

# If you are on Windows and need to stop the server, press CTRL + Break.

# creating your first Django app
# Setup: python manage.py startapp blog


"""
    This will create a blog directory in your djangogirls directory.
    It will contain the following files and directories:
    blog/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
"""

# blog/ is your blog application directory
# blog/migrations/ directory stores database migrations
# blog/admin.py is a configuration file for the admin part of the site
# blog/models.py is where you define your blog models
# blog/tests.py is where you can create tests for your application
# blog/views.py is where you place the logic for your application's views

# add blog to the list of installed apps
"""
    To tell Django that we've created a new app, we need to add it to the list of installed apps.
    We do this in the settings.py file.
    In the mysite/settings.py file, find the INSTALLED_APPS setting and add a line containing 'blog.apps.BlogConfig', just above the last line:
""" 

# Setup: INSTALLED_APPS = [
# Setup:     'blog.apps.BlogConfig',
# Setup:     'django.contrib.admin',
# Setup:     'django.contrib.auth',]

# create a model

"""
    A model is a special type of object in Django that is saved in the database.
    A model's fields are the database columns.
    Each model maps to a single database table.
    Django comes with a built-in admin panel.
    You can use it to create, edit and delete posts and comments.
    Let's open the blog/admin.py file, delete its contents and enter this:
"""







