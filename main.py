# main.py
import sys
from PyQt6.QtWidgets import QApplication

from core.utils.logger import setup_logger, get_logger
from ui.main_window import MainWindow

if __name__ == "__main__":
    # --- Setup Logging ---
    setup_logger()
    logger = get_logger(__name__)
    logger.info("Application starting...")

    # --- Initialize Qt Application ---
    app = QApplication(sys.argv)

    # --- Create and Show Main Window ---
    main_window = MainWindow()
    main_window.show()
    logger.info("Main window shown.")

    # --- Start Event Loop ---
    logger.info("Starting Qt event loop...")
    exit_code = app.exec()
    logger.info(f"Application exiting with code {exit_code}.")
    sys.exit(exit_code)
