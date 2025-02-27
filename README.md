gcloud_service_task 🚀
An ETL (Extract, Transform, Load) pipeline using Apache Beam, Firestore, Cloud Run, and Google Cloud Storage (GCS).

📌 Project Overview 

This project follows a structured ETL process:

1. Extract: Generate and store a CSV file (data.csv).
2. Transform: Process data using an Apache Beam pipeline.
3. Load:
   * Store transformed data in Firestore (NoSQL).
   * Upload the CSV file to Google Cloud Storage (GCS).
   
```
gcloud_etl_pipeline/
│── csv_handling/
│      │── data.csv        # The generated CSV file (output)
│      │── create_csv.py   # Script to generate seeded data
│── dataflow/
│      │── dataflow_pipeline.py  # Apache Beam batch pipeline script and writes data to firestore db
│── storage/
│      │── upload_to_gcs.py  # Script to upload CSV to Google Cloud Storage (GCS)
│── config.py
│      │── config.py       # Stores GCP configurations (bucket name, project ID, etc.)
│── requirements.txt       # Required dependencies for the project
│── main.py                # script to run all the services
│── README.md              # Project Documentation

```
🔧 Setup & Installation

1️⃣ Prerequisites
* Python 3.8+
* Google Cloud SDK (gcloud)
* Apache Beam SDK
* Firestore database
* Google Cloud Storage (GCS) bucket

2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
3️⃣ Set Up Google Cloud
* Login to GCP
```
gcloud auth login
```
* Set your project
```
gcloud config set project YOUR_PROJECT_ID
```

4️⃣ Configure Firestore & GCS

    * Update config.py with your Firestore collection name and GCS bucket.




⚙️ Running the ETL Pipeline

1️⃣ Generate the CSV File
```commandline
python csv_handling/create_csv.py
```
2️⃣ Run the Apache Beam Pipeline
```
python dataflow/dataflow_pipeline.py
```
3️⃣ Upload to Google Cloud Storage
```
python storage/upload_to_gcs.py
```




🚀 Deploying to Cloud Run

1️⃣ Build & Push Docker Image
```
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/gcloud-service-task
```
2️⃣ Deploy to Cloud Run
```
gcloud run deploy gcloud-service-task \
    --image gcr.io/YOUR_PROJECT_ID/gcloud-service-task \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
```
