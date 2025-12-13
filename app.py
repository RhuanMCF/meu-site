from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'mude-esta-chave-depois'  # segurança

# ============================
#       ROTA DE LOGIN
# ============================
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario').strip().lower()
        senha = request.form.get('senha').strip()

        # --- LOGIN DO ADMIN ---
        if usuario == 'admin' and senha == 'admin123':
            session['usuario'] = 'admin'
            return redirect(url_for('admin'))

        # --- LOGIN DO BRUNO ---
        elif usuario == 'bruno' and senha == 'bruno123':
            session['usuario'] = 'bruno'
            return redirect(url_for('bruno'))

        # --- LOGIN DO ICARO ---
        elif usuario in ['icaro', 'ícaro'] and senha == 'icaro123':
            # Mantemos sem acento dentro da sessão para evitar bug
            session['usuario'] = 'icaro'
            return redirect(url_for('icaro'))

        # --- LOGIN INVÁLIDO ---
        else:
            flash('Usuário ou senha incorretos!')

    return render_template('login.html')


# ============================
#       ROTAS PROTEGIDAS
# ============================

@app.route('/admin')
def admin():
    if session.get('usuario') != 'admin':
        return redirect(url_for('login'))
    return render_template('admin.html')


@app.route('/bruno')
def bruno():
    if session.get('usuario') != 'bruno':
        return redirect(url_for('login'))
    return render_template('bruno.html')


@app.route('/icaro')
def icaro():
    if session.get('usuario') != 'icaro':
        return redirect(url_for('login'))
    return render_template('icaro.html')


# ============================
#       LOGOUT
# ============================
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ============================
#       EXECUÇÃO
# ============================
if __name__ == '__main__':
    app.run(debug=True)