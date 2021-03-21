# Episode analysis command line tool

This repo contains a demo python command line tool to 
calculate the total profit or loss for the Trade Episode
in the file provided.

## How to use 

python main.py --file <file to process>

It operates over a CSV file that contains trade-data in a similar form to
that found in the `sample_data` directory. 

## Usage Notes
File provided should contain one Trade Episode that has
- date format of dd/mm/YYYY (23/01/2012)
- contains the following columns `Trade Date `, `Trade Identifier`, `Trade Quantity`, `Trade Price`
- all trades in the same currency
- mo sparse, missing or badly formatted data

It accepts files that contain unordered trades and will order by 'Trade Date' and 'Trade Identifier'


## features not yet included
0. No integration test (is one needed?)
3. Either verify column names exist or Allow important column names to specified
4. Consider use of `NumPy` to do calculations to optimise for large file sets

# Development notes

I'm an engineer with some previous light use of Python 5-6 years ago. 

I've taken a blank-sheet-of-paper approach and looked to select good up-to-date 
choices. This project represents that learning curve. I've documented my choices
and reasoning below.

I've looked to use technologies and patterns that may not be perfect but are
well enough used to be understood by a more experienced python engineer. 

Feedback is welcome. 

## Design notes
A main consideration of the code structure was what I could and should test.
What's going to drive the code? What's going to give me good coverage of the 
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

## Technology selection

### Python environment management: `pipenv`. 
   
   `pipenv` looks to be the [recommended way to manage dependencies](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies) in modern Python  
   
### Data loading: `pandas` 
   
I considered `pandas` vs `csv` for csv file loading. 
   `csv` looked to be operating at a lower level without helpful assumptions - great for low level control.
   `pandas` got the job done and gave me options to consider.
      
   With hindsight, `pandas` is a pretty heavy hammer to get done what I needed, 
   and it might distract as much as it helps. 
   
### Testing framework: `pytest`
   
There were a number of options here. I picked what looked to be a 
   simple popular option with low boilerplate.  

### Project directory structure: Python Standard 
   
Following a mix of [the hitchhiker's guide to python](https://docs.python-guide.org/writing/structure/#structure-of-the-repository) 
   and pytest advice. 
