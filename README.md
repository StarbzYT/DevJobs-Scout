# **Developer Jobs Scout**

---

## **About**

This is a **DevJobs Web Application** made with *Python* (_flask framework_), **HTML** and **CSS** that allows the user to:

> - _**Search**_ for a location and type of dev job they are interested in
> - _**Receive**_ an email if jobs in the specified location were found

---

## **The Result**

## Home Page

![devjobs home](https://user-images.githubusercontent.com/57025422/111890813-652fa900-89aa-11eb-8f86-2d22ba656b14.PNG)

## Success Page

![devjobs update](https://user-images.githubusercontent.com/57025422/111890809-5ea13180-89aa-11eb-85b4-c76baf75b8fb.PNG)

CSS was _decent_...

---

### **Potential improvements:**

> - Deal with the edge cases appropriately (i.e false input/invalid locations or jobs)
> - Implement user authentication (allow anyone to enter their email for a subscription)

---

## **Install**

```bash
pip install flask
```

---

## **Import**

```python
from flask import Flask, request, render_template, redirect
import requests
import smtplib
import auth
```

---

## **Run**

```bash
set FLASK_APP=app.py
set FLASK_DEBUG=1
flask run
```

---

### **Inspiration**

I took an old project from last year (a terminal tool) and created a frontend for it (to make it more visual).
