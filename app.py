from flask import Flask
from werkzeug.utils import import_string, cached_property
from datetime import datetime
import logging
import json

app = Flask(__name__)

class View(object):
    def __init__(self,funcao_importada):
        self.__module__, self.__name__ = funcao_importada.rsplit('.', 1)
        self.funcao_importada = funcao_importada
    @cached_property
    def view(self):
        return import_string(self.funcao_importada)
    def __call__(self, *args, **kwargs):
        return self.view(*args, **kwargs)

class DefinicaoRota:
    def __init__(self,nome,servico,rota,parametros):
        self.nome = nome
        self.servico = servico
        self.rota = rota
        self.parametros = parametros
        self._criarRota()
    
    def __str__(self) -> str:
        return f'[ROTA] {self.nome}: {self.rota} | {self.servico} | opts: {self.parametros}'
    
    def _criarRota(self):
        app.add_url_rule(
            self.rota,
            view_func=View(self.servico),
            methods=self.parametros['methods']
        )

def construirRotas():
    app.logger.info('[ --------------- INICIANDO SERVIDOR --------------- ]')
    rotas = []
    path_mapa_servicos = 'mapa_servicos.json'
    MAPA_SERVICOS = json.load(open(path_mapa_servicos,encoding='utf-8'))
    app.logger.info('> Arquivo do Mapa de Serviços lido com sucesso! [{}]'.format(path_mapa_servicos))
    try:    
        for pasta in MAPA_SERVICOS.keys():
            grupos_pasta = MAPA_SERVICOS[pasta]
            for grupo in grupos_pasta.keys():
                for serv in grupos_pasta[grupo]:
                    funcao_completa = 'servicos.'+pasta+'.'+grupo+'.'+serv['funcao']
                    rota = DefinicaoRota(serv['nome_servico'], funcao_completa, serv['rota'], serv['parametros'])
                    rotas.append(rota)
        app.logger.info('> As {} rotas criadas com sucesso!'.format(len(rotas)))
        return rotas
    except Exception as e:
        app.logger.error('[ERRO] Houve algum problema ao criar as rotas! [{}]'.format(e))
        return rotas

if __name__ == '__main__':
    app.secret_key = 'vito!'
    logging.basicConfig(filename='logs/aplicacao/LOG_{}.log'.format(datetime.now().strftime('%Y%m%d_%H%M%S')), level=logging.DEBUG, encoding='utf-8', format='[%(asctime)s] [%(levelname)s]\t%(message)s')
    construirRotas()
    app.run(host='0.0.0.0',port=5000,debug=True)
