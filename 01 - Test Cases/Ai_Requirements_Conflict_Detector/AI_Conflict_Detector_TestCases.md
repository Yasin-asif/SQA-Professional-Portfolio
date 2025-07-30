# 🧪 AI Requirements Conflict Detector – Test Cases
## Module: Conflict Detection Engine
### Author: Muhammad Yasin Asif
### Version: 1.0
### Date: July 30, 2025

---

## 🔍 Objective
To validate that the AI Requirements Conflict Detector accurately detects conflicting software requirements, handles invalid inputs, and ensures non-conflicting inputs pass cleanly.

---

## 📋 Test Cases Table

| Test Case ID | Title | Pre-conditions | Input Data | Steps | Expected Result | Actual Result | Status |
|--------------|-------|----------------|------------|-------|-----------------|---------------|--------|
| TC-001 | Detect Direct Conflict | System is up and AI API is connected | Req1: "System shall respond within 2s"<br>Req2: "System shall not respond faster than 5s" | 1. Launch tool<br>2. Enter both requirements<br>3. Click 'Detect Conflict' | ✅ Conflict Detected<br>✅ Suggest: Reconciliation needed | _TBD_ | Not Run |
| TC-002 | Detect No Conflict | API working | Req1: "System shall log user actions"<br>Req2: "System shall authenticate users" | Same as above | ✅ No Conflict<br>✅ Requirements accepted | _TBD_ | Not Run |
| TC-003 | Handle Invalid Requirement Format | API up | Req1: "Syst%em sh@ll do..."<br>Req2: "Valid requirement" | Enter malformed req<br>Click Detect | ❌ Error Message: "Invalid requirement input" | _TBD_ | Not Run |
| TC-004 | Empty Requirement Input | API up | Req1: ""<br>Req2: "System must scale to 10k users" | Enter empty string<br>Click Detect | ❌ Error Message: "Please enter valid input" | _TBD_ | Not Run |
| TC-005 | Detect Security Conflict | API working | Req1: "Passwords must be stored in plain text"<br>Req2: "Passwords must be encrypted" | Submit both<br>Click Detect | ✅ Conflict Detected: Security breach warning | _TBD_ | Not Run |
| TC-006 | Handle Redundant Requirements | API live | Req1: "User must login"<br>Req2: "User must log into the system" | Enter both<br>Click Detect | ⚠️ Possible Redundancy<br>✅ Suggest rewrite | _TBD_ | Not Run |
| TC-007 | Detect Performance Conflict | System OK | Req1: "System shall complete task in 2s"<br>Req2: "System shall allow background execution within 10s" | Enter<br>Click Detect | ⚠️ Partial Conflict<br>✅ Alert developer to review performance criteria | _TBD_ | Not Run |
| TC-008 | Stress Input - Max Length | System live | Req1: 500 chars<br>Req2: 500 chars | Paste max-length inputs<br>Click Detect | ✅ Processed without crash<br>✅ Conflict (if present) shown | _TBD_ | Not Run |
| TC-009 | Validate Response Time | System idle | Complex input set | Start timer<br>Click Detect | ✅ Response time < 3 seconds | _TBD_ | Not Run |
| TC-010 | API Failure Handling | Simulate API disconnection | Any valid input | Click Detect | ❌ Error Message: "Service unavailable"<br>✅ Retry option shown | _TBD_ | Not Run |

---

## ✅ Success Criteria
- 100% of valid test cases must pass
- 90% of boundary/performance tests must pass
- All invalid inputs should return meaningful errors

---

## 📌 Notes
- This test suite validates both functional and non-functional requirements
- Covers equivalence partitioning, BVA, and error handling
- Designed for manual execution; automation version available in next step

---

<div align="center">
  <i>Part of <a href="https://github.com/Yasin-asif/SQA-Professional-Portfolio">Muhammad Yasin's SQA Professional Portfolio</a></i>
</div> 