"""
This is Finanal assignment: Python Web Application Creation and Deployment
"""
from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    ''' english to french endpoint '''
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text = translator.english_to_french(textToTranslate)
    # return "Translated text to French"
    return "Translated text to French : " + french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    ''' french to english endpoint '''
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text = translator.french_to_english(textToTranslate)
    # return "Translated text to English"
    return "Translated text to English : " + english_text

@app.route("/")
def render_index_page():
    ''' render page index.html ('/') '''
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
