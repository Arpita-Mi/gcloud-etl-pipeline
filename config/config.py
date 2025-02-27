# Google Cloud Project Settings
import os
from dotenv import load_dotenv
load_dotenv()


GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
PROJECT_ID = os.getenv("PROJECT_ID")
BUCKET_NAME = os.getenv("BUCKET_NAME")
DESTINATION_BLOB_NAME = os.getenv("DESTINATION_BLOB_NAME")
FIRESTORE_COLLECTION = os.getenv("FIRESTORE_COLLECTION")
FILE_PATH=os.getenv("FILE_PATH")