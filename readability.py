from cs50 import get_string

text = get_string("Text: ")
strlength = len(text)
letters = 0
words = 1
sentences = 0

for i in range (strlength):
    j = 0
    if text[i].isalpha():
        j = 1
    letters = letters + j
    k = 0
    if text[i - 1] == " ":
        k = 1
    words = words + k;
    y = 0

    if text[i] == '.' or text[i] == '!' or text[i] == "?":
        y = 1
    sentences = sentences + y;

L = float(letters) / float(words) * 100
S = float(sentences) / float(words) * 100

index = 0.0588 * L - 0.296 * S - 15.8
if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print("Grade " + str(round(index)))
