from flask import Flask, render_template, jsonify


app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Jaipur',
        'salary': 'Rs. 10,000,00'

    },
    {
        'id': 1,
        'title': 'Devops Engineer',
        'location': 'Bengaluru',
        'salary': 'Rs. 10,000,00'

    },
    {
        'id': 1,
        'title': 'Data Engineer',
        'location': 'Remote',
        'salary': 'Rs. 15,000,00'

    },
    {
        'id': 4,
        'title': 'Python Developer',
        'location': 'Delhi',
        'salary': 'Rs.10,000,00'

    }
]

@app.route("/")
def index():
    return render_template("home.html", JOBS=JOBS)

@app.route("/api/jobs")
def list_job():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)
    
