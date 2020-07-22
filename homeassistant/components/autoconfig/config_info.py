""" 自动获取配置文件目录，如果不指定--config则从保存的文件中获取，不存在则使用默认目录（/root/.homeassistant） """
import logging
import os

from homeassistant.util.json import load_json, save_json

_LOGGER = logging.getLogger(__name__)

DOMAIN = "config_info"
CONFIG_NAME = ".config"
CONFIG_PATH = "config_path"


def check_path(curPath: str) -> str:
    file = os.path.join(curPath, CONFIG_NAME)
    config = load_json(file)
    if config:
        return config[CONFIG_PATH]

"""
获取初始化时定义的配置文件目录，如果不存在则创建文件保存并返回配置文件目录。
"""
def config_path(curPath: str, configPath: str, existConfig: bool) -> str:
    file = os.path.join(curPath, CONFIG_NAME)
    config = load_json(file)
    if not config:
        config = content = {CONFIG_PATH: configPath}
        save_json(file, content)
        _LOGGER.info("save config file")
    else:
        if (configPath != config[CONFIG_PATH]) & (not existConfig):
            config[CONFIG_PATH] = configPath
            save_json(file, config)
            _LOGGER.info("update config file")

    _LOGGER.info("config file，config dir is %s", config[CONFIG_PATH])

    if not os.path.isdir(config[CONFIG_PATH]):
        os.makedirs(config[CONFIG_PATH], exist_ok= True)

    return config[CONFIG_PATH]
