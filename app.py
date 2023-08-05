from flask import Flask, render_template, request
from Nodejs_scrapper import scrape_nodejs_documentation

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        if keyword:
            description = scrape_nodejs_documentation(keyword)
            return render_template("index.html", description=description)
    
    return render_template("index.html", description=None)

if __name__ == "__main__":
    app.run(debug=True)
