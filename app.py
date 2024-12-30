from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/programs")
def programs():
    return render_template("programs.html")

@app.route("/admission")
def admission():
    return render_template("admission.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# Chat route to handle the "Chat with G-One" navigation
@app.route('/chat')
def chat():
    return render_template('chat.html')  # your chat page template


course_data = {
    "choose": ["choose your qualification"],
    "Undergraduate": ["Advanced Programming", "Data Structures & Algorithms", "Introduction to Machine Learning"],
    "Postgraduate": ["Deep Learning", "AI and Robotics", "Advanced Data Science", "Cloud Computing"],
    "PhD": ["Research Methods in AI", "Advanced Neural Networks", "AI in Healthcare"]
}

# Route to process the input and recommend courses
@app.route('/recommend', methods=['POST'])
def recommend():
    qualification = request.form.get('qualification')
    recommended_courses = course_data.get(qualification, [])

    if not recommended_courses:
        recommended_courses = ["No courses available for your qualification."]

    return render_template('index.html', recommended_courses=recommended_courses)

if __name__ == "__main__":
    app.run(debug=True)
