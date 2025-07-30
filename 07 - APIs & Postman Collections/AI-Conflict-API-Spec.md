# 🧠 AI Requirements Conflict Detector - API Specification

## Base URL
https://mockserver.aiconflictdetector.com/api

## Authentication
All endpoints require a valid API key in the header:
```
Authorization: Bearer YOUR_API_KEY
```

---

## 🔸 POST `/detect-conflict`

### Description:
Detects if two requirement statements conflict using AI analysis.

### Request Body:
```json
{
  "requirement_1": "System shall log all failed login attempts",
  "requirement_2": "System must never store login failures"
}
```

### Response (No Conflict):
```json
{
  "conflict": false,
  "message": "No conflict detected",
  "confidence": 0.95,
  "timestamp": "2025-07-30T10:30:00Z"
}
```

### Response (Conflict Detected):
```json
{
  "conflict": true,
  "message": "Logical conflict between logging and storage constraints",
  "confidence": 0.87,
  "timestamp": "2025-07-30T10:30:00Z",
  "details": {
    "conflict_type": "logical_contradiction",
    "severity": "medium"
  }
}
```

### Error Response:
```json
{
  "error": "Invalid input format",
  "message": "Both requirements must be non-empty strings",
  "status_code": 400
}
```

---

## 🔸 POST `/rewrite`

### Description:
Returns a clarified version of two conflicting requirements.

### Request Body:
```json
{
  "requirement_1": "System shall log all failed login attempts",
  "requirement_2": "System must never store login failures"
}
```

### Response:
```json
{
  "rewritten": "System shall log failed logins while excluding storage beyond 24h for privacy.",
  "original_requirements": [
    "System shall log all failed login attempts",
    "System must never store login failures"
  ],
  "changes_made": [
    "Added time limitation for storage",
    "Clarified logging scope"
  ],
  "timestamp": "2025-07-30T10:30:00Z"
}
```

---

## 🔸 GET `/health`

### Description:
Health check endpoint to verify API status.

### Response:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "ai_model": "gemini-1.5-flash",
  "uptime": "99.8%",
  "timestamp": "2025-07-30T10:30:00Z"
}
```

---

## 🔸 POST `/validate-input`

### Description:
Validates requirement input format and length.

### Request Body:
```json
{
  "requirement": "System shall respond within 2 seconds"
}
```

### Response:
```json
{
  "valid": true,
  "length": 35,
  "max_length": 500,
  "format": "valid"
}
```

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Bad Request - Invalid input format |
| 401 | Unauthorized - Invalid API key |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error - AI service unavailable |
| 503 | Service Unavailable - System maintenance |

---

<div align="center">
  <i>Part of <a href="https://github.com/Yasin-asif/SQA-Professional-Portfolio">Muhammad Yasin's SQA Professional Portfolio</a></i>
</div> 