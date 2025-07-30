# 🕒 Session-Based Test Charters

This document contains structured charters for exploratory testing sessions, demonstrating systematic approach to unscripted testing.

---

## 📋 Charter Template

Each charter follows this structure:
- **Session ID:** Unique identifier
- **Charter:** Mission statement and objectives
- **Time-box:** Duration limit
- **Areas:** Parts of the application to explore
- **Tester:** Person conducting the session
- **Status:** Current state of the session

---

## 🎯 Active Charters

| Session ID | Charter | Time-box | Status | Tester |
|------------|---------|----------|--------|--------|
| CHAR-01 | Explore AI's handling of semantically similar requirements | 60 mins | ✅ Completed | Muhammad Yasin |
| CHAR-02 | Validate discount code flow on e-commerce checkout | 45 mins | ✅ Completed | Muhammad Yasin |
| CHAR-03 | Stress test API with malformed inputs | 30 mins | 🔄 In Progress | Muhammad Yasin |
| CHAR-04 | Mobile responsiveness across different devices | 90 mins | 📅 Planned | Muhammad Yasin |
| CHAR-05 | Security testing for payment processing | 60 mins | 📅 Planned | Muhammad Yasin |

---

## 📝 Detailed Charter Examples

### CHAR-01: AI Semantic Analysis
**Charter:** Explore how the AI system handles requirements that are semantically similar but not necessarily conflicting.

**Areas to Explore:**
- Synonym detection and handling
- Context-aware conflict analysis
- False positive scenarios
- Edge cases with ambiguous language

**Success Criteria:**
- Identify false conflict detections
- Document semantic analysis limitations
- Generate test cases for improvement

**Time-box:** 60 minutes

**Notes:** Focus on requirements that should NOT conflict but might be flagged as conflicting due to semantic similarity.

---

### CHAR-02: E-Commerce Checkout Flow
**Charter:** Validate the complete checkout process from cart to order confirmation.

**Areas to Explore:**
- Discount code application
- Payment method selection
- Address validation
- Order confirmation process
- Error handling scenarios

**Success Criteria:**
- Complete purchase flow works end-to-end
- Error scenarios are handled gracefully
- User experience is smooth and intuitive

**Time-box:** 45 minutes

**Notes:** Test as a real user would, including edge cases like expired cards, invalid addresses, etc.

---

### CHAR-03: API Stress Testing
**Charter:** Test API endpoints under various stress conditions and malformed inputs.

**Areas to Explore:**
- Large payload handling
- Malformed JSON inputs
- Rate limiting behavior
- Error response consistency
- Performance degradation

**Success Criteria:**
- API remains stable under stress
- Proper error responses for invalid inputs
- Performance metrics within acceptable limits

**Time-box:** 30 minutes

**Notes:** Use tools like Postman and custom scripts to generate load and malformed data.

---

## 📊 Session Metrics

| Metric | Target | Actual | Notes |
|--------|--------|--------|-------|
| Sessions Completed | 5 | 2 | 2 in progress, 1 planned |
| Issues Found | 10+ | 12 | Exceeding expectations |
| Time Efficiency | 90% | 95% | Sessions completed within time-box |
| Coverage | High | High | All major areas explored |

---

## 🔄 Session Management

### Best Practices:
1. **Time-box strictly** - Don't exceed allocated time
2. **Document immediately** - Capture findings in real-time
3. **Focus on charter** - Stay within defined scope
4. **Generate test cases** - Convert findings into formal tests
5. **Share insights** - Communicate findings to team

### Tools Used:
- **Timer:** Session time tracking
- **Notes:** Real-time documentation
- **Screenshots:** Visual evidence capture
- **Mind Maps:** Test idea organization

---

<div align="center">
  <i>Part of <a href="https://github.com/Yasin-asif/SQA-Professional-Portfolio">Muhammad Yasin's SQA Professional Portfolio</a></i>
</div> 