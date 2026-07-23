# Sentiment-Journal

#### Video Demo:https://youtu.be/USpzdbSA08I?si=rf4rYbba97h76y2o
#### Description:

Sentiment Journal is a web-based journaling app that gives you instant emotional feedback on what you write. The idea is simple: you type a journal entry, hit submit, and the app tells you whether your writing came across as positive, negative, or neutral — along with a short supportive message and some color-coded styling to make the result feel intuitive at a glance. Green for positive, red for negative, and yellow-orange for neutral.

The motivation behind this project came from something pretty relatable. Journaling is one of the most common ways people process their thoughts and emotions, but it can be hard to notice emotional patterns while you're in the middle of writing. We wanted to build something that gives you a small moment of reflection right after you write — not a complex AI therapist, just a simple mirror that reads the emotional tone of your words and reflects it back to you. It's a lightweight tool, but it feels genuinely useful.

We designed Sentiment Journal to be intentionally simple and fully understandable. Every line of code in this project can be explained out loud without hesitation, which was something we cared about. CS50 pushes you to build things that are meaningful rather than just impressive on the surface, and that philosophy shaped every decision we made here.

How It Works

The backend is written in Python using Flask. All of the core logic lives in app.py, which handles routing, form submission, and sentiment analysis. The application runs on a single route that accepts both GET and POST requests. When you first load the page, Flask renders the template with no result displayed. When you submit an entry, a POST request is sent to the same route, Flask grabs your text from the form, analyzes it, and passes the result back to the template.

The sentiment analysis uses TextBlob, a Python library that assigns a polarity score to any piece of text on a scale from -1.0 (very negative) to 1.0 (very positive). We use simple conditional logic to classify the score into one of three categories. The thresholds were set manually so the behavior stays predictable and easy to explain — no black-box behavior here.

File Breakdown

app.py is the heart of the application. It imports Flask and TextBlob, defines the route, handles the form data, runs the sentiment analysis, and passes the result to the HTML template. It's short, clean, and readable by design.

templates/index.html defines the structure of the page. It uses Flask's Jinja2 templating engine to dynamically show the sentiment result, emoji, and message only after a submission has been made. The Jinja logic also applies the correct CSS class based on the sentiment value, which controls the color-coded visual feedback.

static/style.css handles all the visual design — layout, typography, spacing, and the three sentiment color schemes. Each sentiment category has its own class with a distinct border color and background tint, making the feedback immediately readable without needing to read the label.

Design Choices

We kept the project to a single-page application with no database and no user accounts. This was a deliberate choice. Adding a database would have introduced complexity that didn't serve the core purpose of the project, and authentication would have shifted the focus away from what we actually wanted to demonstrate: how Python, Flask, HTML, CSS, and NLP can work together in a clean, connected way.

We also chose Bootstrap for basic layout help while writing all the sentiment-specific styling ourselves. This kept the page looking clean without offloading too much of the design work to a framework.

Challenges

The most significant challenge we ran into was getting the dynamic CSS classes to work correctly with Jinja. Early on, our template logic was unintentionally overriding the CSS classes we'd written, so the colors either wouldn't appear at all or defaulted to the same style regardless of the sentiment. After a lot of testing, we figured out that using {{ result|lower }} directly inside the class attribute was the fix — it lets Jinja inject the correct class name cleanly so CSS can pick it up. That single realization made everything click into place, and it taught us a lot about how backend data, templates, and stylesheets actually talk to each other in a real web app.

On the backend side, the trickiest part was figuring out where to draw the line between positive, negative, and neutral. TextBlob gives you a polarity score, but it doesn't tell you what to do with it—that part was up to us. At first we used symmetric thresholds, treating anything above 0.1 as positive and anything below -0.1 as negative. The problem was that TextBlob leans slightly positive by default, so even fairly neutral-sounding entries kept getting classified as positive. We adjusted the thresholds after testing a bunch of real journal-style sentences, landing on above 0.2 for positive and below -0.1 for negative. It's not a perfect system, but it feels honest and consistent, which mattered more to us than chasing precision. We also had to handle the edge case where someone submits an empty form—without that check, TextBlob would run on an empty string and return a neutral result, which would be confusing. Adding a simple if user_input guard before any analysis made the behavior feel intentional rather than accidental.

Conclusion

Sentiment Journal is a complete, functional web application built on the concepts we developed throughout CS50. It's small enough to be fully understandable and large enough to feel like a real product. More than anything, it's a project we're proud of—not because of its complexity, but because of how clearly every piece of it connects.
