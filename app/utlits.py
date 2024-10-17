import argparse

## Setup AppConfig
parser = argparse.ArgumentParser(description="Python application")
parser.add_argument('-d', action='store_true', default=False)
parser.add_argument('-t', action='store_true', default=False)
parser.add_argument('-w', action='store_true', default=False)
parser.add_argument('-pc', action='store_true', default=False)
args = parser.parse_args()
DEBUG = args.d
TEST = args.t
WINDOWS = args.w
PROD_CONTAINER = args.pc
AppConfig = { "debug": DEBUG, "is_windows": WINDOWS, "is_test": TEST , "update_twitter_settings": False, "scheduler_offset": 1,"PROD_CONTAINER": PROD_CONTAINER}
