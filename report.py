import re
import csv
from collections import defaultdict

# Initialize the dictionaries to store error counts and user statistics
error_counts = defaultdict(int)
user_stats = defaultdict(lambda: {"INFO": 0, "ERROR": 0})

# Open and read the log file
with open("fishy.log", "r") as file:
    log_lines = file.readlines()

# Process each line in the log file
for line in log_lines:
    # Match INFO lines
    info_match = re.search(r"\w+ \d+ \d+:\d+:\d+ \w+\[\d+\]: INFO [\w ]+ \(([\w.]+)\)", line)
    # Match ERROR lines
    error_match = re.search(r"\w+ \d+ \d+:\d+:\d+ \w+\[\d+\]: ERROR ([\w ]+) \(([\w.]+)\)", line)

    if info_match:
        user = info_match.group(1)
        user_stats[user]["INFO"] += 1
    elif error_match:
        error_message = error_match.group(1)
        user = error_match.group(2)
        error_counts[error_message] += 1
        user_stats[user]["ERROR"] += 1

# Sort the error counts by the number of occurrences in descending order
sorted_errors = sorted(error_counts.items(), key=lambda x: x[1], reverse=True)
# Add header for the error counts CSV
sorted_errors.insert(0, ["Error", "Count"])

# Sort the user statistics alphabetically by username
sorted_users = sorted(user_stats.items())
# Add header for the user statistics CSV
sorted_users = [["Username", "INFO", "ERROR"]] + [[user, stats["INFO"], stats["ERROR"]] for user, stats in sorted_users]

# Write the error counts to a CSV file
with open("error_message.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sorted_errors)

# Write the user statistics to a CSV file
with open("user_statistics.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sorted_users)

# Debug: Print processed results
print("Error Counts:")
print(sorted_errors)
print("\nUser Statistics:")
print(sorted_users)
