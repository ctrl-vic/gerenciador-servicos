# ------------------------------------------------------------------------------------------------------------
#      < SERVIÇOS DE GERENCIAMENTO DE USUÁRIOS >
#   Aqui estão todos os serviços relacionados as funções de gerenciamento de usuários, grupos e tokens.
#   Atualmente as seguintes rotas/funções estão implementadas:
#
#       /user/                  user : pág. de visualização de usuários
#       /user/<username>        user_param: pág. de visualização de um usuario específico
# 
# 
# ------------------------------------------------------------------------------------------------------------

def user_param(username):
    print('user-', username)
    return 'user-'+str(username)

def user():
    return 'user-vazio'


# ------------------------------------------------------------------------------------------------------------






# @app.route('/semanola', methods=['GET','POST'])
# def semanola_tools():
#     # if request.method == 'GET':
#     #     # render a pagina normal para digitar o usuario
#     # else:
#     #     # se for post, pegar o usuário e carregar
#     #     lfm_user = request.form.get('lfm_user')
#     return render_template(
#         r'semanola.html',
#         tipos_periodo=tipos_periodo,
#         tipos_legenda=tipos_legenda,
#         tamanhos_validos=tamanhos_validos,
#         tipos_ordenacao=tipos_ordenacao,
#     )

# @app.route('/semanola/carregarUsuario/<usuario>', methods=['POST'])
# def semanola_carregar_user(usuario):
#     return jsonify(carregarUsuario(usuario))
