from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# -----------------------------------------------------
# EDIT THESE URLS WITH YOUR ACTUAL LINKS
# -----------------------------------------------------
PROFILE = {
    "name": "Mohsin Ali",
    "role": "Software Engineer",
    "phone": "+919541855245",
    "phone_display": "+91-9541855245",
    "email": "mohsinalijoo@gmail.com",

    # Replace these:
    "linkedin": "https://www.linkedin.com/in/mohsinalijoo/",
    "github": "https://github.com/mohsinalijoo",
}

PROJECTS = [
    {
        "title": "Jan-Aushadhi Finder",
        "description": (
            "Native Android healthcare app built with Kotlin and MVVM. "
            "Features Gemini AI medicine suggestions, GPS-based Jan-Aushadhi "
            "store location, refill reminders and offline-first storage."
        ),
        "stack": "Kotlin • MVVM • Gemini API • Room • Google Maps",
        # Replace with actual repository:
        "github": "https://github.com/Mohsinalijoo/Jan-Aushadhi-Finder-Application"
    },
    {
        "title": "Fake News Classifier",
        "description": (
            "Full-stack Flask NLP application for classifying news as REAL "
            "or FAKE. Compared multiple ML algorithms with an LSTM model "
            "achieving 90%+ test accuracy."
        ),
        "stack": "Python • Flask • TensorFlow • Keras • NLP • SQL",
        # Replace with actual repository:
        "github": "https://github.com/Mohsinalijoo/fake-news-classifier"
    },
    {
        "title": "Book Recommendation System",
        "description": (
            "Recommendation system using collaborative filtering and KNN "
            "to generate personalized book recommendations through an "
            "interactive Streamlit interface."
        ),
        "stack": "Python • Scikit-learn • SciPy • KNN • Streamlit",
        # Replace with actual repository:
        "github": "https://github.com/Mohsinalijoo/Book-recommendation-System-Using-ML"
    }
]


@app.route("/")
def home():
    return render_template(
        "index.html",
        profile=PROFILE,
        projects=PROJECTS
    )


@app.route("/resume")
def resume():
    resume_dir = os.path.join(app.root_path, "resume")
    return send_from_directory(
        resume_dir,
        "Mohsin_Ali_Resume.pdf",
        as_attachment=False
    )


if __name__ == "__main__":
    app.run(debug=True)