import oneagent
import time

if not oneagent.initialize():
    print('Error initializing OneAgent SDK.')

with oneagent.get_sdk().trace_outgoing_web_request("http://aol.com", "POST",headers=None):
    time.sleep(2)
    pass

print('It may take a few moments before the path appears in the UI.')
input('Please wait...')
oneagent.shutdown()