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


def main():
    all_set, sdk = get_sdk()
    if all_set:
        config = get_config(CONFIG_FILE)  # print(config["webRequests"][0]["url"])
        print("Beginning traffic simulation...")
        simulate_requests("http://example1.com/", "POST", 3, sdk)

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
        with one_agent_sdk.trace_outgoing_web_request(target, http_method, headers=None) as outcall:
            pass
        completed_count += 1


if __name__ == '__main__':
    main()