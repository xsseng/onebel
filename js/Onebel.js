doucment.cookie = "OnebelKey = username,userid"; //demo

const Onebelhost = "http://www.onebel.org"; //onebelhost
const secKey = ['ip','devid','mac','cpu']; //要发送的风控指标

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
	var OnebelKey = new Array();
	var OnebelKeyString = getCookie("OnebelKey");
	OnebelKey = OnebelKeyString.split(",");
	//处理数据进行发送
}
/**
   异步函数
   需要id中添加Onebelsent，并且在Onebelname中添加参数名，在stringType中说明取值来自哪里，例如：
   <input id='Onebelsent' Onebelname='username' stringType='value' value=''>
   
   如果input标签因为兼容性问题需要id属性的值配合其他框架可以在外div中添加这个函数，但是必须说明在什么标签里，例如：
    <div id='Onebelsent' Onebelname='username' tagType='a' stringType='innerHTML'>
        <a>
            被获取到的值
        </a>
    </div>
**/
function sentOnebelkey(){
    //这个函数有点长慢慢写
    //情况一，直接套用的情况
    if(document.getElementById("Onebelsent").tagType === undefined || docuemnt.getElementById("Onebelsent").tagType == null){
        if(document.getElementById("Onebelsent").stringType == 'value'){
            //发送valueß∂
        }else if(document.getElementById("Onebelsent").stringType == 'Onebelvalue'){
            //发送Onebelvalue
        }else{
            //发送innerHTML
        }
    }else{
        //情况二，发送div的嵌套标签数据

    } 
}   













