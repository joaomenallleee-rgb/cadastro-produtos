from PyQt5 import uic,QtWidgets
import mysql.connector

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    if formulario.radioButton.isChecked() :
        print("Categoria Informatica foi celecionada")
    elif formulario.radioButton_2.isChecked() :
        print("Categoria alimentos foi selecionada")
    else : 
        print("Categoria eletronicos foi selecionada")
    
    print("Codigo:",linha1)
    print("Descrição:",linha2)
    print("Preço:",linha3)
    categoria = "Eletronicos"
    if formulario.radioButton.isChecked():
        categoria = "Informatica"
    elif formulario.radioButton_2.isChecked():
        categoria = "Alimentos"

    banco = mysql.connector.connect(host="localhost", port=3307,user="root",passwd="", database="cadastro")
    cursor = banco.cursor()
    cursor.execute("INSERT INTO produtos (codigo, descricao, preco, categoria) VALUES (%s, %s, %s, %s)",(linha1, linha2, linha3.replace(",","."),categoria))
    banco.commit()
    banco.close()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    QtWidgets.QMessageBox.information(formulario, "Aviso", "Produtos cadastrados!")



app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
