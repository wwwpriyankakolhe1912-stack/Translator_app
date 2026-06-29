from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Route to serve the main user interface
@app.route('/')
def home():
    return render_template('index.html')

# Route to ensure static assets (like style.css) are served correctly
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    # Runs a local development server on http://127.0.0.1:5000
    app.run(debug=True)
    