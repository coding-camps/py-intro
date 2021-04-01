### py-intro


## requirements
- Add or update requirements package info to package.txt file:  
`pip list --format freeze | grep -Ev "(pip)|(setuptools)|(wheel)" > package.txt`  
- Install packages once from requirements file:  
`pip install -r package.txt`




#### 学习资料
1. Python官方网站：https://www.python.org/  
2. Python3.6.3中文文档：https://www.runoob.com/manual/pythontutorial3/docs/html/  
3. Python 3教程：https://www.runoob.com/python3/python3-tutorial.html
4. 廖雪峰的Python教程：https://www.liaoxuefeng.com/wiki/1016959663602400  
* _本项目教程以#3为主_

- **Python 循环列表删除元素的注意事项**
  - http://wu.run/2020/11/11/python-traversal-delete-needing-attention/

- **装饰器**
  - [Python 函数装饰器](https://www.runoob.com/w3cnote/python-func-decorators.html)

- **生成器**
  - https://www.cnblogs.com/yund/p/17366967.html
  - https://blog.csdn.net/fengbingchun/article/details/120240229

- **迭代器**
  - https://www.cjavapy.com/article/953/
  - https://www.cnblogs.com/tangwei-fuzhou/p/12669087.html


#### 5. Python 文化
> ['Life is short, you need python'](https://sebsauvage.net/python/)

#### 6. 技术风险
> Python 功能强大，但相关的技术也有风险。  
> **忠告：不要用爬虫技术**  
>>1.爬虫容易搞坏网站。（刑法二百八十六条，破坏计算机信息系统罪）  
>>2.爬虫很容易采集个人信息。（网络信息安全法，GDPR等法律相关条款）  
>>3.爬虫很容易采集商业机密和国家机密等。  
>
> **参考**  
>>1.[谈谈爬虫背后的法律风险](https://www.cnblogs.com/binyue/p/11719854.html)  
>>2.[爬虫与反爬虫：一个很不阳光的行业！一文揭秘那些你不知道的套路](http://www.sohu.com/a/217594662_185201)  
>>3.[一个爬虫引发的案件：非法获取公民个人信息 情节严重可判刑](http://www.mpaypass.com.cn/news/201910/17091741.html)
>
> **建议**  
>> 如果想学习爬虫技术，就找个“合适(非法的)”的网站练手。  
