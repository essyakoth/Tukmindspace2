from flask import Flask, render_template

app = Flask(__name__)
# List of articles for the About page
about_articles = [
    {
        "title": "Managing Stress During Exams",
        "summary": "Exams can be stressful, but there are proven techniques to manage anxiety, improve focus, and maintain mental well-being.",
        "link": "#"
    },
    {
        "title": "Dealing with Depression",
        "summary": "Depression affects many students. Recognizing early symptoms and seeking support is key.",
        "link": "#"
    },
    {
        "title": "Building Healthy Habits for Mental Health",
        "summary": "Daily habits like sleep, exercise, and mindfulness can drastically improve mental health.",
        "link": "#"
    }
]


# Home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', articles=about_articles)

# FAQs page
@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

# Resources page
@app.route('/resources')
def resources():
    return render_template('resources.html')

# Student Info page
@app.route('/student-info')
def student_info():
    return render_template('student_info.html')

if __name__ == '__main__':
    app.run(debug=True)
