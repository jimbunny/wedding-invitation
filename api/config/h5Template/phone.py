#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2022/3/26 下午8:38
# software: PyCharm


def phone(url):
    phone =  '''
    <script>
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