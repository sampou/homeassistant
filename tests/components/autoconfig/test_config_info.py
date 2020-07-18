from homeassistant.components.autoconfig import config_info

def config_path_test() -> None:
    curPath = "d://"
    config_dir = config_info.config_path(curPath, "D://", True)
    print(config_dir)


def main_start() -> None:
    sys.argv[0] = '--runner'
    sys.exit(hass_entry.main())


if __name__ == "__main__":
    config_path_test()
    # main_start()