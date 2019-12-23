# formulapy

formulapy is a Python application that will let you get results and informations about each years, and each races of the Formula 1 Championship.

This application is based on the Ergast API ([https://ergast.com/mrd/])

# installation

To use this application, you will need following Python libraries : 
 - terminaltables

This application should not be run under a Python interpreter, but directly into your CLI.

For example you should run it like this : 
`python formulapy` or `./formulapy`

# using the application

There is quite few parameters that you can use in order to get the desired information : 

- `-y` : Will let you specify a year, if you don't it will take the current year
- `-r` : Let you specify a specific round number (For example the Australian Grand Prix = 1)
- `-d` : Will display the drivers standings. Can be used with year argument
- `-c` : Will display the constructors standings. Can also be used with year argument
