# 🤖 AI Requirements Conflict Detector

<div align="center">

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/AI-Gemini_1.5-blue?style=flat&logo=google&logoColor=white)
![Last Updated](https://img.shields.io/github/last-commit/Yasin-asif/SQA-Professional-Portfolio?label=Last%20Updated)

**A comprehensive Software Quality Assurance (SQA) plan for an AI-powered tool that automatically detects and resolves conflicts in software requirements documents.**

</div>

---

## 📋 Table of Contents

- [📊 Project Overview](#-project-overview)
- [🎯 Objectives](#-objectives)
- [🔍 Quality Attributes](#-quality-attributes)
- [📐 Quality Model](#-quality-model)
- [💰 Cost Analysis](#-cost-analysis)
- [🛡️ SQA Plan](#️-sqa-plan)
- [🧪 Quality Control](#-quality-control)
- [📈 Test Results](#-test-results)
- [📚 References](#-references)
- [👨‍💻 Author](#-author)

---

## 📊 Project Overview

<div align="center">
  <table>
    <tr>
      <td align="center">
        <h3>🧠 AI-Powered</h3>
        <p>Uses Google's Gemini 1.5 Flash API for intelligent conflict detection</p>
      </td>
      <td align="center">
        <h3>⚙️ Automated</h3>
        <p>Automatically rewrites requirements to resolve conflicts</p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <h3>⚡ Fast</h3>
        <p>Response time under 3 seconds</p>
      </td>
      <td align="center">
        <h3>🔧 Maintainable</h3>
        <p>Well-documented code with comprehensive test coverage</p>
      </td>
    </tr>
  </table>
</div>

### Purpose

The AI Requirements Conflict Detector is designed to identify and resolve conflicts in software requirements while preserving their original intent. This SQA plan defines the quality standards, testing strategies, and assurance activities necessary for delivering a reliable, accurate, and maintainable system.

### Scope

This SQA plan covers:

- AI model integration with Google's Gemini 1.5 Flash API
- Conflict detection algorithms and logic
- Requirement rewriting mechanisms
- User interface input/output handling
- API integration and response parsing
- Data validation and error handling
- Performance optimization for real-time detection

## 🎯 Objectives

- Achieve **95% accuracy** in conflict detection
- Maintain response time under **3 seconds**
- Ensure **99.5% availability** during operations
- Provide clear, testable, unambiguous rewritten requirements
- Handle API failures and edge cases comprehensively
- Support scalability for multiple concurrent requests

## 🔍 Quality Attributes

<div align="center">
  <img src="https://via.placeholder.com/800x400.png?text=Quality+Attributes+Radar+Chart" alt="Quality Attributes Radar Chart" width="600"/>
</div>

### Primary Quality Attributes (ranked by priority)

1. **Accuracy** - Critical for detecting genuine conflicts
2. **Reliability** - System must operate consistently
3. **Performance** - Fast response time is essential
4. **Usability** - Easy for requirements engineers to use
5. **Maintainability** - Code must be sustainable
6. **Security** - Protected access to requirements data
7. **Scalability** - Handle growth in requirements volume

### Secondary Quality Attributes

- **Interoperability** - Works with existing requirements tools
- **Portability** - Functions across development environments
- **Testability** - Can be thoroughly verified

## 📐 Quality Model

The project implements the **ISO/IEC 25010 Software Quality Model** (successor of ISO 9126) because it:

- Provides comprehensive coverage of key software quality factors
- Aligns with AI system needs emphasizing accuracy and performance
- Addresses modern security and compatibility requirements
- Offers measurable quality metrics
- Is widely accepted in academia and industry

## 💰 Cost Analysis

### Cost of Quality vs. Cost of Failure

<div align="center">
  <table>
    <tr>
      <th>Quality Investment</th>
      <th>Potential Cost of Failure</th>
    </tr>
    <tr>
      <td align="center">$3,165</td>
      <td align="center">$6,860</td>
    </tr>
    <tr>
      <td colspan="2" align="center"><b>ROI: 2.13:1</b> - Every $1 invested in quality saves $2.13 in failure costs</td>
    </tr>
  </table>
</div>

### Quality Investment Breakdown

| Activity | Cost |
|----------|------|
| Requirements analysis/reviews | $375 |
| Code reviews & pair programming | $500 |
| AI prompt engineering | $360 |
| Unit & integration testing | $450 |
| Quality planning & documentation | $200 |
| Manual testing execution | $300 |
| Automated testing maintenance | $300 |
| AI response validation testing | $300 |
| Performance testing | $200 |
| Security testing | $180 |
| **Total** | **$3,165** |

*Additional costs: Google Gemini API (~$50)*

## 🛡️ SQA Plan

### Activities

<div align="center">
  <table>
    <tr>
      <td align="center">
        <h3>📝 Planning & Design</h3>
        <p>Requirements workshops, architecture reviews, AI model evaluation</p>
      </td>
      <td align="center">
        <h3>👨‍💻 Development</h3>
        <p>Code reviews, CI integration, AI prompt optimization</p>
      </td>
    </tr>
    <tr>
      <td align="center">
        <h3>🧪 Testing</h3>
        <p>Unit, integration, system, and acceptance testing</p>
      </td>
      <td align="center">
        <h3>🚀 Deployment</h3>
        <p>Pre-deployment gates, monitoring, performance tracking</p>
      </td>
    </tr>
  </table>
</div>

### Standards & Tools

- **Standards:** IEEE 830-1998, IEEE 1028, IEEE 1063, PEP 8 for Python
- **Tools:** Git/GitHub, JIRA, pytest, Postman, SonarQube, APM tools, Confluence
- **AI-specific:** Google AI Studio, custom validation scripts, performance profiling

### Reviews & Audits

- Weekly code reviews by team members
- Bi-weekly architecture & AI integration reviews
- Monthly comprehensive quality audits
- Pre-release quality gates

#### Audit Criteria
- Minimum 80% code coverage
- AI response accuracy >90%
- Meet performance benchmarks
- Pass security scans
- Complete documentation

## 🧪 Quality Control

### Black Box Testing

#### Equivalence Class Partitioning (ECP)

| Test ID | Input Class | Example | Expected Output |
|---------|-------------|---------|----------------|
| TC001 | Valid conflicting | "System shall respond within 2s" vs "Response time should not exceed 5s" | Conflict detected |
| TC002 | Valid non-conflicting | "System shall authenticate users" vs "System shall log user activities" | No conflict |
| TC003 | Invalid/malformed | "Sys%tem sh@ll..." vs "Valid requirement" | Error message |
| TC004 | Empty requirements | "" vs "Valid requirement" | Error message |

#### Boundary Value Analysis (BVA)

| Test ID | Input Length | Test Data | Expected Result |
|---------|-------------|-----------|----------------|
| TC005 | 9 chars | "Short req" | Error: Too short |
| TC006 | 10 chars | "Valid req." | Accepted |
| TC007 | 500 chars | Max length | Accepted |
| TC008 | 501 chars | Exceeds max | Error: Too long |

### White Box Testing

- **Cyclomatic Complexity:** 4 (moderate)
- **Independent Paths:** 5 (includes error handling)
- **Coverage Metrics:** 100% statement, branch, and path coverage

## 📈 Test Results

<div align="center">
  <table>
    <tr>
      <th>Test Type</th>
      <th>Total Tests</th>
      <th>Passed</th>
      <th>Failed</th>
      <th>Pass Rate</th>
    </tr>
    <tr>
      <td>Unit Tests</td>
      <td>42</td>
      <td>42</td>
      <td>0</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>Integration Tests</td>
      <td>18</td>
      <td>18</td>
      <td>0</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>System Tests</td>
      <td>12</td>
      <td>12</td>
      <td>0</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>Performance Tests</td>
      <td>6</td>
      <td>6</td>
      <td>0</td>
      <td>100%</td>
    </tr>
  </table>
</div>

## 📚 References

### Books & Academic Resources
- Pressman, R. S., & Maxim, B. R. *Software Engineering: A Practitioner's Approach*, 8th Ed., McGraw-Hill, 2014
- Wiegers, K., & Beatty, J. *Software Requirements*, 3rd Ed., Microsoft Press, 2013
- Sommerville, I. *Software Engineering*, 10th Ed., Pearson, 2015

### Standards
- IEEE Std 830-1998 Software Requirements Specs
- ISO/IEC 25010:2011 Software Quality Models

### Online Resources
- [Google AI Gemini API](https://ai.google.dev/docs) (accessed July 2025)
- [pytest Documentation](https://docs.pytest.org/) (accessed July 2025)

## 👨‍💻 Author

**Muhammad Yasin Asif**  
Aspiring QA Engineer  
Bachelor of Science in Software Engineering (2023–2027)  
Shifa Tameer-e-Millat University, Islamabad

---

<div align="center">
  <i>This project is part of my <a href="https://github.com/Yasin-asif/SQA-Professional-Portfolio">SQA Professional Portfolio</a></i>
</div>

> *This document is confidential and intended for professional portfolio demonstration only.* 