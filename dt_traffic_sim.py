# Simple program to simulate traffic in the Dynatrace UI
# Original purpose being to practice serve detection customization (via API)
# NO requests are actually sent out when this program is run (as designed)

import oneagent


def main():
    all_set, sdk = get_sdk()
    if all_set:
        print("Starting the real work...")


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


if __name__ == '__main__':
    main()