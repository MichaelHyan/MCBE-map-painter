##MCBE 地图画生成器

###警告！该工具使用mcfunction实现，不支持傻瓜式操作

###使用方式

1.确保已安装我的世界基岩版(Minecraft Bedrock Edition)、Python以及能自定义画布大小的图片处理软件(如PS，可根据自己需要更改)

2.进入游戏，根据场地确定所需地图画尺寸和位置
注：地图画尺寸受最大模拟距离影响，如超出尺寸请分块分别处理

3.使用图片处理软件将图片改为所需尺寸，注意单位使用像素，导出使用png格式，不要导出其他格式后改后缀

4.安装项目目录的mcaddon文件，会自己做资源包的省略这一步

5.安装完成后进入资源包的目录

PC版存储位置
```
%USERPROFILE%\AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds\behavior_packs\地图画生成器辅助资源
```
6.运行start.bat或map_painter.py，如系统阻止运行则继续选择运行

终端界面弹出后将图片拖至终端界面，此时functions文件夹内出现多个mcfunction文件

mcfunction文件可转移至其他资源包，不一定需要在本资源包下运行

7.启动游戏，启用行为包“地图画生成器辅助资源”，以创造模式进入世界，运行如下指令
```
/function new0 [0为序号，代码辅助里显示几个运行几个]
```
地图画会生成在玩家脚下，玩家位于地图画左上角（地图显示方向）

###注意事项

该工具使用方式相对其他工具并不直观，建议先在空白地图创建地图画后使用结构方块转移至目标存档