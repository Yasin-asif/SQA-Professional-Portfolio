# AI Requirements Conflict Detector  
### Software Quality Assurance (SQA) Plan Submission

---

## SHIFA TAMEER-E-MILLAT UNIVERSITY  
**Program:** Bachelor of Science in Software Engineering (2023–2027)  
**Course Title:** SE3032 – Software Quality Engineering  
**Course Instructor:** Sir Saif ur Rehman  
**Submission Date:** 24 July 2025  

**Submitted By:**  
- Muhammad Yasin Asif (Reg. No: BSSE-23S-0036)  
- Muhammad Fahim (Reg. No: BSSE-23S-0033)  

**Supervisor:**  
Sir Saif ur Rehman, Bachelor of Science in Software Engineering (2023-2027)  

---

## Document Information

| **Category**          | Software Quality Assurance Artifact                      |
|-----------------------|----------------------------------------------------------|
| **Project/Product**    | AI Requirements Conflict Detector                         |
| **Version**           | 1.0                                                      |
| **Author(s)**         | Muhammad Yasin, Muhammad Fahim                           |
| **Reviewer(s)**       | Dr. Saif Ur Rehman Khan                                  |
| **Issue Date**        | 23 July 2025                                             |
| **Distribution**      | Submitted to Instructor                                  |
| **Document Category** | Internal                                                |
| **Privacy Level**     | Confidential                                           |
| **Disclaimer**        | This academic document is confidential and for educational use only. |

---

## Review History

| Sr # | Review Team              | Review Date | Conclusion            | Remarks                    |
|-------|-------------------------|-------------|----------------------|----------------------------|
| 1     | Dr. Saif Ur Rehman Khan |             | Reviewed / Approved  | Meets academic QA requirements |

---

## Modification History

| Ver | Author         | Date          | Section Changed | Description                      |
|-----|----------------|---------------|-----------------|----------------------------------|
| 1.0 | Muhammad Yasin | 23 July 2025  | Initial Draft   | First full version of the artifact |

---

## Contents

