from pydantic import Extra, BaseModel

from nonebot import get_plugin_config


class Config(BaseModel, extra=Extra.ignore, arbitrary_types_allowed=True):
    customize_cmd_animalconvert: str = "兽音加密"
    customize_cmd_animaldeconvert: str = "兽音解密"
    customize_cmd_cherulizing: str = "切噜一下"
    customize_cmd_decherulizing: str = "切噜～"
    at_sender: bool = True


plugin_config = get_plugin_config(Config)
