# Readability
The project guidelines were provided by Harvard CS50x

This program computes the approximate grade level needed to comprehend some text

The program first asks the user to type in some text, and then outputs the grade level for the text, according to the Coleman-Liau formula
The Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.
Uses get_string from the CS50 Library to get the user’s input, and prints to output the answer.
The program counts the number of letters, words, and sentences in the text. Assumed that a letter is any lowercase character from a to z or any uppercase character from A to Z, any sequence of characters separated by spaces counts as a word, and any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.
The program prints as output "Grade X" where X is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.
If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), the program outputs "Grade 16+" instead of giving the exact index number. If the index number is less than 1, the program outputs "Before Grade 1"
