# 简介

腾讯云SCF（云函数）的python脚本。  

- 5252pojieCheckIn
    - 吾爱破解论坛每日签到 （已完成）
- BilibiliCheckIn：
    - 哔哩哔哩直播签到赚银瓜子  （已完成）
    - 每日观看视频赚经验  （已完成）
    - 每日登录赚经验  （已完成）
    - 每日分享赚经验  （未完成，网页端的api不能完成此任务，需客户端的api）
    - 每日投币赚经验  （可以完成但没必要，不投，要白嫖经验！）
- bs4：
    - python依赖包

# 使用

1. 复制代码至云函数，保存文件名为`index.py`
2. 执行方法设置为`index.main`
3. 新建层，上传依赖包`bs4`
4. 层管理绑定刚刚新建的层
5. 测试成功后在触发管理里设置触发器

# 参考

感谢：  

https://github.com/Hsury/Bilibili-Toolkit  
https://github.com/shniubobo/bilibili_bv2av  