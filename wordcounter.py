# Import necessary libraries
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

# Regular expression to find words
RE_WORD = re.compile(r"[\w']+")

# Define the MRWordCounter class inheriting from MRJob
class MRWordCounter(MRJob):

    # Define MapReduce steps
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   reducer=self.reducer_count_words),
            MRStep(mapper=self.mapper_counts,
                   reducer=self.reducer_output)
        ]

    # Mapper function to extract words and yield (word, 1) pairs
    def mapper_get_words(self, _, line):
        words = RE_WORD.findall(line)  # Find all words in the line
        for word in words:
            yield word.lower(), 1  # Yield word in lowercase with count 1

    # Reducer function to count occurrences of each word
    def reducer_count_words(self, word, values):
        yield word, sum(values)  # Yield word with total count

    # Mapper function to format counts as zero-padded numbers
    def mapper_counts(self, word, count):
        yield "%05d" % int(count), word  # Yield count formatted with leading zeros

    # Reducer function to output the results
    def reducer_output(self, count, words):
        for word in words:
            yield count, word  # Yield count and corresponding words

# Run the MRWordCounter job if the script is executed directly
if __name__ == '__main__':
    MRWordCounter.run()
