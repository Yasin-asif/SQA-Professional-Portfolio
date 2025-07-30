# 🛒 E-Commerce Checkout — Exploratory Test Report

**Session Date:** July 29, 2025  
**Tester:** Muhammad Yasin Asif  
**Time-box:** 45 minutes  
**Charter:** Explore checkout flow for usability issues, edge cases, and security vulnerabilities

---

## 🛠 Test Environment:
- **Platform:** E-commerce Web App (Staging)
- **Browser:** Firefox 115, Chrome 115
- **Payment Gateway:** Stripe Test Mode
- **Tools:** Browser DevTools, Network Monitor, Postman

---

## 🧪 Focus Areas:
- Checkout flow usability and user experience
- Payment processing edge cases
- Form validation and error handling
- Security vulnerabilities and data handling
- Mobile responsiveness

---

## 🐛 Key Findings:

| ID | Observation | Severity | Notes |
|----|-------------|----------|-------|
| EXP-EC-01 | Checkout button disappears after applying discount | High | Critical usability issue |
| EXP-EC-02 | Credit card validation allows expired cards | Medium | Security concern |
| EXP-EC-03 | Address autocomplete breaks with special characters | Medium | International user impact |
| EXP-EC-04 | Mobile checkout has overlapping elements | Medium | Responsive design issue |
| EXP-EC-05 | Order confirmation email contains sensitive data | High | Privacy violation |
| EXP-EC-06 | Back button during payment loses cart items | Medium | Poor user experience |

---

## 🔍 Detailed Observations:

### 1. Usability Issues
**Scenario:** User applies discount code
**Issue:** Checkout button becomes invisible
**Impact:** User cannot complete purchase
**Repro Steps:** Apply discount → Button disappears

### 2. Security Testing
**Test:** Expired credit card validation
**Input:** Card expired 12/2020
**Result:** System accepted the card
**Risk:** Potential fraud exposure

### 3. Mobile Experience
**Device:** iPhone 12 (Safari)
**Issue:** Address fields overlap with keyboard
**Impact:** Users cannot see what they're typing
**Frequency:** 100% reproducible

### 4. Data Privacy
**Test:** Order confirmation email
**Issue:** Contains full credit card number
**Risk:** Email compromise exposes payment data
**Compliance:** Violates PCI DSS requirements

---

## 🎯 Recommendations:

### Critical (Fix Immediately):
1. **Fix disappearing checkout button** - Critical business impact
2. **Remove sensitive data from emails** - Security compliance issue
3. **Implement proper card validation** - Security vulnerability

### High Priority:
4. **Fix mobile responsive design** - Affects 60% of users
5. **Preserve cart state on navigation** - Poor user experience
6. **Add input sanitization** - Handle special characters

### Medium Priority:
7. **Improve error messaging** - Better user guidance
8. **Add progress indicators** - Reduce user anxiety
9. **Implement address validation** - Reduce shipping errors

---

## 📊 Session Metrics:
- **Time Spent:** 45 minutes
- **Issues Found:** 6 (2 Critical, 2 High, 2 Medium)
- **User Flows Tested:** 8 different checkout scenarios
- **Devices Tested:** Desktop, Mobile, Tablet

---

## 🔒 Security Findings:
- **Input Validation:** Weak validation on payment forms
- **Data Exposure:** Sensitive data in logs and emails
- **Session Management:** Cart state not properly preserved
- **Error Handling:** Information disclosure in error messages

---

<div align="center">
  <i>Part of <a href="https://github.com/Yasin-asif/SQA-Professional-Portfolio">Muhammad Yasin's SQA Professional Portfolio</a></i>
</div> 