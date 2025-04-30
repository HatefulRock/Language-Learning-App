# ui/pages/reading_page.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from PyQt6.QtGui import QMouseEvent, QTextCursor, QColor, QPalette
from PyQt6.QtCore import Qt, QRect

# Import the logger setup function if you want file-specific logging
from core.utils.logger import get_logger

logger = get_logger(__name__)

class ReadingPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ReadingPage") # Useful for styling later
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True) # Make it non-editable
        self.text_edit.setObjectName("ReadingTextEdit") # For styling

        # --- Sample Text ---
        # Using HTML for potential future styling/structure
        sample_html = """
        <h1>Phase 0 Test</h1>
        <p>This is the <b>Reading Page</b> widget. We need to display text here.</p>
        <p>Later, eye tracking data will tell us where the user is looking.</p>
        <p>For now, <i>click on a word</i> to simulate a fixation and see its bounding box logged.</p>
        <p>Here is some more text to fill the space and allow scrolling. Lorem ipsum dolor sit amet,
        consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
        Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        """
        self.text_edit.setHtml(sample_html)
        # --------------------

        layout.addWidget(self.text_edit)
        self.setLayout(layout)

        logger.info("ReadingPage initialized.")

    def set_text(self, text_content, is_html=False):
        """Sets the text content of the reading area."""
        if is_html:
            self.text_edit.setHtml(text_content)
        else:
            self.text_edit.setPlainText(text_content)
        logger.info("Text content updated.")

    def mousePressEvent(self, event: QMouseEvent):
        """
        Handles mouse clicks to demonstrate coordinate/word finding.
        This simulates where the gaze analysis output would interact.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.pos()
            logger.debug(f"Mouse clicked at widget coordinates: {pos}")

            # Get a text cursor at the clicked position within the QTextEdit
            text_cursor = self.text_edit.cursorForPosition(pos)
            if text_cursor.isNull():
                logger.warning("Clicked outside of text content.")
                return

            # Select the word under the cursor
            text_cursor.select(QTextCursor.SelectionType.WordUnderCursor)
            selected_word = text_cursor.selectedText()

            if not selected_word or not selected_word.strip():
                 logger.debug("No valid word selected under cursor.")
                 return

            # Get the bounding rectangle of the *cursor* (which now covers the selected word)
            # Note: This rect is relative to the QTextEdit's viewport
            bounding_rect: QRect = self.text_edit.cursorRect(text_cursor)

            logger.info(f"Word clicked: '{selected_word}', Bounding Rect (relative to text edit viewport): {bounding_rect}")

            # --- Placeholder for future interaction ---
            # In later phases, if fixation detected here:
            # 1. Get the word/phrase via text_cursor.selectedText() or similar.
            # 2. Get the bounding_rect.
            # 3. Emit a signal: self.translation_requested.emit(selected_word, bounding_rect)
            # 4. The main window/manager would connect this signal to the translation module.
            # 5. Translation module gets result, emits translation_ready(result, bounding_rect)
            # 6. Main window/manager tells this ReadingPage (or an overlay manager)
            #    to display the overlay near bounding_rect.
            # -----------------------------------------

        # Pass the event to the base class implementation if needed
        super().mousePressEvent(event)