#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2022/3/26 下午8:39
# software: PyCharm


def pc(url):
    pc = '''
    <script src="https://cdn.bootcss.com/jquery/1.12.4/jquery.min.js"></script>
    <script>
    $('.barrage-more').css('display', 'none')
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