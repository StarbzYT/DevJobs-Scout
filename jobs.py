# email user specific developer jobs at a given location
import requests  # for api
import smtplib  # for emails
import auth  # custom module


class Jobs:
    location = ""  # user location
    description = ""  # user description (type of developer)
    URL = "https://jobs.github.com/positions"  # base url for API
    jobs_data = []  # json data

    def _jobs_api(self):  # get json data (jobs)
        response = requests.get(Jobs.URL,
                                headers={"Accept": "application/json"},
                                params={"location": location, "description": description}  # query params
                                )
        data = response.json()
        Jobs.jobs_data.append(data)  # data is json filtered with user input and appended to class attr
        Jobs.description = description
        Jobs.location = location
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
            subject = "Developer Jobs"
            message = f"Here are a few {Jobs.description} jobs located in {Jobs.location} you may be interested in!\n{links}"  # message changes depending on user input
            msg = "Subject: "+subject+"\n"+message
            print("Check your email, I found something for you! \U0001f601")
            # send mail and quit
            smpt_object.sendmail(from_address, to_address, msg)
            smpt_object.quit()
        else:
            print(f"Sorry, I could not find any {Jobs.description} jobs in {Jobs.location} for you... \U0001f605")

# only run if this file is called
if __name__ == '__main__':
    user = Jobs()
    # user.send_jobs()
    user.send_jobs()