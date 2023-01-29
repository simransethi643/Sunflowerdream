
from flask import Flask, render_template, request, redirect, session
from datetime import timedelta, date
import datetime

goal = input("What is your goal?")
deadline = input("When is the deadline for this goal (Y-M-D)?")
people = input("How many people are involved in this goal?")
deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d").date()

#days til deadline
days_til_deadline = (deadline - datetime.date.today()).days
tasks_per_week = days_til_deadline // 7

tasks =[]
for i in range (1, days_til_deadline +1):
    day_of_week = datetime.date.today() +datetime.timedelta(days=i)
    task = "Task" +str(i) +":" + goal +"( "+ day_of_week.strftime("%A")
    tasks.append(task)
print("Tasks for each day of the week:")
for task in tasks: 
    print(task)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/goal', methods =['POST YOUR PROOF'])
def goal():
    goal = request.form['goal']
    deadline = request.form['deadline']
    return render_template('goal.html', goal=goal, deadline=deadline)

@app.route('/proof', methods =['POST YOUR PROOF'])
def proof():
    proof = request.form['proof']
    return render_template('proof.html', proof=proof)

if __name__ == '__main__':
    app.run()





