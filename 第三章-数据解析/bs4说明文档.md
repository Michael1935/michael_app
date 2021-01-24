bs4 数据解析的原理
- 实例化一个 BeautifulSoup 对象 并且将页面源码数据加载到该对象中
- 通过调用beautifulSoup对象中相关的属性或者方法将标签定位和数据提取
## 环境安装
- pip install bs4
- pip install xml
## 如何实例化一个BeautifulSoup对象：
- from bs4 import BeautifulSoup
对象的实例化
- 将本地的html文档中的数据加载到该数据对象中
    fp = open('./test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
- 将互联网上获取的页面源码加载到该对象中
    page_test = res.text
    soup = BeautifulSoup(page_test, 'lxml')
    soup.find
        soup.find('tagName') == soup.div
### 属性定位
- soup.find('div', class_/id/attr="song")
- soup.find_all('div')返回所有的符合的类型
- soup.select() // 选择器

### 获取标签之间的文本数据
- soup.a.text/string/get_text()
- text/get_text() 可以获取某一个标签中所有的文本内容
- string 只可以获取该标签下面直系的文本内容
### 获取标签中属性值
- soup.a['href']



