from flask import Flask, request, render_template, redirect
# email user specific developer jobs at a given location
import requests  # for api
import smtplib  # for emails
import auth  # custom module


app = Flask(__name__)  # instantiate app

user_location = []
user_job_type = []
# make home endpoint
@app.route('/', methods=["GET", "POST"])  # need post request to get inputs from html forum
def home():
    # if change is made to website
    if request.method == "POST":
        # get inputs from html
        location = request.form.get("location")  # get location specified
        user_location.append(location)
        # get job type from html
        description = request.form.get("job_type")
        user_job_type.append(description)
        user = Jobs()
        user.send_jobs()
        # re-direct to update end point
        return redirect("/update")
    return render_template("index.html")

@app.route('/update', methods=["GET"])
def update():
    # when post form is submitted
    return render_template("update.html")

class Jobs:
    URL = "https://jobs.github.com/positions"  # base url for API
    jobs_data = []  # json data

    def _jobs_api(self):  # get json data (jobs)
        response = requests.get(Jobs.URL,
                                headers={"Accept": "application/json"},
                                params={"location": user_location[0], "description": user_job_type[0]}  # query params
                                )
        data = response.json()
        Jobs.jobs_data.append(data)  # data is json filtered with user input and appended to class attr
        return Jobs.jobs_data

    def _job_links(self):
        links = []
        data = self._jobs_api()  # run internal method to iterate over Jobs.jobs_data
        for job in data:
            for link in job:
                job_link = link['url']  # key 'url' to GitHub Jobs
                links.append(job_link)
        return links

    def send_jobs(self):  # email auth
        links = self._job_links()
        if links:
            smpt_object = smtplib.SMTP('smtp.gmail.com', 587)
            smpt_object.ehlo()
            smpt_object.starttls()
            # use own authentication data
            email = auth.email()
            password = auth.password()
            smpt_object.login(email, password)
            # next, send the message
            from_address = email
            to_address = email
            subject = "Developer Jobs Update"
            message = f"Here are a few {user_job_type[0]} jobs located in {user_location[0]} you may be interested in!\n{links}"  # message changes depending on user input
            msg = "Subject: "+subject+"\n"+message
            # send mail and quit
            smpt_object.sendmail(from_address, to_address, msg)
            smpt_object.quit()

# only run if this file is called
if __name__ == '__main__':
    app.run()
