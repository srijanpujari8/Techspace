if not firebase_admin._apps:
    try:
        cred_dict = {
            "type": os.environ.get("FIREBASE_TYPE"),
            "project_id": os.environ.get("FIREBASE_PROJECT_ID"),
            "private_key_id": os.environ.get("FIREBASE_PRIVATE_KEY_ID"),
            "private_key": (os.environ.get("FIREBASE_PRIVATE_KEY") or "").replace("\\n", "\n"),
            "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
            "client_id": os.environ.get("FIREBASE_CLIENT_ID"),
            "auth_uri": os.environ.get("FIREBASE_AUTH_URI"),
            "token_uri": os.environ.get("FIREBASE_TOKEN_URI"),
            "auth_provider_x509_cert_url": os.environ.get("FIREBASE_CLIENT_X509_CERT_URL"),
        }

        print("DEBUG:", {k: bool(v) for k, v in cred_dict.items()})  # ← ADD THIS

        if cred_dict["private_key"] and cred_dict["client_email"]:
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
            db = firestore.client()
            print("✅ Firebase SUCCESS")  # ← ADD THIS
        else:
            print("❌ Firebase FAILED - missing keys")  # ← ADD THIS

    except Exception as e:
        print("Firebase init failed:", e)  # Already there