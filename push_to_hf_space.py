
from huggingface_hub import upload_file

repo_id = "lokeshathipatla/tourism-prediction-app"

files_to_upload = [
    "app.py",
    "requirements.txt",
    "Dockerfile"
]

for file in files_to_upload:
    upload_file(
        path_or_fileobj=file,
        path_in_repo=file,
        repo_id=repo_id,
        repo_type="space"
    )

print("Deployment files uploaded successfully!")
