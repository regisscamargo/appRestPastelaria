from flask import Blueprint, render_template, request, redirect, url_for, jsonify
import requests
from funcoes import Funcoes
from mod_login.login import validaSessao

bp_funcionario = Blueprint(
    'funcionario', __name__, url_prefix="/funcionario", template_folder='templates')

''' endereços do endpoint '''
urlApiFuncionarios = "http://localhost:8000/funcionario/"
urlApiFuncionario = "http://localhost:8000/funcionario/%s"
headers = {'x-token': 'abcBolinhasToken', 'x-key': 'abcBolinhasKey'}

''' rotas '''
@bp_funcionario.route('/', methods=['GET', 'POST'])
@validaSessao
def formListaFuncionario():
    try:
        response = requests.get(urlApiFuncionarios, headers=headers)
        result = response.json()
        if (response.status_code != 200):
            raise Exception(result)
        return render_template('formListaFuncionario.html', result=result)
    except Exception as e:
        return render_template('formListaFuncionario.html', erro=e)

@bp_funcionario.route('/form-funcionario/', methods=['POST'])
@validaSessao
def formFuncionario():
    return render_template('formFuncionario.html')

@bp_funcionario.route('/insert', methods=['GET','POST'])
def insert():
    try:
        # dados enviados via FORM
        id_funcionario = 0
        nome = request.form['nome']
        matricula = request.form['matricula']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = Funcoes.cifraSenha(request.form['senha'])
        # monta o JSON para envio a API
        payload = {'id_funcionario': id_funcionario, 'nome': nome, 'matricula': matricula,'cpf': cpf, 'telefone': telefone, 'grupo': grupo, 'senha': senha}
        # executa o verbo POST da API e armazena seu retorno
        response = requests.post(urlApiFuncionarios, headers=headers, json=payload)
        result = response.json()
        return redirect( url_for('funcionario.formListaFuncionario', msg=result) )
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e)
    
@bp_funcionario.route("/form-edit-funcionario", methods=['POST'])
@validaSessao
def formEditFuncionario():
    try:
        # ID enviado via FORM
        id_funcionario = request.form['id']
        # executa o verbo GET da API buscando somente o funcionário selecionado,
        # obtendo o JSON do retorno
        response = requests.get(urlApiFuncionarios + id_funcionario, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 200):
            raise Exception(result[0])
            # renderiza o form passando os dados retornados
        return render_template('formFuncionario.html', result=result[0])
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])
    
@bp_funcionario.route('/edit', methods=['POST'])
def edit():
    try:
        # dados enviados via FORM
        id_funcionario = request.form['id']
        nome = request.form['nome']
        matricula = request.form['matricula']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        grupo = request.form['grupo']
        senha = Funcoes.cifraSenha(request.form['senha'])
        # monta o JSON para envio a API
        payload = {'id_funcionario': id_funcionario, 'nome': nome, 'matricula': matricula,'cpf': cpf, 'telefone':

        telefone, 'grupo': grupo, 'senha': senha}

        # executa o verbo PUT da API e armazena seu retorno
        response = requests.put(urlApiFuncionarios + id_funcionario, headers=headers, json=payload)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return redirect( url_for('funcionario.formListaFuncionario', msg=result[0]) )
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])
    
@bp_funcionario.route('/delete', methods=['POST'])
def delete():
    try:
        # dados enviados via FORM
        id_funcionario = request.form['id_funcionario']
        # executa o verbo DELETE da API e armazena seu retorno
        response = requests.delete(urlApiFuncionarios + id_funcionario, headers=headers)
        result = response.json()
        if (response.status_code != 200 or result[1] != 201):
            raise Exception(result[0])
        return redirect(url_for('funcionario.formListaFuncionario', msg=result[0]))
        #print(result[0])
        #{'msg': 'Excluído com sucesso!', 'id': 4}
        #return jsonify(erro=False, msg=result[0])
    except Exception as e:
        return render_template('formListaFuncionario.html', msgErro=e.args[0])
        #return jsonify(erro=True, msgErro=e.args[0])