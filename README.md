# endpoint
Endpoint - Backend Coding Challenge: Directory Tree


This is a solution to Endpoint's Backend Coding Challenge - Directory Tree. There is a **directory.py** file within the classes module that implements the directory file system within a single system scope. An instantiated object of this class will represent a single file system within a single system scope; differing objects of this class will not have access to respective object's directories/files. 

## how to run
In order to run this program, commands must be put into an input file **with all command keywords CAPITALIZED** and the subsequent arguments following the command keyword. There should be no trailing leading or trailing '/' for any arguments and separate commands must be separated by a newline in order for them to be parsed correctly. An example of a valid input syntax:

```
CREATE nba
CREATE nba/lakers
CREATE nba/celtics/jayson_tatum
CREATE nba/mavericks/luka_doncic
MOVE nba/mavericks/luka_doncic nba/lakers
LIST
CREATE nba/bulls/michael_jordan
DELETE nba/bulls/michael_jordan
```

An example of invalid input syntax:
```
CREATE /nba/heat                                    (INVALID because of leading '/')
MOVE nba/cavaliers/lebron/james/ nba/heat           (INVALID because of trailing '/)
DELETE
nba/nuggets/dikembe/mutombo                         (INVALID because command + arguments not on sameline)
CREATE nba/supersonics DELETE nba/supersonics       (INVALID because multiple commands on sameline)
```

Invalid input syntax will lead to incorrect behavior of command parsing. An example input file is included at `test/example.txt`


Once input file is created with correct syntax, in order to run the program, navigate to the main directory of this program and  execute the following command:
```
python3 main.py PATH/TO/INPUT/FILE1 
```
The program can be run with multiple input files:
```
python3 main.py PATH/TO/INPUT/FILE1 PATH/TO/INPUT/FILE2 ......
```
Instances of `PATH/TO/INPUT/FILE` should be replaced with actual paths to input files. Output will be printed to stdout. 
