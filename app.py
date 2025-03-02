from flask import Flask, request, render_template
import google.generativeai as genai

# Initialize Flask App
app = Flask(__name__)

# API Key Setup
genai.configure(api_key="AIzaSyA2p0be7RlKKcUsG6xyq6MdZU24Rpc2C-A")

# Use the latest model
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    article = ""
    if request.method == "POST":
        topic = request.form.get("topic")
        if topic:
            try:
                response = model.generate_content(topic)
                if hasattr(response, "text"):
                    article = response.text
                else:
                    article = "Failed to generate content."
            except Exception as e:
                article = f"Error: {str(e)}"
    return render_template("index.html", article=article)

if __name__ == "__main__":
    app.run(debug=True)
