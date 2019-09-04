# dt-traffic-sim
This is a program to simulate transactions within Dynatrace for the purposes of practicing configurations. The initial goal of this is for practicing the use of the [service detection API](https://www.dynatrace.com/support/help/extend-dynatrace/dynatrace-api/configuration-api/service-api/detection-rules/).

## What is required?
This needs to be run on a Linux or Windows box with Python 3.X and an installed and running OneAgent. You will be warned and the program will exit if none is detected. You also need to have the oneagent sdk module installed and the rest of the requirements in requirements.txt.

If you are not a Dynatrace employee you can request a [developer instance](https://www.dynatrace.com/developer/trial/) of Dynatrace.

## What happens when it runs?
The program will go through the provided yaml configuration file and simulate the requests specified. See sample-config.yaml for the config file format. Simulating only involves telling Dynatrace that the given requests were made but there are no requests actually ever made! This means that you can simulate and type of request you would be interested in testing for configuration purposes. Unless there is a monitored process that Dynatrace detects as being related to the targets you specify they will show up as external requests in Dynatrace.

## Usage
`py dt_traffic_sim.py -f <config.yaml>`

## Anything next?
Only near term plans are to add the option to simulate web service requests.
