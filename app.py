from PySide6 import QtWidgets, QtCore
from movie import get_movies, Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.setup_connections()
        self.populate_movies()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.textInput = QtWidgets.QLineEdit()
        self.btn_add_movie = QtWidgets.QPushButton("Ajouter un film")
        self.list_movie = QtWidgets.QListWidget()
        self.list_movie.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_remove_movie = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout.addWidget(self.textInput)
        self.layout.addWidget(self.btn_add_movie)
        self.layout.addWidget(self.list_movie)
        self.layout.addWidget(self.btn_remove_movie)

    def setup_connections(self):
        self.btn_add_movie.clicked.connect(self.add_movie)
        self.btn_remove_movie.clicked.connect(self.remove_movie)
        self.textInput.returnPressed.connect(self.add_movie)
    
    def populate_movies(self):
        movies = get_movies()
        # First method
        #for movie in movies:
        #    self.list_movie.addItem(movie.title)

        # Second method
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.list_movie.addItem(lw_item)

    def add_movie(self):
        movie_title = self.textInput.text()
        if not movie_title:
            return False
        movie = Movie(movie_title)
        resultat = movie.add_to_movies()
        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.list_movie.addItem(lw_item)
        
        self.textInput.setText("")

    def remove_movie(self):
        for selected_item in self.list_movie.selectedItems():
            #movie = Movie(selected_item.text())
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.list_movie.takeItem(self.list_movie.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()