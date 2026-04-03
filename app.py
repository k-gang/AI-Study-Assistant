def summarize_notes(text):
    sentences = text.split(".")
    return sentences[:2]

notes = input("Enter your notes: ")

summary = summarize_notes(notes)

print("Summary:")
for line in summary:
    print(line)
