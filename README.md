# Text Analysis Tool 📊

A Python-based desktop application built with **Tkinter** that provides linguistic analysis and data visualization. Users can import files, paste from the clipboard, or type directly to generate statistics and identify word patterns.

## ✨ Features

* **Smart Input Handling:**
    * **File Import:** Load `.txt` files directly into the analyzer.
    * **Clipboard Integration:** One-click paste functionality with error handling.
    * **Dynamic Validation:** The "Text Analysis" button remains disabled until text is detected in the editor (uses `<KeyRelease>` and `<ButtonRelease-1>` event bindings).
* **Linguistic Analysis Engine:**
    * **Word Frequency:** Identifies and ranks the top 5 most used words.
    * **Palindrome Finder:** Locates the longest word that reads the same backward as forward.
    * **Anagram Detection:** Identifies pairs of words containing the exact same letters.
    * **Text Statistics:** Calculates average word length and the consonant-to-vowel ratio.
* **Data Visualization:** * Generates a dynamic bar chart using **Tkinter Canvas** to visually represent word frequency.

## 🚀 How to Run

1.  **Prerequisites:** Ensure you have Python installed (Tkinter comes bundled with standard Python installations).
2.  **Execution:** Run the script using:
    ```bash
    python your_script_name.py
    ```
3.  **Input Text:** Click **Import File**, use the **Paste Text** button, or type directly into the text area.
4.  **Analyze:** Once text is present, the **Text Analysis** button will activate. Click it to launch the results panels.

## 🛠️ Technical Overview

### Classes & Logic
* **`Textanalyzer` Class:** The core processing engine.
    * `clean_text()`: Normalizes input by converting to lowercase and stripping punctuation using `re`.
    * `calculate_statistics()`: Computes frequency, averages, and linguistic ratios.
    * `find_longest_palindrome()` / `find_longest_anagram()`: Pattern matching algorithms for specific word structures.

### GUI Components
* **Primary Window:** Contains the input `Text` widget and control buttons.
* **Secondary Windows (`Toplevel`):** * **Bar Chart Panel:** A visual representation of data.
    * **Statistics Panel:** A summary of text patterns and averages.

## 📝 Dependencies
* `tkinter`: GUI framework.
* `re`: Regular expressions for text cleaning.

---
*Developed as a functional tool for basic linguistic data processing.*
