# 🧪 Test Scenario: TS-002

**Title:** Graceful fallback when Google Gemini API is unavailable  
**Objective:** Ensure the system doesn't crash or hang when the AI model API fails  
**Priority:** Critical  
**Preconditions:** System is operational and connected to internet  

---

## 📋 Steps:

1. Disconnect internet / simulate API failure
2. Submit a pair of requirements
3. Observe system response

---

## ✅ Expected Result:

System shows error message: "AI service unavailable. Try again later."

---

## 🎯 Test Focus:

- **Error Handling** - System's response to external service failures
- **User Experience** - Clear error messaging during service outages
- **System Stability** - Prevention of crashes or infinite loading states
- **Recovery** - Ability to resume normal operation when service returns

---

<div align="center">
  <i>Part of <a href="https://github.com/Yasin-asif/SQA-Professional-Portfolio">Muhammad Yasin's SQA Professional Portfolio</a></i>
</div> 