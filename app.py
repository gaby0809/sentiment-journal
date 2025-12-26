# Import Flask and TextBlob libraries
from flask import Flask, render_template, request
from textblob import TextBlob

# Create Flask application
app = Flask(__name__)

# Display the index page and handle form submission
@app.route("/", methods=["GET", "POST"])
def index():
    # This stores the sentiment result that is shown to the user
    result = ""
    
    # Check if the user submitted the form
    if request.method == "POST":
        # Get the text the user wrote in the journal
        user_input = request.form.get("journal_text")

        # Only analyze if text was entered
        if user_input:
            # Create a TextBlob object
            blob = TextBlob(user_input)

            # Determine sentiment based on polarity
            if blob.sentiment.polarity > 0.1:
                result = "Positive"
            elif blob.sentiment.polarity < -0.1:
                result = "Negative"
            else:
                result = "Neutral"
        else:
            # This is if no text was entered
            result = "You didn't type anything!"

    # Send result back to the HTML template
    return render_template("index.html", result=result)

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)