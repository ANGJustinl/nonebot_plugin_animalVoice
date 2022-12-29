<div align="center">
  
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>


# nonebot_plugin_animalVoice
  
_✨Nonebot兽语译者插件✨_

---
  
<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/ANGJustinl/nonebot_plugin_animalVoice" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot_plugin_animalVoice">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_animalVoice.svg" alt="pypi">
</a>
<a href="https://www.python.org">
    <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="python">
</a>

---  
 </div> 
  
## 💿 安装

### 1. nb-cli安装（推荐）
bot根目录下打开命令行，执行nb命令安装插件，插件配置会自动添加至配置文件 
 
```
nb plugin install nonebot_plugin_face2cartoonpic
```

### 2. pip安装

```
pip install nonebot_plugin_face2cartoonpic --upgrade

```  

打开 nonebot2 项目的 ```bot.py``` 文件, 在其中写入  
```nonebot.load_plugin('nonebot_plugin_animalVoice')```  
  
或在bot路径```pyproject.toml```的```[tool.nonebot]```的```plugins```中添加```nonebot_plugin_animalVoice```即可  
pyproject.toml配置例如： 

``` 

[tool.nonebot]
plugin_dirs = ["src/plugins"]
plugins = ["nonebot_plugin_animalVoice","xxxxx"]

```
  


## 🎉 使用
### 指令表
| 指令 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|
| [兽音加密]/[convert] | 否 | 群聊/私聊 | 发送需要加密的文字 |
| [兽音解密]/[deconvert] | 否 | 群聊/私聊 | 发送需要解密的文字 |
| [切噜一下]/[cherulize] | 否 | 群聊/私聊 | 发送需要解密的文字 |
| [切噜～]/[decherulize] | 否 | 群聊/私聊 | 发送需要解密的文字 |


**注意**

默认情况下, 您应该在指令前加上命令前缀, 通常是 /


### 🧡特别感谢 

HoshinoBot: https://github.com/Ice-Cirno/HoshinoBot 提供了切噜切噜的算法
