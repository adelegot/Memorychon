import sys, os
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,QTableWidget,QTableWidgetItem, QLabel, QLineEdit, QPushButton, QInputDialog,QTextEdit,QMessageBox, QRadioButton, QVBoxLayout, QAction, QHBoxLayout
from PyQt5.QtCore import QCoreApplication,Qt, QSize
from PyQt5.QtGui import QPixmap, QFont, QIcon,  QFontDatabase
from PyQt5.QtCore import QTimer
from PyQt5.QtMultimedia import QSound

app = QApplication([])
ecran = app.primaryScreen()
taille_ecran = ecran.size()
largeur_ecran = taille_ecran.width()
hauteur_ecran = taille_ecran.height()

hauteur_ref= 1800
largeur_ref= 2880

def echelle_x(x):
    return int(x *largeur_ecran / largeur_ref)

def echelle_y(y):
    return int(y * hauteur_ecran / hauteur_ref)

def echelle_font(taille):
    return int(taille * hauteur_ecran / hauteur_ref)

class Fenetre1(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self.setWindowTitle('Bienvenue')
        
        
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Copeland.otf")
        font_id = QFontDatabase.addApplicationFont("fonts/Copeland.otf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        font_path2 = os.path.join(os.path.dirname(__file__), "fonts","Quitle.otf")
        font_id2 = QFontDatabase.addApplicationFont("fonts/Quitle.otf")
        font_families2 = QFontDatabase.applicationFontFamilies(font_id2)[0]
        
        self.label1 = QLabel(self)
        pixmap = QPixmap('image/fod.png')
        pixmap_resized = pixmap.scaled(echelle_x(2880) ,echelle_y(1800))
        self.label1.setPixmap(pixmap_resized)
        self.label1.move(0,0)
       
        self.label = QLabel(self)
        self.label.setText("Les cornichons vous présentent :")
        self.label.setStyleSheet("background-color: #45721C; color: #DED9A3")
        self.label.setFont(QFont(font_families2, 18))
        self.label.move(echelle_x(1670), echelle_y(550))
        
        self.label = QLabel(self)
        self.label.setText("Memorychons")
        self.label.setStyleSheet("background-color: #45721C; color: #DED9A3")
        self.label.setFont(QFont(font_families, 63))
        self.label.setWordWrap(True)
        self.label.move(echelle_x(1550), echelle_y(620))
        
        self.label = QLabel(self)
        self.label.setText("Et si la mémoire n’était pas qu’une question d’images ?")
        self.label.setStyleSheet("background-color: #45721C; color: #DED9A3")
        self.label.setFont(QFont(font_families2, 15))
        self.label.move(echelle_x(1570), echelle_y(850))
       
        self.label = QLabel(self)
        self.label.setText("Découvrez un jeu de Memory pas comme les autres, où chaque paire cache une surprise...")
        self.label.setStyleSheet("background-color: #45721C; color: #DED9A3")
        self.label.setFont(QFont(font_families2, 15))
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(echelle_x(1250), echelle_y(900), echelle_x(1600), echelle_y(100))
        
        self.btn1 = QPushButton(" Jouer", self)
        self.btn1.setStyleSheet(f"""
            QPushButton {{
                border-radius: {echelle_x(95)}px;
                background-color: #173106;
                color: #DED9A3;
                font-size: {echelle_font(45)}px;
                padding: 5px;
            }}""")
        police = QFont(font_families2) 
        self.btn1.setFont(police)
        self.btn1.move(echelle_x(1900), echelle_y(1020))
        self.btn1.resize(echelle_x(200), echelle_y(200))
        self.btn1.clicked.connect(self.ouvre)

        self.setWindowTitle('Bienvenue')
        
    def ouvre(self):
        self.menu = Menu()
        self.menu.showMaximized()
        
        
class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self.setWindowTitle('Bienvenue')
        
        
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Copeland.otf")
        font_id = QFontDatabase.addApplicationFont("fonts/Copeland.otf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        font_path2 = os.path.join(os.path.dirname(__file__), "fonts","Quitle.otf")
        font_id2 = QFontDatabase.addApplicationFont("fonts/Quitle.otf")
        font_families2 = QFontDatabase.applicationFontFamilies(font_id2)[0]
        
        self.label1 = QLabel(self)
        pixmap = QPixmap('image/fod1.png')
        pixmap_resized = pixmap.scaled(echelle_x(2880) ,echelle_y(1800))
        self.label1.setPixmap(pixmap_resized)
        self.label1.move(0,0)
        
        self.label = QLabel(self)
        self.label.setText("MENU")
        self.label.setStyleSheet("background-color: #3C6218; color: #DED9A3")
        self.label.setFont(QFont(font_families, 100))
        self.label.move(echelle_x(1100), echelle_y(250))
        
        self.btn1 = QPushButton("Niveau 1", self)
        self.btn1.setStyleSheet(f"""QPushButton {{ border-radius: {echelle_x(45)}px; background-color: #173106; color: #DED9A3;font-size: {echelle_font(55)}px;padding: 5px; }}""")
        police = QFont(font_families2) 
        self.btn1.setFont(police)
        self.btn1.move(echelle_x(1000), echelle_y(600))
        self.btn1.resize(echelle_x(350), echelle_y(90))
        self.btn1.clicked.connect(self.ouvre2)
        
        self.btn1 = QPushButton("Niveau 2", self)
        self.btn1.setStyleSheet(f"""QPushButton {{ border-radius: {echelle_x(45)}px; background-color: #173106; color: #DED9A3;font-size: {echelle_font(55)}px;padding: 5px; }}""")
        police = QFont(font_families2) 
        self.btn1.setFont(police)
        self.btn1.move(echelle_x(1000), echelle_y(750))
        self.btn1.resize(echelle_x(350), echelle_y(90))
        self.btn1.clicked.connect(self.ouvre3)
        
        self.btn1 = QPushButton("Niveau 3", self)
        self.btn1.setStyleSheet(f"""QPushButton {{ border-radius: {echelle_x(45)}px; background-color: #173106; color: #DED9A3;font-size: {echelle_font(55)}px;padding: 5px; }}""")
        police = QFont(font_families2) 
        self.btn1.setFont(police)
        self.btn1.move(echelle_x(1000), echelle_y(900))
        self.btn1.resize(echelle_x(350), echelle_y(90))
        self.btn1.clicked.connect(self.ouvre4)
        
        self.btn1 = QPushButton("Niveau 4", self)
        self.btn1.setStyleSheet(f"""QPushButton {{ border-radius: {echelle_x(45)}px; background-color: #173106; color: #DED9A3;font-size: {echelle_font(55)}px;padding: 5px; }}""")
        police = QFont(font_families2) 
        self.btn1.setFont(police)
        self.btn1.move(echelle_x(1000), echelle_y(1050))
        self.btn1.resize(echelle_x(350), echelle_y(90))
        self.btn1.clicked.connect(self.ouvre5)
        
        self.btn1 = QPushButton("Niveau 5", self)
        self.btn1.setStyleSheet(f"""QPushButton {{ border-radius: {echelle_x(45)}px; background-color: #173106; color: #DED9A3;font-size: {echelle_font(55)}px;padding: 5px; }}""")
        police = QFont(font_families2) 
        self.btn1.setFont(police)
        self.btn1.move(echelle_x(1450), echelle_y(600))
        self.btn1.resize(echelle_x(350), echelle_y(90))
        self.btn1.clicked.connect(self.ouvre6)
        
        self.btn1 = QPushButton("Niveau 6", self)
        self.btn1.setStyleSheet(f"""QPushButton {{ border-radius: {echelle_x(45)}px; background-color: #173106; color: #DED9A3;font-size: {echelle_font(55)}px;padding: 5px; }}""")
        police = QFont(font_families2) 
        self.btn1.setFont(police)
        self.btn1.move(echelle_x(1450), echelle_y(750))
        self.btn1.resize(echelle_x(350), echelle_y(90))
        self.btn1.clicked.connect(self.ouvre7)
        
        self.btn1 = QPushButton("Niveau 7", self)
        self.btn1.setStyleSheet(f"""QPushButton {{ border-radius: {echelle_x(45)}px; background-color: #173106; color: #DED9A3;font-size: {echelle_font(55)}px;padding: 5px; }}""")
        police = QFont(font_families2) 
        self.btn1.setFont(police)
        self.btn1.move(echelle_x(1450), echelle_y(900))
        self.btn1.resize(echelle_x(350), echelle_y(90))
        self.btn1.clicked.connect(self.ouvre8)
        
        self.btn1 = QPushButton("Niveau 8", self)
        self.btn1.setStyleSheet(f"""QPushButton {{ border-radius: {echelle_x(45)}px; background-color: #173106; color: #DED9A3;font-size: {echelle_font(55)}px;padding: 5px; }}""")
        police = QFont(font_families2) 
        self.btn1.setFont(police)
        self.btn1.move(echelle_x(1450), echelle_y(1050))
        self.btn1.resize(echelle_x(350), echelle_y(90))
        self.btn1.clicked.connect(self.ouvre9)
        
        self.btn1 = QPushButton("1VS1 Classique", self)
        self.btn1.setStyleSheet(f"""QPushButton {{ border-radius: {echelle_x(45)}px; background-color: #173106; color: #DED9A3;font-size: {echelle_font(55)}px;padding: 5px; }}""")
        police = QFont(font_families2) 
        self.btn1.setFont(police)
        self.btn1.move(echelle_x(1130), echelle_y(1200))
        self.btn1.resize(echelle_x(550), echelle_y(90))
        self.btn1.clicked.connect(self.ouvre10)  
        

        self.setWindowTitle('Memorychons')
        
    def ouvre2(self):
        self.fenetre2 = Fenetre2()
        self.fenetre2.showMaximized()
        self.close()
        
    def ouvre3(self):
        self.fenetre3 = Fenetre3()
        self.fenetre3.showMaximized()
        self.close()
    
    def ouvre4(self):
        self.fenetre4 = Fenetre4()
        self.fenetre4.showMaximized()
        self.close()
        
    def ouvre5(self):
        self.fenetre5 = Fenetre5()
        self.fenetre5.showMaximized()
        self.close()
        
    def ouvre6(self):
        self.fenetre6 = Fenetre6()
        self.fenetre6.showMaximized()
        self.close()
        
    def ouvre7(self):
        self.fenetre7 = Fenetre7()
        self.fenetre7.showMaximized()
        self.close()
        
    def ouvre8(self):
        self.fenetre8 = Fenetre8()
        self.fenetre8.showMaximized()
        self.close()
    
    def ouvre9(self):
        self.fenetre9 = Fenetre9()
        self.fenetre9.showMaximized()
        self.close()
        
    def ouvre10(self):
        text, ok = QInputDialog.getText(self, 'Dialogue', 'Entrez le nom du joueur1:')
        if ok:
            text1, ok = QInputDialog.getText(self, 'Dialogue', 'Entrez le nom du joueur2:')
            if ok:
                self.fenetre10 = Fenetre10(text,text1)
                self.fenetre10.showMaximized()
                self.close()
        
        
class Fenetre2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memorychons')
        self.setStyleSheet("background-color: #DED9A3;")
        
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Copeland.otf")
        font_id = QFontDatabase.addApplicationFont("fonts/Copeland.otf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        font_path2 = os.path.join(os.path.dirname(__file__), "fonts","Quitle.otf")
        font_id2 = QFontDatabase.addApplicationFont("fonts/Quitle.otf")
        font_families2 = QFontDatabase.applicationFontFamilies(font_id2)[0]

        self.paires_correctes = 0
        self.renv = []
        self.vie=2
        
        self.niv = QLabel("NIVEAU 1",self)  
        self.niv.setFont(QFont(font_families, 100))
        self.niv.setStyleSheet("color: #45721C;")
        self.niv.setGeometry(echelle_x(900), echelle_y(100), echelle_x(1000), echelle_y(300))
        
        self.vie1 = QLabel(self)
        pixmap = QPixmap('image/heart.png')
        pixmap_resized = pixmap.scaled(echelle_x(70), echelle_y(70))  
        self.vie1.setPixmap(pixmap_resized)
        self.vie1.resize(pixmap_resized.width(), pixmap_resized.height())
        self.vie1.move(echelle_x(100), echelle_y(230))
        
        self.label = QLabel(f"Vies restantes: {self.vie}",self)
        self.label.setFont(QFont(font_families2, 30))
        self.label.setStyleSheet("color: #45721C;")
        self.label.setGeometry(echelle_x(180), echelle_y(220), echelle_x(600), echelle_y(70)) 
        
        self.label1 = QLabel(f"Paires correctes: {self.paires_correctes}", self)
        self.label1.setFont(QFont(font_families2, 30))
        self.label1.setStyleSheet("color: #45721C;")
        self.label1.setGeometry(echelle_x(2150), echelle_y(220), echelle_x(700), echelle_y(70)) 
        
        dimensions=[(echelle_x(1500), echelle_y(500)), (echelle_x(900), echelle_y(500)), (echelle_x(1500), echelle_y(1100)), (echelle_x(900), echelle_y(1100))]
        r=["image/bouzidi.png","image/hagbe.png","image/hagbe.png","image/bouzidi.png"]
        s=0
        for x,y in dimensions:
            self.im = QPushButton(self)
            self.im.setGeometry(x,y, echelle_y(450), echelle_y(450))
            self.im.setIcon(QIcon("image/mimi.png"))  
            self.im.setIconSize(self.im.size())
            image= r[s]
            self.im.clicked.connect(lambda checked= False, b=self.im, im=image: self.retourner(b, im))
            s+=1
        
        
        self.btn_close = QPushButton(self)
        self.btn_close.setGeometry(echelle_x(100), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close.setIcon(QIcon("image/arrow.png"))  
        self.btn_close.setIconSize(self.btn_close.size()) 
        self.btn_close.clicked.connect(self.ouvre)
        
        self.btn_close1 = QPushButton(self)
        self.btn_close1.setGeometry(echelle_x(2600), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close1.setIcon(QIcon("image/arrow2.png"))
        self.btn_close1.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close1.clicked.connect(self.ouvre)

        self.btn_close2 = QPushButton(self)
        self.btn_close2.setGeometry(echelle_x(100), echelle_y(30), echelle_x(100), echelle_y(100))
        self.btn_close2.setIcon(QIcon("image/home.png"))
        self.btn_close2.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close2.clicked.connect(self.ouvre2)
        
        self.showMaximized()
        
    def ouvre(self):
        self.fenetre3 = Fenetre3()
        self.fenetre3.showMaximized()
        self.close()

    def ouvre2(self):
        self.menu = Menu()
        self.menu.showMaximized()
        self.close()

    def retourner(self, bouton, image):
        if bouton in [x[0] for x in self.renv]:
            return None
        bouton.setIcon(QIcon(image))
        self.renv.append((bouton, image))
        if len(self.renv) == 2:
            self.verifier_paire()

    def verifier_paire(self):
        b1, image1 = self.renv[0]
        b2, image2 = self.renv[1]

        if image1 == image2:
            self.paires_correctes += 1
            self.label1.setText(f"Paires correctes: {self.paires_correctes}")
            self.renv = []
            if self.paires_correctes == 2:
                self.felicitation()
        else:
            self.vie -= 1
            self.label.setText(f"Vies restantes: {self.vie}")
            QTimer.singleShot(500, lambda: self.retourner22(b1, b2))
            if self.vie <= 0:
                self.play_audio('son/perdu.wav')
                QMessageBox.critical(self, "Perdu !", "Tu as perdu toutes tes vies ! Réessaie !")
                self.ouvre2()

    def retourner22(self, b1, b2):
        b1.setIcon(QIcon("image/mimi.png"))
        b2.setIcon(QIcon("image/mimi.png"))
        self.renv = []

    def felicitation(self):
        self.play_audio('son/gagner.wav')
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Félicitations !")
        msg_box.setText("Bravo, tu as réussi !")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
        self.ouvre()

    def play_audio(self, sound_file):
        QSound.play(sound_file)
        
class Fenetre3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memorychons')
        self.setStyleSheet("background-color: #DED9A3;")

        self.paires_correctes = 0
        self.renv = []
        self.vie=3
        
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Copeland.otf")
        font_id = QFontDatabase.addApplicationFont("fonts/Copeland.otf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        font_path2 = os.path.join(os.path.dirname(__file__), "fonts","Quitle.otf")
        font_id2 = QFontDatabase.addApplicationFont("fonts/Quitle.otf")
        font_families2 = QFontDatabase.applicationFontFamilies(font_id2)[0]
        
        self.niv = QLabel("NIVEAU 2",self)  
        self.niv.setFont(QFont(font_families, 100))
        self.niv.setStyleSheet("color: #45721C;")
        self.niv.setGeometry(echelle_x(900), echelle_y(100), echelle_x(1000), echelle_y(300))
        
        self.vie1 = QLabel(self)
        pixmap = QPixmap('image/heart.png')
        pixmap_resized = pixmap.scaled(echelle_x(70), echelle_y(70))  
        self.vie1.setPixmap(pixmap_resized)
        self.vie1.resize(pixmap_resized.width(), pixmap_resized.height())
        self.vie1.move(echelle_x(100), echelle_y(230))
        
        self.label = QLabel(f"Vies restantes: {self.vie}",self)
        self.label.setFont(QFont(font_families2, 30))
        self.label.setStyleSheet("color: #45721C;")
        self.label.setGeometry(echelle_x(180), echelle_y(220), echelle_x(600), echelle_y(70)) 
        
        self.label1 = QLabel(f"Paires correctes: {self.paires_correctes}", self)
        self.label1.setFont(QFont(font_families2, 30))
        self.label1.setStyleSheet("color: #45721C;")
        self.label1.setGeometry(echelle_x(2150), echelle_y(220), echelle_x(700), echelle_y(70)) 


        dimensions=[(echelle_x(1200), echelle_y(500)), (echelle_x(600), echelle_y(500)), (echelle_x(1200), echelle_y(1100)), (echelle_x(600), echelle_y(1100)), (echelle_x(1800), echelle_y(500)), (echelle_x(1800), echelle_y(1100))]
        r=["image/bouzidi.png","image/hagbe.png","image/bellagha.png","image/bouzidi.png","image/bellagha.png","image/hagbe.png"]
        s=0
        for x,y in dimensions:
            self.im = QPushButton(self)
            self.im.setGeometry(x,y, echelle_y(450), echelle_y(450))
            self.im.setIcon(QIcon("image/mimi.png"))  
            self.im.setIconSize(self.im.size())
            image= r[s]
            self.im.clicked.connect(lambda checked= False, b=self.im, im=image: self.retourner(b, im))
            s+=1
        
        self.btn_close = QPushButton(self)
        self.btn_close.setGeometry(echelle_x(100), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close.setIcon(QIcon("image/arrow.png"))  
        self.btn_close.setIconSize(self.btn_close.size()) 
        self.btn_close.clicked.connect(self.ouvre1)
        
        self.btn_close1 = QPushButton(self)
        self.btn_close1.setGeometry(echelle_x(2600), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close1.setIcon(QIcon("image/arrow2.png"))
        self.btn_close1.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close1.clicked.connect(self.ouvre)

        self.btn_close2 = QPushButton(self)
        self.btn_close2.setGeometry(echelle_x(100), echelle_y(30), echelle_x(100), echelle_y(100))
        self.btn_close2.setIcon(QIcon("image/home.png"))
        self.btn_close2.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close2.clicked.connect(self.ouvre2)
        
        self.showMaximized()
        
    def ouvre(self):
        self.fenetre4 = Fenetre4()
        self.fenetre4.showMaximized()
        self.close()
        
    def ouvre1(self):
        self.fenetre2 = Fenetre2()
        self.fenetre2.showMaximized()
        self.close()

    def ouvre2(self):
        self.menu = Menu()
        self.menu.showMaximized()
        self.close()

    def retourner(self, bouton, image):
        if bouton in [x[0] for x in self.renv]:
            return None
        bouton.setIcon(QIcon(image))
        self.renv.append((bouton, image))
        if len(self.renv) == 2:
            self.verifier_paire()

    def verifier_paire(self):
        b1, image1 = self.renv[0]
        b2, image2 = self.renv[1]

        if image1 == image2:
            self.paires_correctes += 1
            self.label1.setText(f"Paires correctes: {self.paires_correctes}")
            self.renv = []
            if self.paires_correctes == 3:
                self.felicitation()
        else:
            self.vie -= 1
            self.label.setText(f"Vies restantes: {self.vie}")
            QTimer.singleShot(500, lambda: self.retourner22(b1, b2))
            if self.vie <= 0:
                self.play_audio('son/perdu.wav')
                QMessageBox.critical(self, "Perdu !", "Tu as perdu toutes tes vies ! Réessaie !")
                self.ouvre1()

    def retourner22(self, b1, b2):
        b1.setIcon(QIcon("image/mimi.png"))
        b2.setIcon(QIcon("image/mimi.png"))
        self.renv = []

    def felicitation(self):
        self.play_audio('son/gagner.wav')
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Félicitations !")
        msg_box.setText("Bravo, tu as réussi !")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
        self.ouvre() 

    def play_audio(self, sound_file):
        QSound.play(sound_file)
        
class Fenetre4(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memorychons')
        self.setStyleSheet("background-color: #DED9A3;")

        self.paires_correctes = 0
        self.renv = []
        self.vie=4
        
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Copeland.otf")
        font_id = QFontDatabase.addApplicationFont("fonts/Copeland.otf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        font_path2 = os.path.join(os.path.dirname(__file__), "fonts","Quitle.otf")
        font_id2 = QFontDatabase.addApplicationFont("fonts/Quitle.otf")
        font_families2 = QFontDatabase.applicationFontFamilies(font_id2)[0]
        
        self.niv = QLabel("NIVEAU 3",self)  
        self.niv.setFont(QFont(font_families, 100))
        self.niv.setStyleSheet("color: #45721C;")
        self.niv.setGeometry(echelle_x(900), echelle_y(100), echelle_x(1000), echelle_y(300))
        
        self.vie1 = QLabel(self)
        pixmap = QPixmap('image/heart.png')
        pixmap_resized = pixmap.scaled(echelle_x(70), echelle_y(70))  
        self.vie1.setPixmap(pixmap_resized)
        self.vie1.resize(pixmap_resized.width(), pixmap_resized.height())
        self.vie1.move(echelle_x(100), echelle_y(230))
        
        self.label = QLabel(f"Vies restantes: {self.vie}",self)
        self.label.setFont(QFont(font_families2, 30))
        self.label.setStyleSheet("color: #45721C;")
        self.label.setGeometry(echelle_x(180), echelle_y(220), echelle_x(600), echelle_y(70)) 
        
        self.label1 = QLabel(f"Paires correctes: {self.paires_correctes}", self)
        self.label1.setFont(QFont(font_families2, 30))
        self.label1.setStyleSheet("color: #45721C;")
        self.label1.setGeometry(echelle_x(2150), echelle_y(220), echelle_x(700), echelle_y(70)) 


        dimensions=[(echelle_x(950), echelle_y(500)), (echelle_x(450), echelle_y(500)), (echelle_x(950), echelle_y(1100)), (echelle_x(450), echelle_y(1100)), (echelle_x(1450), echelle_y(1100)), (echelle_x(1450), echelle_y(500)), (echelle_x(1950), echelle_y(500)), (echelle_x(1950), echelle_y(1100))]
        r=["image/aribi.png","image/hagbe.png","image/hagbe.png","image/bouzidi.png","image/aribi.png","image/bellagha.png",'image/bouzidi.png','image/bellagha.png']
        s=0
        for x,y in dimensions:
            self.im = QPushButton(self)
            self.im.setGeometry(x,y, echelle_y(450), echelle_y(450))
            self.im.setIcon(QIcon("image/mimi.png"))  
            self.im.setIconSize(self.im.size())
            image= r[s]
            self.im.clicked.connect(lambda checked= False, b=self.im, im=image: self.retourner(b, im))
            s+=1
        
        self.btn_close = QPushButton(self)
        self.btn_close.setGeometry(echelle_x(100), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close.setIcon(QIcon("image/arrow.png"))  
        self.btn_close.setIconSize(self.btn_close.size()) 
        self.btn_close.clicked.connect(self.close)
        
        self.btn_close1 = QPushButton(self)
        self.btn_close1.setGeometry(echelle_x(2600), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close1.setIcon(QIcon("image/arrow2.png"))
        self.btn_close1.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close1.clicked.connect(self.ouvre)

        self.btn_close2 = QPushButton(self)
        self.btn_close2.setGeometry(echelle_x(100), echelle_y(30), echelle_x(100), echelle_y(100))
        self.btn_close2.setIcon(QIcon("image/home.png"))
        self.btn_close2.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close2.clicked.connect(self.ouvre2)
        
        self.showMaximized()
        
    def ouvre(self):
        self.fenetre5 = Fenetre5()
        self.fenetre5.showMaximized()
        self.close()
        
    def ouvre1(self):
        self.fenetre3 = Fenetre3()
        self.fenetre3.showMaximized()
        self.close()

    def ouvre2(self):
        self.menu = Menu()
        self.menu.showMaximized()
        self.close()

    def retourner(self, bouton, image):
        if bouton in [x[0] for x in self.renv]:
            return None
        bouton.setIcon(QIcon(image))
        self.renv.append((bouton, image))
        if len(self.renv) == 2:
            self.verifier_paire()

    def verifier_paire(self):
        b1, image1 = self.renv[0]
        b2, image2 = self.renv[1]

        if image1 == image2:
            self.paires_correctes += 1
            self.label1.setText(f"Paires correctes: {self.paires_correctes}")
            self.renv = []
            if self.paires_correctes == 4:
                self.felicitation()
        else:
            self.vie -= 1
            self.label.setText(f"Vies restantes: {self.vie}")
            QTimer.singleShot(500, lambda: self.retourner22(b1, b2))
            if self.vie <= 0:
                self.play_audio('son/perdu.wav')
                QMessageBox.critical(self, "Perdu !", "Tu as perdu toutes tes vies ! Réessaie !")
                self.ouvre1()

    def retourner22(self, b1, b2):
        b1.setIcon(QIcon("image/mimi.png"))
        b2.setIcon(QIcon("image/mimi.png"))
        self.renv = []

    def felicitation(self):
        self.play_audio('son/gagner.wav')
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Félicitations !")
        msg_box.setText("Bravo, tu as réussi !")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
        self.ouvre() 

    def play_audio(self, sound_file):
        QSound.play(sound_file)
        
class Fenetre5(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memorychons')
        self.setStyleSheet("background-color: #DED9A3;")

        self.paires_correctes = 0
        self.renv = []
        self.vie=5
        
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Copeland.otf")
        font_id = QFontDatabase.addApplicationFont("fonts/Copeland.otf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        font_path2 = os.path.join(os.path.dirname(__file__), "fonts","Quitle.otf")
        font_id2 = QFontDatabase.addApplicationFont("fonts/Quitle.otf")
        font_families2 = QFontDatabase.applicationFontFamilies(font_id2)[0]
        
        self.niv = QLabel("NIVEAU 4",self)  
        self.niv.setFont(QFont(font_families, 100))
        self.niv.setStyleSheet("color: #45721C;")
        self.niv.setGeometry(echelle_x(900), echelle_y(100), echelle_x(1000), echelle_y(300))
        
        self.vie1 = QLabel(self)
        pixmap = QPixmap('image/heart.png')
        pixmap_resized = pixmap.scaled(echelle_x(70), echelle_y(70))  
        self.vie1.setPixmap(pixmap_resized)
        self.vie1.resize(pixmap_resized.width(), pixmap_resized.height())
        self.vie1.move(echelle_x(100), echelle_y(230))
        
        self.label = QLabel(f"Vies restantes: {self.vie}",self)
        self.label.setFont(QFont(font_families2, 30))
        self.label.setStyleSheet("color: #45721C;")
        self.label.setGeometry(echelle_x(180), echelle_y(220), echelle_x(600), echelle_y(70)) 
        
        self.label1 = QLabel(f"Paires correctes: {self.paires_correctes}", self)
        self.label1.setFont(QFont(font_families2, 30))
        self.label1.setStyleSheet("color: #45721C;")
        self.label1.setGeometry(echelle_x(2150), echelle_y(220), echelle_x(700), echelle_y(70))


        dimensions=[(echelle_x(700), echelle_y(500)), (echelle_x(200), echelle_y(500)), 
                    (echelle_x(700), echelle_y(1000)), (echelle_x(200), echelle_y(1000)), 
                    (echelle_x(1200), echelle_y(1000)), (echelle_x(1200), echelle_y(500)), 
                    (echelle_x(1700), echelle_y(500)), (echelle_x(1700), echelle_y(1000)),
                    (echelle_x(2200), echelle_y(500)), (echelle_x(2200), echelle_y(1000))]
        r=["image/aribi.png","image/bellagha.png","image/aribi.png","image/chivers.png","image/bouzidi.png","image/hagbe.png",'image/bouzidi.png','image/chivers.png',"image/bellagha.png",'image/hagbe.png']
        s=0
        for x,y in dimensions:
            self.im = QPushButton(self)
            self.im.setGeometry(x,y, echelle_y(450), echelle_y(450))
            self.im.setIcon(QIcon("image/mimi.png"))  
            self.im.setIconSize(self.im.size())
            image= r[s]
            self.im.clicked.connect(lambda checked= False, b=self.im, im=image: self.retourner(b, im))
            s+=1
        
        self.btn_close = QPushButton(self)
        self.btn_close.setGeometry(echelle_x(100), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close.setIcon(QIcon("image/arrow.png"))  
        self.btn_close.setIconSize(self.btn_close.size()) 
        self.btn_close.clicked.connect(self.ouvre1)
        
        self.btn_close1 = QPushButton(self)
        self.btn_close1.setGeometry(echelle_x(2600), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close1.setIcon(QIcon("image/arrow2.png"))
        self.btn_close1.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close1.clicked.connect(self.ouvre)

        self.btn_close2 = QPushButton(self)
        self.btn_close2.setGeometry(echelle_x(100), echelle_y(30), echelle_x(100), echelle_y(100))
        self.btn_close2.setIcon(QIcon("image/home.png"))
        self.btn_close2.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close2.clicked.connect(self.ouvre2)
        
        self.showMaximized()
        
    def ouvre(self):
        self.fenetre6 = Fenetre6()
        self.fenetre6.showMaximized()
        self.close()
        
    def ouvre1(self):
        self.fenetre4 = Fenetre4()
        self.fenetre4.showMaximized()
        self.close()

    def ouvre2(self):
        self.menu = Menu()
        self.menu.showMaximized()
        self.close()

    def retourner(self, bouton, image):
        if bouton in [x[0] for x in self.renv]:
            return None
        bouton.setIcon(QIcon(image))
        self.renv.append((bouton, image))
        if len(self.renv) == 2:
            self.verifier_paire()

    def verifier_paire(self):
        b1, image1 = self.renv[0]
        b2, image2 = self.renv[1]

        if image1 == image2:
            self.paires_correctes += 1
            self.label1.setText(f"Paires correctes: {self.paires_correctes}")
            self.renv = []
            if self.paires_correctes == 5:
                self.felicitation()
        else:
            self.vie -= 1
            self.label.setText(f"Vies restantes: {self.vie}")
            QTimer.singleShot(500, lambda: self.retourner22(b1, b2))
            if self.vie <= 0:
                self.play_audio('son/perdu.wav')
                QMessageBox.critical(self, "Perdu !", "Tu as perdu toutes tes vies ! Réessaie !")
                self.ouvre1()

    def retourner22(self, b1, b2):
        b1.setIcon(QIcon("image/mimi.png"))
        b2.setIcon(QIcon("image/mimi.png"))
        self.renv = []

    def felicitation(self):
        self.play_audio('son/gagner.wav')
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Félicitations !")
        msg_box.setText("Bravo, tu as réussi !")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
        self.ouvre() 

    def play_audio(self, sound_file):
        QSound.play(sound_file)
            
class Fenetre6(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memorychons')
        self.setStyleSheet("background-color: #DED9A3;")

        self.paires_correctes = 0
        self.renv = []
        self.vie=6
        
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Copeland.otf")
        font_id = QFontDatabase.addApplicationFont("fonts/Copeland.otf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        font_path2 = os.path.join(os.path.dirname(__file__), "fonts","Quitle.otf")
        font_id2 = QFontDatabase.addApplicationFont("fonts/Quitle.otf")
        font_families2 = QFontDatabase.applicationFontFamilies(font_id2)[0]
        
        self.niv = QLabel("NIVEAU 5",self)  
        self.niv.setFont(QFont(font_families, 100))
        self.niv.setStyleSheet("color: #45721C;")
        self.niv.setGeometry(echelle_x(900), echelle_y(100), echelle_x(1000), echelle_y(300))
        
        self.vie1 = QLabel(self)
        pixmap = QPixmap('image/heart.png')
        pixmap_resized = pixmap.scaled(echelle_x(70), echelle_y(70))  
        self.vie1.setPixmap(pixmap_resized)
        self.vie1.resize(pixmap_resized.width(), pixmap_resized.height())
        self.vie1.move(echelle_x(100), echelle_y(230))
        
        self.label = QLabel(f"Vies restantes: {self.vie}",self)
        self.label.setFont(QFont(font_families2, 30))
        self.label.setStyleSheet("color: #45721C;")
        self.label.setGeometry(echelle_x(180), echelle_y(220), echelle_x(600), echelle_y(70)) 
        
        self.label1 = QLabel(f"Paires correctes: {self.paires_correctes}", self)
        self.label1.setFont(QFont(font_families2, 30))
        self.label1.setStyleSheet("color: #45721C;")
        self.label1.setGeometry(echelle_x(2150), echelle_y(220), echelle_x(700), echelle_y(70)) 


        dimensions=[ (echelle_x(500), echelle_y(400)), (echelle_x(1000), echelle_y(400)), (echelle_x(1500), echelle_y(400)), (echelle_x(2000), echelle_y(400)),
                    (echelle_x(500), echelle_y(800)), (echelle_x(1000), echelle_y(800)), (echelle_x(1500), echelle_y(800)), (echelle_x(2000), echelle_y(800)),
                    (echelle_x(500), echelle_y(1200)), (echelle_x(1000), echelle_y(1200)), (echelle_x(1500), echelle_y(1200)), (echelle_x(2000), echelle_y(1200)) ] 
        r=["image/deprost.png","image/aribi.png","image/bellagha.png","image/chivers.png","image/bouzidi.png","image/bellagha.png",'image/bouzidi.png','image/hagbe.png',"image/deprost.png",'image/hagbe.png','image/aribi.png','image/chivers.png']
        s=0
        for x,y in dimensions:
            self.im = QPushButton(self)
            self.im.setGeometry(x,y, echelle_y(350), echelle_y(350))
            self.im.setIcon(QIcon("image/mimi.png"))  
            self.im.setIconSize(self.im.size())
            image= r[s]
            self.im.clicked.connect(lambda checked= False, b=self.im, im=image: self.retourner(b, im))
            s+=1
            
        self.btn_close = QPushButton(self)
        self.btn_close.setGeometry(echelle_x(100), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close.setIcon(QIcon("image/arrow.png"))  
        self.btn_close.setIconSize(self.btn_close.size()) 
        self.btn_close.clicked.connect(self.ouvre1)
        
        self.btn_close1 = QPushButton(self)
        self.btn_close1.setGeometry(echelle_x(2600), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close1.setIcon(QIcon("image/arrow2.png"))
        self.btn_close1.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close1.clicked.connect(self.ouvre)

        self.btn_close2 = QPushButton(self)
        self.btn_close2.setGeometry(echelle_x(100), echelle_y(30), echelle_x(100), echelle_y(100))
        self.btn_close2.setIcon(QIcon("image/home.png"))
        self.btn_close2.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close2.clicked.connect(self.ouvre2)
        
        self.showMaximized()
        
    def ouvre(self):
        self.fenetre7 = Fenetre7()
        self.fenetre7.showMaximized()
        self.close()
        
    def ouvre1(self):
        self.fenetre5 = Fenetre5()
        self.fenetre5.showMaximized()
        self.close()

    def ouvre2(self):
        self.menu = Menu()
        self.menu.showMaximized()
        self.close()

    def retourner(self, bouton, image):
        if bouton in [x[0] for x in self.renv]:
            return None
        bouton.setIcon(QIcon(image))
        self.renv.append((bouton, image))
        if len(self.renv) == 2:
            self.verifier_paire()

    def verifier_paire(self):
        b1, image1 = self.renv[0]
        b2, image2 = self.renv[1]

        if image1 == image2:
            self.paires_correctes += 1
            self.label1.setText(f"Paires correctes: {self.paires_correctes}")
            self.renv = []
            if self.paires_correctes == 6:
                self.felicitation()
        else:
            self.vie -= 1
            self.label.setText(f"Vies restantes: {self.vie}")
            QTimer.singleShot(500, lambda: self.retourner22(b1, b2))
            if self.vie <= 0:
                self.play_audio('son/perdu.wav')
                QMessageBox.critical(self, "Perdu !", "Tu as perdu toutes tes vies ! Réessaie !")
                self.ouvre1()

    def retourner22(self, b1, b2):
        b1.setIcon(QIcon("image/mimi.png"))
        b2.setIcon(QIcon("image/mimi.png"))
        self.renv = []

    def felicitation(self):
        self.play_audio('son/gagner.wav')
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Félicitations !")
        msg_box.setText("Bravo, tu as réussi !")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
        self.ouvre() 

    def play_audio(self, sound_file):
        QSound.play(sound_file)
        
class Fenetre7(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memorychons')
        self.setStyleSheet("background-color: #DED9A3;")

        self.paires_correctes = 0
        self.renv = []
        self.vie=7
        
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Copeland.otf")
        font_id = QFontDatabase.addApplicationFont("fonts/Copeland.otf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        font_path2 = os.path.join(os.path.dirname(__file__), "fonts","Quitle.otf")
        font_id2 = QFontDatabase.addApplicationFont("fonts/Quitle.otf")
        font_families2 = QFontDatabase.applicationFontFamilies(font_id2)[0]
        
        self.niv = QLabel("NIVEAU 6",self)  
        self.niv.setFont(QFont(font_families, 100))
        self.niv.setStyleSheet("color: #45721C;")
        self.niv.setGeometry(echelle_x(900), echelle_y(100), echelle_x(1000), echelle_y(300))
        
        self.vie1 = QLabel(self)
        pixmap = QPixmap('image/heart.png')
        pixmap_resized = pixmap.scaled(echelle_x(70), echelle_y(70))  
        self.vie1.setPixmap(pixmap_resized)
        self.vie1.resize(pixmap_resized.width(), pixmap_resized.height())
        self.vie1.move(echelle_x(100), echelle_y(230))
        
        self.label = QLabel(f"Vies restantes: {self.vie}",self)
        self.label.setFont(QFont(font_families2, 30))
        self.label.setStyleSheet("color: #45721C;")
        self.label.setGeometry(echelle_x(180), echelle_y(220), echelle_x(600), echelle_y(70)) 
        
        self.label1 = QLabel(f"Paires correctes: {self.paires_correctes}", self)
        self.label1.setFont(QFont(font_families2, 30))
        self.label1.setStyleSheet("color: #45721C;")
        self.label1.setGeometry(echelle_x(2150), echelle_y(220), echelle_x(700), echelle_y(70)) 
        


        dimensions = [
            (echelle_x(100), echelle_y(550)), (echelle_x(100), echelle_y(950)),
            (echelle_x(500), echelle_y(550)), (echelle_x(500), echelle_y(950)),
            (echelle_x(900), echelle_y(550)), (echelle_x(900), echelle_y(950)),
            (echelle_x(1300), echelle_y(550)), (echelle_x(1300), echelle_y(950)),
            (echelle_x(1700), echelle_y(550)), (echelle_x(1700), echelle_y(950)),
            (echelle_x(2100), echelle_y(550)), (echelle_x(2100), echelle_y(950)),
            (echelle_x(2500), echelle_y(550)), (echelle_x(2500), echelle_y(950))
        ]       
        r=["image/eva.png","image/deprost.png","image/aribi.png","image/chivers.png","image/bouzidi.png","image/eva.png",'image/bouzidi.png','image/hagbe.png',"image/bellagha.png",'image/hagbe.png','image/bellagha.png','image/chivers.png','image/aribi.png','image/deprost.png']
        s=0
        for x,y in dimensions:
            self.im = QPushButton(self)
            self.im.setGeometry(x,y, echelle_y(300), echelle_y(300))
            self.im.setIcon(QIcon("image/mimi.png"))  
            self.im.setIconSize(self.im.size())
            image= r[s]
            self.im.clicked.connect(lambda checked= False, b=self.im, im=image: self.retourner(b, im))
            s+=1
            
        self.btn_close = QPushButton(self)
        self.btn_close.setGeometry(echelle_x(100), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close.setIcon(QIcon("image/arrow.png"))  
        self.btn_close.setIconSize(self.btn_close.size()) 
        self.btn_close.clicked.connect(self.ouvre1)
        
        self.btn_close1 = QPushButton(self)
        self.btn_close1.setGeometry(echelle_x(2600), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close1.setIcon(QIcon("image/arrow2.png"))
        self.btn_close1.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close1.clicked.connect(self.ouvre)

        self.btn_close2 = QPushButton(self)
        self.btn_close2.setGeometry(echelle_x(100), echelle_y(30), echelle_x(100), echelle_y(100))
        self.btn_close2.setIcon(QIcon("image/home.png"))
        self.btn_close2.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close2.clicked.connect(self.ouvre2)
        
        self.showMaximized()
        
    def ouvre(self):
        self.fenetre8 = Fenetre8()
        self.fenetre8.showMaximized()
        self.close()
        
    def ouvre1(self):
        self.fenetre6 = Fenetre6()
        self.fenetre6.showMaximized()
        self.close()

    def ouvre2(self):
        self.menu = Menu()
        self.menu.showMaximized()
        self.close()

    def retourner(self, bouton, image):
        if bouton in [x[0] for x in self.renv]:
            return None
        bouton.setIcon(QIcon(image))
        self.renv.append((bouton, image))
        if len(self.renv) == 2:
            self.verifier_paire()

    def verifier_paire(self):
        b1, image1 = self.renv[0]
        b2, image2 = self.renv[1]

        if image1 == image2:
            self.paires_correctes += 1
            self.label1.setText(f"Paires correctes: {self.paires_correctes}")
            self.renv = []
            if self.paires_correctes == 7:
                self.felicitation()
        else:
            self.vie -= 1
            self.label.setText(f"Vies restantes: {self.vie}")
            QTimer.singleShot(500, lambda: self.retourner22(b1, b2))
            if self.vie <= 0:
                self.play_audio('son/perdu.wav')
                QMessageBox.critical(self, "Perdu !", "Tu as perdu toutes tes vies ! Réessaie !")
                
                self.ouvre1()

    def retourner22(self, b1, b2):
        b1.setIcon(QIcon("image/mimi.png"))
        b2.setIcon(QIcon("image/mimi.png"))
        self.renv = []

    def felicitation(self):
        self.play_audio('son/gagner.wav')
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Félicitations !")
        
        msg_box.setText("Bravo, tu as réussi !")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
        self.ouvre() 

    def play_audio(self, sound_file):
        QSound.play(sound_file)
        
class Fenetre8(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memorychons')
        self.setStyleSheet("background-color: #DED9A3;")

        self.paires_correctes = 0
        self.renv = []
        self.vie=8
        
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Copeland.otf")
        font_id = QFontDatabase.addApplicationFont("fonts/Copeland.otf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        font_path2 = os.path.join(os.path.dirname(__file__), "fonts","Quitle.otf")
        font_id2 = QFontDatabase.addApplicationFont("fonts/Quitle.otf")
        font_families2 = QFontDatabase.applicationFontFamilies(font_id2)[0]
        
        self.niv = QLabel("NIVEAU 7",self)  
        self.niv.setFont(QFont(font_families, 100))
        self.niv.setStyleSheet("color: #45721C;")
        self.niv.setGeometry(echelle_x(900), echelle_y(100), echelle_x(1000), echelle_y(300))
        
        self.vie1 = QLabel(self)
        pixmap = QPixmap('image/heart.png')
        pixmap_resized = pixmap.scaled(echelle_x(70), echelle_y(70))  
        self.vie1.setPixmap(pixmap_resized)
        self.vie1.resize(pixmap_resized.width(), pixmap_resized.height())
        self.vie1.move(echelle_x(100), echelle_y(230))
        
        self.label = QLabel(f"Vies restantes: {self.vie}",self)
        self.label.setFont(QFont(font_families2, 30))
        self.label.setStyleSheet("color: #45721C;")
        self.label.setGeometry(echelle_x(180), echelle_y(220), echelle_x(600), echelle_y(70)) 
        
        self.label1 = QLabel(f"Paires correctes: {self.paires_correctes}", self)
        self.label1.setFont(QFont(font_families2, 30))
        self.label1.setStyleSheet("color: #45721C;")
        self.label1.setGeometry(echelle_x(2150), echelle_y(220), echelle_x(700), echelle_y(70)) 

        dimensions=[(echelle_x(900), echelle_y(400)), (echelle_x(900), echelle_y(700)), 
                    (echelle_x(900), echelle_y(1000)), (echelle_x(900), echelle_y(1300)),
                    (echelle_x(1200), echelle_y(400)), (echelle_x(1200), echelle_y(700)), 
                    (echelle_x(1200), echelle_y(1000)), (echelle_x(1200), echelle_y(1300)),
                    (echelle_x(1500), echelle_y(400)), (echelle_x(1500), echelle_y(700)), 
                    (echelle_x(1500), echelle_y(1000)), (echelle_x(1500), echelle_y(1300)),
                    (echelle_x(1800), echelle_y(400)), (echelle_x(1800), echelle_y(700)), 
                    (echelle_x(1800), echelle_y(1000)), (echelle_x(1800), echelle_y(1300))]
        r=["image/eva.png","image/oumaima.png","image/deprost.png","image/chivers.png","image/bouzidi.png","image/eva.png",'image/oumaima.png','image/hagbe.png',"image/bellagha.png",'image/hagbe.png','image/aribi.png','image/chivers.png','image/bouzidi.png','image/deprost.png','image/bellagha.png','image/aribi.png']
        s=0
        for x,y in dimensions:
            self.im = QPushButton(self)
            self.im.setGeometry(x,y, echelle_y(250), echelle_y(250))
            self.im.setIcon(QIcon("image/mimi.png"))  
            self.im.setIconSize(self.im.size())
            image= r[s]
            self.im.clicked.connect(lambda checked= False, b=self.im, im=image: self.retourner(b, im))
            s+=1
            
        self.btn_close = QPushButton(self)
        self.btn_close.setGeometry(echelle_x(100), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close.setIcon(QIcon("image/arrow.png"))  
        self.btn_close.setIconSize(self.btn_close.size()) 
        self.btn_close.clicked.connect(self.ouvre1)
        
        self.btn_close1 = QPushButton(self)
        self.btn_close1.setGeometry(echelle_x(2600), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close1.setIcon(QIcon("image/arrow2.png"))
        self.btn_close1.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close1.clicked.connect(self.ouvre)

        self.btn_close2 = QPushButton(self)
        self.btn_close2.setGeometry(echelle_x(100), echelle_y(30), echelle_x(100), echelle_y(100))
        self.btn_close2.setIcon(QIcon("image/home.png"))
        self.btn_close2.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close2.clicked.connect(self.ouvre2)
        
        self.showMaximized()
        
    def ouvre(self):
        self.fenetre9 = Fenetre9()
        self.fenetre9.showMaximized()
        self.close()
        
    def ouvre1(self):
        self.fenetre7 = Fenetre7()
        self.fenetre7.showMaximized()
        self.close()

    def ouvre2(self):
        self.menu = Menu()
        self.menu.showMaximized()
        self.close()

    def retourner(self, bouton, image):
        if bouton in [x[0] for x in self.renv]:
            return None
        bouton.setIcon(QIcon(image))
        self.renv.append((bouton, image))
        if len(self.renv) == 2:
            self.verifier_paire()

    def verifier_paire(self):
        b1, image1 = self.renv[0]
        b2, image2 = self.renv[1]

        if image1 == image2:
            self.paires_correctes += 1
            self.label1.setText(f"Paires correctes: {self.paires_correctes}")
            self.renv = []
            if self.paires_correctes == 8:
                self.felicitation()
        else:
            self.vie -= 1
            self.label.setText(f"Vies restantes: {self.vie}")
            QTimer.singleShot(500, lambda: self.retourner22(b1, b2))
            if self.vie <= 0:
                self.play_audio('son/perdu.wav')
                QMessageBox.critical(self, "Perdu !", "Tu as perdu toutes tes vies ! Réessaie !")
                
                self.ouvre1()

    def retourner22(self, b1, b2):
        b1.setIcon(QIcon("image/mimi.png"))
        b2.setIcon(QIcon("image/mimi.png"))
        self.renv = []

    def felicitation(self):
        self.play_audio('son/gagner.wav')
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Félicitations !")
        msg_box.setText("Bravo, tu as réussi !")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
        self.ouvre() 

    def play_audio(self, sound_file):
        QSound.play(sound_file)
            
class Fenetre9(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Memorychons')
        self.setStyleSheet("background-color: #DED9A3;")

        self.paires_correctes = 0
        self.renv = []
        self.vie=9
        
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Copeland.otf")
        font_id = QFontDatabase.addApplicationFont("fonts/Copeland.otf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        font_path2 = os.path.join(os.path.dirname(__file__), "fonts","Quitle.otf")
        font_id2 = QFontDatabase.addApplicationFont("fonts/Quitle.otf")
        font_families2 = QFontDatabase.applicationFontFamilies(font_id2)[0]
        
        self.niv = QLabel("NIVEAU 8",self)  
        self.niv.setFont(QFont(font_families, 100))
        self.niv.setStyleSheet("color: #45721C;")
        self.niv.setGeometry(echelle_x(900), echelle_y(100), echelle_x(1000), echelle_y(300))
        
        self.vie1 = QLabel(self)
        pixmap = QPixmap('image/heart.png')
        pixmap_resized = pixmap.scaled(echelle_x(70), echelle_y(70))  
        self.vie1.setPixmap(pixmap_resized)
        self.vie1.resize(pixmap_resized.width(), pixmap_resized.height())
        self.vie1.move(echelle_x(100), echelle_y(230))
        
        self.label = QLabel(f"Vies restantes: {self.vie}",self)
        self.label.setFont(QFont(font_families2, 30))
        self.label.setStyleSheet("color: #45721C;")
        self.label.setGeometry(echelle_x(180), echelle_y(220), echelle_x(600), echelle_y(70)) 
        
        self.label1 = QLabel(f"Paires correctes: {self.paires_correctes}", self)
        self.label1.setFont(QFont(font_families2, 30))
        self.label1.setStyleSheet("color: #45721C;")
        self.label1.setGeometry(echelle_x(2150), echelle_y(220), echelle_x(700), echelle_y(70)) 

        dimensions = [
            (echelle_x(300), echelle_y(400)), (echelle_x(300), echelle_y(800)), (echelle_x(300), echelle_y(1200)),
            (echelle_x(700), echelle_y(400)), (echelle_x(700), echelle_y(800)), (echelle_x(700), echelle_y(1200)),
            (echelle_x(1100), echelle_y(400)), (echelle_x(1100), echelle_y(800)), (echelle_x(1100), echelle_y(1200)),
            (echelle_x(1500), echelle_y(400)), (echelle_x(1500), echelle_y(800)), (echelle_x(1500), echelle_y(1200)),
            (echelle_x(1900), echelle_y(400)), (echelle_x(1900), echelle_y(800)), (echelle_x(1900), echelle_y(1200)),
            (echelle_x(2300), echelle_y(400)), (echelle_x(2300), echelle_y(800)), (echelle_x(2300), echelle_y(1200))
            ]
        r=["image/chivers.png","image/aribi.png","image/deprost.png","image/eva.png","image/bouzidi.png","image/eva.png",'image/bellagha.png','image/hagbe.png',"image/sophie.png",'image/oumaima.png','image/hagbe.png','image/sophie.png','image/chivers.png','image/bouzidi.png','image/deprost.png','image/aribi.png','image/oumaima.png','image/bellagha.png']
        s=0
        for x,y in dimensions:
            self.im = QPushButton(self)
            self.im.setGeometry(x,y, echelle_y(350), echelle_y(350))
            self.im.setIcon(QIcon("image/mimi.png"))  
            self.im.setIconSize(self.im.size())
            image= r[s]
            self.im.clicked.connect(lambda checked= False, b=self.im, im=image: self.retourner(b, im))
            s+=1
            
        self.btn_close = QPushButton(self)
        self.btn_close.setGeometry(echelle_x(100), echelle_y(1550), echelle_x(100), echelle_y(100))
        self.btn_close.setIcon(QIcon("image/arrow.png"))  
        self.btn_close.setIconSize(self.btn_close.size()) 
        self.btn_close.clicked.connect(self.ouvre1)

        self.btn_close2 = QPushButton(self)
        self.btn_close2.setGeometry(echelle_x(100), echelle_y(30), echelle_x(100), echelle_y(100))
        self.btn_close2.setIcon(QIcon("image/home.png"))
        self.btn_close2.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close2.clicked.connect(self.ouvre2)
        self.showMaximized()
        
    def ouvre1(self):
        self.fenetre8 = Fenetre8()
        self.fenetre8.showMaximized()
        self.close()

    def ouvre2(self):
        self.menu = Menu()
        self.menu.showMaximized()
        self.close()

    def retourner(self, bouton, image):
        if bouton in [x[0] for x in self.renv]:
            return None
        bouton.setIcon(QIcon(image))
        self.renv.append((bouton, image))
        if len(self.renv) == 2:
            self.verifier_paire()

    def verifier_paire(self):
        b1, image1 = self.renv[0]
        b2, image2 = self.renv[1]

        if image1 == image2:
            self.paires_correctes += 1
            self.label1.setText(f"Paires correctes: {self.paires_correctes}")
            self.renv = []
            if self.paires_correctes == 9:
                self.felicitation()
        else:
            self.vie -= 1
            self.label.setText(f"Vies restantes: {self.vie}")
            QTimer.singleShot(500, lambda: self.retourner22(b1, b2))
            if self.vie <= 0:
                self.play_audio('son/perdu.wav')
                QMessageBox.critical(self, "Perdu !", "Tu as perdu toutes tes vies ! Réessaie !")
                self.ouvre1()

    def retourner22(self, b1, b2):
        b1.setIcon(QIcon("image/mimi.png"))
        b2.setIcon(QIcon("image/mimi.png"))
        self.renv = []

    def felicitation(self):
        self.play_audio('son/gagner.wav')
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Félicitations !")
        msg_box.setText("Bravo, tu as réussi !")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
        self.ouvre2() 

    def play_audio(self, sound_file):
        QSound.play(sound_file)
        
class Fenetre10(QMainWindow):
    def __init__(self,joueur1,joueur2):
        super().__init__()
        self.setWindowTitle('Memorychons')
        self.setStyleSheet("background-color: #DED9A3;")
        
        self.paires=0
        self.paires_correctes_joueur1 = 0
        self.paires_correctes_joueur2 = 0
        self.renv = []
        self.joueur1=joueur1.upper()
        self.joueur2=joueur2.upper()
        self.tour=self.joueur1
        
        font_path = os.path.join(os.path.dirname(__file__), "fonts", "Copeland.otf")
        font_id = QFontDatabase.addApplicationFont("fonts/Copeland.otf")
        font_families = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        font_path2 = os.path.join(os.path.dirname(__file__), "fonts","Quitle.otf")
        font_id2 = QFontDatabase.addApplicationFont("fonts/Quitle.otf")
        font_families2 = QFontDatabase.applicationFontFamilies(font_id2)[0]
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        central_widget.setLayout(layout)
        titre = QHBoxLayout()
        self.niv = QLabel(f"{self.joueur1} VS {self.joueur2}", self)
        self.niv.setFont(QFont(font_families, 70))
        self.niv.setStyleSheet("color: #45721C; padding: 20px;")
        self.niv.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        titre.addStretch()
        titre.addWidget(self.niv)
        titre.addStretch()
        layout.addLayout(titre)
        layout.addSpacing(20) 
        
        self.label = QLabel(f"C'est au tour de {self.tour}", self)
        self.label.setFont(QFont(font_families, 30))
        self.label.setGeometry(echelle_x(1000), echelle_y(350), echelle_x(800), echelle_y(100))
        self.label.setStyleSheet("color: #45721C;")
        
        self.label1 = QLabel(f"Paires correctes de {self.joueur1}: {self.paires_correctes_joueur1}", self)
        self.label1.setFont(QFont(font_families2, 20))
        self.label1.setStyleSheet("color: #45721C;")
        self.label1.setGeometry(echelle_x(80), echelle_y(220), echelle_x(700), echelle_y(100))
    
        self.label2 = QLabel(f"Paires correctes de {self.joueur2}: {self.paires_correctes_joueur2}", self)
        self.label2.setFont(QFont(font_families2, 20))
        self.label2.setStyleSheet("color: #45721C;")
        self.label2.setGeometry(echelle_x(2150), echelle_y(220), echelle_x(700), echelle_y(100))
            
        dimensions=[(echelle_x(300), echelle_y(500)), (echelle_x(300), echelle_y(900)), (echelle_x(300), echelle_y(1300)),
            (echelle_x(700), echelle_y(500)), (echelle_x(700), echelle_y(900)), (echelle_x(700), echelle_y(1300)),
            (echelle_x(1100), echelle_y(500)), (echelle_x(1100), echelle_y(900)), (echelle_x(1100), echelle_y(1300)),
            (echelle_x(1500), echelle_y(500)), (echelle_x(1500), echelle_y(900)), (echelle_x(1500), echelle_y(1300)),
            (echelle_x(1900), echelle_y(500)), (echelle_x(1900), echelle_y(900)), (echelle_x(1900), echelle_y(1300)),
            (echelle_x(2300), echelle_y(500)), (echelle_x(2300), echelle_y(900)), (echelle_x(2300), echelle_y(1300))]
        r=["image/aribi.png","image/ilhan.png","image/deprost.png","image/eva.png","image/bouzidi.png","image/eva.png",'image/bellagha.png','image/hagbe.png',"image/sophie.png",'image/oumaima.png','image/hagbe.png','image/ilhan.png','image/aribi.png','image/bouzidi.png','image/deprost.png','image/sophie.png','image/oumaima.png','image/bellagha.png']
        s=0
        for x,y in dimensions:
            im = QPushButton(self)
            im.setGeometry(x,y, echelle_y(350), echelle_y(350))
            im.setIcon(QIcon("image/mimi.png"))  
            im.setIconSize(im.size())
            image= r[s]
            im.clicked.connect(lambda checked= False, b=im, im=image: self.retourner(b, im))
            s+=1

        self.btn_close2 = QPushButton(self)
        self.btn_close2.setGeometry(echelle_x(100), echelle_y(30), echelle_x(100), echelle_y(100))
        self.btn_close2.setIcon(QIcon("image/home.png"))
        self.btn_close2.setIconSize(QSize(echelle_x(80), echelle_y(80)))
        self.btn_close2.clicked.connect(self.ouvre2)
        
        self.showMaximized()
        
    def retourner(self, bouton, image):
        if bouton in [x[0] for x in self.renv]:
            return None
        bouton.setIcon(QIcon(image))
        self.renv.append((bouton, image))
        if len(self.renv) == 2:
            self.verifier_paire()

    def verifier_paire(self):
        b1, image1 = self.renv[0]
        b2, image2 = self.renv[1]
        if image1 == image2:
            if self.tour==self.joueur1:
                self.paires_correctes_joueur1 += 1
                self.label1.setText(f"Paires correctes de {self.joueur1}: {self.paires_correctes_joueur1}")
            else:
                self.paires_correctes_joueur2 += 1
                self.label2.setText(f"Paires correctes de {self.joueur2}: {self.paires_correctes_joueur2}")
            self.renv = []
            self.paires+=1
            if self.paires == 9:
                self.felicitation()
        else:
            QTimer.singleShot(500, lambda: self.retourner22(b1, b2))
            if self.tour == self.joueur1:
                self.tour = self.joueur2
            else:
                self.tour= self.joueur1
        self.label.setText(f"C'est au tour de {self.tour}")

    def retourner22(self, b1, b2):
        b1.setIcon(QIcon("image/mimi.png"))
        b2.setIcon(QIcon("image/mimi.png"))
        self.renv = []

    def felicitation(self):
        self.play_audio('son/gagner.wav')
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Félicitations !")
        if self.paires_correctes_joueur1>self.paires_correctes_joueur2:
            msg_box.setText(f"Bravo, {self.joueur1} a gagné !")
        elif self.paires_correctes_joueur1<self.paires_correctes_joueur2:
            msg_box.setText(f"Bravo, {self.joueur2} a gagné !")
        else:
            msg_box.setText("Vous êtes à égalité !")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.exec_()
        self.ouvre2() 
    

    def play_audio(self, sound_file):
        QSound.play(sound_file)
    
    def ouvre2(self):
        self.menu = Menu()
        self.menu.showMaximized()
        self.close()

app = QCoreApplication.instance()

if app is None:
    app = QApplication(sys.argv)

window = Fenetre1()
window.showMaximized()

app.exec_()