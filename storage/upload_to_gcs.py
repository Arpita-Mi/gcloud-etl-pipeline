from google.cloud import storage
import os
from config import config
BUCKET_NAME =  config.BUCKET_NAME
FILE_PATH = config.FILE_PATH
DESTINATION_BLOB_NAME = config.DESTINATION_BLOB_NAME


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.GOOGLE_APPLICATION_CREDENTIALS
def upload_to_gcs(bucket_name, source_file_path, destination_blob_name):
    """Uploads a file to Google Cloud Storage."""
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_path)

        print(f"File {source_file_path} uploaded to gs://{bucket_name}/{destination_blob_name}")
    except Exception as e:
        print(f"error in uploading data to GCS {e}")

if __name__ == "__main__":
    upload_to_gcs(BUCKET_NAME, FILE_PATH, DESTINATION_BLOB_NAME)
