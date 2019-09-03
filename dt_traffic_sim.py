# Simple program to simulate traffic in the Dynatrace UI
# Original purpose being to practice serve detection customization (via API)
# NO requests are actually sent out when this program is run (as designed)

import oneagent
import yaml
import time

CONFIG_FILE = "config.yaml"
WEB_REQUESTS = "webRequests"
URL = "url"
COUNT = "count"
METHOD = "method"


def main():
    all_set, sdk = get_sdk()  # returns a boolean and the sdk if successful
    if all_set:
        config = get_config(CONFIG_FILE)  # access value like: config["webRequests"][0]["url"]
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
            # TODO add some randomness to the duration
            pass
        completed_count += 1


if __name__ == '__main__':
    main()