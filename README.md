# DNS response time test

## 程序目的

测试各个DNS服务器的响应时间并制作成csv表格以便观察，每个DNS响应都会重复3次并取平均值。

## 如何使用

1. 安装Python
2. 找到一个空位置：```cd D:\```
3. 克隆此仓库：```git clone https://github.com/BlazeSnow/DNS-response-time-test```
4. 编辑```server.txt```和```website.txt```，添加自定义的DNS服务器和测试域名
5. 运行Python文件：```.\run.bat```
6. 查看运行结果```results.csv```，可以直接使用```Excel```打开