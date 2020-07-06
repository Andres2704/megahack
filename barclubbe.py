import os
import pymysql.cursors
import json
from flask import Flask,request, jsonify
class bar():
   
    def conexao(self):
        try:
            self.banco=pymysql.connect(
                host='us-cdbr-east-02.cleardb.com',
                user='bb00afca6be4ac',
                password='b1837325',
                db='heroku_2bef9f5656163b1',
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
        except:
            return('erro ao conectar com o bd e pisa mole ')    

    def VerificaLoginBar(self,usuario,senha):#OK
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('select * from bdbar')
                self.resultados = self.cursor.fetchall()
        except:
            return('erro ao fazer a consulta')
        for linha in self.resultados:
            if usuario == linha['strEmail'] and senha == linha['strSenha']:##Usuario e senha digitados
                id_env=linha['idBar']
                break
            else:
                id_env = 0
        return id_env
        
    def VerificarEmail(self,email): #OK

        #self.find = False
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('select * from bdbar')
                self.resultados = self.cursor.fetchall()
        except:
            print('erro ao fazer a consulta')
        for linha in self.resultados:
            if email == linha['strEmail']:
                return True
            else:
                return False                 
   
    def CadastrarBar(self,Email,Senha,Nome,cnpjbar,enderecobar,logo): #OK

        self.conexao()

        try:
            with self.banco.cursor() as self.cursor:
                sql = "INSERT INTO bdbar (strNome, strEndereco, strEmail, strSenha,intCNPJ, strLogo) values (%s,%s,%s,%s,%s,%s)"
                val = [Nome, enderecobar, Email, Senha, cnpjbar, logo]
                self.cursor.execute(sql, val)
                self.banco.commit()
                return True
                #self.VerificaLoginBar()
        except:
            return False
            #print("Erro ao fazer a inserção dos dados no bdbar")

    def InserirProduto(self,idbar,titulo,descricao,preco,tipo,foto):#OK
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                sql = "INSERT INTO bdproduto (idBar,strTitulo, strDescricao, dblPreco, intTipo, strFoto) values (%s,%s,%s,%s,%s,%s)"
                val = [idbar,titulo,descricao,preco,tipo,foto]
                self.cursor.execute(sql, val)
                self.banco.commit()
                return ("Cadastrado")
            
        except:
            return ("Erro ao fazer a inserção dos dados no bdproduto")

    def InserirEvento(self,idbar,titulo,descricao,foto,data):#OK
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                sql = "INSERT INTO bdevento (idBar, strTitulo, srtDescricao, strFoto, dtData) values (%s,%s,%s,%s,%s)"
                val = [idbar,titulo,descricao,foto,data]
                self.cursor.execute(sql, val)
                self.banco.commit()
                return ("Cadastrado")
            
        except:
            return ("Erro ao fazer a inserção dos dados no bdevento")
    
    '''#IMPLEMENTAÇÃO FUTURA (e-commerce)----------------------------------
    def Pedidos(self):##Salvação_do_grupo.png
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('SELECT * FROM bdpedido')
                self.pedidosBar = self.cursor.fetchall()
        except:
            print('erro ao fazer a consulta para os pedidos do bar')
         

        print('PRODUTO  |  CLIENTE   |  Tipo Entrega  |  Pagamento  |  Status')
        for i in self.pedidosBar:
            try:
                with self.banco.cursor() as self.cursor:
                    self.cursor.execute('SELECT strTitulo FROM bdproduto WHERE idProduto ={}'.format(int(i['idProduto'])))
                    self.produtoNome = self.cursor.fetchall()
            except:
                pass
            try:
                with self.banco.cursor() as self.cursor:
                    self.cursor.execute('SELECT strNome FROM bdcliente WHERE idCliente ={}'.format(int(i['idCliente'])))
                    self.clienteNome = self.cursor.fetchall()
            except:
                pass 
            
            if self.idBar==i['idBar']:
                print("{} {} {} {} {}".format(self.produtoNome[0]['strTitulo'], self.clienteNome[0]['strNome'], i['intTipoEntrega'], i['intTipoPagamento'], i['intStatus']))

        self.pedidosBar = json.dumps(self.pedidosBar) #DADOS DOS PEDIDOS
    '''
    def ListarProdutosBar(self,idBar):
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute("SELECT * FROM bdproduto WHERE idBar = {}". format(idBar))
                produtosBar = self.cursor.fetchall()
        except:
            print("erro ao fazer consulta bdprodutos - listarprodutosbar")
        
        #self.produtosdoBar = json.dumps(self.produtosBar) #LISTA DOS PRODUTOS QUE O BAR POSSUI QUANDO ESTE ESTÁ LOGADO
        return produtosBar
    def ListarReviewsBar(self,idBar):
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute("SELECT * FROM bdreview WHERE idBar = {}". format(idBar))
                reviewBar = self.cursor.fetchall()
        except:
            return("erro ao fazer consulta bdprodutos - listarprodutosbar")
        
        #self.produtosdoBar = json.dumps(self.produtosBar) #LISTA DOS PRODUTOS QUE O BAR POSSUI QUANDO ESTE ESTÁ LOGADO
        return reviewBar
    def ListarEventosBar(self, idBar):
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute("SELECT * FROM bdevento WHERE idBar = {}". format(idBar))
                eventosBar = self.cursor.fetchall()
        except:
            print("erro ao fazer consulta bdprodutos - listarprodutosbar")
        
        #self.eventosdoBar = json.dumps(self.eventosBar) #LISTA DOS EVENTOS QUE O BAR POSSUI QUANDO ESTE ESTÁ LOGADO
        return eventosBar
 
class user():

    def conexao(self):
        try:
            self.banco=pymysql.connect(
                host='us-cdbr-east-02.cleardb.com',
                user='bb00afca6be4ac',
                password='b1837325',
                db='heroku_2bef9f5656163b1',
                charset='utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
            )
            return("Conectado")
        except:
            return('erro ao conectar com o bd')    
    def CadastrarUsuario(self,Email,Senha,Nome,Persona,enderecoUsuario):
        
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                sql = "INSERT INTO bdcliente (strNome, intPersona,strEmail,strSenha,strEndereco) values (%s,%s,%s,%s,%s)"
                val = [Nome, Persona, Email, Senha, enderecoUsuario]
                self.cursor.execute(sql, val)
                self.banco.commit()
                return True
        except:
            return False
    def VerificaLogin(self,email,senha):
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('select * from bdcliente')
                self.resultados = self.cursor.fetchall()
        except:
            return('erro ao fazer a consulta')
        for linha in self.resultados:
            if email == linha['strEmail'] and senha == linha['strSenha']:##Usuario e senha digitados
                id_env=linha['idCliente']
                break
            else:
                id_env = 0
        return id_env
    def AddReview(self,idBar,idCliente,review,num_estrelas):
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                sql = "INSERT INTO bdreview (idBar,idCliente, strReview,intEstrelas) values (%s,%s,%s,%s)"
                val = [idBar, idCliente, review, num_estrelas]
                self.cursor.execute(sql, val)
                self.banco.commit()
                return("Cadastrado")
        except:
            return("Erro ao fazer a inserção dos dados")
    def VerificarEmail(self, email):

        self.find = False
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('select * from bdcliente')
                self.resultados = self.cursor.fetchall()
        except:
            print('erro ao fazer a consulta')
        for linha in self.resultados:
            if email == linha['strEmail']:
                ##self.find = True
                return True
            else:
                return False
    def ListarCervejas(self):
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('select * from bdcerveja')
                cervejas = self.cursor.fetchall()
        except:
            return('erro ao fazer a consulta no banco de dados bdCerveja')

        return cervejas #DADOS DAS CERVEJAS AQUI FIA DA PUTA te fode vagabundo
   def Listarbar(self):
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('select idBar, intCNPJ, strEmail, strEndereco, strLogo, strNome from bdbar')
                bares = self.cursor.fetchall()
        except:
            print('erro ao fazer a consulta - bdbar') 
            
        #self.dadosBares = json.dumps(self.bares) #DADOS DAS CERVEJAS AQUI FIA DA PU
        return bares
    def ListarFavoritos(self,idcliente):
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('SELECT * FROM bdfavoritos WHERE idCliente ={}'.format(idcliente))
                favoritos = self.cursor.fetchall()
        except:
            return('erro ao fazer a consulta - bdfavoritos')

        #self.dadosFavoritos = json.dumps(self.favoritos) #DADOS DAS CERVEJAS AQUI FIA DA PUTA te fode vagabundo
        return favoritos 
    def ListarColecao(self,idcliente):
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('SELECT * FROM bdfavoritocol WHERE idCliente ={}'.format(idcliente))
                colecao = self.cursor.fetchall()
        except:
            return('erro ao fazer a consulta - bdfavoritocol')

        return colecao
    '''#IMPLEMENTAÇÃO FUTURA (e-comerce)-------------------------------------
    def ListarPedidos(self):
        self.conexao()
        
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('SELECT * FROM bdpedido WHERE idCliente ={}'.format(self.idCliente))
                self.pedidos = self.cursor.fetchall()
        except:
            print('erro ao fazer a consulta - bdpedido')

        #self.dadosPedidos = json.dumps(self.pedidos) #Pedidos realizados 
        #print(self.dadosPedidos)
        return self.pedidos
    '''
    def ListarEventos(self,idBar):#OK
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('SELECT * FROM bdevento WHERE idBar ={}'.format(idBar))
                self.eventos = self.cursor.fetchall()
        except:
            return('erro ao fazer a consulta - bdevento')

        #self.dadosEventos = json.dumps(self.eventos) #Eventos disponíveis 
        return(self.eventos)
    def ListarConquistas(self,idinsignia):
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('SELECT * FROM bdconquista')
                resultado = self.cursor.fetchall()
        except:
            return ('erro ao fazer a consulta - bdproduto')

        return resultado
    def ListarProdutos(self,idBar):#OK
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('SELECT * FROM bdproduto WHERE idBar ={}'.format(idBar))
                self.produtos = self.cursor.fetchall()
        except:
            return ('erro ao fazer a consulta - bdproduto')

        return self.produtos
    def ListarInsignias(self):
        self.conexao()
        try:
            with self.banco.cursor() as self.cursor:
                self.cursor.execute('SELECT * FROM bdinsigena')     
                resultados = self.cursor.fetchall()
        except:
            return ('erro ao fazer a consulta - bdinsigena')
        return resultados   

app = Flask(__name__)
app.config["DEBUG"] = True
###HOME---------------------------------------------------------------------
@app.route('/', methods=['GET'])
def home():
    return "<h1>Ambev club</h1><p>API do API do birubiru.</p>"
###INSIGNIAS----------------------------------------------------------------
@app.route('/api/usuario/insignia/all', methods=['GET'])
def api_all_insignia():
    return jsonify(user().ListarInsignias())
@app.route('/api/usuario/insignia', methods=['GET'])
def api_id_insignia():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    results = []
    for insignia in user().ListarInsignias(): #TESTAR
        if insignia['idInsignea'] == id:
            results.append(insignia)
    return jsonify(results)
'''@app.route('/api/usuario/insignia/cliente', methods=['GET'])
def api_id_insignia_cliente():
    if 'idCliente' in request.args:
        idcliente = int(request.args['idCliente'])
    else:
        return "Error: No id field provided. Please specify an id."
    results = []
    for insignia in user().ListarConquistas(): #TESTAR
        if insignia['idCliente'] == idcliente:
            results.append(user().ListarConquistas(insignia['idInsignea']))
    return jsonify(results)'''
###FAVORITOS----------------------------------------------------------------
@app.route('/api/usuario/favoritos', methods=['GET'])
def api_id_favoritos():
    if 'idCliente' in request.args:
        idcliente = int(request.args['idCliente'])
    else:
        return "Error: No id field provided. Please specify an id."
    return jsonify(user().ListarFavoritos(idcliente))
###COLEÇAO------------------------------------------------------------------
@app.route('/api/usuario/colecao', methods=['GET'])
def api_id_colecao():
    if 'idCliente' in request.args:
        idcliente = int(request.args['idCliente'])
    else:
        return "Error: No id field provided. Please specify an id."
    return jsonify(user().ListarColecao(idcliente))
###REVIEWS------------------------------------------------------------------
@app.route('/api/bar/review', methods=['GET'])
def api_all_review():
    if 'idBar' in request.args:
        idBar = int(request.args['idBar'])
    else:
        return "Error: No id field provided. Please specify an id."
    return jsonify(bar().ListarReviewsBar(idBar))
###ADDPRODUTO---------------------------------------------------------------
@app.route('/api/bar/add/produto', methods=['GET'])
def api_ADD_Produto():
    if 'idBar' and  'strTitulo' and 'strDescricao' and 'dblPreco' and 'intTipo' and 'strFoto' in request.args:
        idbar= request.args['idBar']
        titulo= request.args['strTitulo']
        descricao= request.args['strDescricao']
        preco= request.args['dblPreco']
        tipo=int(request.args['intTipo'])
        foto=request.args['strFoto']
    else:  
        return "Error: missing fields on request."
    
    return jsonify(bar().InserirProduto(idbar,titulo,descricao,preco,tipo,foto))
###ADDEVENTO----------------------------------------------------------------
@app.route('/api/bar/add/evento', methods=['GET'])
def api_ADD_Evento():
    if 'idBar' and  'strTitulo' and 'strDescricao' and 'strFoto' and 'dtData' in request.args:
        idbar= int(request.args['idBar'])
        titulo= request.args['strTitulo']
        descricao= request.args['strDescricao']
        foto=request.args['strFoto']
        data=request.args['dtData']
    else:  
        return "Error: missing fields on request."
    
    return jsonify(bar().InserirEvento(idbar,titulo,descricao,foto,data)) 
###ADDREVIEW----------------------------------------------------------------
@app.route('/api/usuario/add/review', methods=['GET'])
def api_ADD_review():
    if 'idBar' and  'idCliente' and 'strReview' and 'intEstrelas' in request.args:
        idbar= request.args['idBar']
        idCliente= request.args['idCliente']
        review= request.args['strReview']
        num_estrelas=request.args['intEstrelas']
    else:  
        return "Error: missing fields on request."
    
    return jsonify(user().AddReview(idbar,idCliente,review,num_estrelas))
###CERVEJAS-----------------------------------------------------------------
@app.route('/api/usuario/cervejas/all', methods=['GET'])
def api_all_cerveja():
    return jsonify(user().ListarCervejas())
@app.route('/api/usuario/cervejas', methods=['GET'])
def api_id_cerveja():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []
    for cerveja in user().ListarCervejas():
        print(cerveja)
        if cerveja['idCerveja'] == id:
            results.append(cerveja)

    return jsonify(results) 
###PRODUTOS-----------------------------------------------------------------
@app.route('/api/usuario/produtos/all', methods=['GET'])
def api_all_produto():
    if 'idBar' in request.args:
        idBar = int(request.args['idBar'])
    else:
        return "Error: No idBar field provided. Please specify an id."

    return jsonify(user().ListarProdutos(idBar))
@app.route('/api/usuario/produtos', methods=['GET'])
def api_id_produto():
    if 'idBar' and 'id' in request.args:
        id = int(request.args['id'])
        idBar = int(request.args['idBar'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []
    for produto in user().ListarProdutos(idBar): #TESTAR
        print(produto)
        if produto['idProduto'] == id:
            results.append(produto)
    return jsonify(results)
###EVENTOS DE UM BAR--------------------------------------------------------
@app.route('/api/usuario/eventos/all', methods=['GET'])
def api_all_eventos():
    if 'idBar' in request.args:
        idBar = int(request.args['idBar'])
    else:
        return "Error: No idBar field provided. Please specify an id."

    return jsonify(user().ListarEventos(idBar))
@app.route('/api/usuario/eventos', methods=['GET'])
def api_id_eventos():
    if 'idBar' and 'id' in request.args:
        id = int(request.args['id'])
        idBar = int(request.args['idBar'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []
    for eventos in user().ListarEventos(idBar):
        print(eventos)
        if eventos['idEvento'] == id:
            results.append(eventos)

    return jsonify(results) 
###BARES--------------------------------------------------------------------
@app.route('/api/usuario/bares/all', methods=['GET'])
def api_all_bares():
    return jsonify(user().Listarbar())
@app.route('/api/usuario/bares', methods=['GET'])
def api_id_bares():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []
    for bar in user().Listarbar():
        print(bar)
        if bar['idBar'] == id:
            results.append(bar)

    return jsonify(results) 
###AUTENTICAÇÃO USUARIO-----------------------------------------------------
@app.route('/api/usuario/autenticar', methods=['GET'])
def api_autenticar_usuario():
    if 'strEmail' in request.args and 'strSenha' in request.args:
        email = request.args['strEmail']
        senha = request.args['strSenha']
    else:
        return "Error: No strEmail or strSenha field provided. Please specify an id."

    return jsonify(user().VerificaLogin(email,senha))
###AUTENTICAÇÃO BAR---------------------------------------------------------
@app.route('/api/bar/autenticar', methods=['GET'])
def api_autenticar_bar():
    if 'strEmail' in request.args and 'strSenha' in request.args:
        email = request.args['strEmail']
        senha = request.args['strSenha']
    else:
        return "Error: No strEmail or strSenha field provided. Please specify an id."

    return jsonify(bar().VerificaLoginBar(email,senha))
###CADASTRAR----------------------------------------------------------------
@app.route('/api/usuario/cadastrar/email', methods=['GET'])
def api_verificar_email_usuario():
    if 'strEmail' in request.args:
        email = request.args['strEmail']
    else:
        return "Error: No strEmail or field provided. Please specify an email."

    return jsonify(user().VerificarEmail(email))
@app.route('/api/usuario/cadastrar', methods=['GET'])
def api_cadastrar_usuario():
    if 'strEmail' and 'strSenha' and  'strNome' and 'intPersona' and 'strEndereco' in request.args:
        email= request.args['strEmail']
        senha= request.args['strSenha']
        nome= request.args['strNome']
        persona= int(request.args['intPersona'])
        endereco=request.args['strEndereco']
    else:  
        return "Error: missing fields on request."
    
    return jsonify(user().CadastrarUsuario(email,senha,nome,persona,endereco))
@app.route('/api/bar/cadastrar/email', methods=['GET'])
def api_verificar_email_bar():
    if 'strEmail' in request.args:
        email = request.args['strEmail']
    else:
        return "Error: No strEmail or field provided. Please specify an email."

    return jsonify(bar().VerificarEmail(email))
@app.route('/api/bar/cadastrar', methods=['GET'])
def api_cadastrar_bar():
    if 'strNome'and 'strEndereco'and 'strEmail'and 'strSenha'and'intCNPJ'and 'strLogo' in request.args:
        email= request.args['strEmail']
        senha= request.args['strSenha']
        nome= request.args['strNome']
        CNPJ= int(request.args['intCNPJ'])
        endereco=request.args['strEndereco']
        logo=request.args['strLogo']
        
    else:  
        return "Error: missing fields on request."
    
    return jsonify(bar().CadastrarBar(email,senha,nome,CNPJ,endereco,logo))
@app.route('/api/conexao', methods=['GET'])
def api_conexao():    
    return jsonify(user().conexao())
###CADASTRAR----------------------------------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
