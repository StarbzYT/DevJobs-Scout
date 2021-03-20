from flask import Flask, request, render_template
import jobs  # file to find jobs

app = Flask(__name__)  # instantiate app

# make home endpoint
@app.route('/', methods=["GET", "POST"])  # need post request to get inputs from html forum
def home():
    # if change is made to website
    if request.method == "POST":
        # get inputs from html
        location = request.form.get("location")  # get location specified
        # get job type from html
        job_type = request.form.get("job_type")
        return "Thank you for using DevJobs Scout!"
    return render_template("index.html")

# only run if this file is called
if __name__ == '__main__':
    app.run()
