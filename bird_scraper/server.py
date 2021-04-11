from flask import Flask, render_template, request, redirect, send_file
from sof import get_jobs
from exporter import save_to_file

app = Flask("scrapper!!!")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

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
    return render_template("report.html", searchWord=word, jobCnt=len(jobs), jobs=jobs)

@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        print("hungry")
        return send_file("jobs.csv", as_attachment=True)
        
    except:
        return redirect("/")
