#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2022/3/26 下午8:38
# software: PyCharm
from config.h5Template.font import choseFont


def phone(url, name):
    font = choseFont(name)
    phone = '''
    <style>
    #talkbubble {
       width: 70.1562px;
        height: 22.1562px;
        padding: 2px 2px 2px 7px;
        right: 20%;
        top: 3%;
        background: #a3a3a3;
        opacity: 1;
        position: absolute;
        display: none;
        z-index: 1000000;
        transform-origin: center center;
        touch-action: pan-y;
        user-select: none;
        -webkit-user-drag: none;
        -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
        -moz-border-radius: 10px;
        -webkit-border-radius: 10px;
        border-radius: 5px;
    }
    #talkbubble:before {
        content: "";
        position: absolute;
        left: 100%;
        top: 5px;
        width: 0;
        height: 0;
        border-top: 6px solid transparent;
        border-left: 12px solid #a3a3a3;
        border-bottom: 6px solid transparent;
    }
    .maka-Arrow1 {
        position: absolute;
        bottom: 20px;
        left: 50%;
        margin-left: -20px;
        width: 40px;
        text-align: center;
        display: none;
        z-index: 1999;
        animation-name: arrowing;
        -webkit-animation-name: arrowing;
        animation-duration: 1.5s;
        -webkit-animation-duration: 1.5s;
        animation-iteration-count: infinite;
        -webkit-animation-iteration-count: infinite;
        background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.2) 100%)
    }
    .barrage-more {
        display: none !important;
    }
    </style>
    <div class="maka-Arrow1" style="display: block;"><img src="https://img1.maka.im/assets/usual/slideguide-3-view.png" alt=""><div style="font-size: 15px;color: #fff;">slide here</div></div>
    <div id="talkbubble">เล่นเพลง</div>
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
        var audio = document.getElementById("bgmedia"),
        play = function() {
            //audio.play();
            //document.getElementById("bgmedia").play();
            document.removeEventListener("touchstart",play,false);
        };
        // audio.play();
       // document.getElementById("bgmedia").play();
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
            try{
                var dom1 = document.querySelector('.stopAnimation');
                // 不包括padding border 仅仅是width 这个ie也许有兼容性问题
                // console.log(getComputedStyle(dom1).width);
                var contentBg = document.getElementById("talkbubble");//第一步
                contentBg.style.top = (parseFloat(getComputedStyle(dom1).width.substring(0,7))-22.1562/2).toString() + "px" //第二步
                contentBg.style.right =  (parseFloat(getComputedStyle(dom1).width.substring(0,7))/2*3+18).toString() + "px"
            }catch (e){
                var dom1 = document.querySelector('.runAnimation');
                // 不包括padding border 仅仅是width 这个ie也许有兼容性问题
                // console.log(getComputedStyle(dom1).width);
                var contentBg = document.getElementById("talkbubble");//第一步
                contentBg.style.top = (parseFloat(getComputedStyle(dom1).width.substring(0,7))-22.1562/2).toString() + "px" //第二步
                contentBg.style.right =  (parseFloat(getComputedStyle(dom1).width.substring(0,7))/2*3+18).toString() + "px"
            }
            $('#talkbubble').css('display', 'block')
            $('.maka-Arrow').css('display', 'none !important')
            $('div').css('font-family', ' ''' + str(font.get('name')) + ''' ', ' ''' + str(font.get('family')) + ''' !important')
        }, 2000);
        setTimeout(function () {
            $('.maka-Arrow').css('display', 'none !important')
        }, 1);
        setTimeout(function () {
           $('.maka-Arrow').css('display', 'none !important')
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
    var touchStatus = 0;
    box.addEventListener("touchend", (e) => {
        touchStatus=1;
        // event.preventDefault();
        endTime = new Date().getTime()
        endDistanceX = e.changedTouches[0].screenX
        endDistanceY = e.changedTouches[0].screenY
        moveTime = endTime - startTime
        moveDistanceX = startDistanceX - endDistanceX
        moveDistanceY = startDistanceY - endDistanceY
        {#console.log(moveDistanceX, moveDistanceY)#}
        // 判断滑动距离超过40 且 时间小于500毫秒
        if ((Math.abs(moveDistanceX) > 40 || Math.abs(moveDistanceY) > 40) && moveTime < 500) {
            var myAudio = document.getElementById('bgmedia');
            if (myAudio.duration > 0 && !myAudio.paused) {
                $('#talkbubble').css('display', 'none')
                //Its playing...do your job
            } else {
                $('#talkbubble').css('display', 'block')
                //Not playing...maybe paused, stopped or never played.
            }
            $('.maka-Arrow1').css('display', 'none')
            $('.cd-stretchy-nav').css('display', 'block')
            $('.barrage-content').css('display', 'block')
            setTimeout(function () {
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
     setTimeout(function () {
        if(touchStatus==0){
            $('.cd-stretchy-nav').css('display', 'block')
            $('.barrage-content').css('display', 'block')
            $('.maka-Arrow1').css('display', 'none')
            $('.maka-Arrow').css('display', 'block')
        }
    }, 10000);
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