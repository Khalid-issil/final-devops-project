from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
task_id_counter = 1


@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    global task_id_counter

    title = request.form.get("title", "").strip()

    if title:
        tasks.append({
            "id": task_id_counter,
            "title": title
        })
        task_id_counter += 1

    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("home"))


@app.route("/health")
def health():
    return {"status": "ok", "app": "DevOps Task Manager"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)