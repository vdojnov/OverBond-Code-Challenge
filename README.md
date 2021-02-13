# OverBond Coding Challenge

## Getting Started

This program was written in Python 3.7.8 as part of the interview process with OverBond for the Full Stack Engineer Position.

The program takes a CSV file as a parameter in the CLI. There are two programs you can run ```challenge_one.py``` and ```challenge_two.py``` corresponding to the coding challenge criteria.

There are no necessary requirements to install, and so a ```requirements.txt``` file is not included.

## Challenge One

The challenge was to find a government bond benchmark (closest terms) for each corporate bond, the find the spread (corporate bond yield - government bond yield). 

1. Open the terminal on your computer and ```cd``` into the submission folder containing the code.

2. To run the ```challenge_one.py``` program you need to pass in a csv file in the command line like so. There is a sample csv file ```sample_input.csv``` in the submission directory.

```Shell
python challenge_one.py sample_input.csv
```

3. The program will run and will create a ```output_challenge_one.csv``` file in the submission directory. If the ```output_challenge_one.csv``` already exists in this directory it will be overwritten.

### Sample input

| bond   | type       | term        | yield |
|--------|------------|-------------|-------|
| C1     | corporate  | 10.3 years  | 5.30% |
| G1     | government | 9.4 years   | 3.70% |
| G2     | government | 12 years    | 4.80% |

### Sample output

```csv
bond,benchmark,spread_to_benchmark
C1,G1,1.60%
```

## Challenge Two

This challenge calculates the spread to the government bond curve through linear interpolation.

1. Open the terminal on your computer and ```cd``` into the submission folder containing the code.

2. To run the ```challenge_two.py``` program you need to pass in a csv file in the command line like so. There is a sample csv file ```sample_input.csv``` in the submission directory.

```Shell
python challenge_two.py sample_input.csv
```

3. The program will run and will create a ```output_challenge_two.csv``` file in the submission directory. If the ```output_challenge_two.csv``` already exists in this directory it will be overwritten.

### Sample input

| bond   | type       | term        | yield |
|--------|------------|-------------|-------|
| C1     | corporate  | 10.3 years  | 5.30% |
| C2     | corporate  | 15.2 years  | 8.30% |
| G1     | government | 9.4 years   | 3.70% |
| G2     | government | 12 years    | 4.80% |
| G3     | government | 16.3 years  | 5.50% |

### Sample output

```csv
bond,spread_to_curve
C1,1.22%
C2,2.98%
```

## Testing

There are prewritten automated tests written using Python unittest framework. You can run the test from the terminal:

1. Open the terminal on your computer and ```cd``` into the submission folder containing the code.

2. To run the ```test.py``` program:

```Shell
python test.py
```

3. The program will run and will give you are report in the terminal stating if the tests have passed or failed.


## My approach

My approach was to try to come up with something that could be implemented in the limited amount of time I had to complete this. Rather than going brute force and for each corporate bond checking every single government bond, I decided to split apart my corporate and government bonds and sort by term. Although sorting can be an expensive algorithm, I decided that it would be best to trade of the sorting in the beginning for reduced iterations, ease of access, and calculations later. 

My strategy for both challenge one and challenge two were very similar. Having 2 stored lists one with government bonds and one with corporate bonds, I was able to loop through each corporate bond and keep a cursor on the government bond list. A corporate bond with a higher term than the previous bond's term is never going to be benchmarked with a government bond that has a lower term than the government bond which was previously used to benchmark. Similarly for finding which two government bonds to use to find the trendline for linear interpolation, I just iterate forward, once you pass a government bond while iterating, you dont need to ever look at it again. For both challenges, every time you find a match, you keep the curser and start of the interation for the next coroprate bond, in the position of the previous government bond. I tried to make the algorithm more efficient by minimizing the amount of looping needed, by having the lists sorted, you only loop through each list (corporate/government) once.

Thank you for taking the time to look over my application.

Sincerely,
Viktor Dojnov

