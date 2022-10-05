from flask import Flask

# import blueprint criado
from mod_funcionario.funcionario import bp_funcionario
from mod_cliente.cliente import bp_cliente
from mod_produto.produto import bp_produto
from mod_index.index import bp_index
from mod_erro.erro import bp_erro

app = Flask(__name__)
# registro das rotas do blueprint
app.register_blueprint(bp_funcionario)
app.register_blueprint(bp_cliente)
app.register_blueprint(bp_produto)
app.register_blueprint(bp_index)
app.register_blueprint(bp_erro)

if __name__ == "__main__":
    """ Inicia o aplicativo WEB Flask """
    app.run(host='0.0.0.0', port=5000, debug=True)