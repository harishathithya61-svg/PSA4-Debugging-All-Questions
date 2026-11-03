"""
PSA 4 - Question 2: Nested Loops, Loop Control and Prime Number Generation
Department of Computer Science and Engineering - Cybersecurity
JAIN (Deemed-to-be University)
"""

def generate_primes(start, end):
    """
    Generates all prime numbers within an inclusive range [start, end].
    Includes both boundaries, handles edge cases (numbers < 2),
    and avoids unnecessary divisor checks using early loop termination.
    """
    primes = []

    # 1. Inclusive Range Boundary: range(start, end + 1)
    for number in range(start, end + 1):
        # 2. Guard clause for numbers less than 2
        if number < 2:
            continue

        is_prime = True

        # 3. Correct divisor range up to floor(sqrt(number)) inclusive:
        # int(number ** 0.5) + 1 ensures the square root itself is tested as a divisor.
        limit = int(number ** 0.5)
        for divisor in range(2, limit + 1):
            if number % divisor == 0:
                is_prime = False
                # 4. Loop Control: Exit immediately once a divisor is found
                break

        if is_prime:
            primes.append(number)

    return primes


def run_tests():
    print("=" * 60)
    print("QUESTION 2: PRIME NUMBER GENERATION TEST EXECUTION")
    print("=" * 60)

    # Test Case 1: Standard Range (1 to 30)
    result_1_30 = generate_primes(1, 30)
    expected_1_30 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print(f"\n[Test Case 1] generate_primes(1, 30)")
    print(f"Output:   {result_1_30}")
    print(f"Expected: {expected_1_30}")
    assert result_1_30 == expected_1_30, "Test Case 1 Failed!"

    # Test Case 2: Single Prime Boundary Range (2, 2)
    result_2_2 = generate_primes(2, 2)
    expected_2_2 = [2]
    print(f"\n[Test Case 2] generate_primes(2, 2)")
    print(f"Output:   {result_2_2}")
    print(f"Expected: {expected_2_2}")
    assert result_2_2 == expected_2_2, "Test Case 2 Failed!"

    # Test Case 3: Range with No Primes (14, 16)
    result_14_16 = generate_primes(14, 16)
    expected_14_16 = []
    print(f"\n[Test Case 3] generate_primes(14, 16)")
    print(f"Output:   {result_14_16}")
    print(f"Expected: {expected_14_16}")
    assert result_14_16 == expected_14_16, "Test Case 3 Failed!"

    # Test Case 4 (Edge Case): Perfect Squares (testing why original failed for 4, 9, 25)
    result_squares = generate_primes(4, 25)
    print(f"\n[Test Case 4 - Perfect Squares Verification] generate_primes(4, 25)")
    print(f"Output:   {result_squares}")
    assert 4 not in result_squares and 9 not in result_squares and 25 not in result_squares, "Squares classified as prime!"

    # Test Case 5 (Edge Case): Negative and Zero range (-5, 1)
    result_neg = generate_primes(-5, 1)
    print(f"\n[Test Case 5 - Negative and Zero] generate_primes(-5, 1)")
    print(f"Output:   {result_neg}")
    assert result_neg == [], "Negative or 0/1 classified as prime!"

    print("\nAll Test Cases Passed Successfully!\n" + "=" * 60)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        run_tests()
    else:
        # Default behavior: run generate_primes(1, 30) and tests
        print("Primes between 1 and 30:", generate_primes(1, 30))
        run_tests()