1. [Executive Summary](#executive-summary)  
   1.1 [Purpose](#purpose)  
   1.2 [Scope](#scope)  
   1.3 [Objectives](#objectives)  
2. [Quality Attributes](#quality-attributes)  
   2.1 [Identified Attributes](#identified-attributes)  
   2.2 [Rationale](#rationale)  
3. [Quality Model](#quality-model)  
   3.1 [Applied Model](#applied-model)  
   3.2 [Justification](#justification)  
4. [Cost Analysis](#cost-analysis)  
   4.1 [Cost of Quality](#cost-of-quality)  
   4.2 [Cost of Failure](#cost-of-failure)  
5. [Software Quality Assurance (SQA) Plan](#software-quality-assurance-sqa-plan)  
   5.1 [Activities](#activities)  
   5.2 [Standards & Tools](#standards--tools)  
   5.3 [Reviews & Audits](#reviews--audits)  
6. [Software Quality Control (SQC)](#software-quality-control-sqc)  
   6.1 [Black Box Testing](#black-box-testing)  
   6.2 [White Box Testing](#white-box-testing)  
7. [Summary of SQA Artifact](#summary-of-sqa-artifact)  
   7.1 [Conclusion](#conclusion)  
8. [References](#references)  

---

## Executive Summary

### Purpose

The Software Quality Assurance (SQA) Artifact for the AI Requirements Conflict Detector serves as a comprehensive quality framework ensuring the development of a reliable, accurate, and maintainable system. This artifact defines quality standards, testing strategies, and assurance activities for delivering a robust AI-powered tool to detect and resolve conflicts in software requirements while preserving their original intent.

### Scope

This artifact covers all components of the AI Requirements Conflict Detector system, including:  

- AI model integration with Google's Gemini 1.5 Flash API  
- Conflict detection algorithms and logic  
- Requirement rewriting mechanisms  
- User interface input/output handling  
- API integration and response parsing  
- Data validation and error handling  
- Performance optimization for real-time detection  

### Objectives

- Achieve **95% accuracy** in conflict detection  
- Maintain response time under **3 seconds**  
- Ensure **99.5% availability** during operations  
- Provide clear, testable, unambiguous rewritten requirements  
- Handle API failures and edge cases comprehensively  
- Support scalability for multiple concurrent requests  

---

## Quality Attributes

### Identified Attributes

**Primary Quality Attributes** (ranked by priority):  

1. **Accuracy**  
2. **Reliability**  
3. **Performance**  
4. **Usability**  
5. **Maintainability**  
6. **Security**  
7. **Scalability**  

**Secondary Quality Attributes:**  
- Interoperability  
- Portability  
- Testability  

### Rationale

Accuracy is paramount as incorrect conflict detection or inappropriate rewrites could lead to system failures or misunderstood requirements. Reliability ensures consistent service delivery, performance improves user adoption, usability enhances acceptance, while maintainability and security protect and ease ongoing development. Scalability ensures growth to meet demand.

---

## Quality Model

### Applied Model

The project uses the **ISO/IEC 25010 Software Quality Model** (successor of ISO 9126).

### Justification

- Comprehensive coverage of key software quality factors.  
- Aligns with AI system needs emphasizing accuracy and performance.  
- Modern standard addressing current security and compatibility.  
- Provides measurable quality metrics.  
- Widely accepted in academia and industry.  

---

## Cost Analysis

### Cost of Quality

| Activity                        | Hours | Rate/hr | Cost   |
|--------------------------------|-------|---------|--------|
| Requirements analysis/reviews   | 15    | $25     | $375   |
| Code reviews & pair programming | 20    | $25     | $500   |
| AI prompt engineering           | 12    | $30     | $360   |
| Unit & integration testing Dev  | 18    | $25     | $450   |
| Quality planning & documentation| 8     | $25     | $200   |
| Manual testing execution        | 15    | $20     | $300   |
| Automated testing maintenance   | 10    | $30     | $300   |
| AI response validation testing  | 12    | $25     | $300   |
| Performance testing             | 8     | $25     | $200   |
| Security testing               | 6     | $30     | $180   |
| **Total Cost of Quality**       |       |         |**$3,165**|

- External dependencies: Google Gemini API (~$50)  
- Testing tools: Open source (no cost)  

### Cost of Failure

| Failure Type            | Cost                       |
|------------------------|----------------------------|
| Debugging & rework     | $1,560                     |
| User-impact failures    | $5,300                     |
| **Total Potential Loss**| **$6,860**                 |

**Return on Investment:** Spending $3,215 on QA avoids $6,860 losses (~2.13:1 ROI).

---

## Software Quality Assurance (SQA) Plan

### Activities

- **Phase 1: Planning & Design**  
  Requirements workshops, architecture reviews, AI model evaluation, quality metrics definition  
- **Phase 2: Development**  
  Code reviews, CI integration, AI prompt optimization, progress audits  
- **Phase 3: Testing**  
  Unit, integration, system, and user acceptance testing  
- **Phase 4: Deployment & Maintenance**  
  Pre-deployment gates, post-deployment monitoring, performance tracking, ongoing assessments  

### Standards & Tools

- **Standards:** IEEE 830-1998, IEEE 1028, IEEE 1063, PEP 8 for Python  
- **Tools:** Git/GitHub, JIRA, pytest, Postman, SonarQube, APM tools, Confluence  
- **AI-specific:** Google AI Studio, custom validation scripts, performance profiling  

### Reviews & Audits

- Weekly code reviews by team members  
- Bi-weekly architecture & AI integration reviews  
- Monthly comprehensive quality audits  
- Pre-release quality gates  

**Audit Criteria:**  
- Minimum 80% code coverage  
- AI response accuracy >90%  
- Meet performance benchmarks  
- Pass security scans  
- Complete documentation  

---

## Software Quality Control (SQC)

### Black Box Testing

#### Equivalence Class Partitioning (ECP)

| Test ID | Input Class           | Requirement 1                       | Requirement 2                    | Expected Output                       |
|---------|-----------------------|-----------------------------------|---------------------------------|-------------------------------------|
| TC001   | Valid conflicting     | "System shall respond within 2s"  | "Response time should not exceed 5s" | Conflict detected, rewritten requirements |
| TC002   | Valid non-conflicting | "System shall authenticate users" | "System shall log user activities" | No conflict detected                 |
| TC003   | Invalid/malformed     | "Sys%tem sh@ll..."                | "Valid requirement"             | Error message                       |
| TC004   | Empty requirements    | ""                                | "Valid requirement"             | Error message                       |

#### Boundary Value Analysis (BVA)

| Test ID | Input Length | Test Data           | Expected Result  |
|---------|--------------|---------------------|------------------|
| TC005   | 9 chars      | "Short req"         | Error: Too short |
| TC006   | 10 chars     | "Valid req."        | Accepted        |
| TC007   | 250 chars    | Medium length       | Accepted        |
| TC008   | 500 chars    | Max length          | Accepted        |
| TC009   | 501 chars    | Exceeds max length  | Error: Too long |

#### API Response Time Validation

| Test ID | Scenario                    | Expected Response Time | Status (Pass/Fail) |
|---------|-----------------------------|-----------------------|--------------------|
| TC010   | Single requirement conflict | < 3 seconds           |                    |
| TC011   | Complex multi-part conflict | < 5 seconds           |                    |
| TC012   | Maximum input length conflict | < 10 seconds         |                    |

### White Box Testing

- **Cyclomatic Complexity:** 4 (moderate)  
- **Independent Paths:** 5 (includes error handling)  
- **Coverage Metrics:** 100% statement, branch, and path coverage  
- Tests verify all critical logic, errors, and API integration points  

---

## Summary of SQA Artifact

### Conclusion

This artifact establishes a comprehensive quality framework for the AI Requirements Conflict Detector, aiming for reliability, accuracy, and maintainability through:  

- Clear, measurable quality objectives  
- Comprehensive black-box and white-box testing  
- Cost-effective QA plan with positive ROI  
- Systematic reviews and audits  
- Full logic coverage ensuring robust conflict detection  
- Compliance with security and maintainability best practices  

**Lessons Learned:**  
- AI systems require specialized non-deterministic testing  
- Prompt engineering critically impacts accuracy  
- Performance and error handling are vital for API-dependent tools  
- User-centric design enhances usability and acceptance  

---

## References

### Books

- Pressman, R. S., & Maxim, B. R. *Software Engineering: A Practitioner’s Approach*, 8th Ed., McGraw-Hill, 2014  
- Wiegers, K., & Beatty, J. *Software Requirements*, 3rd Ed., Microsoft Press, 2013  
- Sommerville, I. *Software Engineering*, 10th Ed., Pearson, 2015  

### Journals & Conferences

- Davis, A. M. "The Art of Requirements Triage." IEEE Computer Society, 2003  
- Wagner, S. "Software Product Quality Control." IEEE Software, 2013  
- Boehm, B., & Turner, R. "Balancing Agility and Discipline." Agile Dev. Conf., 2004  
- Leffingwell, D. "ROI from Effective Requirements." SPI Conference, 1997  

### Standards

- IEEE Std 830-1998 Software Requirements Specs  
- ISO/IEC 25010:2011 Software Quality Models  

### Online Resources

- [Google AI Gemini API](https://ai.google.dev/docs) (accessed July 2025)  
- [pytest Documentation](https://docs.pytest.org/) (accessed July 2025)  

---

> *This document is confidential and intended for academic evaluation only.*

