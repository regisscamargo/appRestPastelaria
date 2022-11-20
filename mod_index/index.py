from flask import Blueprint, render_template

bp_index = Blueprint('index', __name__, url_prefix="/", template_folder='templates')

''' rotas dos formulários '''
@bp_index.route('/')
def formIndex():
    return render_template('formIndex.html'), 200

'''
Rota antiga de app...
@app.route('/funcionario/')
def formListaFuncionario():
    # return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
    return render_template('formListaFuncionario.html'), 200
'''