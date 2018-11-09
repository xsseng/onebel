document.cookie = "OnebelKey = username,userid"; //demo

const Onebelhost = "http://www.onebel.org"; //onebelhost
const secKey = ['ip', 'devid', 'mac']; //要发送的风控指标
var onebeldata = new Array(); //所有data全部丢进来
var postdata = new Array(); //经过处理的数据
var disdata = new Array();
var onebelstatus = 0;

/**
前端将数据发送到 http://www.onebel.org/getdata 例如
http://www.onebel.org/getdata?Onebelkey=Onebel_username&username=用户的用户名&secKey=其他风控指标&ip=用户的IP&devid=用户的设备id&mac=macaddress&cpu=cputype
当然建议通过post的方式提交，因为get有长度限制
**/
//读取cookie函数
function getCookie(cookieName) {
    var strCookie = document.cookie;
    var arrCookie = strCookie.split("; ");
    for(var i = 0; i < arrCookie.length; i++){
        var arr = arrCookie[i].split("=");
        if(cookieName == arr[0]){
            return arr[1];
        }
    }
    return "";
}
//初始化函数
function __autoloadkey(){
	var OnebelKeyType = new Array();
	var OnebelKeyString = getCookie("OnebelKey");
	OnebelKeyType = OnebelKeyString.split(",");
    for (var i = OnebelKeyType.length - 1; i >= 0; i--) {
        //OnebelKeyType[i]
        onebeldata.push(OnebelKeyType[i] + "=" + getCookie(OnebelKeyType[i]));
        onebelstatus = 1;
    //处理数据进行发送
    }
}
/**
   异步函数
   需要id中添加Onebelsent，并且在Onebelname中添加参数名，在stringType中说明取值来自哪里，例如：
   <input id='Onebelsent' Onebelname='username' stringType='value' value=''>
   
   如果input标签因为兼容性问题需要id属性的值配合其他框架可以在外div中添加这个函数，但是必须说明在什么标签里，例如：
    <div id='Onebelsent' Onebelname='username' tagType='1' stringType='innerHTML'>
        <a>
            被获取到的值
        </a>
    </div>
**/
function getOnebelkey(){
    //这个函数有点长慢慢写
    //情况一，直接套用的情况
    if(document.getElementById("Onebelsent").getAttribute("tagType") === undefined || document.getElementById("Onebelsent").getAttribute("tagType") == null){
        if(document.getElementById("Onebelsent").getAttribute("stringType") == "value"){
            //发送value属性的值
            onebeldata.push(document.getElementById("Onebelsent").getAttribute("Onebelname") + "=" + document.getElementById("Onebelsent").value);
        }else if(document.getElementById("Onebelsent").getAttribute("stringType") == "Onebelvalue"){
            //发送Onebelvalue属性的值
            onebeldata.push(document.getElementById("Onebelsent").getAttribute("Onebelname") + "=" + document.getElementById("Onebelsent").getAttribute("Onebelvalue"));
        }else{
            //发送innerHTML
            onebeldata.push(document.getElementById("Onebelsent").getAttribute("Onebelname") + "=" + document.getElementById("Onebelsent").innerHTML);
        }
    }else{
        //情况二，发送嵌套标签里的数据
        if(document.getElementById("Onebelsent").getAttribute("stringType") ==  "value"){
            //发送子元素的value
            onebeldata.push(document.getElementById("Onebelsent").getAttribute("Onebelname") + "=" + document.getElementById("Onebelsent").children[0].value);
        }else if(document.getElementById("Onebelsent").getAttribute("stringType") ==  "Onebelname"){
            //发送子元素的Onebelvalue
            onebeldata.push(document.getElementById("Onebelsent").getAttribute("Onebelname") + "=" + document.getElementById("Onebelsent").children[0].getAttribute("Onebelname"));
        }else{
            //发送子元素的innerHTML
            onebeldata.push(document.getElementById("Onebelsent").getAttribute("Onebelname") + "=" + document.getElementById("Onebelsent").children[0].innerHTML);
        }

    } 
}   
//发送函数
function sentKey(host,path,data){
    var xmlhttp;
    if (window.XMLHttpRequest){
        xmlhttp = new XMLHttpRequest();
    }else{
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange = function(){
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
            //返回数据处理办法
            return xmlhttp.responseText;
        }
    }
    xmlhttp.open("POST", host + path, true);
    xmlhttp.send(data);
}
//处理onebeldata变为postdata
//可能存在多次重复的数据，例如["username=cookie","username=startinput", "username=endinput"]
//根据程序的逻辑性来说如果有cookie data先发送一次cookiedata，如果用户输入，则再次发送inputdata，去除数组中靠前的相同数值
function getPostdata(onebeldata){
    for (var i = onebeldata.length - 1; i >= 0; i--) {
        if(!isInArray(disdata,onebeldata[i].split("=")[0])){
            postdata.push(onebeldata[i]);
            disdata.push(onebeldata[i].split("=")[0]);
        }
    }
}

//兼容方式判断数值是否存在数组中
function isInArray(arr,value){
    for(var i = 0; i < arr.length; i++){
        if(value === arr[i]){
            return true;
        }
    }
    return false;
}









