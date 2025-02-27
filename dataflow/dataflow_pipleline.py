import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from google.cloud import storage
import csv
import os
from config import config
# Set up GCP credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.GOOGLE_APPLICATION_CREDENTIALS
from google.cloud import firestore
db = firestore.Client()



def read_csv_from_gcs():
    """Reads the CSV file from Google Cloud Storage."""
    client = storage.Client()
    bucket = client.bucket(config.BUCKET_NAME)
    blob = bucket.blob(config.DESTINATION_BLOB_NAME)

    csv_data = blob.download_as_text().splitlines()
    return (csv.reader(csv_data))


class ProcessCSV(beam.DoFn):
    """Parses CSV data and transforms it into a dictionary format."""
    def process(self, element):
        try:
            if not isinstance(element, list) or len(element) < 3:
                print(f"Skipping invalid row: {element}")
                return

            record = {
                "id": str(element[0]).strip(),
                "description": str(element[1]).strip(),
                "is_active": element[2].strip().lower() == "true"
            }
            yield record
        except Exception as e:
            print(f"Error processing row: {element} → {e}")


class WriteDataToFirestore(beam.DoFn):
    """Writes the data to firestore collections"""
    def process(self,record):
        try:
            doc_ref = db.collection(config.FIRESTORE_COLLECTION).document(record["id"])
            doc_ref.set(record)
            print(f"Inserted: {record}")
            yield record
        except Exception as e:
            print(f"Error inserting record: {e}")

def run():
    """Runs the Apache Beam pipeline."""
    try:
        options = PipelineOptions(
            runner="DirectRunner",  # Use "DataflowRunner" if deploying to GCP
            project=config.PROJECT_ID
        )

        with beam.Pipeline(options=options) as pipeline:
            transformed_data = (
                    pipeline
                    | "Read CSV from GCS" >> beam.Create(read_csv_from_gcs())
                    | "Process CSV Data" >> beam.ParDo(ProcessCSV())
                    | "Write to Forestore" >> beam.ParDo(WriteDataToFirestore())
            )
            print("Successfully SAVED DATA")
    except Exception as e:
        print(f"Pipeline Failed : {e}")

if __name__ == "__main__":
    run()
