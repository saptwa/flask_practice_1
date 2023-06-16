from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Devops Engineer',
  'location': 'Munich, Germany',
  'salary': '64,000 €'
}, {
  'id': 2,
  'title': 'Backend Engineer',
  'location': 'Munich, Germany',
  'salary': '65,000 €'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Berlin, Germany',
  'salary': '62,000 €'
}, {
  'id': 4,
  'title': 'UI/UX Designer',
  'location': 'Frankfurt, Germany',
  'salary': '60,000 €'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
