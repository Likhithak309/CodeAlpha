from flask import Flask, render_template, request

app = Flask(__name__)

# Simple dictionary-based translation
translations = {
    "hello": "नमस्ते",
    "how are you": "आप कैसे हैं",
    "i am fine": "मैं ठीक हूँ",
    "what is your name": "आपका नाम क्या है",
    "thank you": "धन्यवाद",
    "good morning": "सुप्रभात",
    "good evening": "शुभ संध्या",
    "where are you": "आप कहाँ हैं",
    "i am learning ai": "मैं एआई सीख रहा हूँ",
    "this is my project": "यह मेरा प्रोजेक्ट है"
}

reverse_translations = {v: k for k, v in translations.items()}

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""

    if request.method == 'POST':
        text = request.form['text'].lower().strip()
        src = request.form['source']
        dest = request.form['target']

        if not text:
            translated_text = "Please enter some text"

        elif src == dest:
            translated_text = "Choose different languages"

        else:
            if src == "en" and dest == "hi":
                translated_text = translations.get(text, "Translation not found")

            elif src == "hi" and dest == "en":
                translated_text = reverse_translations.get(text, "Translation not found")

            else:
                translated_text = "Unsupported language"

    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)