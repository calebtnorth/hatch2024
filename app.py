from flask import (
    Flask,
    request,
    redirect,
    alert,
    render_template_string,
    send_from_directory
    
)
from requests import get
from os import path, getcwd, getenv
from acgtsec.decrypt import userCheck, Decrypt, grabFasta
from acgtsec.database import makeTable, newFileSignal
from acgtalgo.genetics import generate_chemical_weight

app = Flask(__name__, root_path=path.join(getcwd(), "acgtsite"))
app.config["UPLOAD_FOLDER"] = "/Users/calebnorth/Desktop/hatchdata/upload"

@app.route("/")
def blank():
    return redirect("/home.html")

@app.route("/home.html")
def home():
    with open("acgtsite/home.html") as file:
        return render_template_string(file.read())
    
@app.route("/index.html")
def index():
    with open("acgtsite/index.html") as file:
        return render_template_string(file.read(), log_visible = "visible", upload_visible = "hidden")
    
### POST
@app.route("/login", methods=["POST"])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if userCheck(username, password):
            redirect("/index.html")
    with open("acgtsite/index.html") as file:
        return render_template_string(file.read(), log_visible = "hidden", upload_visible = "visible")
    
### UPLOAD
@app.route('/upload', methods=['POST']) 
def upload_file():
    print('asdfsadf')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        file.save(path.join(app.config['UPLOAD_FOLDER'], file.filename))

        # Example usage
        db_file = 'client.db'
        table_name = 'client'

        makeTable(db_file, table_name)
        newFileSignal('client','MTFSA')

        decrypted = Decrypt()

        with open("acgtsite/index.html") as file:
            newFileSignal("client", "MTHFR")
            return render_template_string(file.read(), log_visible = "hidden", upload_visible = "visible")
    

### INTERNAL FILE SERVING (DEBUG ONLY)
# nginx replaces this functionally on the server side
# this should NEVER be called in production
@app.route("/<string:resource>/<path:filename>")
def send_resource(resource, filename):
    if app.debug == True:
        return send_from_directory(resource, filename)
    return "Bad request", 400