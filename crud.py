#coding: utf-8

from appJar import gui
import MySQLdb

#conexao = MySQLdb.connect("192.168.56.101","va1_user","va1_user","mundo")
# conexao.select_db("mundo")
#cursor = conexao.cursor()



#cursor.execute("SELECT * FROM Pais;")
# pegar o primeiro resultado
#result1 = cursor.fetchone()
# pegar todos os resultados
#result = cursor.fetchall()

app = gui("CRUD de MySQL")

def usando(btn):
	# print "Você me usou!"
	pass

def pesquisar(btn):
	termo = app.getEntry("txtBusca")
	if  termo == '':
		app.errorBox("Erro",'Informe um termo para pesquisar!')
	else:
		# SELECT * FROM Cidade WHERE NomeCidade LIKE '%Belo%'
		cursor.execute("SELECT NomeCidade,NomeEstado FROM Cidade "+
			"INNER JOIN Estado ON Estado.idEstado = Cidade.Estado_idEstado "
			+ "WHERE NomeCidade LIKE '%" + termo + "%'" )
		rs = cursor.fetchall()


		app.clearListBox("lBusca")

		for x in rs:
			app.addListItem("lBusca",x[0] + ' - ' + x[1])
		#app.addListItems("lBusca",rs)

def inserir(btn):
	app.showSubWindow('janela_inserir')

def salvar_estado(btn):
	cidade = app.getEntry('txtcidade')
	idestado = app.getEntry('txtestado')
	cursor.execute("INSERT INTO Cidade (NomeCidade, Estado_idEstado) VALUES('{}',{})".format(cidade,idestado))
	#cursor.execute("INSERT INTO Cidade (NomeCidade, Estado_idEstado) VALUES('%s',%s)" % (cidade,idestado))
	conexao.commit()
	app.hideSubWindow('janela_inserir')

def atualizar(btn):
	app.showSubWindow('janela_atualizar')
	
def deletar(btn):
	app.showSubWindow('janela_deletar')
	
	
def update_cidade(btn):	
	cidadeI = app.getEntry("txtcidade atual")	
	cidadeA = app.getEntry("txtcidade a ser inserido")
	cursor.execute("UPDATE Cidade SET nomeCidade = "+cidadeA+" WHERE idCidade = "+cidadeI)
	conexao.commit()

def update_estado(btn):
	estadoI = app.getEntry("txtestado atual")	
	estadoA = app.getEntry("txtestado a ser inserido")
	cursor.execute("UPDATE Estado SET nomeEstado = "+estadoA+" WHERE idEstado = "+estadoI)
	conexao.commit()

def update_pais(btn):
	paisI = app.getEntry("txtpais atual")
	paisA = app.getEntry("txtpais a ser inserido")	
	cursor.execute("UPDATE Pais SET nomePais = "+paisA+" WHERE idPais = "+paisI)
	conexao.commit()


		

	
	
	
	
	



def deletar_cidade(btn):	
	cidadeDel = app.getEntry("txtCidade a ser deletada")
	if cidadeDel == '':
		pass
	else:
		cursor.execute("DELETE from Cidade WHERE idCidade = "+cidadeDel)
	conexao.commit()

def deletar_estado(btn):
	estadoDel = app.getEntry("txtEstado a ser deletado")
	if estadoDel == '':
		pass
	else:
		cursor.execute("DELETE from Estado WHERE idEstado = "+estadoDel)
	conexao.commit()
def deletar_pais(btn):
	paisDel = app.getEntry("txtPais a ser deletado")
	if cidadeDel == '':
		pass
	else:
		cursor.execute("DELETE from Pais WHERE idPais = "+paisDel)
	conexao.commit()

def conectar(btn):
	flag = 1
	while flag == 1:
		try:
			user = app.getEntry("usuario")
			password = app.getEntry("senha")	
			global conexao			
			conexao = MySQLdb.connect("192.168.56.101",user,password,"mundo")	
			global cursor			
			cursor = conexao.cursor()			
			flag = 0
			app.showSubWindow('janela_inicio')
			break
		except:
			app.errorBox("Erro", "Usuario ou senha incorretos", parent=None)
			flag = 2
# this is a pop-up
app.startSubWindow("janela_inserir", modal=True)
app.addLabel("l1", "Inserindo dados...")
app.addEntry('txtestado')
app.addEntry('txtcidade')
app.addButton('Salvar cidade',salvar_estado)
app.setEntryDefault("txtestado", "ID do Estado")
app.setEntryDefault("txtcidade", "Nome da cidade")
app.stopSubWindow()

# this is a pop-up
app.startSubWindow("janela_atualizar", modal=True)

app.addEntry('txtcidade atual')
app.addEntry('txtcidade a ser inserido')
app.addButton('Att cidade',update_cidade)

app.addEntry('txtestado atual')
app.addEntry('txtestado a ser inserido')
app.addButton('Att estado',update_estado)


app.addEntry('txtpais atual')
app.addEntry('txtpais a ser inserido')

app.addButton('Att pais',update_pais)

app.setEntryDefault("txtcidade a ser inserido", "Cidade a ser inserida")
app.setEntryDefault("txtcidade atual", "ID cidade")

app.setEntryDefault("txtestado atual", "ID estadp")
app.setEntryDefault("txtestado a ser inserido", "Estado a ser inserido")

app.setEntryDefault("txtpais atual", "ID pais")
app.setEntryDefault("txtpais a ser inserido", "Pais a ser inserido")

app.stopSubWindow()

# this is a pop-up
app.startSubWindow("janela_deletar", modal=True)

app.addEntry('txtCidade a ser deletada')
app.setEntryDefault("txtCidade a ser deletada", "ID cidade")
app.addButton('Deletar Cidade',deletar_cidade)

app.addEntry('txtEstado a ser deletado')
app.setEntryDefault("txtEstado a ser deletado", "ID estado")
app.addButton('Deletar Estado',deletar_estado)

app.addEntry('txtPais a ser deletado')
app.setEntryDefault("txtPais a ser deletado", "ID pais")
app.addButton('Deletar Pais',deletar_pais)

app.stopSubWindow()

app.startSubWindow("janela_inicio", modal=True)
app.addLabel("lNome",'',0,0,2)
app.addButton("Exibir dados",usando,1,0)
app.addButton("Inserir dado",inserir,1,1)
app.addButton("Atualizar dado",atualizar,2,0)
app.addButton("Excluir dado",deletar,2,1)
app.addEntry("txtBusca",3,0,2)
app.setEntryDefault("txtBusca", "Digite o termo...")
app.addButton("Pesquisar",pesquisar, 4,0,2)
app.addListBox("lBusca",[],5,0,2)
app.setListBoxRows("lBusca",5)
app.stopSubWindow()

app.addLabelEntry("usuario",1,0)
app.addLabelSecretEntry("senha",2,0)
app.addButton("Conectar",conectar,3,0)

app.go()
