# Onebel

Onebel是一个开源的**安全数据缓存系统**，通过三方身份验证使数据库中的敏感数据安全存储和使用，它具有强大的检测引擎，计算对关键敏感数据的合规性。更多信息请关注我们的官网 www.onebel.org

# 快速安装
Onebel基于python3+flask，在主目录下拥有venv的环境，故而你可以很快起一个onebel环境

```
pip install virtualenv
git clone https://github.com/xsseng/onebel.git
cd onebel/onebel/
source venv/bin/activate
python run.py
```

接着访问localhost，你就可以看到`onebel is worked！`

当然你需要他正确的工作，需要进入`module/config.py`输入你的MySQL与Redis的配置


# Onebel.js文档

## 配置

## 预加载模式

你要为需要使用Onebel的网页率先设置一个**OnebelKey**，以便于预发送数据。正确的做法是将cookie放在浏览器的响应头或放在`<head>`标签中，比如如果你要将名为username和userid的cookie发送到服务器，你可以在响应头设置：

`Set-Cookie: OnebelKey = username, userid`

你也可在`<script>`标签中添加如下语句：

`document.cookie = "OnebelKey = username, userid";`

在这之后你才可以载入预加载函数，他会自动封装好数据发送到Onebel服务器

`const Onebelhost = "http://yourdomain/"; `
`const Onebelpath = "/api/";`
`__autoloadkey();`

## 用户输入模式

除了预加载外，我们也许需要用户的输入来发送到Onebel，例如用户登陆时输入的用户名，你必须按照规范将数据储存在标签或属性值中。你需要id中添加Onebelsend，并且在Onebelname中添加参数名，在stringType中说明取值来自哪里，例如：

   `<input id='Onebelsend' Onebelname='username' stringType='value' value=''>`
   
如果input标签因为兼容性问题需要id属性的值配合其他框架可以在外div中添加这个函数，但是必须用tagType表达在第几个标签中，例如：
   
```html
<div id='Onebelsend' Onebelname='username' tagType='1' stringType='innerHTML'>
  <a>
    被获取到的值
  </a>
</div>
```

然后你需要通过函数执行操作，以下是正确的演示：

```
<label>
  <span>请输入用户名</span>
  <input id='Onebelsend' Onebelname='username' stringType='value' name='username' value='' onchange="getOnebelkey()">
</label>
<label>
  <span>请输入密码</span>
  <input id='' name=password value=''>
</label>
```
