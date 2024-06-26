from nonebot import on_command
from nonebot.params import Arg
from nonebot.adapters.onebot.v11 import MessageEvent, Message, Bot
from nonebot.typing import T_State

from .config import plugin_config as Config
from .AnimalVoice.converter import msg_convert, msg_deconvert

convert = on_command(
    Config.customize_cmd_animalconvert,
    aliases={"animalvoice", "convert"},
    priority=5,
    block=True,
)
deconvert = on_command(
    Config.customize_cmd_animaldeconvert,
    aliases={"deanimalvoice", "deconvert"},
    priority=5,
    block=True,
)
help = on_command(
    "译者帮助",
    priority=5,
    block=True,
)
if_at_sender = Config.at_sender


@convert.handle()
async def _(state: T_State):
    return


# 这里用got是因为必须单独消息发送否则容易乱
@convert.got("msg", prompt="请发送加密前文字")
async def get_image(state: T_State, msgs: Message = Arg()):
    msg_input = msgs
    if not str:
        await convert.send("不是文字啊", at_sender=if_at_sender)
        msg_input = str(msg_input)
    state["msg"] = msg_input


@convert.handle()
async def _(bot: Bot, state: T_State, event: MessageEvent):
    msg_input = str(state["msg"][0])
    try:
        msg = msg_convert(msg_input)
    except Exception as e:
        await convert.finish("寄，加密失败了，报错为{}".format(e), reply_message=True)

    msgs = []
    msgs.append(
        {
            "type": "node",
            "data": {
                "name": "兽音译者bot",
                "uin": bot.self_id,
                "content": "加密结果\n{}".format(msg),
            },
        }
    )
    await bot.call_api("send_group_forward_msg", group_id=event.group_id, messages=msgs)
    await convert.finish()


@deconvert.handle()
async def _(state: T_State):
    return


# 这里用got是因为必须单独消息发送否则容易乱
@deconvert.got("msg", prompt="请发送需要解密的文字")
async def get_image(state: T_State, msgs: Message = Arg()):
    msg_input = msgs
    if not str:
        await deconvert.send("不是文字啊", at_sender=if_at_sender)
        msg_input = str(msg_input)
    state["msg"] = msg_input


@deconvert.handle()
async def _(bot: Bot, state: T_State, event: MessageEvent):
    msg_input = str(state["msg"][0])
    try:
        msg = msg_deconvert(msg_input)
    except Exception as e:
        await deconvert.finish("寄，解密失败了，报错为{}".format(e), reply_message=True)

    msgs = []
    msgs.append(
        {
            "type": "node",
            "data": {
                "name": "兽音译者bot",
                "uin": bot.self_id,
                "content": "解密结果\n{}".format(msg),
            },
        }
    )
    await bot.call_api("send_group_forward_msg", group_id=event.group_id, messages=msgs)
    await deconvert.finish()


@help.handle()
async def _(bot: Bot, event: MessageEvent):
    msgs = []
    msgs.append(
        {
            "type": "node",
            "data": {
                "name": "译者bot",
                "uin": bot.self_id,
                "content": "指令如下"
                + "\n兽音加密 /"
                + Config.customize_cmd_animalconvert
                + "\n兽音解密 /"
                + Config.customize_cmd_animaldeconvert
                + "\n切噜一下加密 /"
                + Config.customize_cmd_cherulizing
                + "\n切噜～解密 /"
                + Config.customize_cmd_decherulizing,
            },
        }
    )
    await bot.call_api("send_group_forward_msg", group_id=event.group_id, messages=msgs)
    await help.finish()
