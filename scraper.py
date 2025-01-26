import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd

def get_input():
    Collegename = input("Enter Institute Name (CSPIT/DEPSTAR) : ").upper()
    branchname = input("Enter Branch name with Degree (eg. BTECH(CE), BTECH (AIML)) : ").upper()
    semester = int(input("Enter Semester : "))
    year = input("Enter Month and year of examination (eg. NOVEMBER 2024) : ").upper()
    yearofadm = int(input("Enter the year of admission: "))
    return Collegename, branchname, semester, year, yearofadm

def get_branch_code(Collegename, branchname):
    if "CSPIT" in Collegename and "CS" in branchname:
        return "CS"
    elif "CSPIT" in Collegename and "IT" in branchname:
        return "IT"
    elif "CSPIT" in Collegename and "EC" in branchname:
        return "EC"
    elif "CSPIT" in Collegename and "AIML" in branchname:
        return "AIML"
    elif "CSPIT" in Collegename and "EE" in branchname:
        return "EE"
    elif "CSPIT" in Collegename and "ME" in branchname:
        return "ME"
    elif "CSPIT" in Collegename and "CE" in branchname:
        return "CE"
    elif "DEPSTAR" in Collegename and "CS" in branchname:
        return "DCS"
    elif "DEPSTAR" in Collegename and "IT" in branchname:
        return "DIT"
    elif "DEPSTAR" in Collegename and "CE" in branchname:
        return "DCE"
    else:
        raise ValueError("Invalid College name or branch name")

def get_student_data(driver, Collegename, branchname, semester, year, student_id):
    try:
        institute_select = Select(driver.find_element(By.ID, 'ddlInst'))
        institute_select.select_by_visible_text(Collegename)
        
        degree_select = Select(driver.find_element(By.ID, 'ddlDegree'))
        degree_select.select_by_visible_text(branchname)
        
        semester_select = Select(driver.find_element(By.ID, 'ddlSem'))
        semester_select.select_by_visible_text(str(semester))
        
        exam_select = Select(driver.find_element(By.ID, 'ddlScheduleExam'))
        exam_select.select_by_visible_text(year)
        
        student_id_input = driver.find_element(By.ID, 'txtEnrNo')
        student_id_input.clear()
        student_id_input.send_keys(student_id)
        
        show_marksheet_button = driver.find_element(By.ID, 'btnSearch')
        show_marksheet_button.click()
        
        time.sleep(2)
        
        student_name_element = driver.find_element(By.ID, 'uclGrd1_lblStudentName')
        student_name = student_name_element.text.strip()
        student_sgpa_element = driver.find_element(By.ID, 'uclGrd1_lblSGPA')
        student_sgpa = student_sgpa_element.text.strip()
        student_cgpa_element = driver.find_element(By.ID, 'uclGrd1_lblCGPA')
        student_cgpa = student_cgpa_element.text.strip()
        back_button = driver.find_element(By.ID, 'ibtnBack')
        back_button.click()
        
        return student_name, student_id, student_sgpa, student_cgpa
    except Exception as e:
        print(f"Failed to retrieve data for {student_id}: {e}")
        return None, None, None, None

def main():
    Collegename, branchname, semester, year, yearofadm= get_input()
    branchcode = get_branch_code(Collegename, branchname)
    no_of_students = int(input("Enter the number of students : "))

    driver = webdriver.Chrome()
    link = "https://charusat.edu.in:912/UniExamResult/frmUniversityResult.aspx"
    driver.get(link)

    students_data = []
    for student_id in range(1, no_of_students + 1):
        student_id_str = f"{yearofadm}{branchcode}{student_id:03d}"
        student_name, student_id, student_sgpa, student_cgpa = get_student_data(driver, Collegename, branchname, semester, year, student_id_str)
        if student_name:
            students_data.append([student_name, student_id, student_sgpa, student_cgpa])
            print(f"Retrieved data for {student_id_str}: {student_name}")

    driver.quit()

    detail = pd.DataFrame(students_data, columns=['Student Name', 'Student ID', 'SGPA', 'CGPA'])
    detail.to_excel('example.xlsx', index=False)
    print("Data has been successfully saved to example.xlsx")

if __name__ == "__main__":
    main()
