from os.path import splitext
from timeit import timeit
import argparse

## Parse arguments ##
parser = argparse.ArgumentParser(description='Test some algorithms.')
parser.add_argument('filename', type=str, nargs='?', default='Amount.txt',
                    help='The name of the file to process')

args = parser.parse_args()

## Algorithm functions ##
# Slow change algorithm
def changeslow(amounts):
    pass

# Greedy algorithm
def changegreedy(amounts):
    pass

# Dynamic programming algorithm
def changedp(amounts):
    pass

## Test class ##
class some_test:
    def __init__(self, input_filename):
        # Store a set of sets
        self.sets = []

        # File-names
        input_filename = input_filename
        output_filename = splitext(input_filename)[0] + 'change.txt'
        time_results_filename = 'timing_results.txt'

        # Open files for writing and store handles
        self.output_file = open(output_filename, 'w')
        self.time_results_file = open(time_results_filename, 'w')

    def __del__(self):
        print('\nClosing file handles...')
        self.output_file.close()
        self.time_results_file.close()

    def test_sets(self, f):
        if not self.sets:
            self.sets.append([1,2,3,4])

        self.time_results_file.write(f.__name__ + '\n')

        for i in self.sets:
            # Call the function on the set
            print('Calling ' + f.__name__ + '...')
            self.test_algorithm(f, i)

            # Perform timing
            t = self.time_algorithm(f, i)

            # Print results to stdout
            print('time: ' + str(t) + ' seconds')

            # Write results to file
            self.time_results_file.write(str(t)+'\n')

    def test_algorithm(self, f, s=[1,2,3,4]):
        # Call the function and test the set
        return f(s)

    def time_algorithm(self, f, s=[1,2,3,4], number=1):
        # Print timing event information
        return timeit(lambda:f(s), number=number)

## Program entry point ##
if __name__ == '__main__':
    # Create a tester 't'
    t = some_test(args.filename)

    # Call each algorithm individually for testing and timing
    t.test_sets(changeslow)
    t.test_sets(changegreedy)
    t.test_sets(changedp)
