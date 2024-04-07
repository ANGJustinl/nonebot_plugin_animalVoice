from . import animalvoice_main, cheru_main
from nonebot.plugin import PluginMetadata

from .config import plugin_config as Config

Config.customize_cmd_animalconvert

__plugin_meta__ = PluginMetadata(
    name="兽语译者插件",
    description="加密/解密 一句话/图片 为兽语/切噜语",
    usage="发送 /译者帮助 获取帮助",
    homepage="https://github.com/ANGJustinl/nonebot_plugin_animalVoice",
    supported_adapters={"~onebot.v11"},
    type="application",
    config=Config,
    extra={
        "menu_data": [
            {
                "func": "兽音加密",
                "trigger_method": "on_cmd",
                "trigger_condition": "/" + Config.customize_cmd_animalconvert,
                "brief_des": "将 文字/图片 加密为 兽语",
                "detail_des": "发送命令激活后再发送要加密内容",
            },
            {
                "func": "切噜一下加密",
                "trigger_method": "on_cmd",
                "trigger_condition": "/" + Config.customize_cmd_cherulizing,
                "brief_des": "将 文字/图片 加密为 切噜语",
                "detail_des": "发送命令激活后再发送要加密内容",
            },
            {
                "func": "兽音解密",
                "trigger_method": "on_cmd",
                "trigger_condition": "/" + Config.customize_cmd_animaldeconvert,
                "brief_des": "将 兽语 解密",
                "detail_des": "发送命令激活后再发送要解密内容",
            },
            {
                "func": "切噜～解密",
                "trigger_method": "on_cmd",
                "trigger_condition": "/" + Config.customize_cmd_decherulizing,
                "brief_des": "将 切噜～语 解密",
                "detail_des": "发送命令激活后再发送要解密内容",
            },
        ],
        "menu_template": "default",
    },
)
