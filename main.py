import argparse

from os.path import splitext
from timeit import timeit
from itertools import izip_longest as zip2

## Parse arguments ##
parser = argparse.ArgumentParser(description='Test some algorithms.')
parser.add_argument('filename', type=str, nargs='?', default='Amount.txt',
                    help='The name of the file to process')

args = parser.parse_args()

## Algorithm functions ##
# Slow change algorithm
def changeslow(amounts):
    return 0

# Greedy algorithm
def changegreedy(amounts):
    return 0

# Dynamic programming algorithm
def changedp(amounts):
    return 0

## Test class ##
class some_test:
    def __init__(self, input_filename):
        self.sets = []
        self.process_input(input_filename)

        # File-names
        output_filename = splitext(input_filename)[0] + 'change.txt'
        time_results_filename = 'timing_results.txt'

        # Open files for writing and store handles
        self.output_file = open(output_filename, 'w')
        self.time_results_file = open(time_results_filename, 'w')

    def __del__(self):
        print('\nClosing file handles...')
        self.output_file.close()
        self.time_results_file.close()

    def process_input(self, filename):
        with open(filename, 'r') as f:
            # Unzip the file into two sets
            z_1, z_2 = zip2(*zip(f,f))

            # Create the test set
            for i, l in enumerate(z_1):
                self.sets.append([l.replace('\n',''), z_2[i].replace('\n','')])

    def test_sets(self, f):
        if not self.sets:
            self.sets.append([1,2,3,4])

        self.time_results_file.write(f.__name__ + '\n')

        for i in self.sets:
            # Call the function on the set
            print('\nCalling ' + f.__name__ + '...\n--------\n Change: ' 
                  + i[0] + '\n Amount: ' + i[1])

            # Run and store results for algorithm
            r = self.test_algorithm(f, i[0])

            # Write to stdout and file handle
            print(' Returned: ' + str(r))
            self.output_file.write(i[0] + '\n' + str(r) + '\n')

            # Perform timing
            t = self.time_algorithm(f, i[0])

            # Print results to stdout and file handle
            print('\n Time: ' + str(t) + ' seconds')
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
