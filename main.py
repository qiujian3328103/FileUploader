import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLineEdit, QFileDialog, QMessageBox, 
                             QProgressDialog)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
import time
from MainWindow import Ui_MainWindow
import resource_rc

class myApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # set the secret key as password format 
        self.lineEdit_secretKey.setEchoMode(QLineEdit.EchoMode.Password)
        # Load settings
        self.loadSettings()

        # Connect the button's clicked signal to the selectFiles function
        self.pushButton_select.clicked.connect(self.selectFiles)
        self.pushButton_submit.clicked.connect(self.submitFiles)
        self.pushButton_clear.clicked.connect(self.clearList)

    def loadSettings(self):
        settings = QSettings("setting.ini", QSettings.IniFormat)

        # Assuming you have lineEdit widgets named lineEdit_url, lineEdit_secretKey, and lineEdit_bucketName
        self.lineEdit_url.setText(settings.value("LineEdit/url", ""))
        self.lineEdit_secretKey.setText(settings.value("LineEdit/secretKey", ""))
        self.lineEdit_bucketName.setText(settings.value("LineEdit/bucketName", ""))

    def selectFiles(self):
        # Open a file dialog and get selected file paths
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Select Files", "", "All Files (*)")

        # If files are selected, add them to the listWidget
        if file_paths:
            self.listWidget.addItems(file_paths)

    def submitFiles(self):
        # Get the count of items in the listWidget
        itemCount = self.listWidget.count()

        # If there are no items in the listWidget, show an error message
        if itemCount == 0:
            QMessageBox.warning(self, "Error", "Please select at least one file.")
            return
        
        # If there are items, print their filenames and paths
        for index in range(itemCount):
            file_path = self.listWidget.item(index).text()
            print(f"Filename: {os.path.basename(file_path)}")
            print(f"Path: {file_path}")

        files = [self.listWidget.item(index).text() for index in range(self.listWidget.count())]

        # Initialize progress dialog
        self.progress_dialog = QProgressDialog("Processing Files...", "Cancel", 0, 100, self)
        self.progress_dialog.setAutoClose(True)
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.show()

        # Create the worker thread and connect signals
        self.worker = FileProcessor(files)
        self.worker.progress_signal.connect(self.update_progress)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(self.progress_dialog.close)
        self.worker.start()
    
    def update_progress(self, progress):
        self.progress_dialog.setValue(progress)
    

    def clearList(self):
        # Create a confirmation dialog
        reply = QMessageBox.question(self, "Confirmation",
                                     "Are you sure you want to clear all the items?",
                                     QMessageBox.Yes | QMessageBox.No)

        # If user confirms, clear the items in the listWidget
        if reply == QMessageBox.Yes:
            self.listWidget.clear()


class FileProcessor(QThread):
    progress_signal = pyqtSignal(int)  # Signal to update progress
    # Add other signals as needed

    def __init__(self, files):
        super().__init__()
        self.files = files

    def run(self):
        total_files = len(self.files)
        for index, file in enumerate(self.files):
            # Simulating time-consuming process
            time.sleep(5)  # Wait for 1 second for each file

            # Emit the progress signal
            progress_percentage = int((index + 1) / total_files * 100)
            self.progress_signal.emit(progress_percentage)


if __name__== "__main__":
    import os
    os.environ['QT_MAC_WANTS_LAYER'] = '1'
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app.aboutToQuit.connect(app.deleteLater)  #### use to prevet the keranl dying every time
    try:
        app.setStyle('Fusion')
    except:
        pass

    window = myApp()
    window.show()
    sys.exit(app.exec())
