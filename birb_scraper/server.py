from flask import Flask, render_template, request, redirect, send_file
from getBirbs import get_jobs

app = Flask("scraper!!!")

db = {}

@app.route("/")
def home():
    return render_template("h.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/info")
def info():
    return render_template("work-single.html")


@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        job_exists = db.get(word)
        if job_exists:
            jobs = job_exists
        else:
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("index.html", searchWord=word, jobCnt=len(jobs), jobs=jobs)


