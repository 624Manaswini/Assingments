from flask import Flask, request

app = Flask(__name__)

@app.route("/favicon.ico")  
def favicon():
    return app.send_static_file("favicon.ico")


@app.route("/")
def home():
    return """
  <html>
  <head><title>Daily Notepad</title></head>
  <body>
    <h2>Welcome to Notepad</h2>
    <h3>Click the below links and start your day</h3>
    <ul>
      <li><a href='/updatefortoday'>Write Today's Note</a></li><br>
      <li><a href='/share'>View today's Notes</a></li><br>
      <li><a href='/clearnotepadtxt'>Erase All Notes</a></li>
    </ul>
  </body>
  </html>
  """



@app.route("/updatefortoday", methods=["GET", "POST"])
def writenote():
  if request.method == "POST":
    content = request.form.get("note", "")
    with open("notepad.txt", "a") as f:
      f.writelines(content + "\n")
    return "<p>Note added!</p><a href='/'>Back to Home</a>"
  return """
  <html>
  <head><title>Write Note</title></head>
  <body>
    <form method="post" action="/updatefortoday">
      <textarea name="note" rows="8" cols="50"></textarea><br><br>
      <input type="submit" value="Save Note here" />
    </form>
  </body>
  </html>
  """

@app.route("/share", methods = ["GET"])
def view():
  try:
    with open("notepad.txt", "r") as f:
      notes = f.readlines()
  except FileNotFoundError:
    notes = "No notes available."
  return f"<pre>{notes}</pre><a href='/'>Back to Home</a>"

@app.route("/clearnotepadtxt", methods = ["GET"])
def clear():
  open("notepad.txt", "w").close()
  return "<p>All notes have been erased.</p><a href='/'>Back to Home</a>"

if __name__ == "__main__":
  app.run()
