from flask import Flask, render_template

# criar app
app = Flask(__name__)
app.config['DEBUG'] = True  # Habilitar modo de depuração

# criar primeira rota(pagina)
@app.route("/")
def homepage():
    return render_template('homepage.html')

# rodar o nosso app
if __name__ == "__main__":
    app.run()