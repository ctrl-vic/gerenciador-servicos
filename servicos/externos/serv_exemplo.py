# ------------------------------------------------------------------------------------------------------------
#      < SERVIÇO DE EXEMPLO >
#   Este é um exemplo do que seria um serviço externo.
#   Atualmente as seguintes rotas/funções estão implementadas:
#
#       /teste/                  user : pág. de visualização de usuários
# 
# 
# ------------------------------------------------------------------------------------------------------------

def teste():
    print('teste')
    return 'teste'

# logging.basicConfig(filename='logs/logs_app/LOG_{}.log'.format(datetime.now().strftime('%Y%m%d_%H%M%S')), level=logging.DEBUG, encoding='utf-8', format='[%(asctime)s] [%(levelname)s]\t%(message)s')