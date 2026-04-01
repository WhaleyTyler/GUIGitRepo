# converter.py
# Student: Tyler Whaley | Course: CSPC3118  | Project: Assignment 7 (PySide6) | Date: 04-01-2026

import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QRadioButton, QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout,
    QMessageBox, QFrame
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

INCH_TO_METER = 0.0254

class ConverterWindow(QMainWindow):
    """Main window class for the measurement converter app."""
    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        self.setWindowTitle("Measurement Converter (PySide6)")
        self._build_ui()
        self._wire_events()
        self._reset_form()

    def _build_ui(self):
        """Build the UI elements for the measurement converter app."""
        central = QWidget(self)
        self.setCentralWidget(central)

        # Create the main title label
        self.lblTitle = QLabel("Converter App")
        self.lblTitle.setStyleSheet("font-size: 24px; font-weight: bold;")

        # Create input label and text field for user entry
        self.lblPrompt = QLabel("Enter a value and\nchoose conversion")
        self.lblPrompt.setStyleSheet("font-size: 15px; font-weight: bold;")
        self.txtInput = QLineEdit()
        self.txtInput.setPlaceholderText("e.g., 10")
        self.txtInput.setFixedWidth(90)

        # Create group to hold conversion options
        self.grp = QGroupBox("Convert Measurement")
        self.grp.setFixedSize(200, 80)

        # Create Radio Buttons
        self.rbInToM = QRadioButton("Inches to Meters")
        self.rbInToM.setStyleSheet("color: white;")
        self.rbMToIn = QRadioButton("Meters to Inches")
        self.rbMToIn.setStyleSheet("color: white;")

        # Add radio buttons to the vertical Layout inside group box
        vgrp = QVBoxLayout()
        vgrp.addWidget(self.rbInToM)
        vgrp.addWidget(self.rbMToIn)
        self.grp.setLayout(vgrp)

        # Create buttons for user action
        self.btnConvert = QPushButton("Convert")
        self.btnClear = QPushButton("Clear")
        self.btnExit = QPushButton("Exit")

        # Set size for all buttons
        for btn in [self.btnConvert, self.btnClear, self.btnExit]:
            btn.setFixedWidth(150)
            btn.setFixedHeight(40)

        # Create label to display conversion results
        self.lblResult = QLabel("")
        self.lblResult.setAlignment(Qt.AlignCenter)
        self.lblResult.setStyleSheet("font-size: 18px; font-weight: bold;")

        # Load and display the image
        self.imgFrame = QFrame()
        self.imgLabel = QLabel(alignment=Qt.AlignCenter)
        pix = QPixmap("assets/house.png")
        self.imgLabel.setPixmap(pix.scaled(180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        vimg = QVBoxLayout(self.imgFrame)
        vimg.addWidget(self.imgLabel)

        # Create the grid layout and position all widgets
        grid = QGridLayout(central)
        grid.setContentsMargins(20, 20, 20, 20)
        grid.setHorizontalSpacing(25)
        grid.setVerticalSpacing(20)

        # Place image in the top-left
        grid.addWidget(self.imgFrame, 0, 0, 2, 1, alignment=Qt.AlignTop | Qt.AlignLeft)

        # Title and prompt area
        grid.addWidget(self.lblTitle, 0, 1, 1, 1, alignment=Qt.AlignLeft)
        grid.addWidget(self.lblPrompt, 1, 1, 1, 1, alignment=Qt.AlignLeft)
        grid.addWidget(self.txtInput, 1, 2, 1, 1, alignment=Qt.AlignLeft)

        # Radio group under prompt
        grid.addWidget(self.grp, 2, 1, 1, 2, alignment=Qt.AlignLeft)

        # Result centered below
        grid.addWidget(self.lblResult, 3, 0, 1, 3, alignment=Qt.AlignCenter)

        # Create layout for buttons at bottom
        hbtns = QHBoxLayout()
        hbtns.addWidget(self.btnConvert)
        hbtns.addWidget(self.btnClear)
        hbtns.addWidget(self.btnExit)
        grid.addLayout(hbtns, 4, 0, 1, 3)

        # Optional theming: ensure contrast/readability
        self.setStyleSheet("""
            QMainWindow { background: #E6D9FF; }
            QLabel, QRadioButton { color: #1F1F1F; font-size: 14px; }
            QGroupBox { color: white;
            font-size: 14px;
            background: #4a148c;
            font-weight: bold;
            border: none;
            padding: 10px;
            }
            QLineEdit { font-size: 14px;
            font-weight: bold;
            padding: 6px;
            background: #4a148c; 
            color: white;
            border: 2px solid lightgray;
            }
            QPushButton { 
            font-size: 14px;
            padding: 8px 20px;
            background: #E6D9FF;
            color: black;
            font-weight: bold;
            border: 2px solid white;
            }
            QPushButton::hover
            {
            border: 2px solid #2196F3;
            }
        """)

    def _wire_events(self):
        """Connect button clicks to their event handlers."""
        self.btnConvert.clicked.connect(self.on_convert)
        self.btnClear.clicked.connect(self.on_clear)
        self.btnExit.clicked.connect(QApplication.instance().quit)

    def _reset_form(self):
        """Reset the form to its default value."""
        self.txtInput.clear()
        self.lblResult.clear()
        self.rbInToM.setChecked(True)
        self.txtInput.setFocus()

    def _error(self, message: str):
        """Display an error message."""
        QMessageBox.critical(self, "Error", message)

    def on_clear(self):
        """Handle clear button clicks by resetting the form."""
        self._reset_form()

    def on_convert(self):
        """Validate input and perform selected conversion."""
        text = self.txtInput.text().strip()

        # Check for empty text
        if not text:
            self._error("Please enter a value.")
            return

        # Check that the input is numeric
        try:
            value = float(text)
        except ValueError:
            self._error("Value entered is not numeric.")
            return

        # Check if the value is positive
        if value <= 0:
            self._error("Value entered is not positive.")
            return

        # Perform conversion based on selected button
        if self.rbInToM.isChecked():
            meters = value * INCH_TO_METER

            # Check if the result is negative
            if meters < 0:
                self._error("Converted value is negative.")
                return

            self.lblResult.setText(f"{value:.3f} inches = {meters:.3f} meters")

        else:
            inches = value / INCH_TO_METER

            # Check if the result is negative
            if inches < 0:
                self._error("Converted value is negative.")
                return

            self.lblResult.setText(f"{value:.3f} meters = {inches:.3f} inches")

def main():
    """Start the application."""
    app = QApplication(sys.argv)
    w = ConverterWindow()
    w.resize(720, 320)
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
