from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Project data list (for dynamic display)
projects = [
    {
        "name": "Book Recommendation System",
        "desc": "Trained a recommendation model using Scikit-learn and Scipy for data processing. Utilized Collaborative Filtering to suggest personalized book recommendations.Developed an interactive interface with Streamlit to generate real-time book suggestions. Used K-Nearest Neighbors (KNN) Algorithm.",
        "bg": "pr1.jpg"
    },
    {
        "name": "Door Security System (IOT)",
        "desc": "Door security system where the automated message is send to the user’s mobile phone to notify that the door is open.",
        "bg": "pr2.jpg"
    },
    {
        "name": "Hospital Appointment Scheduling Chatbot",
        "desc": "Created a hospital appointment chatbot using Botpress to help users book specialist appointments via a simple conversational interface, with built-in validation and efficient scheduling flows.",
        "bg": "pr3.jpg"
    },
    {

        "name": "Fake News Detection Using ML",
        "desc": "A Flask-based Fake News Detection Web Application that classifies news articles as REAL or FAKE using a Machine Learning model.The system supports both manual text input and live news fetching using NewsAPI, providing predictions along with confidence scores.",
        "bg": "pr4.jpg"
    },
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Contact form logic (this just displays a thank you for demo)
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        flash('Thank you for contacting me!', 'success')
        # Production: Integrate with an email backend (Flask-Mail, SMTP, or Formspree)
        return redirect(url_for('index'))
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
