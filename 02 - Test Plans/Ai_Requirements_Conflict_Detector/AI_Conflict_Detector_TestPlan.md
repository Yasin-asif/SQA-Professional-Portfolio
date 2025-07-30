# 🧪 TEST PLAN  
## AI Requirements Conflict Detector  
**Version:** 1.0  
**Author:** Muhammad Yasin Asif  
**Date:** July 2025  
**Course:** SE3032 – Software Quality Engineering  
**Institution:** Shifa Tameer-e-Millat University  
**Supervisor:** Sir Saif ur Rehman  

---

## 📌 1. Test Plan Identifier  
AIConflictDetector-TestPlan-v1.0

---

## 📘 2. Introduction  
This test plan outlines the comprehensive strategy, approach, scope, resources, and schedule for testing the **AI Requirements Conflict Detector**. The tool integrates with Google's Gemini 1.5 Flash API to detect and resolve software requirement conflicts intelligently. The testing approach aims to validate functional correctness, performance, reliability, and error handling.

---

## 🔎 3. Test Items  
- Conflict detection logic (AI-driven)  
- Rewriting mechanism for resolving conflicts  
- Google Gemini API integration  
- Requirement input/output module  
- Performance timing (response < 3s)  
- Input validation and exception handling

---

## ✅ 4. Features to Be Tested  
| # | Feature | Description |
|---|---------|-------------|
| F1 | Conflict Detection | AI identifies logical contradictions between requirements |
| F2 | Requirement Rewriting | Automatically generates clarified, non-conflicting versions |
| F3 | Input Validation | Detects malformed or incomplete inputs |
| F4 | API Integration | Handles Gemini 1.5 API responses accurately |
| F5 | Performance | Ensures response within 3 seconds |
| F6 | Edge Case Handling | Handles empty inputs, long strings, and semantic ambiguity |

---

## 🚫 5. Features Not To Be Tested  
- Gemini 1.5 Flash model's internal behavior  
- Graphical UI styling (CLI or basic GUI only)  
- Enterprise-level scalability or concurrent users > 100

---

## 🧠 6. Approach  
Testing follows both **black-box** and **white-box** strategies:  

- **Black Box Testing**:  
  - Equivalence Class Partitioning  
  - Boundary Value Analysis  
  - Functional & Input-output validation  

- **White Box Testing**:  
  - Control Flow Graph (CFG) path coverage  
  - Exception and branch logic validation  

- **Performance Testing**:  
  - API response time under 3 seconds  

- **Unit Testing**:  
  - Python modules and methods (via `pytest`)  

- **Integration Testing**:  
  - Google Gemini API + local parsing pipeline  

---

## 🔐 7. Entry & Exit Criteria  

### ✅ Entry Criteria  
- Codebase complete and unit-testable  
- Gemini API key configured  
- Development environment set up  
- AI prompts stabilized

### ✅ Exit Criteria  
- All critical path test cases passed  
- >90% AI response accuracy achieved  
- Performance tests pass under load  
- No critical bugs remain open  
- QA report reviewed by supervisor

---

## 📦 8. Deliverables  
- 📄 Test Plan (this document)  
- 📂 Test Cases Document  
- 📈 Test Execution Report  
- 🐞 Bug/Defect Log  
- ✅ QA Summary Report  
- 🧪 Automated Test Scripts (pytest, if any)

---

## 🧑‍💻 9. Testing Tasks  

| Task                          | Owner               | Status   |
|-------------------------------|---------------------|----------|
| Test Plan Creation            | Muhammad Yasin      | ✅ Done  |
| Manual Test Case Design       | Muhammad Yasin      | ✅ Done  |
| Manual Test Execution         | Muhammad Yasin      | ⏳ In Progress |
| API Mock Testing              | Muhammad Yasin      | 🔜 Planned |
| QA Summary Report             | Muhammad Yasin      | 🔜 Planned |

---

## 🛠️ 10. Environmental Needs  
- OS: Windows/Linux  
- Language: Python 3.x  
- Dependencies: Google Gemini API, PyTest  
- Tools: Postman, VSCode, GitHub, Git  
- Internet: Required for Gemini API connection  

---

## 👥 11. Roles & Responsibilities  
| Role          | Name               | Responsibility                    |
|---------------|--------------------|-----------------------------------|
| QA Engineer   | Muhammad Yasin     | Planning, execution, reporting    |
| Supervisor    | Sir Saif ur Rehman | Review, academic evaluation       |

---

## 📆 12. Schedule  

| Phase                  | Dates           |
|------------------------|-----------------|
| Planning & Design      | July 20–21, 2025 |
| Test Case Development  | July 22, 2025    |
| Manual Execution       | July 23–24, 2025 |
| QA Reporting           | July 25, 2025    |

---

## ⚠️ 13. Risks & Mitigation  

| Risk                                      | Impact    | Mitigation                                  |
|-------------------------------------------|-----------|----------------------------------------------|
| Gemini API Quota Limit                    | High      | Use mocks and sandbox API environment        |
| AI Response Non-Determinism               | High      | Define expected response structure strictly  |
| Internet Connectivity Issues              | Medium    | Test offline functionality separately        |
| Time constraint for final testing         | Medium    | Prioritize critical path coverage early      |

---

## ✍️ 14. Approval  

**Prepared By:**  
**Muhammad Yasin Asif**  
BSSE-23S-0036 – Shifa Tameer-e-Millat University  

**Reviewed By:**  
**Sir Saif ur Rehman**  
Course Instructor – SE3032  

---

<div align="center">
  <i>Part of <a href="https://github.com/Yasin-asif/SQA-Professional-Portfolio">Muhammad Yasin's SQA Professional Portfolio</a></i>
</div> 