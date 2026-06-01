def get_next_difficulty(scores, prev_difficulty):
    avg = sum(scores) / len(scores)

    if avg < 40:
        next_diff = "easy"
    elif avg < 70:
        next_diff = "medium"
    else:
        next_diff = "hard"

    # Prevent sudden jumps
    if prev_difficulty == "easy" and next_diff == "hard":
        return "medium"
    if prev_difficulty == "hard" and next_diff == "easy":
        return "medium"

    return next_diff
