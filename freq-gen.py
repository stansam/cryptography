import matplotlib.pyplot as plt
from collections import Counter

def plot_letter_frequency(input_string):
    # Convert the string to lowercase and remove non-alphabetic characters
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalpha())

    # Count the frequency of each letter
    letter_counts = Counter(cleaned_string)

    # Extract letters and corresponding counts
    letters, counts = zip(*letter_counts.items())

    # Plot the bar chart
    plt.bar(letters, counts, color='skyblue')
    plt.xlabel('Letters')
    plt.ylabel('Frequency')
    plt.title('Letter Frequency in the Given String')
    plt.show()

# Example usage:
user_input = input("Enter a string: ")
plot_letter_frequency(user_input)
