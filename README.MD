# 项目简介

&emsp;&emsp;腾讯云SCF（云函数）、Github Actions的python脚本，用于每天自动签到，一个是吾爱破解论坛的一个是哔哩哔哩的，作为我了解SCF的示例。

# 功能实现

## 52pojieCheckIn
- 【已完成】每日签到

## BilibiliCheckIn
- 【已完成】每日直播签到赚银瓜子
- 【已完成】每日观看视频赚经验
- 【已完成】每日登录赚经验
 ---
- 【未完成】每日分享赚经验  

>&emsp;&emsp;客户端分享API：  
>```
>https://app.bilibili.com/x/v2/view/share/click
>https://app.bilibili.com/x/v2/view/share/complete
>```
>&emsp;&emsp;网页端分享API：  
>```
>https://api.bilibili.com/x/web-interface/share/add
>```
>&emsp;&emsp;这两个接口貌似都能完成`客户端分享视频`的任务，但是以`Cookie`登录却无法完成，可能需要`access_key`，那就必须使用账号密码登录来获取，而使用`账号密码`登录就容易出现验证，参考了多个项目的实现方式，发现都是针对图形验证码的，而我测试的时候要么是手机验证要么是滑块验证（就很玄学），这对于`SCF`来说不太适合。水平有限，如果你有适合`SCF`的解决方法麻烦提一个`issue`或`Pr`，感谢。

- 【未完成】每日投币赚经验  

>&emsp;&emsp;可以完成但没必要，不投，要白嫖经验！如果你需要的话，请使用`https://api.bilibili.com/x/web-interface/coin/add`这个接口，提交参数为`aid`、`multiply`、`cross_domain`、`csrf`

 
# 项目结构

|  文件   | 描述 |
|  :----:   | :----: |
| 52pojieCheckIn.py | 吾爱破解论坛 |
| BilibiliCheckIn.py | 哔哩哔哩 |
| bs4.zip | python3依赖包 |

# 使用说明

## 注意事项

&emsp;&emsp;吾爱破解论坛的签到有点奇怪，没研究是啥问题引起的，有时可以正常签到有时又提示：不是进行中的任务，可以尝试循环签到几次（反正我是这么解决的，哈哈哈），知道原因的同学麻烦发个Pr，感谢。

## 获取Cookie

&emsp;&emsp;打开浏览器，按F12，在Network处查找，还不会的话请自行百度！

## Server酱

&emsp;&emsp;可选，用于消息反馈，如需使用其他同类型产品，修改一下`pushinfo`函数就行。 官网：http://sc.ftqq.com/3.version

## 腾讯云SCF（云函数）

1. 复制代码至`云函数`，保存文件名为`index.py`
2. `执行方法`设置为`index.main`
3. 新建`层`，上传依赖包`bs4`
4. 在`层管理`绑定刚刚新建的`层`
5. 测试成功后在`触发管理`里设置触发器

# 参考资料

感谢：  

https://github.com/Hsury/Bilibili-Toolkit  
https://github.com/shniubobo/bilibili_bv2av  