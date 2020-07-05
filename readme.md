## **BarClub back-end em Python por:**
### *Luis Felipe Pessoa Teixeira - luis.eletroeletronica@gmail.com*
### *Andres Benoit - andres.benoit7@gmail.com*
=============================================

### Bibliotecas utilizadas
- PyMysql - Para fazer a comunicação com o banco de dados
- JSON - Para retornar Json files na API
- Flask - Framework para a API

### Guia para utilizar a API do BarClub:

1. Lista de Cervejas - https://muammuam.herokuapp.com/api/usuario/cervejas/all
2. Cerveja Específica - https://muammuam.herokuapp.com/api/usuario/cervejas?id=
3. Lista de bares - https://muammuam.herokuapp.com/api/usuario/bares/all
4. Produtos do Bar - https://muammuam.herokuapp.com/api/usuario/produtos/all?idBar=
5. Produto específico - https://muammuam.herokuapp.com/api/usuario/produtos?idBar=&id=
6. Eventos do Bar - https://muammuam.herokuapp.com/api/usuario/eventos/all?idBar=
7. Evento específico - https://muammuam.herokuapp.com/api/usuario/eventos?idBar=&id=
7. Dados do bar - https://muammuam.herokuapp.com/api/usuario/bares?id
9. Verificar Login Cliente - https://muammuam.herokuapp.com/api/usuario/autenticar?strEmail=&strSenha=
10. Verificar Login Bar - https://muammuam.herokuapp.com/api/bar/autenticar?strEmail=&strSenha=  
12. Verificar a existência do email do Cliente - https://muammuam.herokuapp.com/api/usuario/cadastrar/email?strEmail=
12. Veriricar a existência do email do Bar - https://muammuam.herokuapp.com/api/bar/cadastrar/email?strEmail=
13. Cadastrar Usuário - https://muammuam.herokuapp.com/api/usuario/cadastrar?strEmail=&strSenha=&strNome=&intPersona=&strEndereco=
14. Cadastrar Bar - https://muammuam.herokuapp.com/api/bar/cadastrar?strNome=&strEndereco=&strEmail=&strSenha=&intCNPJ=&strLogo=
15. Lista de insígnias - https://muammuam.herokuapp.com/api/usuario/insignia/all
16. Retornar uma insígnias - https://muammuam.herokuapp.com/api/usuario/insignia?id=
17. Retornar os favoritos do cliente - https://muammuam.herokuapp.com/api/usuario/favoritos?idCliente=
18. Retornar a coleção do cliente - https://muammuam.herokuapp.com/api/usuario/colecao?idCliente=
19. Retornar a classificação do bar - https://muammuam.herokuapp.com/api/bar/review?idBar=
20. Adicionar um produto ao bar - https://muammuam.herokuapp.com/api/bar/add/produto?idBar=&strTitulo=&strDescricao=&dblPreco=&intTipo=&strFoto=
21. Adicionar um evento ao bar - https://muammuam.herokuapp.com/api/bar/add/evento?idBar=&strTitulo=&strDescricao=&strFoto=&dtData=
22. Adicionar uma classificação ao bar - https://muammuam.herokuapp.com/api/usuario/add/review?idBar=&idCliente=&strReview=&intEstrelas=

=============================================

### Classes desenvolvidas
#### class bar():
Utilizada para inserir os métodos do bar
#### class user():
Utilizada para inserir os métodos do cliente

=============================================

### Funções extras 

##### def pedidos: e def ListarPedidos:
Podem ser utilizada futuramente para dar início a um e-commerce



