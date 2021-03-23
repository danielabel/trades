# Episode analysis command line tool

This repo contains a demo python command line tool to 
calculate the final balance (profit or loss) for a Trade Episode.

It's designed to operate over a CSV file that contains trade data 
in a form matching that in the file located in the `sample_data` directory.

As well as reporting the final balance of the episode it also produces a plot 
of the trades as a PDF.

## Pre-requisites 
1. [python 3.9](https://www.python.org/downloads/) - (supports [pyenv](https://github.com/pyenv/pyenv))
2. [pipenv](https://github.com/pypa/pipenv)

## How to use 

Clone the github repo to your local machine, install Python 3.9 and `pipenv`

Run the following commands

`pipenv sync` to install the required libraries 

and then 

`pipenv run episode` to run using the sample file provided. 

A plot will be produced and saved to `plot.pdf`
   
### options

 - `--file <file to process>` to process a given file

 - `--plot <filename>` to change the name of the plot file output

example: `pipenv run episode --file data.csv --plot my-graph.pfd`  

## Usage Notes
File provided should contain a single Trade Episode that: 
 * as a csv file that contains the following columns `Trade Date`, `Trade Identifier`, `Trade Quantity`, `Trade Price` 
 * `Trade Date` should use a UK date format: dd/mm/YYYY (23/01/2012)
 * all trades should be in the same currency
 * contains mo sparse, missing or badly formatted data

It accepts files that contain unordered trades and will order by 'Trade Date' and  then 'Trade Identifier'

It calculates the balance to the nearest cent and rounds up by a half-cent 

## features not yet included

1. Large data set handling - the command is untested with larger data sets
2. Error handling - reporting should be sufficient for many cases but is basic 

# Development notes

## Test automation

To run the tests - execute the following 

```
pipenv sync -d

pipenv run test
```

## Background
The author is an engineer with some previous light use of Python, 5-6 years ago. 
This project represents a learning curve of picking up Python.

This code project takes a blank-sheet-of-paper approach and looks to 
select some good enough, up-to-date python technology choices. 
The choices are documented below. 

Feedback is welcome. 

## Design notes

### Currency processing
I've coded to avoid using floats in Currency calculations as floats always go 
wrong somewhere. Apologies if this is overkill, or makes the code for this
example harder to parse. I have a feeling there's probably a neater more 
'pythonic' way to do this. 

### Performance
Whilst I've not tested this with large data files, I've assumed a need to
write code with some performance considerations in mind for larger data sets. 

With this in mind I've used `zip` and `reduce` rather than the easier to read
dataframe manipulations.

### Code structure
I was interested in exploring a module (Node.js) vs class (Java) approach to 
code style and if there was a need for encapsulation.  This is reflected in the final code. 

I am not certain I've built a python-istic file structure. 
`EpisodeApp` might be better as a Package rather than a class, but my feeling is
that what I have is good enough at this scale. Feedback very welcome here. 

### Problems not solved / incomplete work 
1. The tests cannot load the source modules without an empty test file in the root directory 
2. Performance needs - I would have liked to have time to see what size files might be expected and tested / benchmarked the routines and maybe looked into direct use of `NumPy` to do calculations to optimise if needed under test.
3. More mature (and tested) exception handling

## Technology selection

### Python environment management: `pipenv`. 
   
   `pipenv` looks to be the [recommended way to manage dependencies](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies) in modern Python  
   
### Data loading: `pandas` 
   
I considered `pandas` vs `csv` for csv file loading. 

`csv` looked to be operating at a lower level - great for low level control, but 
required a lot of control to have it working usefully and flexibly.
`pandas` looked o get the job of loading in and manipulating CSV files 
at a high level of abstraction and helped get stuff done.

`pandas` is a pretty heavy hammer to do what was needed, but I gained a lot
of good defaults and probably produced a more flexible tool.

### Data loading: also `pandas`

Having made the choice of `pandas` for loading the data it seemed reasonable to
also use this as a default for rendering a plot of the episode. 
There are a lot of wonderful plotting and graphing tools in the Python world, and
it would be great to explore them further, but as an addition to this sample 
project, they felt like overkill.

### Unit testing framework: `pytest`
   
There were a number of options here. I picked what looked to be a 
   simple popular option with low boilerplate.  

### Project directory structure: Python Standard 
   
I worked to follow a mix of [the hitchhiker's guide to python](https://docs.python-guide.org/writing/structure/#structure-of-the-repository) 
   and pytest advice.  
