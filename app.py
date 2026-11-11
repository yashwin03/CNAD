from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Simple HTML template stored as a string for single-file convenience
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Sample App</title>
</head>
<body>
    <h1>Welcome to Flask!</h1>
    
    <!-- Form that submits data via POST -->
    <form method="POST" action="/">
        <label for="name">Enter your name:</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Greet Me</button>
    </form>

    {% if greeting %}
        <h2>{{ greeting }}</h2>
    {% endif %}

    <p>Check out the sample <a href="/api/status">JSON API endpoint</a>.</p>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    greeting = None
    if request.method == "POST":
        user_name = request.form.get("name", "Guest")
        greeting = f"Hello, {user_name}! Your form was submitted successfully."
    return render_template_string(HTML_TEMPLATE, greeting=greeting)

@app.route("/user/<username>")
def show_user(username):
    return f"<h3>Profile page for: {username}</h3>"

@app.route("/api/status")
def api_status():
    return jsonify({
        "status": "online",
        "framework": "Flask",
        "message": "API is working properly"
    })

if __name__ == "__main__":
    app.run(debug=True)
