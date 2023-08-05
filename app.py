from flask import Flask, render_template, request
from Nodejs_scrapper import scrape_nodejs_docs
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        keyword = request.form["keyword"]
        result = scrape_nodejs_docs(keyword)
        return render_template("index.html", result=result, keyword=keyword)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
