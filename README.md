# Some Algorithms
=================

This simple program requires Python. 

## Start

To start, clone the program locally,

~~~~~~~~
$ git clone https://github.com/rshoger/alg-p2.git
~~~~~~~~

## Run

Execute this program from the command-line,

~~~~~~~~
$ python main.py <filename>
~~~~~~~~

or see `python main.py --help` for instructions.

## Virtualize

If you have trouble with python or installing python, please use Vagrant to
create a virtual-machine with a python environment pre-configured.

From your host boot and connect to the virtual-machine,

~~~~~~~~
$ vagrant up && vagrant ssh
~~~~~~~~

after connecting, switch to the project directory.

~~~~~~~~
$ cd /vagrant
~~~~~~~~

The project can be run as described in the ***Run*** section above.
