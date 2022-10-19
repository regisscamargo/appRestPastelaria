from flask import Blueprint, render_template

bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' rotas dos formulários '''
@bp_cliente.route('/', methods=['GET', 'POST'])
def formListaCliente():
    return render_template('formListaCliente.html'), 200

@bp_cliente.route('/form-cliente', methods=['GET', 'POST'])
def formCliente():
    return render_template('formCliente.html'), 200

'''
Rota antiga de app...
@app.route('/funcionario/')
def formListaFuncionario():
    # return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
    return render_template('formListaFuncionario.html'), 200
'''