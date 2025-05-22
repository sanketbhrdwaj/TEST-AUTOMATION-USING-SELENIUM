# Selenium Automation Task

This project automates the login and navigation functionality of a sample web application using Selenium WebDriver and Python with pytest.

## 🌐 Test Site
[Practice Test Login](https://practicetestautomation.com/practice-test-login/)

## 🔑 Login Credentials
- Username: `student`
- Password: `Password123`

## 🛠 Requirements
- Python 3.x
- Google Chrome
- ChromeDriver (must be in your PATH)

Install dependencies:
```
pip install -r requirements.txt
```

## 🚀 How to Run
```
pytest test_login.py --html=report.html
```

## 📄 Description
- Logs in with valid credentials
- Verifies successful login
- Logs out and confirms redirection

## 📑 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
