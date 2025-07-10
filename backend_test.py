#!/usr/bin/env python3
"""
Comprehensive Backend API Testing for Teacher Management System
Tests all CRUD operations for teachers and students, database connectivity, and error handling.
"""

import requests
import json
import uuid
import time
from datetime import datetime
import os

# Get base URL from environment or use default
BASE_URL = os.getenv('NEXT_PUBLIC_BASE_URL', 'https://03bcb5c0-91f4-4b82-9bdd-c241f506cc8c.preview.emergentagent.com')
API_BASE = f"{BASE_URL}/api"

class TeacherManagementAPITester:
    def __init__(self):
        self.created_teachers = []
        self.created_students = []
        self.test_results = {
            'passed': 0,
            'failed': 0,
            'errors': []
        }
    
    def log_result(self, test_name, success, message=""):
        """Log test results"""
        if success:
            self.test_results['passed'] += 1
            print(f"✅ {test_name}: PASSED {message}")
        else:
            self.test_results['failed'] += 1
            self.test_results['errors'].append(f"{test_name}: {message}")
            print(f"❌ {test_name}: FAILED {message}")
    
    def test_teacher_crud_operations(self):
        """Test all teacher CRUD operations"""
        print("\n=== TESTING TEACHER CRUD OPERATIONS ===")
        
        # Test data for teacher creation
        teacher_data = {
            "name": "Dr. Sarah Johnson",
            "email": "sarah.johnson@school.edu",
            "phone": "+1-555-0123",
            "department": "Mathematics",
            "subject": "Advanced Calculus",
            "hireDate": "2020-08-15",
            "salary": 75000,
            "qualification": "PhD in Mathematics",
            "experience": 8
        }
        
        # 1. Test POST /api/teachers - Create teacher
        try:
            response = requests.post(f"{API_BASE}/teachers", json=teacher_data, timeout=10)
            if response.status_code == 200:
                teacher = response.json().get('teacher')
                if teacher and 'id' in teacher:
                    self.created_teachers.append(teacher['id'])
                    self.log_result("POST /api/teachers", True, f"Created teacher with ID: {teacher['id']}")
                    
                    # Verify all required fields are present
                    required_fields = ['id', 'name', 'email', 'phone', 'department', 'subject', 'hireDate', 'qualification', 'experience', 'createdAt', 'updatedAt']
                    missing_fields = [field for field in required_fields if field not in teacher]
                    if missing_fields:
                        self.log_result("Teacher field validation", False, f"Missing fields: {missing_fields}")
                    else:
                        self.log_result("Teacher field validation", True, "All required fields present")
                else:
                    self.log_result("POST /api/teachers", False, "No teacher data in response")
            else:
                self.log_result("POST /api/teachers", False, f"Status: {response.status_code}, Response: {response.text}")
        except Exception as e:
            self.log_result("POST /api/teachers", False, f"Exception: {str(e)}")
        
        # 2. Test GET /api/teachers - Get all teachers
        try:
            response = requests.get(f"{API_BASE}/teachers", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if 'teachers' in data and isinstance(data['teachers'], list):
                    self.log_result("GET /api/teachers", True, f"Retrieved {len(data['teachers'])} teachers")
                else:
                    self.log_result("GET /api/teachers", False, "Invalid response format")
            else:
                self.log_result("GET /api/teachers", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_result("GET /api/teachers", False, f"Exception: {str(e)}")
        
        # 3. Test GET /api/teachers/{id} - Get single teacher
        if self.created_teachers:
            teacher_id = self.created_teachers[0]
            try:
                response = requests.get(f"{API_BASE}/teachers/{teacher_id}", timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if 'teacher' in data and data['teacher']['id'] == teacher_id:
                        self.log_result("GET /api/teachers/{id}", True, f"Retrieved teacher: {teacher_id}")
                    else:
                        self.log_result("GET /api/teachers/{id}", False, "Teacher data mismatch")
                else:
                    self.log_result("GET /api/teachers/{id}", False, f"Status: {response.status_code}")
            except Exception as e:
                self.log_result("GET /api/teachers/{id}", False, f"Exception: {str(e)}")
        
        # 4. Test PUT /api/teachers/{id} - Update teacher
        if self.created_teachers:
            teacher_id = self.created_teachers[0]
            update_data = {
                "name": "Dr. Sarah Johnson-Smith",
                "salary": 80000,
                "experience": 9
            }
            try:
                response = requests.put(f"{API_BASE}/teachers/{teacher_id}", json=update_data, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if 'teacher' in data and data['teacher']['name'] == update_data['name']:
                        self.log_result("PUT /api/teachers/{id}", True, f"Updated teacher: {teacher_id}")
                    else:
                        self.log_result("PUT /api/teachers/{id}", False, "Update not reflected in response")
                else:
                    self.log_result("PUT /api/teachers/{id}", False, f"Status: {response.status_code}")
            except Exception as e:
                self.log_result("PUT /api/teachers/{id}", False, f"Exception: {str(e)}")
        
        # 5. Test DELETE /api/teachers/{id} - Delete teacher (we'll create a new one for deletion)
        delete_teacher_data = {
            "name": "Test Teacher for Deletion",
            "email": "delete.test@school.edu",
            "phone": "+1-555-9999",
            "department": "Test Department",
            "subject": "Test Subject",
            "hireDate": "2023-01-01",
            "salary": 50000,
            "qualification": "Test Qualification",
            "experience": 1
        }
        
        try:
            # Create teacher to delete
            response = requests.post(f"{API_BASE}/teachers", json=delete_teacher_data, timeout=10)
            if response.status_code == 200:
                teacher_to_delete = response.json().get('teacher')
                if teacher_to_delete and 'id' in teacher_to_delete:
                    delete_id = teacher_to_delete['id']
                    
                    # Now delete the teacher
                    delete_response = requests.delete(f"{API_BASE}/teachers/{delete_id}", timeout=10)
                    if delete_response.status_code == 200:
                        self.log_result("DELETE /api/teachers/{id}", True, f"Deleted teacher: {delete_id}")
                    else:
                        self.log_result("DELETE /api/teachers/{id}", False, f"Status: {delete_response.status_code}")
                else:
                    self.log_result("DELETE /api/teachers/{id}", False, "Could not create teacher for deletion test")
        except Exception as e:
            self.log_result("DELETE /api/teachers/{id}", False, f"Exception: {str(e)}")
    
    def test_student_crud_operations(self):
        """Test all student CRUD operations"""
        print("\n=== TESTING STUDENT CRUD OPERATIONS ===")
        
        # Ensure we have a teacher to assign students to
        teacher_id = None
        if self.created_teachers:
            teacher_id = self.created_teachers[0]
        
        # Test data for student creation
        student_data = {
            "name": "Emma Wilson",
            "email": "emma.wilson@student.edu",
            "phone": "+1-555-0456",
            "grade": "10th Grade",
            "section": "A",
            "teacherId": teacher_id,
            "parentName": "Robert Wilson",
            "parentPhone": "+1-555-0457"
        }
        
        # 1. Test POST /api/students - Create student
        try:
            response = requests.post(f"{API_BASE}/students", json=student_data, timeout=10)
            if response.status_code == 200:
                student = response.json().get('student')
                if student and 'id' in student:
                    self.created_students.append(student['id'])
                    self.log_result("POST /api/students", True, f"Created student with ID: {student['id']}")
                    
                    # Verify all required fields are present
                    required_fields = ['id', 'name', 'email', 'phone', 'grade', 'section', 'parentName', 'parentPhone', 'createdAt', 'updatedAt']
                    missing_fields = [field for field in required_fields if field not in student]
                    if missing_fields:
                        self.log_result("Student field validation", False, f"Missing fields: {missing_fields}")
                    else:
                        self.log_result("Student field validation", True, "All required fields present")
                else:
                    self.log_result("POST /api/students", False, "No student data in response")
            else:
                self.log_result("POST /api/students", False, f"Status: {response.status_code}, Response: {response.text}")
        except Exception as e:
            self.log_result("POST /api/students", False, f"Exception: {str(e)}")
        
        # 2. Test GET /api/students - Get all students
        try:
            response = requests.get(f"{API_BASE}/students", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if 'students' in data and isinstance(data['students'], list):
                    self.log_result("GET /api/students", True, f"Retrieved {len(data['students'])} students")
                else:
                    self.log_result("GET /api/students", False, "Invalid response format")
            else:
                self.log_result("GET /api/students", False, f"Status: {response.status_code}")
        except Exception as e:
            self.log_result("GET /api/students", False, f"Exception: {str(e)}")
        
        # 3. Test GET /api/students/{id} - Get single student
        if self.created_students:
            student_id = self.created_students[0]
            try:
                response = requests.get(f"{API_BASE}/students/{student_id}", timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if 'student' in data and data['student']['id'] == student_id:
                        self.log_result("GET /api/students/{id}", True, f"Retrieved student: {student_id}")
                    else:
                        self.log_result("GET /api/students/{id}", False, "Student data mismatch")
                else:
                    self.log_result("GET /api/students/{id}", False, f"Status: {response.status_code}")
            except Exception as e:
                self.log_result("GET /api/students/{id}", False, f"Exception: {str(e)}")
        
        # 4. Test PUT /api/students/{id} - Update student
        if self.created_students:
            student_id = self.created_students[0]
            update_data = {
                "name": "Emma Wilson-Smith",
                "grade": "11th Grade",
                "section": "B"
            }
            try:
                response = requests.put(f"{API_BASE}/students/{student_id}", json=update_data, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    if 'student' in data and data['student']['name'] == update_data['name']:
                        self.log_result("PUT /api/students/{id}", True, f"Updated student: {student_id}")
                    else:
                        self.log_result("PUT /api/students/{id}", False, "Update not reflected in response")
                else:
                    self.log_result("PUT /api/students/{id}", False, f"Status: {response.status_code}")
            except Exception as e:
                self.log_result("PUT /api/students/{id}", False, f"Exception: {str(e)}")
        
        # 5. Test DELETE /api/students/{id} - Delete student
        delete_student_data = {
            "name": "Test Student for Deletion",
            "email": "delete.student@test.edu",
            "phone": "+1-555-8888",
            "grade": "9th Grade",
            "section": "Z",
            "teacherId": teacher_id,
            "parentName": "Test Parent",
            "parentPhone": "+1-555-8889"
        }
        
        try:
            # Create student to delete
            response = requests.post(f"{API_BASE}/students", json=delete_student_data, timeout=10)
            if response.status_code == 200:
                student_to_delete = response.json().get('student')
                if student_to_delete and 'id' in student_to_delete:
                    delete_id = student_to_delete['id']
                    
                    # Now delete the student
                    delete_response = requests.delete(f"{API_BASE}/students/{delete_id}", timeout=10)
                    if delete_response.status_code == 200:
                        self.log_result("DELETE /api/students/{id}", True, f"Deleted student: {delete_id}")
                    else:
                        self.log_result("DELETE /api/students/{id}", False, f"Status: {delete_response.status_code}")
                else:
                    self.log_result("DELETE /api/students/{id}", False, "Could not create student for deletion test")
        except Exception as e:
            self.log_result("DELETE /api/students/{id}", False, f"Exception: {str(e)}")
    
    def test_error_handling(self):
        """Test error handling scenarios"""
        print("\n=== TESTING ERROR HANDLING ===")
        
        # Test 404 for non-existent teacher
        try:
            fake_id = str(uuid.uuid4())
            response = requests.get(f"{API_BASE}/teachers/{fake_id}", timeout=10)
            if response.status_code == 404:
                self.log_result("404 Error for non-existent teacher", True, "Correctly returned 404")
            else:
                self.log_result("404 Error for non-existent teacher", False, f"Expected 404, got {response.status_code}")
        except Exception as e:
            self.log_result("404 Error for non-existent teacher", False, f"Exception: {str(e)}")
        
        # Test 404 for non-existent student
        try:
            fake_id = str(uuid.uuid4())
            response = requests.get(f"{API_BASE}/students/{fake_id}", timeout=10)
            if response.status_code == 404:
                self.log_result("404 Error for non-existent student", True, "Correctly returned 404")
            else:
                self.log_result("404 Error for non-existent student", False, f"Expected 404, got {response.status_code}")
        except Exception as e:
            self.log_result("404 Error for non-existent student", False, f"Exception: {str(e)}")
        
        # Test invalid endpoint
        try:
            response = requests.get(f"{API_BASE}/invalid-endpoint", timeout=10)
            if response.status_code == 404:
                self.log_result("404 Error for invalid endpoint", True, "Correctly returned 404")
            else:
                self.log_result("404 Error for invalid endpoint", False, f"Expected 404, got {response.status_code}")
        except Exception as e:
            self.log_result("404 Error for invalid endpoint", False, f"Exception: {str(e)}")
    
    def test_database_connectivity(self):
        """Test database connectivity by attempting basic operations"""
        print("\n=== TESTING DATABASE CONNECTIVITY ===")
        
        # Test basic connectivity by trying to fetch teachers
        try:
            response = requests.get(f"{API_BASE}/teachers", timeout=10)
            if response.status_code == 200:
                self.log_result("Database connectivity", True, "Successfully connected to database")
            elif response.status_code == 500:
                self.log_result("Database connectivity", False, "Database connection error (500)")
            else:
                self.log_result("Database connectivity", False, f"Unexpected status: {response.status_code}")
        except Exception as e:
            self.log_result("Database connectivity", False, f"Exception: {str(e)}")
    
    def test_data_persistence(self):
        """Test that data persists correctly"""
        print("\n=== TESTING DATA PERSISTENCE ===")
        
        if not self.created_teachers:
            self.log_result("Data persistence test", False, "No teachers created to test persistence")
            return
        
        teacher_id = self.created_teachers[0]
        
        # Fetch the teacher multiple times to ensure data persists
        try:
            response1 = requests.get(f"{API_BASE}/teachers/{teacher_id}", timeout=10)
            time.sleep(1)  # Small delay
            response2 = requests.get(f"{API_BASE}/teachers/{teacher_id}", timeout=10)
            
            if response1.status_code == 200 and response2.status_code == 200:
                teacher1 = response1.json().get('teacher')
                teacher2 = response2.json().get('teacher')
                
                if teacher1 and teacher2 and teacher1['id'] == teacher2['id']:
                    self.log_result("Data persistence", True, "Data persists correctly across requests")
                else:
                    self.log_result("Data persistence", False, "Data inconsistency detected")
            else:
                self.log_result("Data persistence", False, f"Failed to fetch teacher data for persistence test")
        except Exception as e:
            self.log_result("Data persistence", False, f"Exception: {str(e)}")
    
    def run_all_tests(self):
        """Run all test suites"""
        print(f"🚀 Starting comprehensive backend API testing for Teacher Management System")
        print(f"📍 Testing API at: {API_BASE}")
        print(f"⏰ Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Run all test suites
        self.test_database_connectivity()
        self.test_teacher_crud_operations()
        self.test_student_crud_operations()
        self.test_error_handling()
        self.test_data_persistence()
        
        # Print final results
        print(f"\n{'='*60}")
        print(f"🏁 TEST SUMMARY")
        print(f"{'='*60}")
        print(f"✅ Tests Passed: {self.test_results['passed']}")
        print(f"❌ Tests Failed: {self.test_results['failed']}")
        print(f"📊 Success Rate: {(self.test_results['passed'] / (self.test_results['passed'] + self.test_results['failed']) * 100):.1f}%")
        
        if self.test_results['errors']:
            print(f"\n🔍 FAILED TESTS:")
            for error in self.test_results['errors']:
                print(f"   • {error}")
        
        print(f"\n⏰ Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Return overall success status
        return self.test_results['failed'] == 0

if __name__ == "__main__":
    tester = TeacherManagementAPITester()
    success = tester.run_all_tests()
    
    if success:
        print(f"\n🎉 ALL TESTS PASSED! Backend API is working correctly.")
        exit(0)
    else:
        print(f"\n⚠️  SOME TESTS FAILED! Please check the errors above.")
        exit(1)