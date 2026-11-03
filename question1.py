"""
PSA 4 - Question 1: Operator Precedence, Type Conversion and Conditional Reasoning
Department of Computer Science and Engineering - Cybersecurity
JAIN (Deemed-to-be University)
"""

def evaluate(m1, m2, m3, attendance):
    """
    Evaluates student eligibility for an academic scholarship based on:
    1. All three subject marks >= 40.
    2. Average of three marks >= 75.
    3. Attendance percentage >= 75.
    """
    # 1. Type Conversion: Ensure all inputs are numerical (float)
    m1 = float(m1)
    m2 = float(m2)
    m3 = float(m3)
    attendance = float(attendance)

    # 2. Correct Operator Precedence for Average: (m1 + m2 + m3) / 3
    average = (m1 + m2 + m3) / 3.0

    # 3. Independent and Correct Boolean Conditions:
    # Check all subject marks independently using AND
    marks_pass = (m1 >= 40) and (m2 >= 40) and (m3 >= 40)
    average_pass = average >= 75.0
    attendance_pass = attendance >= 75.0

    if marks_pass and average_pass and attendance_pass:
        return average, "Eligible"
    else:
        return average, "Not Eligible"


def run_tests():
    print("=" * 60)
    print("QUESTION 1: SCHOLARSHIP ELIGIBILITY TEST EXECUTION")
    print("=" * 60)

    # Test Case 1: Standard qualifying student
    # Marks: 80, 70, 90; Attendance: 85
    avg1, status1 = evaluate(80, 70, 90, 85)
    print(f"\n[Test Case 1] Input: 80 70 90 85")
    print(f"Calculated Average: {avg1:.2f}")
    print(f"Eligibility Status: {status1}")
    assert avg1 == 80.0 and status1 == "Eligible", "Test Case 1 Failed!"

    # Test Case 2: One mark below 40, but average and attendance meet threshold
    # Marks: 90, 35, 100; Attendance: 85 -> Average = (90+35+100)/3 = 75.0, Attendance = 85
    avg2, status2 = evaluate(90, 35, 100, 85)
    print(f"\n[Test Case 2] Input: 90 35 100 85 (One mark < 40)")
    print(f"Calculated Average: {avg2:.2f}")
    print(f"Eligibility Status: {status2}")
    assert avg2 == 75.0 and status2 == "Not Eligible", "Test Case 2 Failed!"

    # Test Case 3 (Edge Case): Boundary values - exactly 40 for all marks, exactly 75 average, exactly 75 attendance
    # Marks: 75, 75, 75; Attendance: 75 -> Average = 75.0
    avg3, status3 = evaluate(75, 75, 75, 75)
    print(f"\n[Test Case 3 - Boundary Edge Case] Input: 75 75 75 75")
    print(f"Calculated Average: {avg3:.2f}")
    print(f"Eligibility Status: {status3}")
    assert avg3 == 75.0 and status3 == "Eligible", "Test Case 3 Failed!"

    # Test Case 4 (Edge Case): High marks, failing attendance (< 75)
    avg4, status4 = evaluate(95, 90, 92, 74.9)
    print(f"\n[Test Case 4 - Attendance Edge Case] Input: 95 90 92 74.9")
    print(f"Calculated Average: {avg4:.2f}")
    print(f"Eligibility Status: {status4}")
    assert status4 == "Not Eligible", "Test Case 4 Failed!"

    print("\nAll Test Cases Passed Successfully!\n" + "=" * 60)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        # Interactive mode or fallback to test run
        try:
            user_input = input("Enter marks and attendance (e.g. 80 70 90 85): ").strip()
            if not user_input:
                print("No input provided. Running automated tests instead...\n")
                run_tests()
            else:
                data = user_input.split()
                if len(data) != 4:
                    print("Error: Exactly 4 numerical inputs required (m1, m2, m3, attendance).")
                else:
                    avg, status = evaluate(data[0], data[1], data[2], data[3])
                    print(f"Average: {avg:.2f}")
                    print(f"Status: {status}")
        except EOFError:
            run_tests()
