#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2022/3/26 下午8:39
# software: PyCharm


def pc(url):
    pc = '''
    <script src="https://cdn.bootcss.com/jquery/1.12.4/jquery.min.js"></script>
    <script>
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
            setTimeout(function () {
            $('.barrage-more').css('display', 'none')
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

    var loadJS = function (url, callback, location) {
        location = location || document.head

        var scriptTag = document.createElement('script');
        scriptTag.onload = callback;
        // scriptTag.onreadystatechange = callback;
        scriptTag.src = url;
        location.appendChild(scriptTag);
      };

      function drawQRcode () {
        var canvas = document.getElementById('qrcode-canvas')
        QRCode.toCanvas(canvas, window.location.href, {
          scale: 4,
          width: 130,
          height: 130
        })
      }

      function doPCActions() {
        loadJS('https://cdn.jsdelivr.net/npm/qrcode/build/qrcode.min.js', drawQRcode);
      }
      function doMobileActions () {
        window.location.href="''' + url + '''"
      }

      isMobile() ? doMobileActions() : doPCActions();
    }();
</script>
'''
    return pc