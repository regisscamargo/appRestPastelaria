from flask import Blueprint, render_template, request, redirect, url_for
import requests
from funcoes import Funcoes


bp_produto = Blueprint('produto', __name__, url_prefix="/produto", template_folder='templates')

''' endereços do endpoint '''
urlApiProdutos = "http://localhost:8000/produto/"
urlApiProduto = "http://localhost:8000/produto/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}


''' rotas dos formulários '''
@bp_produto.route('/', methods=['GET', 'POST'])
def formListaProduto():
    try:
        response = requests.get(urlApiProdutos, headers=headers)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result)
        return render_template('formListaProduto.html', result=result)
    except Exception as e:
        return render_template('formListaProduto.html', erro=e)

@bp_produto.route('/form-produto', methods=['GET', 'POST'])
def formProduto():
    return render_template('formProduto.html'), 200

@bp_produto.route('/insert', methods=['GET','POST'])
def insert():
    try:
        # dados enviados via FORM
        id_produto = 0
        nome = request.form['nome']
        valor_unitario = 10
        descricao = request.form['descricao']
        foto = request.form['foto']
        # monta o JSON para envio a API
        payload = {'id_produto': id_produto, 'nome': nome, 'valor_unitario': valor_unitario,'descricao': descricao}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(urlApiProdutos, headers=headers, json=payload)
        result = response.json()
        return redirect( url_for('produto.formListaProduto', msg=result) )
    except Exception as e:
        return render_template('formListaProduto.html', msgErro=e)
'''
Rota antiga de app...
@app.route('/funcionario/')
def formListaFuncionario():
    # return "<h1>Rota da página de Funcionários da nossa WEB APP</h1>", 200
    return render_template('formListaFuncionario.html'), 200
'''