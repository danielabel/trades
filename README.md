# Episode analysis command line tool

This repo contains a demo python command line tool.
 

## How to use 

This is WIP: Currently the app is only operated by running test code.

## Usage Notes
- Assumed date format is dd/mm/YYYY (23/01/2012)
- Will order data by 'Trade Date' and 'Trade Identifier'


## features not yet included
0. No integration test (is one needed?)
1. Verify all trades are all in same currency - or set as an assumption
2. Verify that an episode is complete 
3. Either verify column names exist or Allow important column names to specified
4. Consider use of `NumPy` to do calculations to optimise for large file sets
5. deal with gaps, nulls, nan
6. use better than float for currency

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
