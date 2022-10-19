from flask import Blueprint, render_template

bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

''' rotas dos formulários '''
@bp_produto.route('/', methods=['GET', 'POST'])
def formListaProduto():
    return render_template('formListaProduto.html'), 200

@bp_produto.route('/form-produto', methods=['GET', 'POST'])
def formProduto():
    return render_template('formProduto.html'), 200

'''
Rota antiga de app...
@app.route('/funcionario/')
def formListaFuncionario():
    # return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
    return render_template('formListaFuncionario.html'), 200
'''