import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

if not firebase_admin._apps:

    cred_json = os.environ.get("FIREBASE_CREDENTIALS")

    cred = credentials.Certificate(json.loads(cred_json))

    firebase_admin.initialize_app(cred)

db = firestore.client()