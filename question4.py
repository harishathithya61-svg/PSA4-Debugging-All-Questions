"""
PSA 4 - Question 4: Lists, Mutation, Comprehensions and Sorting
Department of Computer Science and Engineering - Cybersecurity
JAIN (Deemed-to-be University)
"""

def process_marks(marks):
    """
    Processes marks according to 5 requirements:
    1. Remove all marks below 40.
    2. Remove duplicate marks.
    3. Sort remaining marks in ascending order.
    4. Identify marks greater than or equal to 60.
    5. Display the three highest qualifying marks (or all if < 3).
    """
    # Req 1, 2, 3: Filter marks >= 40, deduplicate via set, and sort in ascending order
    # Avoiding in-place list mutation during iteration
    processed_marks = sorted(list({mark for mark in marks if mark >= 40}))

    # Req 4: Qualifying marks >= 60 (inclusive boundary condition)
    qualified = [mark for mark in processed_marks if mark >= 60]

    # Req 5: Three highest qualifying marks (sorted descending for top display, or top 3)
    # If fewer than three exist, returns all of them
    top_three = sorted(qualified, reverse=True)[:3]

    return processed_marks, qualified, top_three


def run_tests():
    print("=" * 60)
    print("QUESTION 4: MARKS PROCESSING TEST EXECUTION")
    print("=" * 60)

    # Test Case 1: Provided Dataset
    input_marks = [35, 60, 45, 80, 35, 55, 60, 95, 40, 80]
    processed, qual, top3 = process_marks(input_marks)

    print("\n[Test Case 1 - Provided List]")
    print("Input marks:    ", input_marks)
    print("Processed marks:", processed)
    print("Qualified marks:", qual)
    print("Top three:      ", top3)

    assert processed == [40, 45, 55, 60, 80, 95], f"Processed marks failed! Got {processed}"
    assert qual == [60, 80, 95], f"Qualified marks failed! Got {qual}"
    assert top3 == [95, 80, 60], f"Top three failed! Got {top3}"

    # Test Case 2 (Edge Case): Fewer than 3 qualifying marks
    input_edge1 = [30, 42, 65, 75, 20]
    processed2, qual2, top3_2 = process_marks(input_edge1)
    print("\n[Test Case 2 - Fewer than 3 Qualifying Marks]")
    print("Input marks:    ", input_edge1)
    print("Processed marks:", processed2)
    print("Qualified marks:", qual2)
    print("Top three:      ", top3_2)
    assert qual2 == [65, 75] and top3_2 == [75, 65]

    # Test Case 3 (Edge Case): Boundary marks exactly 40 and 60 with duplicates
    input_edge2 = [40, 40, 60, 60, 39, 59]
    processed3, qual3, top3_3 = process_marks(input_edge2)
    print("\n[Test Case 3 - Boundary Values 40 and 60]")
    print("Input marks:    ", input_edge2)
    print("Processed marks:", processed3)
    print("Qualified marks:", qual3)
    print("Top three:      ", top3_3)
    assert processed3 == [40, 59, 60] and qual3 == [60] and top3_3 == [60]

    print("\nAll Test Cases Passed Successfully!\n" + "=" * 60)


if __name__ == "__main__":
    marks = [35, 60, 45, 80, 35, 55, 60, 95, 40, 80]
    processed_marks, qualified, top_three = process_marks(marks)
    print("Processed marks:", processed_marks)
    print("Qualified marks:", qualified)
    print("Top three:", top_three)
    print()
    run_tests()
