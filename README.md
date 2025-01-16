# DNS response time test

## 程序目的

测试各个DNS服务器的响应时间并制作成csv表格以便观察，每个DNS响应都会重复3次并取平均值。

## 如何使用

1. 安装Python：<https://www.python.org/>
2. 安装Git：<https://git-scm.com/>
3. 安装Python库：```pip install dnspython```
4. 找到一个空位置：```cd D:\```
5. 克隆此仓库：```git clone https://github.com/BlazeSnow/DNS-response-time-test```
6. 编辑```server.txt```和```website.txt```，添加自定义的DNS服务器和测试域名
7. 运行Python文件：```.\run.bat```
8. 查看运行结果```results.csv```，可以直接使用```Excel```打开