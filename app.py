
from flask import Flask, render_template, request, redirect, session
from datetime import datetime, timedelta, date
import datetime

#ask stuff
goal = input("What is your goal?")
deadline = input("When is the deadline for this goal (Y-M-D)?")
people = int(input("How many people are involved in this goal?"))
time_limit = int(input("How many hours in a day can you dedicate to this goal?"))
deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d").date()

#days til deadline
days_left = deadline - datetime.date.today()
num_days = days_left.days

total_hrs = num_days* time_limit *people

time_limit = total_hrs / num_days

time_limit = time_limit /people

tasks =[]
for i in range(num_days):
    task = f"Day {i +1}: Spend time working on {time_limit} hours on {goal}"
    tasks.append(task)

for task in tasks:
    print(task)

if people + goal + deadline == 0:
    print("Please re=enter your input. For any questions and concerns, please contact 484-620-2787")

def generate_data(goal, deadline, time_limit, people):
    goals_data ={
        "goal":goal,
        "deadline": deadline,
        "time_limit": time_limit,
        "total_hrs": total_hrs,
        "task" : task
    }
    return goals_data   

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        progress_bar =[]
        for day in range(days_left):
            progress_bar.append(time_limit)
        return render_template("timeline.html", progress_bar=progress_bar)
    return render_template("index.html")

@app.route("/timeline")
def timeline():
    return render_template("timeline.html")

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







