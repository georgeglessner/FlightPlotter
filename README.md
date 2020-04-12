# Flight Plotter

A simple script to create a bar chart of your flight data captured from [MyFlights](https://github.com/georgeglessner/MyFlights). 

Note: Before you run the script you will need to change the URL on [line 4 of the bash script](https://github.com/georgeglessner/FlightPlotter/blob/master/getdata.sh#L4) to match your MyFlights repo. Or, if you are not using a repo to store your flights, simply remove this line completely and modify the following line to point to your `flights` folder. 

## Usage

`pip3 install -r requirements.txt`

`bash plotdata.sh`