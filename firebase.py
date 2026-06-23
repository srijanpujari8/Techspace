import firebase_admin
from firebase_admin import credentials, firestore

db = None
firebase_error = None

try:
    if not firebase_admin._apps:
        cred = credentials.Certificate({
            "type": "service_account",
            "project_id": "techspace-27",
            "private_key_id": "685e81c4a6109d6dc7a28927ad0390b18e0c5457",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDHA42/BOxtUhUX\nrlaGTzCUvw7HyEHik1wt3HBn9uB8GPA/5fA1XXPHXWuLc5eczNU2V2vIUn87H/z1\n7ZLergVKS+I3s3ocajxdIkzWg6hoABr7m86Ge71DlNFACOUln18i/DFb7EJsp14q\nlnAKjD6Loeza8ehmqFcRTgwkHkDu6WpgUAJXKyMbPPDgqKzQo7BOyHQo4zJvADJF\nZVJP3rJ16kPNtxWUpufXpE5v1a00Ui/kbjVPdtTLPxtpH185Jbp/D2uG5+fIj7Tx\nyHjuNiN5HDBmJWLf27pESo0fLnS3OyXD/LvyPXZRk5rbJXvQ6wnHyO8Fia6lXVlB\nhHXbPffDAgMBAAECggEAEVbf7LqzFrtGFzAbXcxcgTk8Qm/SPbl1GJHSQVyjJmzN\n0eNo0F16Du62xgmmNgUqtndbbrKxXydkVNEEMN6cm2KNLSk4BG3FIKAybaY+8ADC\nWRW0Isd5MAAxUxDzVhnSoiuy6T1mdC0I6VD+Jg0eDfBnwJO/GeKk418Xc7YnFimc\njl5UGIApAuKf9BOnJdAjumteCi7TDf6QYd+2CqDk9x2LI8LK8Ep919k/APKEzHLC\nxDxhveg7n5Gb/5sl8VX+EymldfM6kheelKXzek3BgMv85gEXaMy8eSKynVVEtxLA\nwcFV+OBtqaHXcEkAfvCrrCNHXkXGDiWSZqV6sKZQAQKBgQD6QXzxwDQYNqbeUIMY\nTmVachgBnkLlJFW0qPcuXXBT7SR8icLmYUCESRKgdsZ9smg+/79GzucHwmT/4Aki\nrMAldaSpdNYpUo1ItoPK+ZtJydjg1z07gvNwOkZ81mTstFuOGc6/Y/HjXSUJ7IqA\ndffY6YO6/9fL0TDBqFS6iFBTwwKBgQDLlPdb9nL8DQrfEAeqgE2CfcWtkA6gd1Zd\nq316MRELO6LL9ZZzY5OqMw9D40qld1pUSiKaeJUcwfWnoYO9jtIbIJBM+7YUqWFZ\nqIx/US0EQHUABhM4Z5I9wq2LwTcxMrCdSoAiS9V1RbFR+t68O2ypnSEW5od1cDZA\nbpmRn3WMAQKBgQDlp59vgwDLj6vGrIABmD/upnFdWszs11FHfx+HDvx8KE2pdArF\nvE2mmCBd3WH+C/EajzwLUOg2+LATGJeJmJqkRbecQroeJcG+DrAXXsShDHjYrO1m\nZZ/dR71T5rOrfT/fwdM3VBKwodPRrZ7UkG2oQ3M98ncodYqWzVEj9OAyXQKBgQCv\neO7cbUgeyH8eVQrGg2BLoWzJdOmmljXy9uVodPJj5Dsl4cCUJLgac3gs47Rrerx4\n+o1o55Ze+y9qFWUf9gJTL3YxZKREmto2FXlEJAvRJl2yb4oRi/QZF7vOQfP4i+B/\nMr/Oz95k/nUgXEOvqui2KaFjw7/uEZIxZyMmyXLgAQKBgQCZlET4yjDkIWipU0nM\nOa+L+bIGitxmOndoF7+51a3yVPpLwyg24gRTjd4AawYPpjD4AUQceINEG7HoLp0e\nON4RqcFoLRQnXLmLpdD+nKnsuolt9d//xIAicabu6Pk8k8VJxGK0l7PgbLPswEuS\nQkcjt0W94twGdgeFzNTdJ0TA7g==\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-fbsvc@techspace-27.iam.gserviceaccount.com",
            "client_id": "111456424698047117978",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40techspace-27.iam.gserviceaccount.com",
        })
        firebase_admin.initialize_app(cred)
        db = firestore.client()
except Exception as e:
    firebase_error = str(e)
    print(f"Firebase failed: {e}")