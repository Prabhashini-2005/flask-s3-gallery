from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
from botocore.client import Config

AWS_ACCESS_KEY_ID = "REPLACE_WITH_YOUR_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY = "REPLACE_WITH_YOUR_SECRET_ACCESS_KEY"
AWS_REGION = "eu-north-1"
S3_BUCKET = "prabhashini-image-gallery-1"

app = Flask(__name__)
app.secret_key = "change_this_secret_123"

s3_client = boto3.client(
    "s3",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    config=Config(signature_version="s3v4")
)


def list_images():
    response = s3_client.list_objects_v2(Bucket=S3_BUCKET)
    urls = []
    if "Contents" in response:
        for obj in response["Contents"]:
            key = obj["Key"]
            if key.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                url = s3_client.generate_presigned_url(
                    "get_object",
                    Params={"Bucket": S3_BUCKET, "Key": key},
                    ExpiresIn=3600
                )
                urls.append(url)
    return urls


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(url_for("index"))
        file = request.files["file"]
        if file.filename == "":
            return redirect(url_for("index"))

        s3_client.upload_fileobj(file, S3_BUCKET, file.filename)
        flash("Image uploaded successfully!")
        return redirect(url_for("index"))

    image_urls = list_images()
    return render_template("index.html", image_urls=image_urls)


if __name__ == "__main__":
    app.run(debug=True)


