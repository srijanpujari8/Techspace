import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

db = None
firebase_error = None

try:
    if not firebase_admin._apps:
        cred_json = os.environ.get("FIREBASE_CREDENTIALS")
        
        if not cred_json:
            raise Exception("FIREBASE_CREDENTIALS env variable not found!")
            
        cred = credentials.Certificate(json.loads(cred_json))
        firebase_admin.initialize_app(cred)
        db = firestore.client()
except Exception as e:
    firebase_error = str(e)
    print(f"Firebase failed: {e}")