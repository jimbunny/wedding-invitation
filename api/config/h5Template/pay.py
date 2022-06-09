#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:jingtongyu
# datetime:2022/3/26 下午8:39
# software: PyCharme


def pay(GPSUrl, boyPhone, girlPhone, payQrcode, payName, menuColor="#cd91c8", fontColor="#fff"):
    payContact = '''
    <link rel="stylesheet" href="/static/website_v2/css/reset.css">
    <!-- CSS reset -->
    <link rel="stylesheet" type="text/css" href="/static/website_v2/css/default.css">
    <link rel="stylesheet" href="/static/website_v2/css/menu.css">
    <!-- Resource style -->
    <script src="/static/website_v2/js/modernizr.js"></script>
    <!-- Modernizr -->
    <style>
        .cd-stretchy-nav .stretchy-nav-bg {
            background-color: ''' + str(menuColor) + ''';
        }
        .cd-stretchy-nav ul a div{
            color: ''' + str(fontColor) + ''';
        }
    </style>
    <nav class="cd-stretchy-nav">
        <a class="cd-nav-trigger">
            <img style="width: 40px; height: 40px; margin-top: 10px;" src="/static/website_v2/images/add_button.png">
        </a>
        <ul>
          <li>
            <a href=" ''' + str(GPSUrl) + ''' " class="active">
                <img style="width: 40px; height: 40px;" src="/static/website_v2/images/GPS_button.png">
              <div>GPS นำทาง</div>
            </a>
          </li>
          <li>
            <a href="tel:''' + str(girlPhone) + ''' ">
                <img style="width: 40px; height: 40px;" src="/static/website_v2/images/girl_phone.png">
              <div>เบอร์เจ้าสาว</div></a>
          </li>
          <li>
            <a href="tel:''' + str(boyPhone) + '''">
                <img style="width: 40px; height: 40px;" src="/static/website_v2/images/boy_phone.png">
              <div>เบอร์เจ้าบ่าว</div></a>
          </li>
          <li>
            <a type="button" id="girlMoney" data-toggle="modal" data-target="#moneyModalCenter">
              <img style="width: 40px; height: 40px;" src="/static/website_v2/images/girl_money.png">
              <div>โอนเงิน</div></a>
          </li>
        </ul>
        <span aria-hidden="true" class="stretchy-nav-bg"></span>
      </nav>
<div class="barrage-input-wrap" id="modalShowMoney" style="display: none; position: fixed; left: 0px; bottom: 0px;height: 0px; width: 100%; background-color:transparent; padding: 9.375px 11.7188px; box-sizing: border-box; z-index: 2000; pointer-events: initial;">
<!-- Modal -->
<div class="modal fade" id="moneyModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
     <div class="modal-header">
        <button type="button" class="close" style="cursor: pointer;" data-dismiss="modal" aria-hidden="true">×</button>
        <h4 class="modal-title" id="myModalLabel">''' + str(payName) + '''</h4>
      </div>
      <div class="modal-body">
        <img style="width: 200px;height: 200px;" src="''' + str(payQrcode) + '''">
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        // <button type="button" class="btn btn-primary" style="float:right;">download</button>
      </div>
    </div>
  </div>
</div>

</div>
<script>
    $("#girlMoney").click(function() {
var modalShowMoneyDiv = document.getElementById('modalShowMoney');
modalShowMoneyDiv.style.display = 'block';
})
</script>
    <script src="/static/website_v2/js/jquery-2.1.1.min.js" type="text/javascript"></script>
    <script src="/static/website_v2/js/main.js"></script>
    <!-- Resource jQuery --></body>
'''
    return payContact