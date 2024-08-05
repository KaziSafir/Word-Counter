# Word-Counter
MapReduce job to count word frequencies in a text file using the 'MRJob' library
# Part 1: Library Imports

MRJob and MRStep: Used for defining and running MapReduce jobs.

Regular Expressions: Utilized to identify words in the text.

# Part 2: Word Extraction

Regular Expression Setup: Defines a pattern to find words in text.

# Part 3: Class Definition

MRWordCounter:  A class that extends MRJob to define a MapReduce job.

# Part 4: MapReduce Steps

Steps Method: Defines the sequence of MapReduce steps:

First Step: Extracts words and counts occurrences.

Second Step: Formats counts and outputs the results.

# Part 5: Mapper Functions

Word Extraction Mapper: Extracts words from lines of text and associates each word with a count of 1.

Count Formatting Mapper: Formats word counts as zero-padded numbers for sorting.

# Part 6: Reducer Functions

Count Reducer: Aggregates counts for each word to get the total occurrences.

Output Reducer: Outputs the final results, sorting by formatted counts.

# Part 7: Execution

Main Execution: Runs the MapReduce job when the script is executed directly.
