from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        user_input = request.form.get("journal_text")

        if user_input:
            blob = TextBlob(user_input)

            if blob.sentiment.polarity > 0.1:
                result = "Positive"
            elif blob.sentiment.polarity < -0.1:
                result = "Negative"
            else:
                result = "Neutral"
        else:
            result = "You didn't type anything!"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)