import sys
# Se estiver usando PyQt6, basta trocar "PySide6" por "PyQt6" nos imports
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt

class OverlayWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.largura = 300
        self.altura = 150
        self.resize(self.largura, self.altura)
        
        # 1. Configura as flags da janela (Sem borda e sempre no topo)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        
        # 2. Ativa a transparência total do fundo da janela
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        
        # Define o tamanho inicial do seu overlay
        self.resize(400, 200)
        
        # Layout interno
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # 3. Criando elementos visíveis
        # Texto estilizado com CSS para garantir legibilidade no fundo transparente
        self.label = QLabel("Este é um Texto de Overlay!")
        self.label.setStyleSheet("""
            QLabel {
                color: #FFFFFF; 
                font-size: 24px; 
                font-weight: bold;
                background-color: rgba(0, 0, 0, 0.6); /* Fundo preto 60% transparente */
                padding: 10px;
                border-radius: 8px;
            }
        """)
        
        # Botão para fechar o overlay facilmente
        self.btn_fechar = QPushButton("Fechar Overlay")
        self.btn_fechar.clicked.connect(self.close)
        self.btn_fechar.setStyleSheet("""
            QPushButton {
                background-color: #E74C3C;
                color: white;
                font-size: 14px;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #C0392B;
            }
        """)
        
        # Adiciona os elementos ao layout
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.btn_fechar, alignment=Qt.AlignmentFlag.AlignLeft)
        
        self.setOnSide()

    def setOnSide(self):        
        tela = QApplication.primaryScreen()
        geometria_tela = tela.availableGeometry()
                
        self.adjustSize()
                
        largura_real = self.width()
        altura_real = self.height()
                
        margin_offset = 20                 
        x = geometria_tela.left() + geometria_tela.width() - largura_real - margin_offset                
        y = geometria_tela.top() + (geometria_tela.height() // 2) - (altura_real // 2)
                
        self.move(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = OverlayWindow()
    overlay.show()
    sys.exit(app.exec())
