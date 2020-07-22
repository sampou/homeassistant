from homeassistant.components.autoconfig import config_info
from homeassistant import __main__ as hass_entry
import sys

def config_path_test() -> None:
    curPath = "d://"
    config_dir = config_info.config_path(curPath, "D://xxx1/xx", False)
    print(config_dir)


def main_start() -> None:
    sys.argv[0] = '--runner'
    # sys.argv[1] = '--config=D://scs/sxs'
    sys.exit(hass_entry.main())


if __name__ == "__main__":
    config_path_test()
    # main_start()