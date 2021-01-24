xpath 解析
> 最常用且最便捷高效的一种解析方式 通用性
## xpath 解析原理
- 1 实例化一个etree的对象，且需要被解析的页面源码数据加载到该对象中
- 2 调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获
## 环境安装
- pip install lxml
## 如何实例化一个etree对象
- 将本地的html文档中的源码数据加载到etree对象中
  etree.parse(filePath)
- 可以将从互联网上获取的源码数据加载到该对象中
  etree.HTML('page_text')
- xpath('xpath表达式')

