from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# FAQ data
questions = [
    "What is AI?",
    "Define artificial intelligence",
    "What is machine learning?",
    "Explain machine learning",
    "What is Python?",
    "Tell me about Python",
    "How to learn programming?",
    "How can I start coding?",
    "What is your name?",
    "Who are you?",
    "What is deep learning?",
    "Explain deep learning",
    "What is data science?",
    "Define data science",
    "What is NLP?",
    "What is natural language processing?",
    "What is chatbot?",
    "Explain chatbot",
    "What is coding?",
    "Why is programming important?"
]

answers = [
    "AI stands for Artificial Intelligence, which enables machines to think and learn.",
    "AI stands for Artificial Intelligence, which enables machines to think and learn.",
    "Machine learning is a subset of AI that allows systems to learn from data.",
    "Machine learning is a subset of AI that allows systems to learn from data.",
    "Python is a popular programming language used in AI and web development.",
    "Python is a popular programming language used in AI and web development.",
    "You can learn programming through practice, courses, and projects.",
    "You can start coding by learning basics and practicing regularly.",
    "I am a chatbot created to answer your questions.",
    "I am a chatbot created to answer your questions.",
    "Deep learning is a type of machine learning using neural networks.",
    "Deep learning is a type of machine learning using neural networks.",
    "Data science involves analyzing data to extract useful insights.",
    "Data science involves analyzing data to extract useful insights.",
    "NLP stands for Natural Language Processing, used to understand human language.",
    "NLP stands for Natural Language Processing, used to understand human language.",
    "A chatbot is a program that can simulate conversation with users.",
    "A chatbot is a program that can simulate conversation with users.",
    "Coding is the process of writing instructions for computers.",
    "Programming is important because it helps build software and solve problems."
]

# Vectorize questions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""

    if request.method == 'POST':
        user_input = request.form['message']

        user_vec = vectorizer.transform([user_input])
        similarity = cosine_similarity(user_vec, X)
        index_max = similarity.argmax()

        if similarity[0][index_max] < 0.3:
            response = "Sorry, I don't understand."
        else:
            response = answers[index_max]

    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)