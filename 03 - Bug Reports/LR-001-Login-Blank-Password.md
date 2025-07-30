# 🐞 Bug Report: LR-001

**Title:** Login form allows blank password submission  
**Severity:** High  
**Priority:** P1  
**Module:** Login Form  
**Environment:**  
- Chrome v115  
- Windows 10  
- Web App Version 2.4

---

## 🔁 Steps to Reproduce:

1. Navigate to the login page  
2. Enter a valid username  
3. Leave the password field blank  
4. Click the Login button  

---

## ✅ Expected Result:

System **blocks submission** and shows: _"Password cannot be blank"_

## ❌ Actual Result:

Form **submits**, and system **attempts login** with a blank password.

## 📌 Status: `Open`

---

<div align="center">
  <i>Part of <a href="https://github.com/Yasin-asif/SQA-Professional-Portfolio">Muhammad Yasin's SQA Professional Portfolio</a></i>
</div> 