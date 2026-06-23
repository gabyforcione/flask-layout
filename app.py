from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    aluno = {
        "nome": "gaby forcione",
        "turma": "1 medio"
    }
    professor = [
        {
            "nome": "Felipe Ishara",
            "materia": "web"
        },
        {
            "nome": "welligton",
            "materia": "historia"      
        }
    ]
    return render_template('index.html', title='home', aluno=aluno)

@app.route("/boletim")
def boletim():
    return render_template('boletim.html', title='boletim')
