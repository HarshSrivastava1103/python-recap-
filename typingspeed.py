import time

# Sentence to type
sentence = "Python programming is fun and helps you build amazing projects."

print("===== Typing Speed Test =====")
print("\nType the following sentence exactly as shown:\n")
print(sentence)

input("\nPress Enter when you are ready...")

# Start timer
start_time = time.time()

# User input
typed_text = input("\nStart typing:\n")

# Stop timer
end_time = time.time()

# Calculate time taken
time_taken = end_time - start_time

# Calculate WPM
word_count = len(typed_text.split())
minutes = time_taken / 60
wpm = word_count / minutes if minutes > 0 else 0

# Calculate Accuracy
correct_characters = 0

for i in range(min(len(sentence), len(typed_text))):
    if sentence[i] == typed_text[i]:
        correct_characters += 1

accuracy = (correct_characters / len(sentence)) * 100

# Display Results
print("\n===== Results =====")
print("Time Taken: {:.2f} seconds".format(time_taken))
print("Words Typed:", word_count)
print("Typing Speed: {:.2f} WPM".format(wpm))
print("Accuracy: {:.2f}%".format(accuracy))

# Feedback
if wpm >= 60:
    print("Excellent! You are a fast typist.")
elif wpm >= 40:
    print("Good job! Keep practicing.")
else:
    print("Practice more to improve your typing speed.")