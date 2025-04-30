# ui/main_window.py
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt6.QtCore import QSize

# Import the specific page widget
from ui.pages.reading_page import ReadingPage
from core.utils.logger import get_logger

logger = get_logger(__name__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Eye-Tracking Language Assistant (Phase 0)")
        self.setMinimumSize(QSize(800, 600)) # Set a reasonable starting size

        # --- Central Widget Setup ---
        # In this phase, ReadingPage is the only content
        self.reading_page = ReadingPage(self)
        self.setCentralWidget(self.reading_page)
        # ---------------------------

        # Placeholder for status bar (useful later)
        self.statusBar().showMessage("Status: Ready")

        logger.info("MainWindow initialized.")

        # Example of how to load initial text (optional for Phase 0)
        # self.reading_page.set_text("Loaded from MainWindow!")