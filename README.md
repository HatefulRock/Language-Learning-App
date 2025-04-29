# Eye-Tracking Language Learning Assistant (Project Name TBD)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) <!-- Choose your license -->
<!-- Add other badges as relevant: build status, coverage, etc. -->

An intelligent desktop application designed to assist language learners by leveraging real-time eye tracking to provide contextual help and streamline vocabulary acquisition while reading texts in a foreign language.

**[ Placeholder:]**

## ✨ Overview

Learning a new language often involves extensive reading, which can be challenging due to unknown vocabulary and complex sentence structures. This application aims to make the reading process smoother and more efficient by:

1.  **Monitoring eye gaze:** Using a standard webcam and computer vision (MediaPipe), the app tracks where the user is looking on the screen while reading.
2.  **Detecting difficulty:** If the user's gaze lingers on a specific word or phrase for an extended period (indicating potential difficulty), the app automatically triggers assistance.
3.  **Providing contextual help:** An overlay appears near the difficult word, offering translations, Pinyin (for Chinese), definitions, and example sentences, powered by translation APIs and optional LLM integration.
4.  **Facilitating vocabulary learning:** Users can easily save encountered words/phrases to personalized flashcard decks with context.
5.  **Spaced Repetition System (SRS):** Integrated flashcard review system helps users memorize vocabulary efficiently.
6.  **Supporting diverse content:** Users can read pre-loaded texts, generate custom texts using AI (LLMs), or upload their own PDF documents (including OCR for scanned PDFs).
7.  **Multi-Language Support:** Designed to be configurable for various source and target languages.
8.  **Voice Integration:** Includes Text-to-Speech (TTS) for pronunciation and Speech-to-Text (STT) for pronunciation practice.
9.  **Learning Analytics:** Provides statistics and insights into the user's reading habits and vocabulary acquisition progress.
10. **Active Recall:** Includes quizzes and dynamic tests based on the user's vocabulary.

## 🎯 Motivation

*   Reduce the friction and intimidation often associated with reading foreign language texts.
*   Provide immediate, context-aware assistance without breaking the reading flow significantly.
*   Accelerate vocabulary learning by seamlessly integrating reading with flashcard creation and SRS.
*   Offer a personalized and adaptive learning experience based on the user's real-time reading behaviour.

## 🚀 Key Features

*   **Real-time Eye Tracking:** Webcam-based gaze tracking using MediaPipe.
*   **Gaze-Triggered Assistance:** Automatic translation/definition overlays on difficult words.
*   **Multi-Language Support:** Configurable source and target languages.
*   **PDF & AI Content:** Load PDFs (with OCR) or generate texts via LLMs.
*   **Flashcards with SRS:** Integrated spaced repetition system for vocabulary.
*   **Text-to-Speech (TTS):** Hear words and sentences pronounced.
*   **Speech-to-Text (STT):** Practice pronunciation with feedback.
*   **User Stats & Insights:** Track learning progress.
*   **Quizzes & Testing:** Active recall exercises.
*   **Multi-Page Interface:** Dedicated sections for Library, Flashcards, Stats, Reading, etc.

## 🛠️ Tech Stack

*   **Core Language:** Python 3.x
*   **GUI Framework:** PyQt6 / PySide6
*   **Computer Vision / Eye Tracking:** OpenCV (`opencv-python`), MediaPipe (`mediapipe`)
*   **Numerical Computation:** NumPy (`numpy`)
*   **Text Processing:**
    *   Language-aware segmentation (e.g., spaCy, Jieba for Chinese)
    *   GUI Framework's text layout capabilities
*   **PDF Processing:** PyMuPDF (`PyMuPDF`)
*   **OCR:** PyTesseract (`pytesseract`) wrapper for Tesseract OCR / Cloud OCR APIs
*   **API Interaction:** Requests (`requests`), specific client libraries (e.g., `openai`)
*   **Database:** SQLite3 (for flashcards, stats, dictionary data)
*   **Voice:** pyttsx3 (Local TTS), SpeechRecognition (Local STT Wrapper) / Cloud APIs
*   **Packaging (Optional):** PyInstaller, cx_Freeze

## ⚙️ Getting Started

### Prerequisites

*   Python 3.8+
*   `pip` package manager
*   Git
*   **Tesseract OCR Engine:** Required for OCR functionality on scanned PDFs if using the local option.
    *   Install Tesseract for your OS (see [Tesseract documentation](https://tesseract-ocr.github.io/tessdoc/Installation.html)).
    *   Install necessary language data packs (e.g., `chi_sim`, `eng`, `spa`, `fra`). Ensure the Tesseract executable is in your system's PATH or configure the path in the application settings.
*   Webcam connected and accessible.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **API Keys & Configuration:**
    *   External services (Translation APIs, LLM APIs, Cloud Voice/OCR) require API keys.
    *   Copy the example configuration file (if provided) or create `config/settings.json`.
    *   Use environment variables or a secure secrets management method. See `config/settings_manager.py` for how settings are loaded.
    *   Configure necessary paths (e.g., Tesseract path if not in PATH) and default languages in `config/settings.json`.

## ▶️ Usage

1.  **Configure Settings:** Ensure API keys (if using cloud services), language preferences, and eye-tracking parameters (like fixation duration threshold) are set correctly in `config/settings.json` or via the in-app settings UI.

2.  **Run the application:**
    ```bash
    python main.py
    ```

3.  **Initial Setup:**
    *   The first time, you might be prompted to run the eye-tracking calibration routine. Follow the on-screen instructions.

4.  **Main Workflow:**
    *   Navigate using the sidebar/tabs (Home, Library, Flashcards, Stats, Settings).
    *   Go to the Library or use the Content Loader to open a text file, PDF, or generate text via AI.
    *   The text will open in the Reading Page.
    *   Read the text. Ensure the eye-tracking system is active (indicator in UI).
    *   If you linger on a word while in translation mode, an overlay should appear.
    *   Use buttons on the overlay or context menus to save words to flashcards.
    *   Access other features like TTS/STT via UI controls.
    *   Review vocabulary in the Flashcards section.
    *   Check progress in the Stats section.

## 🗺️ Roadmap

The project follows a phased development approach:

1.  ⏳ **Phase 0:** Setup & Basic Text Rendering/Coordinate Mapping.
2.  ⏳ **Phase 1:** Core Interaction Loop with Mocked (Mouse) Input.
3.  ⏳ **Phase 2:** Real Eye Tracking Integration & Calibration (*Iterative*).
4.  ⏳ **Phase 3:** Language-Specific Handling (e.g., Chinese).
5.  ⏳ **Phase 4:** Content Loading (PDF, AI Gen).
6.  ⏳ **Phase 5:** Flashcards & SRS Implementation.
7.  ⏳ **Phase 6:** Voice Features (TTS/STT).
8.  ⏳ **Phase 7:** Multi-Language Generalization.
9.  ⏳ **Phase 8:** Stats & Quizzes Implementation.
10. ⏳ **Phase 9:** Polish, Testing, Documentation, Packaging.


## 🙌 Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Ensure your code adheres to project styling conventions (e.g., using Black, Flake8).
5.  Write or update tests for your changes.
6.  Commit your changes (`git commit -m 'Add some feature'`).
7.  Push to the branch (`git push origin feature/your-feature-name`).
8.  Open a Pull Request.

Please provide a clear description of your changes in the Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. *(Create a LICENSE.md file with the MIT license text)*

## 🙏 Acknowledgements (Optional)

*   

---

