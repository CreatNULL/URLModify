## 这是什么?

```text
    这是一个python的工具，用于处理 URL。 Hunter,fofa，弄出来的有的不携带协议，有的携带协议
  
  我: 
  	桀桀桀~ 看我python大法~

   可能有bug
```
## 注意
    不支持中文域名
    不支持ipv6
    对于不常见的域名，或者自定义的域名，误识别为非URL，因为脚本是搜集了wiki页面、腾讯页面、阿里页面的所有出现的顶级域名，对于其他的认为不合法的域名
    解决方案:
        找到 topdomain.py 文件中添加自定义的顶级域名
![image](https://github.com/user-attachments/assets/a57cfe85-f610-42cb-91e0-c46fb0e5d1f6)

## 如何使用

将需要的URL 例如下方，在左侧选择不同功能， 测试数据:

```text
1.jpg
2.png
.cpp

# 非法, 正常 0-255
http://192.168.1.256  

# 非法，缺少端口号
http://localhost:

# 非法, 多了个.
http://.example.com

# 非法
http://example..local

# 非法, 虽然两个// 可以解析, 但是 /?query 好像没见到果这样的
http://localhost:8080//?query=1

# 非法
http://localhost/path?=value

# 算他合法因为有时候测试需要 ../../ 测试目录穿越
http://localhost/..

# 非法
http://192.168.1.1:-80

www.baidu.com:8080/queyr

# 非法
www.baidu.com:80801/queyr

www.baidu.com:8080/?queyr

# 非法
www.baidu.com:80801/queyr

127.0.0.1:8080

# 非法
127.0.0.1:89080

http://192.168.5.10:808/queyr?

localhost
localhost/query
localhost?index
htt://www.baidu.com

合法的域名
example1.com
example2.org
test-site.net
my-domain.info
subdomain.example.com
example123.co
shop.example.us
blog.example.io
service.example.biz
domain.example.aero
mywebsite.coop
example.travel
webapp.example.name
example.ac
example.tech
example.xyz
example.cloud
example.store
example.pro
myapp.example.me
myportfolio.example.cc

不合法的域名
example-.com
-website.com
example..com
example@domain.com
example.com.
site..example.com
example..co.uk
website..org
example.123.com
!example.com
example#domain.com
example%domain.com
example&site.com
example(1).com
example*site.com
example+domain.com
example=site.com
example?domain.com
example/domain.com
example:port.com
example;site.com

合法的 IP 地址
192.168.0.1
10.1.1.1
172.31.255.255
198.51.100.14
203.0.113.76
127.0.0.1
192.0.2.1
::1
2001:db8::ff00:42:8329
255.255.255.255

不合法的 IP 地址
192.168.300.1
1234.567.89.0
256.256.256.256
192.168.1.1.1
192.168..1
10.0.0
-10.0.0.1
192.168.1.256
0.0.0.0.0
300.300.300.300
999.999.999.999

畸形 URL
http://example.com/path?param=
https://:80/path
ftp://example.com//path
http://example.com//path//
http://example.com?query&=
https://example.com#fragment#
http://:80
http:///example.com
ftp://username:password@server:port/path
http://example.com:port/

畸形 IP
192.168..1
192.168.1.1.1
1234.567.89.0
192.168.-1.1
0.0.0.256
999.999.999.999
300.300.300.300
256.256.256.256
-1.1.1.1
172.16.0.0.1

畸形域名
example..com
example!@#.com
www.-example.com
example.com.
site..example.net
example#site.com
example%domain.com
example@domain.com
example^domain.com
example&site.com
example*domain.com



http://www.google.com
http://www.yahoo.com/
http://www.yahoo.com:8080
http://www.yahoo.com:8080/
http://www.yahoo.com:8080/?index=1
http://www.yahoo.com:8080/?index=0
https://www.google.com
https://www.yahoo.com:8080/
 
https://www.yahoo.com:8080/?index=1
ftp://www.ftp.com
ftp://www.ftp.com:21
ftp://127.0.0.1
ftp://127.0.0.1:21
ftp://127.0.0.1:21?index=1
ftp://127.0.0.1:21/
127.0.0.1
127.0.0.1/query?index=1
127.0.0.1:8080
127.0.0.1:8080/
127.0.0.1:8080/?index=1

www.baidu.com/url
www.baidu.com/query?name=小明
ftp://www.baidu.com/query?name=小明
www.baidu.com:8080
www.baidu.com:8080/url
www.baidu.com:8080/url=我
www.baidu.com
www.baidu.com?index=1
www.我.com
www.我
www.baidu.com:443
www.baidu.com:21
www.1
www.1.
www.1.c
wwww.1.cc
www.1.cc.com
wwww.1.cc
wwww.1.cc.
ww.1.bc
"""www".com.com""""
```
能一、URL 分类

有两种输出模式:

第一种:  将URL 分类到不同的列
![image](https://github.com/user-attachments/assets/bbbbf82b-3045-459c-afbf-6e4520ca70d4)



第二种: 将 URL 一行一行的分类
![image](https://github.com/user-attachments/assets/cdd07ca0-8441-44db-a2fd-46484b19275f)


### 功能二、提取URL信息

提取URL中的协议、端口等信息，如果本身没有携带对应信息，则同样是没有的，如果想有可使用添加端口，添加协议功能
![image](https://github.com/user-attachments/assets/95eb8a74-b99a-4fbe-9e35-6090f973784e)


### 功能三、添加端口

给域名、URL、IP 添加端口，如果本身携带，则不添加，URL携带协议，则自动依据协议添加端口

![image](https://github.com/user-attachments/assets/6891927c-6c7a-4741-ac66-242d35d8add6)


### 功能四、添加协议

同上，依据端口添加协议
![image](https://github.com/user-attachments/assets/4d505463-3e18-4d65-8c57-36b2c4c75b54)


### 功能五、去除空行 、空格

![image](https://github.com/user-attachments/assets/5f49e65b-d726-4444-89a5-0de2c5f83143)


### 功能六、出去两边的引号

有时候复制下来说不定一行URL 左右两边会有 引号存在

![image](https://github.com/user-attachments/assets/5d8b9b47-a3e2-4381-9dcf-bbee0ab1e6ef)




### 其他

##### 1. 控制输出是否去除空行

![image](https://github.com/user-attachments/assets/8e08c391-7645-4270-827a-a17a63f4b806)


##### 2. 下载保存

![image](https://github.com/user-attachments/assets/d24adf25-6bdd-4e39-a987-3ec73320b996)


##### 3. 如何复制一整列，点一下列标题，然后变成黄色后，在黄色处单机右键复制

![image](https://github.com/user-attachments/assets/ef47296b-fe11-4c08-bd84-303c33ec95de)
![image](https://github.com/user-attachments/assets/a8067590-2954-4aa2-877a-dc45bfc71de6)


##### 5.主题颜色不好看？想换？

在这themes 下的 themes下添加自定义主题样式，默认提供了一个清新绿，一个像素（默认风格)

![image](https://github.com/user-attachments/assets/1ad83286-7c2b-4a3d-b11c-4d1f6112c85a)


在URLmodfiy_GUI.py 中 导入

![image](https://github.com/user-attachments/assets/138155f2-6ddf-430c-acb1-dfe5df1664bd)


换成导入的主题

![image](https://github.com/user-attachments/assets/4c011342-1bb7-49ce-855d-418e340b9759)


#### 6. 想要添加端口、添加协议时，更多的自动匹配？

修改 modfiy ->urlmodfiy.py -> map 的 self.map_protocol_to_port 和 self.map_port_to_protocol
![image](https://github.com/user-attachments/assets/dab7f66d-7a00-4574-bf5e-f27e1e040943)


##### 7. 去重
![image](https://github.com/user-attachments/assets/6d815a47-5373-4c31-9bbe-09a805e3eaf7)


## 使用示例
如果数据量比较多，建议先复制到txt文本中，然后再复制到输入框中不然可能会有些卡
先看看有没有不合法的域名
![image](https://github.com/user-attachments/assets/3e3f7f5c-c9e3-4c18-9b82-b6549e59f464)
可以看到，有些没有协议，再给它添加协议，勾选去重，去空行
![image](https://github.com/user-attachments/assets/3e6941a5-8be8-4713-8e36-ef5870aae725)
可以下载保存，也可以单独复制处理后的url


