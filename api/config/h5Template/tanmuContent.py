tanmuContent = '''
     
<style>
    .barrage-input-tip {
        z-index: 1999;
        position: absolute;
        left: 10px;
        width: 179.883px;
        height: 35.7422px;
        line-height: 35.7422px;
        border-radius: 35.7422px;
        box-sizing: border-box;
        color: rgb(255, 255, 255);
        margin-left: 45.7031px;
        background-color: {{ data.tanmuBtnColor }};
        opacity: 0.65;
        pointer-events: initial;
        padding: 0px 16.9922px;
        font-size: 14.0625px;
        display: block;
    }
    .data-box{display:none}
    .barrage_box_top{width:100%;height:160px;margin:0px auto;}
    .barrage_box_top .barrage-row{margin-bottom:20px;}
    .barrage_box_top .barrage-item{
    background-color: {{ data.tanmuColor }};margin-bottom:10px; white-space:nowrap;color:{{ data.fontColor }}; font-size: 12px; transform: scale(1); opacity: 1; transition: all 0.65s ease-in 0s;padding: 6px 8px 0px 8px; height: 32px;display: inline-block;border-radius: 25px;
    }
</style>

<div class="maka-barrage-dom" style="top: 0px; left: 0px; background-color: transparent; z-index: 1000;">
    <div class="barrage-content" style="position: fixed; box-sizing: border-box; padding: 11.7188px; right: 0px; bottom: 0px; z-index: 1000; width: 100%; pointer-events: none; background: linear-gradient(rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.2) 100%);">
        <div class="barrage-words row" style="margin-top: 11.7188px; height: 212.695px;"><div class="barrage-word" style="min-height: 32.2266px; line-height: 32.2266px; font-size: 12.8906px; padding: 4.10156px; border-radius: 22.8516px; bottom: 94.3359px; max-width: 310.547px; background-color: rgba(47, 50, 52, 0.6); transform: scale(1); opacity: 0; transition: bottom 2s ease-out 0s, opacity 0.75s linear 0.75s;">
        </div>
    </div>
    <div class="barrage-bottom row" id="barrageBtn" style="padding-bottom: env(safe-area-inset-bottom); margin-top: 14.0625px; position: fixed; left: 11.7188px; bottom: 47px; pointer-events: initial;">
        <div class="barrage-input-tip" data-toggle="modal" data-target="#myModal"  style="background:{{ data.tanmuColor }}; width: 179.883px; height: 35.7422px; line-height: 35.7422px; border-radius: 35.7422px; box-sizing: border-box; color: rgb(255, 255, 255); margin-left: 45.7031px; background-color: rgb(47, 50, 52); opacity: 0.65; pointer-events: initial; padding: 0px 16.9922px; font-size: 14.0625px;">ฝากคำอวยพร...</div>
    </div>
    <div class="backdrop" style="position: fixed; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0); z-index: 999; display: none; top: 0px; left: 0px; pointer-events: initial;"></div>
    <div class="barrage-btn tanBtn" style="padding-bottom: env(safe-area-inset-bottom); margin-top: 14.0625px; position: fixed; left: 11.7188px; bottom: 11.7188px; pointer-events: initial;">
      <div class="correct-icon" id="tanmuOpen" style="background: url(&quot;https://i.ibb.co/1QmGHWV/danmu-open1.png&quot;) 0% 0% / contain no-repeat; border-radius: 100%; width: 35.7422px; height: 35.7422px;"></div>
      <div class="close-icon" id="tanmuClose" style="background: url(&quot;https://i.ibb.co/QNwcxLx/danmu-close1.png&quot;) 0% 0% / contain no-repeat; border-radius: 100%; width: 35.7422px; height: 35.7422px; display: none;">
        <b style="position: absolute; color: rgb(255, 255, 255); top: 2.92969px; left: 19.9219px; font-weight: 600; font-size: 8.78906px; transform: scale(0.8);">{{ data.greetings | length }}</b>
      </div>
    </div>
    <div id="j-barrage-top" class="barrage_box barrage_box_top" style="position: fixed; box-sizing: border-box; padding: 0px; right: 0px; bottom: 0px; z-index: 1000; width: 100%; pointer-events: none;"></div>
  </div>
  <div class="barrage-input-wrap" id="modalShow" style="display: none; position: fixed; left: 0px; bottom: 0px;height: 0px; width: 100%; background-color:transparent; padding: 9.375px 11.7188px; box-sizing: border-box; z-index: 2000; pointer-events: initial;">

    <!-- 模态框（Modal） -->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div style="width:100%;" class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" style="cursor: pointer;" data-dismiss="modal" aria-hidden="true">×</button>
                    <h4 class="modal-title" id="myModalLabel">อวยพร</h4>
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
</div>
<div class="alert alert-danger hide">ส่งคำอวยพรล้มเหลว！</div>
<div class="alert alert-success hide">ส่งคำอวยพรสำเร็จ！</div>
  
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
        white-space:nowrap;
        overflow:hidden;
        text-overflow:ellipsis;
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
            color:red;
        }
        50%{
            color:green;
        }
        100%{
            color:#6993f9;
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
      message: 'โปรดกรอกคำอวยพร, ความยาวไม่เกิน 40 ตัวอักษร',
      validators: {
        notEmpty: {
          message: 'โปรดกรอกคำอวยพร'
        },
        stringLength: {
            max: 40,
            message: 'ความยาวไม่เกิน 40 ตัวอักษร'
        },
      }
    },
  }
});
var that = this
$("#subBtn").click(function () {  //非submit按钮点击后进行验证，如果是submit则无需此句直接验证
  $("form").bootstrapValidator('validate');  //提交验证
  if ($("form").data('bootstrapValidator').isValid()) {  //获取验证结果，如果成功，执行下面代码
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
                $(".alert-success").addClass("show");
                window.setTimeout(function(){
                    $(".alert-success").removeClass("show");
                },1000);//显示的时间
            } else {
                $(".alert-danger").addClass("show");
                window.setTimeout(function(){
                    $(".alert-danger").removeClass("show");
                },1000);//显示的时间
            };
        },
        error : function() {
            {#alert("Error！");#}
            $(".alert-danger").addClass("show");
            window.setTimeout(function(){
                $(".alert-danger").removeClass("show");
            },1000);//显示的时间
        }
    });
  }
});
</script>

'''