"""
PyTest Demo - Login Functionality Tests
Author: Muhammad Yasin Asif
Date: July 2025
"""

import pytest
from unittest.mock import Mock, patch
import requests


class TestLoginFunctionality:
    """Test suite for login functionality using PyTest"""
    
    @pytest.fixture
    def valid_credentials(self):
        """Fixture providing valid login credentials"""
        return {
            "username": "admin",
            "password": "password123"
        }
    
    @pytest.fixture
    def invalid_credentials(self):
        """Fixture providing invalid login credentials"""
        return {
            "username": "invalid_user",
            "password": "wrong_password"
        }
    
    def test_valid_login(self, valid_credentials):
        """Test successful login with valid credentials"""
        result = self.login(valid_credentials["username"], valid_credentials["password"])
        assert result["status"] == "success"
        assert result["message"] == "Login successful"
        assert "token" in result
    
    def test_invalid_login(self, invalid_credentials):
        """Test failed login with invalid credentials"""
        result = self.login(invalid_credentials["username"], invalid_credentials["password"])
        assert result["status"] == "error"
        assert result["message"] == "Invalid credentials"
        assert "token" not in result
    
    def test_empty_username(self):
        """Test login with empty username"""
        result = self.login("", "password123")
        assert result["status"] == "error"
        assert result["message"] == "Username cannot be empty"
    
    def test_empty_password(self):
        """Test login with empty password"""
        result = self.login("admin", "")
        assert result["status"] == "error"
        assert result["message"] == "Password cannot be empty"
    
    @pytest.mark.parametrize("username,password,expected_status", [
        ("admin", "password123", "success"),
        ("user1", "pass1", "success"),
        ("invalid", "wrong", "error"),
        ("", "password", "error"),
        ("admin", "", "error"),
    ])
    def test_login_parameterized(self, username, password, expected_status):
        """Parameterized test for various login scenarios"""
        result = self.login(username, password)
        assert result["status"] == expected_status
    
    @patch('requests.post')
    def test_login_api_call(self, mock_post, valid_credentials):
        """Test login API integration"""
        # Mock successful API response
        mock_response = Mock()
        mock_response.json.return_value = {
            "status": "success",
            "message": "Login successful",
            "token": "abc123"
        }
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        result = self.login_api(valid_credentials["username"], valid_credentials["password"])
        
        assert result["status"] == "success"
        mock_post.assert_called_once()
    
    def test_password_encryption(self, valid_credentials):
        """Test that passwords are properly encrypted"""
        encrypted_password = self.encrypt_password(valid_credentials["password"])
        assert encrypted_password != valid_credentials["password"]
        assert len(encrypted_password) > len(valid_credentials["password"])
    
    @pytest.mark.slow
    def test_login_performance(self, valid_credentials):
        """Performance test for login functionality"""
        import time
        start_time = time.time()
        
        for _ in range(10):
            self.login(valid_credentials["username"], valid_credentials["password"])
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Login should complete within 5 seconds for 10 attempts
        assert execution_time < 5.0
    
    # Helper methods (simulated login functionality)
    def login(self, username, password):
        """Simulated login function"""
        if not username:
            return {"status": "error", "message": "Username cannot be empty"}
        if not password:
            return {"status": "error", "message": "Password cannot be empty"}
        
        # Simulate valid credentials
        valid_users = {
            "admin": "password123",
            "user1": "pass1"
        }
        
        if username in valid_users and valid_users[username] == password:
            return {
                "status": "success",
                "message": "Login successful",
                "token": "abc123"
            }
        else:
            return {
                "status": "error",
                "message": "Invalid credentials"
            }
    
    def login_api(self, username, password):
        """Simulated API login function"""
        response = requests.post("https://api.example.com/login", 
                               json={"username": username, "password": password})
        return response.json()
    
    def encrypt_password(self, password):
        """Simulated password encryption"""
        # Simple hash simulation
        return f"encrypted_{password}_hash"


class TestLoginSecurity:
    """Security-focused login tests"""
    
    def test_sql_injection_prevention(self):
        """Test SQL injection prevention"""
        malicious_input = "admin'; DROP TABLE users; --"
        result = self.login(malicious_input, "password")
        assert result["status"] == "error"
    
    def test_xss_prevention(self):
        """Test XSS prevention"""
        malicious_input = "<script>alert('xss')</script>"
        result = self.login(malicious_input, "password")
        assert result["status"] == "error"
    
    def test_brute_force_protection(self):
        """Test brute force attack protection"""
        for i in range(5):
            result = self.login("admin", f"wrong_password_{i}")
            assert result["status"] == "error"
        
        # After 5 failed attempts, should be locked out
        result = self.login("admin", "password123")
        assert result["status"] == "error"
        assert "locked" in result["message"].lower()
    
    def login(self, username, password):
        """Simulated login with security checks"""
        # Simulate security validation
        if ";" in username or "<script>" in username:
            return {"status": "error", "message": "Invalid input detected"}
        
        # Simulate brute force protection
        if hasattr(self, '_failed_attempts') and self._failed_attempts >= 5:
            return {"status": "error", "message": "Account temporarily locked"}
        
        return {"status": "error", "message": "Invalid credentials"}


if __name__ == "__main__":
    pytest.main([__file__, "-v"]) 