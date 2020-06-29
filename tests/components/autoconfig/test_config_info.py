from homeassistant.components.autoconfig import config_info

if __name__ == "__main__":
    curPath = "d://"
    config_dir = config_info.config_path(curPath, "D://", True)
    print(config_dir)