#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2022/3/26 下午8:38
# software: PyCharm
from config.h5Template.font import choseFont


def phone(url, name):
    font = choseFont(name)
    phone = '''
    <script src="/static/js/jquery.min.js"></script>
    <link href=' ''' + str(font.get('url')) + ''' ' rel='stylesheet' type='text/css'>
    <script>
      var browser = {
            versions: function () {
                var u = navigator.userAgent, app = navigator.appVersion;
                return {         //移动终端浏览器版本信息
                    trident: u.indexOf('Trident') > -1, //IE内核
                    presto: u.indexOf('Presto') > -1, //opera内核
                    webKit: u.indexOf('AppleWebKit') > -1, //苹果、谷歌内核
                    gecko: u.indexOf('Gecko') > -1 && u.indexOf('KHTML') == -1, //火狐内核
                    mobile: !!u.match(/AppleWebKit.*Mobile.*/), //是否为移动终端
                    ios: !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/), //ios终端
                    android: u.indexOf('Android') > -1 || u.indexOf('Linux') > -1, //android终端或uc浏览器
                    iPhone: u.indexOf('iPhone') > -1, //是否为iPhone或者QQHD浏览器
                    iPad: u.indexOf('iPad') > -1, //是否iPad
                    webApp: u.indexOf('Safari') == -1 //是否web应该程序，没有头部与底部
                };
            }()
        }
        if (browser.versions.mobile) {//判断是否是移动设备打开
            var ua = navigator.userAgent.toLowerCase();//获取判断用的对象
            if (ua.match(/line/i) == "line") {
                var url = window.location.href;
                if (url.indexOf("?") < 0) {
                    url += "?openExternalBrowser=1";
                } else {
                    // 網址有參數 ? 時, 用 & 加參數
                    url += "&openExternalBrowser=1";
                }
                window.location.href = url;
            }
            if (browser.versions.ios) {
               // alert("IOS浏览器打开"); //是否在IOS浏览器打开
            } 
            if(browser.versions.android){
                //alert("安卓浏览器打开") //是否在安卓浏览器打开
            } 
        } else {
            // alert("PC");       
        }
            
    
    function audioAutoPlay(id) {
        var audio = document.getElementById(id),
        play = function() {
            audio.play();
            document.removeEventListener("touchstart",play,false);
        };
        audio.play();
        document.addEventListener("WeixinJSBridgeReady", function() {
            play();
        }, false);
        document.addEventListener('YixinJSBridgeReady', function() {
            play();
        }, false);
        document.addEventListener("touchstart", play, false);
    }
    audioAutoPlay('bgmedia');
    
    var interval = setInterval(function () {
        var readystate = document.readyState.toLowerCase();
        console.log(readystate)
        if (readystate == 'complete')
        {
        setTimeout(function () {
            $('.barrage-more').css('display', 'none')
            $('div').css('font-family', ' ''' + str(font.get('name')) + ''' ', ' ''' + str(font.get('family')) + ''' !important')
        }, 2000);
        setTimeout(function () {
            $('.barrage-more').css('display', 'none')
            $('div').css('font-family', ' ''' + str(font.get('name')) + ''' ', ' ''' + str(font.get('family')) + ''' !important')
        }, 5000);
        clearInterval(interval);
        }
    },500)
    let box = document.querySelector('body') // 监听对象
    let startTime = '' // 触摸开始时间
    let startDistanceX = '' // 触摸开始X轴位置
    let startDistanceY = '' // 触摸开始Y轴位置
    let endTime = '' // 触摸结束时间
    let endDistanceX = '' // 触摸结束X轴位置
    let endDistanceY = '' // 触摸结束Y轴位置
    let moveTime = '' // 触摸时间
    let moveDistanceX = '' // 触摸移动X轴距离
    let moveDistanceY = '' // 触摸移动Y轴距离
    box.addEventListener("touchstart", (e) => {
        startTime = new Date().getTime()
        startDistanceX = e.touches[0].screenX
        startDistanceY = e.touches[0].screenY
    })
    box.addEventListener("touchend", (e) => {
        endTime = new Date().getTime()
        endDistanceX = e.changedTouches[0].screenX
        endDistanceY = e.changedTouches[0].screenY
        moveTime = endTime - startTime
        moveDistanceX = startDistanceX - endDistanceX
        moveDistanceY = startDistanceY - endDistanceY
        {#console.log(moveDistanceX, moveDistanceY)#}
        // 判断滑动距离超过40 且 时间小于500毫秒
        if ((Math.abs(moveDistanceX) > 40 || Math.abs(moveDistanceY) > 40) && moveTime < 500) {
            $('.barrage-content').css('display', 'block')
            setTimeout(function () {
                $('.barrage-more').css('display', 'none')
                $('div').css('font-family', ' ''' + str(font.get('name')) + ''' ', ' ''' + str(font.get('family')) + ''' !important')
            }, 2000);
            // 判断X轴移动的距离是否大于Y轴移动的距离
            if (Math.abs(moveDistanceX) > Math.abs(moveDistanceY)) {
            // 左右
            {#console.log(moveDistanceX > 0 ? 'left' : 'right')#}
            } else {
            // 上下
            {#console.log(moveDistanceY > 0 ? 'up' : 'down')#}
            }
        }
    })
    
    !function () {
      function isMobile() {
        var mobileDeviceReg = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobi/i
        return mobileDeviceReg.test(navigator.userAgent) || window.innerWidth < 500
      }


      function doMobileActions () {
      }

      function doPCActions() {
        window.location.href="''' + url + '''"
      }

      isMobile() ? doMobileActions() : doPCActions();
    }();
</script>
'''
    return phone