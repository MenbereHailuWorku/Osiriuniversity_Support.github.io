from flask import Flask, render_template_string, request, redirect, url_for
from flask_ngrok import run_with_ngrok

app = Flask(__name__)

# Define the HTML templates with updated CSS and content
template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #eef2f7;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #333;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(template, title="Home")

if __name__ == '__main__':
    run_with_ngrok(app)
    app.run()