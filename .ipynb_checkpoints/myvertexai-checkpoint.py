import vertexai
from google.auth import default

PROJECT_ID = "project-230934ed-7015-46b8-afc"   # use project ID, NOT "My First Project"
REGION = "us-central1"

# This automatically uses ADC from gcloud login
credentials, project = default()

vertexai.init(
    project=PROJECT_ID,
    location=REGION,
    credentials=credentials
)

print("Connected to Vertex AI successfully!")