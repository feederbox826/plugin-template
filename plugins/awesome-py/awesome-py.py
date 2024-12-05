import stashapi.log as log
import json
import sys
from stashapi.stashapp import StashInterface

json_input = json.loads(sys.stdin.read())
FRAGMENT_SERVER = json_input["server_connection"]
stash = StashInterface(FRAGMENT_SERVER)

def test():
    log.info("Testing awesome-py plugin")
    log.error("This is an error message")
    log.warning("This is a warning message")
    log.info("This is an info message")
    log.debug("This is a debug message")
    log.trace("This is a trace message")

if 'mode' in json_input['args']:
    PLUGIN_ARGS = json_input['args']["mode"]
    if 'test' in PLUGIN_ARGS:
        test()