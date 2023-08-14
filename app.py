from flask import Flask, render_template

# Inicialize o Flask
app = Flask(__name__)

# Defina a rota e a função da view 
@app.route('/')
def hello_world():
    return render_template('homepage.html')

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)


# Executa o aplicativo se o arquivo for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)
