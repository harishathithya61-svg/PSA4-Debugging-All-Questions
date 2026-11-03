"""
PSA 4 - Question 3: Recursion, Base Cases and Function Return Values
Department of Computer Science and Engineering - Cybersecurity
JAIN (Deemed-to-be University)
"""

def digit_sum(number):
    """
    Recursively calculates the sum of all digits of a non-negative integer.
    Base case: Single-digit number (< 10) returns itself.
    Recursive step: Adds the least significant digit (number % 10) to the
    sum of the remaining digits (digit_sum(number // 10)).
    """
    # Defensive input check
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base case: Any single-digit number (0 to 9)
    if number < 10:
        return number

    # Extract least significant digit
    digit = number % 10

    # Recursive call contributing directly to the final accumulated return value
    return digit + digit_sum(number // 10)


def run_tests():
    print("=" * 60)
    print("QUESTION 3: RECURSIVE DIGIT SUM TEST EXECUTION")
    print("=" * 60)

    # Test Case 1: Multi-digit integer 5824 (5 + 8 + 2 + 4 = 19)
    res_5824 = digit_sum(5824)
    print(f"\n[Test Case 1] digit_sum(5824)")
    print(f"Output:   {res_5824}")
    print(f"Expected: 19")
    assert res_5824 == 19, "Test Case 1 Failed!"

    # Test Case 2: Single digit 7 (Base case)
    res_7 = digit_sum(7)
    print(f"\n[Test Case 2] digit_sum(7)")
    print(f"Output:   {res_7}")
    print(f"Expected: 7")
    assert res_7 == 7, "Test Case 2 Failed!"

    # Test Case 3: Zero 0 (Base case)
    res_0 = digit_sum(0)
    print(f"\n[Test Case 3] digit_sum(0)")
    print(f"Output:   {res_0}")
    print(f"Expected: 0")
    assert res_0 == 0, "Test Case 3 Failed!"

    # Test Case 4 (Edge Case): Large number 99999
    res_large = digit_sum(99999)
    print(f"\n[Test Case 4 - Large Number] digit_sum(99999)")
    print(f"Output:   {res_large}")
    print(f"Expected: 45")
    assert res_large == 45, "Test Case 4 Failed!"

    print("\nAll Test Cases Passed Successfully!\n" + "=" * 60)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        num = 5824
        print(f"Sum of digits of {num}:", digit_sum(num))
        run_tests()
