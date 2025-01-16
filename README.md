# DNS response time test

## 程序目的

测试各个DNS服务器的响应时间并制作成csv表格以便观察，每个DNS响应都会重复3次并取平均值

## 输出示例

|                        | 223.5.5.5 | 223.6.6.6 | 119.29.29.29 | 114.114.114.114 | 114.114.115.115 |
| ---------------------- | --------- | --------- | ------------ | --------------- | --------------- |
| baidu.com              | 12        | 9         | 13           | 434             | 30              |
| bilibili.com           | 11        | 11        | 12           | 28              | 32              |
| icloud.com.cn          | 11        | 9         | 12           | 27              | 31              |
| gateway.icloud.com     | 10        | 12        | 14           | 30              | 31              |
| gateway.icloud.com.cn  | 10        | 12        | 16           | 29              | 29              |
| courier.push.apple.com | 11        | 11        | 13           | 32              | 31              |
| github.com             | 10        | 10        | 12           | 30              | 31              |
| api.onedrive.com       | 11        | 11        | 13           | 31              | 31              |
| microsoft.com          | 9         | 10        | 12           | 32              | 30              |
| blazesnow.com          | 11        | 9         | 10           | 31              | 30              |
| blazesnow.cn           | 11        | 10        | 11           | 30              | 29              |

## 如何使用

1. 安装Python：<https://www.python.org/>
2. 安装Git：<https://git-scm.com/>
3. 安装Python库：```pip install dnspython```
4. 找到一个空位置：```cd D:\```
5. 克隆此仓库：```git clone https://github.com/BlazeSnow/DNS-response-time-test```
6. 编辑```server.txt```和```website.txt```，添加自定义的DNS服务器和测试域名
7. 运行Python文件：```.\run.bat```
8. 查看运行结果```results.csv```，可以直接使用```Excel```打开