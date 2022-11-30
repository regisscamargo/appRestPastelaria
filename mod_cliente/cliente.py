from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import requests
from funcoes import Funcoes
from mod_login.login import validaSessao


bp_cliente = Blueprint('cliente', __name__, url_prefix="/cliente", template_folder='templates')

''' endereços do endpoint '''
urlApiClientes = "http://localhost:8000/cliente/"
urlApiCliente = "http://localhost:8000/cliente/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas dos formulários '''
@bp_cliente.route('/', methods=['GET', 'POST'])
@validaSessao
def formListaCliente():
    try:
        response = requests.get(urlApiClientes, headers=headers)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result)
        return render_template('formListaCliente.html', result=result)
    except Exception as e:
        return render_template('formListaCliente.html', erro=e)

@bp_cliente.route('/form-cliente', methods=['GET', 'POST'])
@validaSessao
def formCliente():
    return render_template('formCliente.html'), 200

@bp_cliente.route('/insert', methods=['GET','POST'])
def insert():
    try:
        # dados enviados via FORM
        id_cliente = 0
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        dia_fiado = 5
        compra_fiado = True
        senha = Funcoes.cifraSenha(request.form['senha'])
        # monta o JSON para envio a API
        payload = {'id_cliente': id_cliente, 'nome': nome,'cpf': cpf, 'telefone': telefone, 'dia_fiado': dia_fiado, 'senha': senha, 'compra_fiado': compra_fiado}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(urlApiClientes, headers=headers, json=payload)
        result = response.json()
        return redirect(url_for('cliente.formListaCliente', msg=result) )
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e)

@bp_cliente.route("/form-edit-cliente", methods=['POST'])
def formEditCliente():
    try:
        # ID enviado via FORM
        id_cliente = request.form['id']
        # executa o verbo GET da API buscando somente o funcionário selecionado,
        # obtendo o JSON do retorno
        response = requests.get(urlApiClientes + id_cliente, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
            # renderiza o form passando os dados retornados
        return render_template('formCliente.html', result=result[0])
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])
    
@bp_cliente.route('/edit', methods=['POST'])
def edit():
    try:
        # dados enviados via FORM
        id_cliente = request.form['id']
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        dia_fiado = 5
        compra_fiado = True
        senha = Funcoes.cifraSenha(request.form['senha'])
        # monta o JSON para envio a API
        payload = {'id_cliente': id_cliente, 'nome': nome,'cpf': cpf, 'telefone': telefone, 'dia_fiado': dia_fiado, 'senha': senha, 'compra_fiado': compra_fiado}

        # executa o verbo PUT da API e armazena seu retorno
        response = requests.put(urlApiClientes + id_cliente, headers=headers, json=payload)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return redirect( url_for('cliente.formListaCliente', msg=result[0]) )
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])
    
@bp_cliente.route('/delete', methods=['POST'])
def delete():
    try:
        # dados enviados via FORM
        id_cliente = request.form['id_cliente']
        # executa o verbo DELETE da API e armazena seu retorno
        response = requests.delete(urlApiClientes + id_cliente, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return redirect(url_for('cliente.formListaCliente', msg=result[0]))
        #print(result[0])
        #{'msg': 'Excluído com sucesso!', 'id': 4}
        #return jsonify(erro=False, msg=result[0])
    except Exception as e:
        return render_template('formListaCliente.html', msgErro=e.args[0])
        #return jsonify(erro=True, msgErro=e.args[0])