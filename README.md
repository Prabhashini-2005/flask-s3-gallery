# AWS S3 Image Gallery with Flask

A simple Flask web application that lets you upload images from your browser and display them as a gallery, with all images stored in an Amazon S3 bucket.[web:156][web:193]

## Features

- Upload images directly from the browser using a simple HTML form.  
- Store and retrieve images from an AWS S3 bucket.  
- Display all images in a clean gallery layout.  
- Show a success message after each upload using Flask flash messages.[web:155][web:160]

## Tech Stack

- Python, Flask  
- HTML, CSS, Jinja2 templates  
- AWS S3, boto3 (AWS SDK for Python)[web:156][web:159]

## Project Structure

```text
flask-s3-gallery/
├── app.py
├── templates/
│   └── index.html
└── venv/ 
# ignored in git
app.py contains the Flask routes and S3 integration logic, and index.html renders the upload form and image gallery.[web:100][web:155]

How It Works
The home page (/) shows one page with the upload form and the current image gallery, using images stored in S3.[web:100][web:156]

When the user uploads an image, Flask uses boto3 to send the file to the configured S3 bucket (prabhashini-image-gallery-1).[web:156][web:193]

To display the gallery, the app lists objects in the bucket and generates pre‑signed URLs for each image, then renders them as <img> tags in the HTML template.[web:100][web:156]

Note: For security, AWS credentials should be provided via environment variables or a local config file and must never be committed to GitHub.[web:131][web:173]
