#!/bin/bash
rm -rf data
mkdir data
git clone https://github.com/georgeglessner/MyFlights.git
cd MyFlights/flights/

# Copy all data to data folder
for dir in */; do
	cp $dir/* ../../data
done

# Return to main dir
# remove MyFlights Folder
# Plot data
cd ../..
rm -rf MyFlights
python3 plot.py

