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
    .barrage-more {
        display: none !important;
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
    <div class="barrage-bottom row" id="barrageBtn" style="padding-bottom: env(safe-area-inset-bottom); position: relative; min-height: 35.7422px; width: 100%;">
        <div class="barrage-input-tip" data-toggle="modal" data-target="#myModal"  style="background:{{ data.tanmuColor }}; width: 179.883px; height: 35.7422px; line-height: 35.7422px; border-radius: 35.7422px; box-sizing: border-box; color: rgb(255, 255, 255); margin-left: 45.7031px; background-color: rgb(47, 50, 52); opacity: 0.65; pointer-events: initial; padding: 0px 16.9922px; font-size: 14.0625px;">ฝากคำอวยพร...</div>
    </div>
   <div id="j-barrage-top" class="barrage_box barrage_box_top" style="position: fixed; box-sizing: border-box; padding: 0px; right: 0px; bottom: 0px; z-index: 1000; width: 100%; pointer-events: none;"></div>
    <ul id="data" class="data-box" style="z-index:1999;">
    {% for k in data.greetings %}
        <li style="width:100%;"><div class="barrage-item">{{ k }}</div></li>
    {% endfor %}
    </ul>
    <div class="backdrop" style="position: fixed; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0); z-index: 999; display: none; top: 0px; left: 0px; pointer-events: initial;"></div>
    <div class="barrage-btn tanBtn" style="padding-bottom: env(safe-area-inset-bottom); margin-top: 14.0625px; position: fixed; left: 11.7188px; bottom: 11.7188px; pointer-events: initial;">
      <div class="correct-icon" id="tanmuOpen" style="background: url(&quot;https://i.ibb.co/1QmGHWV/danmu-open1.png&quot;) 0% 0% / contain no-repeat; border-radius: 100%; width: 35.7422px; height: 35.7422px;"></div>
      <div class="close-icon" id="tanmuClose" style="background: url(&quot;https://i.ibb.co/QNwcxLx/danmu-close1.png&quot;) 0% 0% / contain no-repeat; border-radius: 100%; width: 35.7422px; height: 35.7422px; display: none;">
        <b style="position: absolute; color: rgb(255, 255, 255); top: 2.92969px; left: 19.9219px; font-weight: 600; font-size: 8.78906px; transform: scale(0.8);">{{ data.greetings | length }}</b>
      </div>
    </div>
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
                          <input type="text" class="form-control" name="name"  placeholder="ชื่อ-นามสกุล" />
                        </div>
                      </div>
                      <div class="form-group">
                        <div class="col-md-24" style="padding-left:10px;padding-right: 10px;">
                          <input type="text" class="form-control" name="greetings" placeholder="คำอวยพร" />
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

<script>
$(function () {
    var top = new Barrage('#j-barrage-top', {
        //dataUrl: "http://hdsupport.tgbus.com/api/index?aid=36&cid=1&s=get_targets",
        dataBox: "#data",
        number: 3,
        speed: 1,
        hoverStop: true,
        direction: "top",
        //margin: [30,40],
        structure: function (data, index) {
            var text = data.title.substring(0, 50);
            return '<li style="width:100%;">' + text + '</li>';
        }
    });
});

$("#barrageBtn").click(function() {
    var modalShowDiv = document.getElementById('modalShow');
    modalShowDiv.style.display = 'block';
})

var kg = true; //给一个开关并赋值，用来进行后面的 if else 条件判断

$(".tanBtn").click(function() { //给button按钮一个点击事件
     if (kg) { //进行判断
        var tanmuOpenDiv= document.getElementById('tanmuOpen');
        tanmuOpenDiv.style.display = 'block';
        var tanmuCloseDiv= document.getElementById('tanmuClose');
        tanmuCloseDiv.style.display='none';
        var barrageDiv= document.getElementById('j-barrage-top');
        barrageDiv.style.display = 'block';
        var barrageBtnDiv= document.getElementById('barrageBtn');
        barrageBtnDiv.style.display = 'block';

     } else {
        var tanmuOpenDiv= document.getElementById('tanmuOpen');
        tanmuOpenDiv.style.display = 'none';
        var tanmuCloseDiv= document.getElementById('tanmuClose');
        tanmuCloseDiv.style.display='block';
        var barrageDiv= document.getElementById('j-barrage-top');
        barrageDiv.style.display = 'none';
        var barrageBtnDiv= document.getElementById('barrageBtn');
        barrageBtnDiv.style.display = 'none';
        }
    kg = !kg; //这里的感叹号是取反的意思，如果你没有写，当你点击切换回第一张图片时，就会不生效
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
                    var tanmu = $("#mar")
                    var contect = ""
                    for (var i=0;i<result.data.length;i++)
                    {
                        contect = contect + '</br>\n' + '<div class="barrgae-word">'+result.data[i]+'</div>'
                    }
                    tanmu.html(contect)
                };
            },
            error : function() {
                alert("Error！");
            }
        });
      }
    });
</script>

'''