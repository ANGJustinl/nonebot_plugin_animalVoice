from nonebot import on_command
from nonebot.params import Arg
from nonebot.adapters.onebot.v11 import MessageEvent, Message, Bot
from nonebot.typing import T_State

from .config import plugin_config as Config
from .Cheru import cheru2str, str2cheru

cherulizing = on_command(
    Config.customize_cmd_cherulizing, aliases={"cherulize"}, priority=5, block=True
)
decherulizing = on_command(
    Config.customize_cmd_decherulizing, aliases={"decherulize"}, priority=5, block=True
)
if_at_sender = Config.at_sender


@cherulizing.handle()
async def _():
    return


# 这里用got是因为必须单独消息发送否则容易乱
@cherulizing.got("msg", prompt="切噜什么切噜～♪")
async def get_image(bot: Bot, state: T_State, msgs: Message = Arg()):
    msg_input = msgs
    if len(msg_input) > 500:
        await bot.send("切、切噜太长切不动勒切噜噜...", at_sender=if_at_sender)
        return
    state["msg"] = msg_input


@cherulizing.handle()
async def _(bot: Bot, state: T_State, event: MessageEvent):
    msg_input = str(state["msg"][0])
    try:
        msg = str2cheru(msg_input)
    except Exception as e:
        await cherulizing.finish("切、切噜报错切不动勒切噜噜{}".format(e), reply_message=True)

    msgs = []
    msgs.append(
        {
            "type": "node",
            "data": {
                "name": "风间千爱瑠",
                "uin": bot.self_id,
                "content": "切噜～♪\n{}".format(msg),
            },
        }
    )
    await bot.call_api("send_group_forward_msg", group_id=event.group_id, messages=msgs)
    await cherulizing.finish()


@decherulizing.handle()
async def _(state: T_State):
    return


# 这里用got是因为必须单独消息发送否则容易乱
@decherulizing.got("msg", prompt="请发送需要解密的文字")
async def get_image(bot: Bot, state: T_State, msgs: Message = Arg()):
    msg_input = msgs
    if len(msg_input) > 1501:
        await bot.send("切、切噜太长切不动勒切噜噜...", at_sender=if_at_sender)
        return
    state["msg"] = msg_input


@decherulizing.handle()
async def _(bot: Bot, state: T_State, event: MessageEvent):
    msg_input = str(state["msg"][0])
    try:
        msg = "你的的切噜噜是：\n{}".format(cheru2str(msg_input))
    except Exception as e:
        await decherulizing.finish("切、切噜报错切不动勒切噜噜{}".format(e), reply_message=True)

    msgs = []
    msgs.append(
        {
            "type": "node",
            "data": {"name": "风间千爱瑠", "uin": bot.self_id, "content": msg},
        }
    )
    await bot.call_api("send_group_forward_msg", group_id=event.group_id, messages=msgs)
    await decherulizing.finish()
