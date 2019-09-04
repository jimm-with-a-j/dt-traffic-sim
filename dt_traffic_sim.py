# Simple program to simulate traffic in the Dynatrace UI
# Original purpose being to practice service detection customization (via API)
# NO requests are actually sent out when this program is run (as designed)

import oneagent
import yaml
import time
import argparse

# YAML properties
WEB_REQUESTS = "webRequests"
URL = "url"
COUNT = "count"
METHOD = "method"


def main():

    args = return_args()  # args specified in configure_arg_parser() function
    config_file = args.config_file

    all_set, sdk = get_sdk()  # returns a boolean if init went well and the sdk if successful
    if all_set:
        config = get_config(config_file)  # access value like: config["webRequests"][0]["url"]
        print("Beginning traffic simulation...")

        completed_counter = 0  # used in loop
        while completed_counter < len(config[WEB_REQUESTS]):
            simulate_requests(config[WEB_REQUESTS][completed_counter][URL],
                              config[WEB_REQUESTS][completed_counter][METHOD],
                              config[WEB_REQUESTS][completed_counter][COUNT],
                              sdk)
            completed_counter += 1

        time.sleep(8)
        oneagent.shutdown()


def get_sdk():
    oneagent.initialize()
    sdk = oneagent.get_sdk()

    if sdk.agent_state == 0:
        print("OneAgent initialized...")
        all_set = True
    else:
        print("OneAgent initialization failed...")
        print("Check that OneAgent is running...")
        all_set = False
    return all_set, sdk


def get_config(yaml_config_file):
    with open(yaml_config_file) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
        return config


def simulate_requests(target, http_method, count, one_agent_sdk):
    completed_count = 0
    while completed_count < count:
        with one_agent_sdk.trace_outgoing_web_request(target, http_method, headers=None):
            # this is where the real request would go if we weren't just simulating traffic
            pass
        completed_count += 1


def return_args():
    configured_arg_parser = configure_arg_parser()
    return configured_arg_parser.parse_args()


def configure_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file",
                        help="use the specified config file",
                        action="store", dest="config_file",
                        required=True)
    return parser


if __name__ == '__main__':
    main()
