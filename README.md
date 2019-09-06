# dt-traffic-sim
Dynatrace is a powerful APM tool that can be customized quite a bit to map to your application and organization more accurately. One challenge with all of these possible configurations is that it can be difficult or undesirable to test these configurations on "real" data. 

This is a program to simulate transactions within Dynatrace for the purposes of practicing configurations. The initial goal of this is for practicing the use of the [service detection API](https://www.dynatrace.com/support/help/extend-dynatrace/dynatrace-api/configuration-api/service-api/detection-rules/).

## What is required?
This needs to be run on a Linux or Windows box with Python 3.X and an installed and running OneAgent. You will be warned and the program will exit if none is detected. You also need to have the oneagent sdk module installed and the rest of the requirements in requirements.txt.

`pip install -r requirements.txt`

If you are not a Dynatrace employee you can request a [developer instance](https://www.dynatrace.com/developer/trial/) of Dynatrace. Employees should follow our internal procedures.

## What happens when it runs?
Once installed you run the python program and supply a YAML configuration file (see sample-config.yaml) which specifies what requests you would like to simulate. When run the program will go through your config file and simulate the requests so that they will show up within the Dynatrace UI.

You can make the Dynatrace configuration changes (e.g. service detection rules) and then run the program again to see how your rules will work on real traffic without waiting.

![Requests in UI](/images/example-in-ui.png)

## How does it work?
When run it makes use of the [OneAgent SDK for python](https://github.com/Dynatrace/OneAgent-SDK-for-Python) and for all of the desired requests reports to OneAgent and Dynatrace that the given requests have been made even though **no requests ever actually leave the program**.

See [here](https://github.com/Dynatrace/OneAgent-SDK-for-Python) to get an idea of how this works. Basically we are 'timing' nothing.

## Usage
`py dt_traffic_sim.py -f <config.yaml>`

## Anything next?
Only near term plans are to add the option to simulate web service requests.
