# Episode analysis command line tool

This repo contains a demo python command line tool to 
calculate the total profit or loss for the Trade Episode
in the file provided.

It's designed to operate over a CSV file that contains trade-data 
in a form matching tha to the file located in the `sample_data` directory. 

## Pre-requisites 
1. [python 3.9](https://www.python.org/downloads/) - (or homebrew or [pyenv](https://github.com/pyenv/pyenv))
2. [pipenv](https://github.com/pypa/pipenv)

## How to use 

Clone the github repo to your local machine, install Python 3.9 and `pipenv`

Run the following commands

`pipenv install` to install the required libraries

and then 

`pipenv run episode` to run the sample file provided. A plot will be produced and saved to `plot.pdf`
   
### options

`pipenv run episode  --file <file to process>` to process a given file

`pipenv run episode  --plot <filename>` to change the name of the plot file output


## Usage Notes
File provided should contain one Trade Episode that: 
 * a UK date format: dd/mm/YYYY (23/01/2012)
 * contains the following columns `Trade Date `, `Trade Identifier`, `Trade Quantity`, `Trade Price`
 * has all trades in the same currency
 * contains mo sparse, missing or badly formatted data

It accepts files that contain unordered trades and will order by 'Trade Date' and 'Trade Identifier'

It calculates the price result to the nearest cent and rounds up from a half-cent 

## features not yet included

1. Verifying column names exist - failing fast
2. Large data sets - Consider direct use of `NumPy` to do calculations to optimise if needed under test.

# Development notes

## Background
I'm an engineer with some previous light use of Python 5-6 years ago. 

I've taken a blank-sheet-of-paper approach and looked to select good up-to-date 
choices. This project represents that learning curve. I've documented my choices
and reasoning below.

I've looked to use technologies and patterns that may not be perfect but are
well enough used to be understood by a more experienced python engineer. 

Feedback is welcome. 

## Testing and changing

To run the tests - execute the following after installing the libraries 

`pipenv run test`

## Design notes
A main consideration of the code structure was what I could and should test.
Asking: What's going to drive the code? What's going to give me good coverage of the 
key behaviours, with a good drivable interface?

My initial approach was to get working functionality in a series of tests, 
with the intention to wrap the combined behaviours either in an integration
test with a light command line wrapper, or a direct test on the command line
if that worked well.

### Currency processing

I've coded to avoid using floats in Currency calculations as floats always go 
wrong somewhere. Apologies if this is overkill or makes the code for this
example harder to parse.  

### Performance

Whilst I've not tested this with large data files, I've assumed a need to
write code with some performance considerations in mind for larger data sets. 

With this in mind I've used `zip` and `reduce` rather than the easier to read
dataframe manipulations.

### Problems not solved / incomplete work 
1. The tests cannot load the source modules without an empty test file in the root directory 
2. Performance needs - I would have liked to have time to see what size files might be expected and tested / benchmarked the routines
3. an acceptance test [pytest can cature stdout](https://docs.pytest.org/en/stable/capture.html) so there is a simple option
4. I've selected to not use objects so so have low encapsulation - validate this approach 

## Technology selection

### Python environment management: `pipenv`. 
   
   `pipenv` looks to be the [recommended way to manage dependencies](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies) in modern Python  
   
### Data loading: `pandas` 
   
I considered `pandas` vs `csv` for csv file loading. 
   `csv` looked to be operating at a lower level without helpful assumptions - great for low level control.
   `pandas` got the job done and gave me options to consider.
      
   With hindsight, `pandas` is a pretty heavy hammer to get done what I needed, 
   and it might distract as much as it helps.

   The tradeoffs at this point seem to be good defaults vs opaque. 
   For example: the loading of files is simple but more complex 
   processing (calculating profit) was a little tricksy. 
   
### Unit testing framework: `pytest`
   
There were a number of options here. I picked what looked to be a 
   simple popular option with low boilerplate.  

### Project directory structure: Python Standard 
   
Following a mix of [the hitchhiker's guide to python](https://docs.python-guide.org/writing/structure/#structure-of-the-repository) 
   and pytest advice. 
