# 📝 Student Result Scraper

A Python script to scrape student result data from the **CHARUSAT** university result portal using Selenium. The script dynamically accepts user inputs to configure the scraping process and saves the extracted data into an Excel file. 📊

## 🌟 Features

- **User Input**: The script prompts the user for:
  - 🏫 Institute name (CSPIT or DEPSTAR)
  - 📚 Branch name with degree (e.g., BTECH(CE), BTECH(AIML))
  - 📆 Semester number
  - 🗓️ Examination month and year (e.g., NOVEMBER 2024)
  - 🔢 Year of Admission to generate dynamic student IDs
  - 👩‍🎓👨‍🎓 Number of students to scrape
- **Dynamic Scraping**: Automatically fills dropdown selections and retrieves results based on user inputs. ⚡
- **Excel Output**: Saves the extracted data into an Excel file (`students_data.xlsx`) with columns for:
  - **Student Name**
  - **Student ID**
  - **SGPA**
  - **CGPA**

## 🛠️ Requirements

- **Python**: 3.7 or higher 🐍
- **Google Chrome**: Ensure it is installed 🌐
- **ChromeDriver**: Download the version matching your Chrome browser 🖥️
- **Python Libraries**:
  - `selenium` 🚗
  - `pandas` 🐼
  - `openpyxl` (optional, for Excel file generation) 📋

## 🖥️ Usage
  - Run the script:
    ```bash
    python scraper.py
  Follow the prompts:
  - Enter the institute name, branch name, semester, examination month/year, year of admission, and number of students.
  - The script will scrape the results.
  - Results will be saved into an Excel file named students_data.xlsx. 📁

## 📦 Output
   The Excel file will contain the following columns:
   - Student Name
   - Student ID
   - SGPA
   - CGPA

## ⚠️ Limitations
  - This script currently works only for CSPIT and DEPSTAR institutes.
  - Requires a stable internet connection during the scraping process.
  - This script relies on the structure of the CHARUSAT university result portal. If the portal layout changes, the script may need adjustments.

## ✨ Future Enhancements
  - Add support for more universities or portals.
  - Develop a web interface for easier use.
  - Implement a database for result storage and retrieval.
  - Add progress tracking during scraping.

## 🤝 Contributing
  - Contributions are welcome! Feel free to submit a pull request or open an issue to improve this script. 😊

## 🚀 Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/kaustav3071/student-result-scraper.git
   cd student-result-scraper
