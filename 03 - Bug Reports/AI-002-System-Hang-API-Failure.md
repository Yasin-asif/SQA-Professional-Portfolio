# 🐞 Bug Report: AI-002

**Title:** System hangs indefinitely when Google Gemini API fails  
**Severity:** Critical  
**Priority:** P1  
**Module:** AI Conflict Detector  
**Environment:**  
- Web App  
- Firefox v115  
- Windows 10  
- Simulated API failure (throttled network)

---

## 🔁 Steps to Reproduce:

1. Simulate Google Gemini API downtime or failure  
2. Submit requirements for conflict detection  
3. Observe system behavior  

---

## ✅ Expected Result:

System shows **error message within 5 seconds**, and no hang occurs.

## ❌ Actual Result:

System hangs **indefinitely with no error message** or timeout.

## 📌 Status: `Open`

---

<div align="center">
  <i>Part of <a href="https://github.com/Yasin-asif/SQA-Professional-Portfolio">Muhammad Yasin's SQA Professional Portfolio</a></i>
</div> 