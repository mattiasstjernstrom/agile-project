class ConfigDebug:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:password@localhost/grupparbete"  # File-based SQL database
    SECRET_KEY = "SDFA11#"

    # Login Variables
    SECURITY_LOGIN_USER_TEMPLATE = "security/login_user.html"
    SECURITY_POST_LOGOUT_VIEW = "/login"
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True

    ## Python intergrated mail server:
    ## "python -m smtpd -n -c DebuggingServer localhost:8025"
    # MAIL_SERVER = "localhost"
    # MAIL_PORT = 8025
    # MAIL_USE_SSL = False
    # MAIL_USE_TLS = False

    # Flask-Mail SMTP server settings for development
    MAIL_SERVER = "127.0.0.1"
    MAIL_PORT = 1025
    MAIL_USE_SSL = False
    MAIL_USE_TLS = False

    ## Username and password for email server
    # MAIL_USERNAME = "email@example.com"
    # MAIL_PASSWORD = "password"
    # MAIL_DEFAULT_SENDER = '"MyApp" <noreply@example.com>'

    # Flask-User settings
    USER_APP_NAME = (
        "Flask-User Basic App"  # Shown in and email templates and page footers
    )
    USER_ENABLE_EMAIL = True  # Enable email aution
    USER_ENABLE_USERNAME = False  # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"

    SECURITY_PASSWORD_SALT = "341231232"
