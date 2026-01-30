'''
Tutorial Test Week 10 - Question 1
Student Grade Symbol Table (Binary Search Tree)

@Author: Alok More
'''
from collections import OrderedDict

class GradeBook:
    """
    A gradebook that maintains students and their grades in sorted order by student_id.
    Uses Binary Search Tree principles for efficient ordered operations.
    """
    
    def __init__(self):
        """Initialize an empty gradebook"""
        # TODO: Initialize your data structure here
        # Hint: You'll need to store students in a way that maintains order
        self.grade_book = OrderedDict({}) # Ordered symbol table so oreder is maintained
    
    def add_student(self, student_id, grade):
        """
        Add a student with their grade (maintains order by student_id).
        If student already exists, update their grade.
        
        Args:
            student_id (str): The student's ID (e.g., "S001")
            grade (int): The student's grade (0-100)
        
        Returns:
            str: Confirmation message
        """
        # TODO: Implement adding/updating student
        # Return format: "Student {student_id} added with grade {grade}."
        # Or: "Student {student_id} grade updated to {grade}."
        if len(self.grade_book) == 0:
            self.grade_book[student_id] = grade # Adds student if grade book is empty.
            return f"Student {student_id} added with grade {grade}."

        elif student_id in self.grade_book:
            self.grade_book[student_id] = grade # Updates grade of student.
            return f"Student {student_id} grade updated to {grade}."

        else:
            self.grade_book[student_id] = grade
            return f"Student {student_id} added with grade {grade}."
    
    def get_grade(self, student_id):
        """
        Get the grade for a given student.
        
        Args:
            student_id (str): The student's ID
        
        Returns:
            int or None: The student's grade, or None if not found
        """
        # TODO: Implement grade lookup
        if len(self.grade_book) == 0:
            return "Empty grade book."
        
        elif student_id in self.grade_book:
            return self.grade_book[student_id]
        
        else: return None
    
    def get_min_grade(self):
        """
        Get the lowest grade in the gradebook.
        
        Returns:
            int or None: The minimum grade, or None if gradebook is empty
        """
        # TODO: Implement finding minimum grade
        # Hint: This requires searching through all students, not just leftmost
        if len(self.grade_book) == 0: return None

        else:
            values = []

            for k in self.grade_book:
                values.append(self.grade_book[k])

            mini = 100

            for i in range(len(values)):
                if values[i] < mini:
                    mini = values[i]

            return mini 
    
    def get_max_grade(self):
        """
        Get the highest grade in the gradebook.
        
        Returns:
            int or None: The maximum grade, or None if gradebook is empty
        """
        # TODO: Implement finding maximum grade
        # Hint: This requires searching through all students, not just rightmost
        if len(self.grade_book) == 0: return None

        else:
            values = []

            for k in self.grade_book:
                values.append(self.grade_book[k])

            max = 0

            for i in range(len(values)):
                if values[i] < max:
                    max = values[i]

            return max 
    
    def get_students_in_range(self, low_id, high_id):
        """
        Get all students with IDs in the range [low_id, high_id] (inclusive).
        
        Args:
            low_id (str): Lower bound student ID
            high_id (str): Upper bound student ID
        
        Returns:
            list: List of (student_id, grade) tuples sorted by student_id
        """
        # TODO: Implement range query
        # Return format: [("S001", 85), ("S002", 90), ...]
        if len(self.grade_book) == 0: return None

        elif low_id not in self.grade_book or high_id not in self.grade_book:
            return "ID(s) not in grade book"

        else:
            id = list(self.grade_book.keys())
            start = id.index(low_id)
            end = id.index(high_id)
            wanted = id[start:end+1]

            ranged = OrderedDict((i, self.grade_book[i]) for i in wanted)
            return list(ranged.items())

    def get_all_students_sorted(self):
        """
        Get all students sorted by student_id.
        
        Returns:
            list: List of (student_id, grade) tuples sorted by student_id
        """
        # TODO: Implement in-order traversal
        # Return format: [("S001", 85), ("S002", 90), ...]
        keys = list(self.grade_book.keys()) # Created a list of the ids for better sorting.
        n = len(keys)

        while n > 1:
            for i in reversed(range(n-1)): # Checking from previous id to see if last id is smaller
                if keys[i+1] < keys[i]:
                    keys[i+1], keys[i] = keys[i], keys[i+1] # Swaps ids if last id is smaller

            n -= 1

        self.grade_book = OrderedDict((k, self.grade_book[k]) for k in keys)
        return list(self.grade_book.items())
    
    def count_students(self):
        """
        Get the total number of students in the gradebook.
        
        Returns:
            int: Number of students
        """
        # TODO: Implement student count
        return len(self.grade_book)


# Simple testing code
if __name__ == "__main__":
    print("Testing GradeBook Class")
    print("=" * 50)
    
    gradebook = GradeBook()
    
    # Test 1: Add students
    print("\n1. Adding students:")
    print(gradebook.add_student("S003", 85))
    print(gradebook.add_student("S001", 92))
    print(gradebook.add_student("S005", 78))
    print(gradebook.add_student("S002", 88))
    
    # Test 2: Update student
    print("\n2. Updating student:")
    print(gradebook.add_student("S003", 90))
    
    # Test 3: Get grade
    print("\n3. Getting grades:")
    print(f"S001 grade: {gradebook.get_grade('S001')}")
    print(f"S999 grade: {gradebook.get_grade('S999')}")
    
    # Test 4: Min and max grades
    print("\n4. Min and max grades:")
    print(f"Min grade: {gradebook.get_min_grade()}")
    print(f"Max grade: {gradebook.get_max_grade()}")
    
    # Test 5: Count students
    print("\n5. Student count:")
    print(f"Total students: {gradebook.count_students()}")
    
    # Test 6: All students sorted
    print("\n6. All students (sorted):")
    print(gradebook.get_all_students_sorted())
    
    # Test 7: Students in range
    print("\n7. Students in range S002-S004:")
    print(gradebook.get_students_in_range("S002", "S004"))
    
    print("\n" + "=" * 50)
    print("Testing complete!")
