from logic.difficulty import get_next_difficulty
import json
from datetime import datetime

LOG_FILE = "difficulty_log.json"

if __name__ == "__main__":
    scores = []
    for i in range(3):
        score = input(f"Enter score {i+1} (or press Enter to skip): ")
        if score.strip() != "":
            scores.append(int(score))

    if len(scores) == 0:
        print("No scores provided. Please enter at least one.")
    else:
        prev_difficulty = input("Enter previous difficulty (easy/medium/hard): ").strip().lower()
        if prev_difficulty not in ["easy", "medium", "hard"]:
            print("Invalid previous difficulty. Defaulting to 'medium'.")
            prev_difficulty = "medium"

        next_diff = get_next_difficulty(scores, prev_difficulty)

        result = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "scores": scores,
            "previous_difficulty": prev_difficulty,
            "next_difficulty": next_diff
        }

        # prints to the consoel
        print(result)

        #add the data to the log file.
        try:
            with open(LOG_FILE, "a") as f:
                f.write(json.dumps(result) + "\n")
            print(f"Logged to {LOG_FILE}")
        except Exception as e:
            print(f"Error writing log: {e}")
