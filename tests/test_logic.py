from ..logic.difficulty import get_next_difficulty

def test_cases():
    assert get_next_difficulty([10, 20, 30], "medium") == "easy"
    assert get_next_difficulty([80, 90, 100], "medium") == "hard"
    assert get_next_difficulty([80, 90, 100], "easy") == "medium"   # prevents immediate jump
    assert get_next_difficulty([20, 30, 40], "hard") == "medium"    # prevents immediate jump
    assert get_next_difficulty([50, 60, 70], "medium") == "medium"

if __name__ == "__main__":
    test_cases()
    print("All tests passed!")
