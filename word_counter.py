import sys
import pandas as pd


class WordCounter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = self.read_data()

    def read_data(self):
        data = pd.read_csv(self.file_path)
        return data['INCIDENTNEIGHBORHOOD'].value_counts()

    def calculate_probability_of_most_frequent_word(self):
        total_occurrences = sum(self.words)
        most_frequent_word = self.words.idxmax()
        most_frequent_count = self.words.max()
        probability = most_frequent_count / total_occurrences
        print(f"The most frequent word in the column is {most_frequent_word}")
        print(f"and the probability for its presence is {probability}")
        print(f"All words and their frequencies: \n{self.words.to_dict()}")

    # Your existing methods


if __name__ == "__main__":
    # File name handling, defaulting to 'data.csv'
    file_name = sys.argv[1] if len(sys.argv) > 1 else './data/data.csv'
    obj = WordCounter(file_name)
    obj.calculate_probability_of_most_frequent_word()
