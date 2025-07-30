# 🤖 AI Conflict Detector — Exploratory Test Report

**Session Date:** July 28, 2025  
**Tester:** Muhammad Yasin Asif  
**Time-box:** 60 minutes  
**Charter:** Explore AI conflict resolution behavior for requirement ambiguity & edge cases

---

## 🛠 Test Environment:
- **Platform:** Web App (Localhost)
- **Browser:** Chrome 115
- **API:** Google Gemini 1.5 Flash
- **Tools:** Postman, Stopwatch, Notepad++

---

## 🧪 Focus Areas:
- AI behavior with ambiguous, contradictory, and long inputs
- Misleading punctuation or synonyms
- Non-English or multilingual entries
- Repeatedly rewritten requirements

---

## 🐛 Key Findings:

| ID | Observation | Severity | Notes |
|----|-------------|----------|-------|
| EXP-AI-01 | AI misclassified two neutral requirements as conflicting | Medium | Semantic similarity likely confused logic |
| EXP-AI-02 | Rewriting loop: AI keeps rewriting same sentence | High | Infinite loop scenario possible |
| EXP-AI-03 | Input with emoji causes 500 error | Medium | No validation on non-standard characters |
| EXP-AI-04 | No language detection on Urdu input | Low | Should fall back gracefully or show warning |
| EXP-AI-05 | Very long requirements (>1000 chars) timeout | High | Performance issue with large inputs |
| EXP-AI-06 | Special characters in requirements break parsing | Medium | Need input sanitization |

---

## 🔍 Detailed Observations:

### 1. Semantic Ambiguity Testing
**Input:** 
- "System shall authenticate users"
- "System shall verify user identity"

**Result:** AI flagged as conflicting (incorrectly)
**Analysis:** The AI seems to treat synonyms as contradictions

### 2. Edge Case: Emoji Input
**Input:** "System shall 🚀 respond quickly"
**Result:** 500 Internal Server Error
**Impact:** Complete system failure with non-standard characters

### 3. Performance Under Load
**Test:** Multiple rapid submissions
**Result:** Response time degraded from 2s to 8s
**Risk:** System becomes unusable under stress

### 4. Language Handling
**Input:** "سیستم صارف کی شناخت کرے گا" (Urdu)
**Result:** Processed but with low confidence
**Issue:** No language detection or warning

---

## 🎯 Recommendations:

### High Priority:
1. **Add semantic context validation rules** - Prevent false conflict detection
2. **Limit rewrite recursion** - Prevent infinite loops
3. **Implement input sanitization** - Handle special characters gracefully

### Medium Priority:
4. **Add language detection** - Warn users about unsupported languages
5. **Performance optimization** - Handle large inputs better
6. **Rate limiting** - Prevent API abuse

### Low Priority:
7. **Multi-language support** - Expand beyond English
8. **Confidence scoring** - Show AI confidence levels to users

---

## 📊 Session Metrics:
- **Time Spent:** 60 minutes
- **Issues Found:** 6 (2 High, 3 Medium, 1 Low)
- **Areas Covered:** 4 major functionality areas
- **Test Cases Generated:** 12 new test scenarios

---

<div align="center">
  <i>Part of <a href="https://github.com/Yasin-asif/SQA-Professional-Portfolio">Muhammad Yasin's SQA Professional Portfolio</a></i>
</div> 