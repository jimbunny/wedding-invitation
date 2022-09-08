
def tanmuContent(template_type="turn"):
    disappear = '''
    .barrage-content {
        display:block;
        position: fixed;
        ox-sizing: border-box; 
        right: 0px; 
        bottom: 0px; 
        z-index: 1001; 
        width: 100%; 
        pointer-events: none; 
        background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.2) 100%);
    }'''
    disappear2 = ''
    if template_type == "turn":
        disappear = '''
        .barrage-content {
            display:none;
            position: fixed;
            ox-sizing: border-box; 
            right: 0px; 
            bottom: 0px; 
            z-index: 1000; 
            width: 100%; 
            pointer-events: none; 
            background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.2) 100%);
        }
        '''
        disappear2 = '''
               .cd-stretchy-nav {
                   display: none;
               }'''

    tanmuContent = '''
    <script src="/static/website_v2/js/jquery-2.1.1.min.js" type="text/javascript"></script>
    <script src="/static/website_v2/js/main.js"></script>
    <!-- Resource jQuery -->
    
    <style>
        .barrage-input-tip {
            z-index: 1000;
            position: absolute;
            left: 10px;
            width: calc(100% - 65px - {{ data.isGPS }}*40px - {{ data.isFunction }}*60px - {{ data.isPay }}*40px - {{ data.isPresent }}*40px);
            height: 35px;
            line-height: 35px;
            border-radius: 35px;
            box-sizing: border-box;
            color: {{ data.tanmuBtnFontColor }};
            margin-left: 45.7031px;
            background-color: {{ data.tanmuBtnColor }};
            opacity: 0.65;
            pointer-events: initial;
            padding: 0px 17px;
            font-size: 14px;
            display: block;
        }
        .data-box{display:none}
        .barrage_box_top{width:100%;height:160px;margin:0px auto;}
        .barrage_box_top .barrage-row{margin-bottom:20px;}
        .barrage_box_top .barrage-item{
        background-color: {{ data.tanmuColor }};margin-bottom:10px; white-space:nowrap;color:{{ data.fontColor }}; font-size: 12px; transform: scale(1); opacity: 1; transition: all 0.65s ease-in 0s;padding: 6px 8px 0px 8px; height: 32px;display: inline-block;border-radius: 25px;
        }
        @keyframes tanlianxia{0%{-webkit-transform:translateY(0px);}8%{-webkit-transform:translateY(-10px);}13%{-webkit-transform:translateY(0px);}16%{-webkit-transform:translateY(-5px);}19%{-webkit-transform:translateY(0px);}22%{-webkit-transform:translateY(-2px);}25%{-webkit-transform:translateY(0px);}100%{-webkit-transform:translateY(0px);}}
		@keyframes tanlianxia2{0%{-webkit-transform:translateX(0px) rotate(90deg);}8%{-webkit-transform:translateX(10px) rotate(90deg);}13%{-webkit-transform:translateX(0px) rotate(90deg);}16%{-webkit-transform:translateX(5px) rotate(90deg);}19%{-webkit-transform:translateX(0px) rotate(90deg);}22%{-webkit-transform:translateX(2px) rotate(90deg);}25%{-webkit-transform:translateX(0px) rotate(90deg);}100%{-webkit-transform:translateX(0px) rotate(90deg);}}
        @-webkit-keyframes tanlianxia{0%{-webkit-transform:translateY(0px);}8%{-webkit-transform:translateY(-10px);}13%{-webkit-transform:translateY(0px);}16%{-webkit-transform:translateY(-5px);}19%{-webkit-transform:translateY(0px);}22%{-webkit-transform:translateY(-2px);}25%{-webkit-transform:translateY(0px);}100%{-webkit-transform:translateY(0px);}}
		@-webkit-keyframes tanlianxia2{0%{-webkit-transform:translateX(0px) rotate(90deg);}8%{-webkit-transform:translateX(10px) rotate(90deg);}13%{-webkit-transform:translateX(0px) rotate(90deg);}16%{-webkit-transform:translateX(5px) rotate(90deg);}19%{-webkit-transform:translateX(0px) rotate(90deg);}22%{-webkit-transform:translateX(2px) rotate(90deg);}25%{-webkit-transform:translateX(0px) rotate(90deg);}100%{-webkit-transform:translateX(0px) rotate(90deg);}}
    
        ''' + str(disappear) + '''
    </style>
    
    <div class="maka-barrage-dom" style="top: 0px; left: 0px; background-color: transparent; z-index: 1000;">
        <div class="barrage-content">
            <div class="barrage-words row" style="margin-top: 11.7188px; height: 212.695px;"><div class="barrage-word" style="min-height: 32.2266px; line-height: 32.2266px; font-size: 12.8906px; padding: 4.10156px; border-radius: 22.8516px; bottom: 94.3359px; max-width: 310.547px; background-color: rgba(47, 50, 52, 0.6); transform: scale(1); opacity: 0; transition: bottom 2s ease-out 0s, opacity 0.75s linear 0.75s;">
            </div>
        </div>
        
        {% if data.isGPS %}
        <div style="padding-bottom: 5px; margin-top: 14.0625px; position: fixed; right: calc(10px + {{ data.isFunction }}*60px); bottom: 11.7188px; pointer-events: initial;">
          <div id="gpsBtn" class="correct-icon" style="background: url(/static/website_v2/images/gpsBtn.png) 0% 0% / contain no-repeat; border-radius: 100%; width: 35px; height: 35px;"></div>
        </div>
        {% endif %}
        {% if data.isPay %}
        <div style="padding-bottom: 5px; margin-top: 14.0625px; position: fixed; right: calc(10px + {{ data.isGPS }}*40px + {{ data.isFunction }}*60px); bottom: 11.7188px; pointer-events: initial;">
          <div  id="girlMoney" data-toggle="modal" data-target="#moneyModalCenter" class="correct-icon"  style="animation:6s ease 0s infinite normal none running tanlianxia ; -webkit-animation:6s ease 0s infinite normal none running tanlianxia; background: url(/static/website_v2/images/moneyBtn.png) 0% 0% / contain no-repeat; border-radius: 100%; width: 35px; height: 35px;"></div>
        </div>
        {% endif %}
        {% if data.isPresent %}
        <div style="padding-bottom: 5px; margin-top: 14.0625px; position: fixed; right: calc(10px + {{ data.isGPS }}*40px + {{ data.isPay }}*40px + {{ data.isFunction }}*60px); bottom: 11.7188px; pointer-events: initial;">
          <div class="correct-icon" id="present" data-toggle="modal" data-target="#presentModal" style="animation:6s ease 0s infinite normal none running tanlianxia ; -webkit-animation:6s ease 0s infinite normal none running tanlianxia; background: url(/static/website_v2/images/presentBtn.png) 0% 0% / contain no-repeat; border-radius: 100%; width: 35px; height: 35px;"></div>
        </div>
        {% endif %}

        <div class="barrage-bottom row" id="barrageBtn" style="padding-bottom: 0px; margin-top: 14.0625px; width:100%; position: fixed; left: 11.7188px; bottom: 52px; pointer-events: initial;">
            <div class="barrage-input-tip" data-toggle="modal" data-target="#myModal">ฝากคำอวยพร...</div>
        </div>
        <div class="backdrop" style="position: fixed; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0); z-index: 999; display: none; top: 0px; left: 0px; pointer-events: initial;"></div>
        <div class="barrage-btn tanBtn" style="padding-bottom: 0px; margin-top: 14.0625px; position: fixed; left: 11.7188px; bottom: 16.7188px; pointer-events: initial;">
          <div class="correct-icon" id="tanmuOpen" style="background: url(/static/website_v2/images/tanmuOpen.png) 0% 0% / contain no-repeat; border-radius: 100%; width: 35px; height: 35px;"></div>
          <div class="close-icon" id="tanmuClose" style="background: url(/static/website_v2/images/tanmuClose.png) 0% 0% / contain no-repeat; border-radius: 100%; width: 35px; height: 35px; display: none;">
            <b style="position: absolute; color: rgb(255, 255, 255); top: 3.52969px; left: 19.9219px; font-weight: 600; font-size: 8.78906px; transform: scale(0.8);">{{ data.greetings | length }}</b>
          </div>
        </div>
        <div id="j-barrage-top" class="barrage_box barrage_box_top" style="position: fixed; box-sizing: border-box; padding: 0px; right: 0px; bottom: 0px; z-index: 1000; width: 100%; pointer-events: none;"></div>
      </div>
      <div class="barrage-input-wrap" id="modalShow" style="display: none; position: fixed; left: 0px; bottom: 0px;height: 0px; width: 100%; background-color:transparent; padding: 9.375px 11.7188px; box-sizing: border-box; z-index: 2000000000000; pointer-events: initial;">
    
        <!-- 模态框（Modal） -->
        <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
            <div style="width:100%;" class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" style="cursor: pointer;" data-dismiss="modal" aria-hidden="true">×</button>
                        <h4 class="modal-title" id="myModalLabel" style="color:#000">อวยพร</h4>
                    </div>
                    <div class="modal-body">
                        <form action="" id="form" class="form-horizontal">
                          <div class="form-group">
                            <div class="col-md-24" style="padding-left:10px;padding-right: 10px;">
                              <input type="text" class="form-control" style="width:100% !important;" name="name"  placeholder="ชื่อ-นามสกุล" />
                            </div>
                          </div>
                          <div class="form-group">
                            <div class="col-md-24" style="padding-left:10px;padding-right: 10px;">
                              <input type="text" class="form-control" style="width:100% !important;" name="greetings" placeholder="คำอวยพร" />
                            </div>
                          </div>
                          <div class="form-group">
                            <div class="col-md-24 col-md-offset-2" style="padding-left:10px;padding-right: 10px;">
                              <button id="subBtn" type="submit" class="btn btn-primary" style="width:100%;">ส่ง</button>
                            </div>
                          </div>
                        </form>
                    </div>
                </div><!-- /.modal-content -->
            </div><!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->
      </div>

        <div class="barrage-input-wrap" id="modalShowPresent" style="display: none; position: fixed; left: 0px; bottom: 0px;height: 0px; width: 100%; background-color:transparent; padding: 9.375px 11.7188px; box-sizing: border-box; z-index: 2000000000000; pointer-events: initial;">

        <!-- 模态框（Modal） -->
        <div class="modal fade" id="presentModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
            <div style="width:100%;" class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" style="cursor: pointer;" data-dismiss="modal" aria-hidden="true">×</button>
                        <h4 class="modal-title" id="myModalLabel" style="color:#000">ลงทะเบียนร่วมงาน</h4>
                    </div>
                    <div class="modal-body">
                        <form action="" id="presentForm" class="form-horizontal">
                          <div class="form-group">
                            <div class="col-md-24" style="padding-left:10px;padding-right: 10px;">
                              <input type="text" class="form-control" style="width:100% !important;" name="name"  placeholder="ชื่อ" />
                            </div>
                          </div>
                          <div class="form-group">
                            <div class="col-md-24" style="padding-left:10px;padding-right: 10px;">
                              <input type="text" class="form-control" style="width:100% !important;" name="present" placeholder="จำนวนผู้ร่วมงาน" />
                            </div>
                          </div>
                          <div class="form-group">
                            <div class="col-md-24 col-md-offset-2" style="padding-left:10px;padding-right: 10px;">
                              <button id="subPresentBtn" type="submit" class="btn btn-primary" style="width:100%;">ส่ง</button>
                            </div>
                          </div>
                        </form>
                    </div>
                </div><!-- /.modal-content -->
            </div><!-- /.modal-dialog -->
        </div>
        <!-- /.modal -->
      </div>

        <div class="barrage-input-wrap" id="modalShowMoney" style="display: none; position: fixed; left: 0px; bottom: 0px;height: 0px; width: 100%; background-color:transparent; padding: 9.375px 11.7188px; box-sizing: border-box; z-index: 2000000000000; pointer-events: initial;">
        <!-- Modal -->
        <div class="modal fade" id="moneyModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
             <div class="modal-header">
                <button type="button" class="close" style="cursor: pointer;" data-dismiss="modal" aria-hidden="true">×</button>
                <h4 class="modal-title" id="myModalLabel" style="color:#000">{{ data.payName }}</h4>
              </div>
              <div class="modal-body">
                <img style="width: 100%;" src="{{ data.payQrCodeUrl }}">
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal" style="color:#000">Close</button>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
    <div class="alert alert-danger tanmuAlertError hide" style="z-index: 999999999999999999999999999999">ส่งคำอวยพรล้มเหลว！</div>
    <div class="alert alert-success tanmuAlertError hide" style="z-index: 999999999999999999999999999999">ส่งคำอวยพรสำเร็จ！</div>
    <div class="alert alert-danger presentAlertError hide" style="z-index: 999999999999999999999999999999">ส่งคำลงทะเบียนร่วมงานล้มเหลว！</div>
    <div class="alert alert-success presentAlertSuccess hide" style="z-index: 999999999999999999999999999999">ส่งคำลงทะเบียนร่วมงานสำเร็จ！</div>
    <script>
    $("#girlMoney").click(function() {
        var modalShowMoneyDiv = document.getElementById('modalShowMoney');
        modalShowMoneyDiv.style.display = 'block';
    })
    $("#present").click(function() {
        var modalShowPresentMoneyDiv = document.getElementById('modalShowPresent');
        modalShowPresentMoneyDiv.style.display = 'block';
    })
    $("#gpsBtn").click(function() {
        window.open("{{ data.GPSUrl }}")
    })
      </script>
  <link rel="stylesheet" href="/static/website_v2/css/reset.css">
    <!-- CSS reset -->
    <link rel="stylesheet" type="text/css" href="/static/website_v2/css/default.css">
    <link rel="stylesheet" href="/static/website_v2/css/menu.css">
    <!-- Resource style -->
    <script src="/static/website_v2/js/modernizr.js"></script>
    <!-- Modernizr -->
    <style> ''' + str(disappear2) + '''
        .cd-stretchy-nav .stretchy-nav-bg {
            background-size: 100% 100%;
            background-image: url("data:image/png;base64,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");
        }
        .cd-stretchy-nav ul a div{
            color: {{ data.functionFontColor }};
            background-color: {{ data.functionBKColor }};
        }
    </style>
    {% if data.isFunction %}
    <nav class="cd-stretchy-nav">
        <a class="cd-nav-trigger">
            <img class="functionMenu" src="{{ data.functionMenuBgImg }}">
        </a>
        <ul>
          <li>
            <a href="{{ data.functionGPSUrl }}" class="active">
                <img style="width: 30px; height: 30px; margin-bottom:5px;" src="/static/website_v2/images/GPS_button.png">
              <div>GPS นำทาง</div>
            </a>
          </li>
          <li>
            <a href="tel:{{ data.functionGirlPhone }} ">
                <img style="width: 30px; height: 30px; margin-bottom:5px;" src="/static/website_v2/images/girl_phone.png">
              <div>เบอร์เจ้าสาว</div></a>
          </li>
          <li style="margin-bottom:25px">
            <a href="tel:{{ data.functionBoyPhone }}">
                <img style="width: 30px; height: 30px; margin-bottom:5px;" src="/static/website_v2/images/boy_phone.png">
              <div>เบอร์เจ้าบ่าว</div></a>
          </li>
        </ul>
        <span aria-hidden="true" class="stretchy-nav-bg"></span>
      </nav>
    {% endif %}
    <script src="/static/js/bootstrap.min.js"></script>
    <script src="/static/js/bootstrapValidator.min.js"></script>
    <script type="text/javascript" src="/static/js/index.js"></script>
    <style type="text/css">
        *{
            padding:0;
            margin:0;
        }
        a{
            text-decoration: none;
        }
    
        .form-control{
            display: inline-block;
            width: auto;
            padding: 6px 12px;
            font-size: 14px;
            line-height: 1.42857143;
            color: #555;
            background-color: #fff;
            background-image: none;
            border: 1px solid #ccc;
            border-radius: 4px;
            -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075);
            box-shadow: inset 0 1px 1px rgba(0,0,0,.075);
            -webkit-transition: border-color ease-in-out .15s,-webkit-box-shadow ease-in-out .15s;
            -o-transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
            transition: border-color ease-in-out .15s,box-shadow ease-in-out .15s;
        }
    
        .btn{
            display: inline-block;
            padding: 6px 12px;
            margin-bottom: 0;
            font-size: 14px;
            font-weight: 400;
            line-height: 1.42857143;
            text-align: center;
            white-space: nowrap;
            vertical-align: middle;
            -ms-touch-action: manipulation;
            touch-action: manipulation;
            cursor: pointer;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
            background-image: none;
            border: 1px solid transparent;
            border-radius: 4px;
        }
    
        .btn-primary {
            color: #fff;
            background-color: #337ab7;
            border-color: #2e6da4;
        }
    
        /*组件主样式*/
        .overflow-text{
            display: block;
            opacity:0;
            clear: both;
            padding:0 10px;
            border-radius: 10px;
            box-sizing: border-box;
            max-width: 100%;
            color:#fff;
            animation:colorchange 3s infinite alternate;
            -webkit-animation:colorchange 3s infinite alternate; /*Safari and Chrome*/
        }
        @keyframes colorchange{
            0%{
                color: {{ data.tanmuFontColor }};
            }
            50%{
                color: {{ data.tanmuFontColor }};
            }
            100%{
                color: {{ data.tanmuFontColor }};
            }
        }
        /*组件主样式*/
        .alert{
            position: fixed;
            width: 50%;
            margin-left: 20%;
            z-index: 2000;
        }
    </style>
    <script type="text/javascript">
      var Obj;
      $.ajax({
            //几个参数需要注意一下
            type: "GET",//方法类型
            dataType: "json",//预期服务器返回的数据类型
            url: "/api/v1/h5/greetings/"+{{ data.id }},//url
            success: function (result) {
                console.log(result);//打印服务端返回的数据(调试用)
                if (result.code == 0) {
                    // 数据初始化
                    Obj = $('#j-barrage-top').barrage({
                        data : result.data, //数据列表
                        row : 1,   //显示行数
                        time : 2500, //间隔时间
                        gap : 100,    //每一个的间隙
                        position : 'fixed', //绝对定位
                        direction : 'bottom left', //方向
                        ismoseoverclose : true, //悬浮是否停止
                        height : 30, //设置单个div的高度
                        bgColor : ['{{ data.tanmuBgColor }}']
                    })
                    Obj.start();
                } else {
                    alert("tanmu Error");
                };
            },
            error : function() {
                alert("tanmu Error");
            }
        });
    
    </script>
    <script>
    
    $("#barrageBtn").click(function() {
    var modalShowDiv = document.getElementById('modalShow');
    modalShowDiv.style.display = 'block';
    })
    
    const myTimeout = setTimeout(closeTanmuFunction, 100);
    
    function closeTanmuFunction() {
      document.getElementById("tanmuOpen").click();
    }
    
    var kg = true; //给一个开关并赋值，用来进行后面的 if else 条件判断
    
    $(".tanBtn").click(function() { //给button按钮一个点击事件
     if (kg) { //进行判断
        var tanmuOpenDiv= document.getElementById('tanmuOpen');
        tanmuOpenDiv.style.display = 'block';
        var tanmuCloseDiv= document.getElementById('tanmuClose');
        tanmuCloseDiv.style.display='none';
        Obj.start();
        var barrageBtnDiv= document.getElementById('barrageBtn');
        barrageBtnDiv.style.display = 'block';
    
     } else {
        var tanmuOpenDiv= document.getElementById('tanmuOpen');
        tanmuOpenDiv.style.display = 'none';
        var tanmuCloseDiv= document.getElementById('tanmuClose');
        tanmuCloseDiv.style.display='block';
        Obj.close();
        var barrageBtnDiv= document.getElementById('barrageBtn');
        barrageBtnDiv.style.display = 'none';
        }
    kg = !kg; //这里的感叹号是取反的意思，如果你没有写，当你点击切换回第一张图片时，就会不生效
    })

    $('#myModal').on('hidden.bs.modal', function (e) {
        // 清空表单和验证
        // Reset a form
        document.getElementById("form").reset();
        $('#form').bootstrapValidator("resetForm",true);
    })
    
    $('#presentModal').on('hidden.bs.modal', function (e) {
        // 清空表单和验证
        // Reset a form
        document.getElementById("presentForm").reset();
        $('#presentForm').bootstrapValidator("resetForm",true);
    })
    
    $('form').bootstrapValidator({
      //默认提示
      message: 'This value is not valid',
      // 表单框里右侧的icon
      feedbackIcons: {
        valid: 'glyphicon glyphicon-ok',
        invalid: 'glyphicon glyphicon-remove',
        validating: 'glyphicon glyphicon-refresh'
      },
      excluded: [':disabled'],
      submitHandler: function (validator, form, submitButton) {
        // 表单提交成功时会调用此方法
        // validator: 表单验证实例对象
        // form jq对象 指定表单对象
        // submitButton jq对象 指定提交按钮的对象
      },
      fields: {
        name: {
          message: 'ปรดกรอกชื่อ, ความยาวไม่เกิน 20 ตัวอักษร',
          validators: {
            notEmpty: {   //不能为空
              message: 'โปรดกรอกชื่อ'
            },
            stringLength: {
                max: 20,
                message: 'ความยาวไม่เกิน 20 ตัวอักษร'
            },
          }
        },
        greetings: {
          message: 'โปรดกรอกคำอวยพร, ความยาวไม่เกิน 400 ตัวอักษร',
          validators: {
            notEmpty: {
              message: 'โปรดกรอกคำอวยพร'
            },
            stringLength: {
                max: 400,
                message: 'ความยาวไม่เกิน 400 ตัวอักษร'
            },
          }
        },
      }
    });

    $('presentForm').bootstrapValidator({
      //默认提示
      message: 'This value is not valid',
      // 表单框里右侧的icon
      feedbackIcons: {
        valid: 'glyphicon glyphicon-ok',
        invalid: 'glyphicon glyphicon-remove',
        validating: 'glyphicon glyphicon-refresh'
      },
      excluded: [':disabled'],
      submitHandler: function (validator, form, submitButton) {
        // 表单提交成功时会调用此方法
        // validator: 表单验证实例对象
        // form jq对象 指定表单对象
        // submitButton jq对象 指定提交按钮的对象
      },
      fields: {
        name: {
          message: 'ปรดกรอกชื่อ, ความยาวไม่เกิน 20 ตัวอักษร',
          validators: {
            notEmpty: {   //不能为空
              message: 'โปรดกรอกชื่อ'
            },
            stringLength: {
                max: 20,
                message: 'ความยาวไม่เกิน 20 ตัวอักษร'
            },
          }
        },
        present: {
          message: 'กรุณากรอกหมายเลข',
          validators: {
            notEmpty: {
              message: 'กรุณากรอกหมายเลข'
            },
          }
        },
      }
    });


    var that = this
    $("#subBtn").click(function () {  //非submit按钮点击后进行验证，如果是submit则无需此句直接验证
      $("#form").bootstrapValidator('validate');  //提交验证
      if ($("#form").data('bootstrapValidator').isValid()) {  //获取验证结果，如果成功，执行下面代码
         $.ajax({
            //几个参数需要注意一下
            type: "POST",//方法类型
            dataType: "json",//预期服务器返回的数据类型
            url: "/api/v1/h5/greetings/"+{{ data.id }},//url
            data: $('#form').serialize(),
            success: function (result) {
                console.log(result);//打印服务端返回的数据(调试用)
                if (result.code == 0) {
                    $("#myModal").modal('hide');
                    //添加评论
                    //此格式与dataa.js的数据格式必须一致
                    var addVal = {
                        text : result.data
                    }
                    //添加进数组
                    Obj.data.unshift(addVal);
                    $(".tanmuAlertSuccess").addClass("show");
                    window.setTimeout(function(){
                        $(".tanmuAlertSuccess").removeClass("show");
                    },1000);//显示的时间
                } else {
                    $(".tanmuAlertError").addClass("show");
                    window.setTimeout(function(){
                        $(".tanmuAlertError").removeClass("show");
                    },1000);//显示的时间
                };
            },
            error : function() {
                {#alert("Error！");#}
                 document.getElementById("form").reset();
                $('#form').bootstrapValidator("resetForm",true);
                $(".tanmuAlertError").addClass("show");
                window.setTimeout(function(){
                    $(".tanmuAlertError").removeClass("show");
                },1000);//显示的时间
            }
        });
      }
    });

    var that = this
    $("#subPresentBtn").click(function () {  //非submit按钮点击后进行验证，如果是submit则无需此句直接验证
      $("#presentForm").bootstrapValidator('validate');  //提交验证
      if ($("#presentForm").data('bootstrapValidator').isValid()) {  //获取验证结果，如果成功，执行下面代码
         $.ajax({
            //几个参数需要注意一下
            type: "POST",//方法类型
            dataType: "json",//预期服务器返回的数据类型
            url: "/api/v1/h5/presents/"+{{ data.id }},//url
            data: $('#presentForm').serialize(),
            success: function (result) {
                console.log(result);//打印服务端返回的数据(调试用)
                if (result.code == 0) {
                    $("#presentModal").modal('hide');
                    $(".presentAlertSuccess").addClass("show");
                    window.setTimeout(function(){
                        $(".presentAlertSuccess").removeClass("show");
                    },1000);//显示的时间
                } else {
                    $(".presentAlertError").addClass("show");
                    window.setTimeout(function(){
                        $(".presentAlertError").removeClass("show");
                    },1000);//显示的时间
                };
            },
            error : function() {
                {#alert("Error！");#}
                document.getElementById("presentForm").reset();
                $('#presentForm').bootstrapValidator("resetForm",true);
                $(".presentAlertError").addClass("show");
                window.setTimeout(function(){
                    $(".presentAlertError").removeClass("show");
                },1000);//显示的时间
            }
        });
      }
    });
    </script>
    
    '''
    return tanmuContent