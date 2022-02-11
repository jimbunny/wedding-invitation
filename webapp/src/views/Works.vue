<template>
  <div class="works-box">
    <s-header :name="'Works'"></s-header>
    <div class="cart-body">
      <van-checkbox-group @change="groupChange" v-model="result" ref="checkboxGroup">
        <van-swipe-cell :right-width="50" v-for="(item, index) in list" :key="index">
          <div class="good-item">
            <van-checkbox :name="item.id" />
            <div class="good-img"><img :src="prefix(item.picture)" alt=""></div>
            <div class="good-desc">
              <div class="good-title">
                <span>{{ item.name }}</span>
                <!-- <span>x{{ item.goodsCount }}</span> -->
                <!-- <van-button plain @click="goToDetail(item)" size="mini" type="info">detail</van-button> -->
                <van-tag plain @click="goToDetail(item)"  type="primary">detail</van-tag>
              </div>
              <div class="good-btn">
                <div class="price">¥{{ item.outPrice }}</div>
                <!-- <van-stepper
                  integer
                  :min="1"
                  :value="item.goodsCount"
                  :name="item.cartItemId"
                  async-change
                  @change="onChange"
                /> -->
                <van-count-down :time="item.time" ref="countDown" @finish="finish">
                  <template #default="timeData">
                    <span class="block">{{ timeData.hours }}</span>
                    <span class="colon">:</span>
                    <span class="block">{{ timeData.minutes }}</span>
                    <span class="colon">:</span>
                    <span class="block">{{ timeData.seconds }}</span>
                  </template>
                </van-count-down>
              </div>
            </div>
          </div>
          <van-button
            slot="right"
            square
            icon="delete"
            type="danger"
            class="delete-button"
            @click="deleteGood(item.no)"
          />
        </van-swipe-cell>
      </van-checkbox-group>
    </div>
    <van-submit-bar
      v-if="list.length > 0"
      class="submit-all"
      :price="total * 100"
      button-text="结算"
      @submit="onSubmit"
    >
      <van-checkbox @click="allCheck" v-model="checkAll">全选</van-checkbox>
    </van-submit-bar>
    <div class="empty" v-if="!list.length">
    <van-icon name="smile-o" />
      <div class="title">购物车空空空如也</div>
      <van-button color="rgb(23, 157, 254)" type="primary" @click="goTo" block>前往首页</van-button>
    </div>
    <nav-bar></nav-bar> 
    <!--<div class="height100">
      <van-uploader
	  class="mt-3"
	  :max-size="3 * 1024 * 1024"
	  :before-read="beforeRead"
	  @oversize="onOversize"
	>
	  <van-button icon="manager-o" size="small" type="primary">更换头像</van-button>
	</van-uploader>-->
  <!-- 剪裁图片组件 -->
  <!--   <van-popup
      class="bg-tran"
      v-model="showCropper"
      closeable
      position="top"
      :style="{ height: '100%' }"
    >
      <div class="flex-column-center height100">
        <vueCropper
          ref="cropper"
          :img="option.img"
          :outputSize="option.outputSize"
          :outputType="option.outputType"
          :info="option.info"
          :full="option.full"
          :autoCropWidth="option.autoCropWidth"
          :autoCropHeight="option.autoCropHeight"
          :canMove="option.canMove"
          :canMoveBox="option.canMoveBox"
          :original="option.original"
          :autoCrop="option.autoCrop"
          :fixed="option.fixed"
          :fixedNumber="option.fixedNumber"
          :centerBox="option.centerBox"
          :infoTrue="option.infoTrue"
          :fixedBox="option.fixedBox"
          :high="option.high"
          :mode="option.mode"
        ></vueCropper>
        <div class="popup_bottom">
          <div class="bottom_item"><span @click="cancelCropper">取消</span></div>
          <div class="bottom_item"><span @click="rotateImage" class="font18"><van-icon name="replay" /></span></div>
          <div class="bottom_item"><span @click="getCropBlob">确定</span></div>
        </div>
      </div>
    </van-popup>
    </div>
  </div>-->
  </div>
</template>

<script>
import { Toast } from 'vant'
import navBar from '@/components/NavBar'
import sHeader from '@/components/SimpleHeader'
import { VueCropper }  from 'vue-cropper' 
// import { getCart, deleteCartItem, modifyCart } from '../service/cart'
import { okCode } from '../config/settings'

export default {
  data() {
    return {
      checked: false,
      list: [],
      all: false,
      result: [],
      checkAll: true,
      email: "",
      showCropper: false, // 截图弹窗遮罩默认隐藏
      imageAccept: "/jpg,/png,/jpeg",
      imageFileName: '',
      option: {
        img: '',
        outputSize: 0.8,
        info: false, // 裁剪框的大小信息
        outputType: 'jpeg', // 裁剪生成图片的格式
        canScale: false, // 图片是否允许滚轮缩放
        autoCrop: true, // 是否默认生成截图框
        autoCropWidth: window.innerWidth - 100 + 'px', // 默认生成截图框宽度
        autoCropHeight: window.innerWidth - 100 + 'px', // 默认生成截图框高度
        high: true, // 是否按照设备的dpr 输出等比例图片
        fixedBox: true, // 固定截图框大小 不允许改变
        fixed: true, // 是否开启截图框宽高固定比例
        fixedNumber: [1, 1], // 截图框的宽高比例
        full: true, // 是否输出原图比例的截图
        canMoveBox: false, // 截图框能否拖动
        original: false, // 上传图片按照原始比例渲染
        centerBox: false, // 截图框是否被限制在图片里面
        infoTrue: false, // true 为展示真实输出图片宽高 false 展示看到的截图框宽高
        mode: '100% auto' // 图片默认渲染方式
      },
    }
  },
  components: {
    navBar,
    sHeader,
    // VueCropper
  },
  async mounted() {
    // const user = await this.$store.dispatch("user/getInfo");
    // this.email = user.email
    // this.init()
  },
  computed: {
    total: function() {
      let sum = 0
      let _list = this.list.filter(item => this.result.includes(item.id))
      _list.forEach(item => {
        sum += item.outPrice
      })
      return sum
    },
  },
  methods: {
    // 上传文件过大
		onOversize() {
		  this.$toast('图片不能大于3M');
		},
		
		// 获取文件后缀
		getFileSuffix(fileName) {
		  return fileName.match(/\/\w+$/)[0].toLowerCase();
		},
		
		// 选择图片上传前操作，调起剪裁组件
		beforeRead(file) {
		  if (!this.imageAccept.includes(this.getFileSuffix(file.type))) {
		    return this.$toast('请上传 jpg/png 格式图片');
		  }
		  this.showCropper = true;
		  this.imageFileName = file.name;
		  // 本地图片转成base64，用于截图框显示本地图片
		  this.imageToBase64(file);
    },
    // 将本地图片转化为Base64，否则vue-cropper组件显示不出要本地需要剪裁的图片
    imageToBase64(file) {
      let reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => {
        // 截图框中的图片
        this.option.img = reader.result;
      }
      reader.onerror = function (error) {
        console.log('Error: ', error)
      }
    },

    // 确认剪裁并上传图片
    async getCropBlob() {
      this.$toast('上传中', 0);
      let formData = new FormData();
      this.$refs.cropper.getCropBlob((data) => {
        formData.append('avatar', data, this.imageFileName);
        // formData私有类对象，访问不到，可以通过get判断值是否传进去
        console.log(formData,formData.get('avatar'));
        // 上传图片至服务器
        changeAvatar(formData)
        .then(res => {
          if(res.code === 200){
            this.$toast('更改头像成功');
          } else {
            this.$toast('上传失败');
          }
        })
        .catch(err => console.error(err));
      })
    },

    // 旋转图片
    rotateImage() {
      this.$refs.cropper.rotateRight();
    },

    // 取消截图上传头像
    cancelCropper() {
      this.showCropper = false; // 隐藏切图遮罩
      this.showPopup = true;
    },
    goToDetail(item) {
      this.$router.push({ path: `product/${item.no}` })
    },
    async init() {
      Toast.loading({ message: '加载中...', forbidClick: true });
      const { code, data } = await getCart({ email: this.email })
      if (code === okCode) {
        this.list = data
        this.result = data.map(item => item.id)
      } else {
        Toast.fail('获取购物车信息失败！')
      }
      Toast.clear()
    },
    goBack() {
      this.$router.go(-1)
    },
    goTo() {
      this.$router.push({ path: 'home' })
    },
    finish() {
      this.init();
    },
    async onChange(value, detail) {
      if (this.list.filter(item => item.id == detail.name)[0].goodsCount == value) return
      Toast.loading({ message: '修改中...', forbidClick: true });
      const params = {
        cartItemId: detail.name,
        goodsCount: value
      }
      const { data } = await modifyCart(params)
      this.list.forEach(item => {
        if (item.cartItemId == detail.name) {
          item.goodsCount = value
        }
      })
      Toast.clear();
    },
    async onSubmit() {
      if (this.result.length == 0) {
        Toast.fail('请选择商品进行结算')
        return
      }
      const params = JSON.stringify(this.result)
      // for(let i = 0; i < this.result.length; i++) {
      //   await deleteCartItem(this.result[i])
      // }
      this.$router.push({ path: `create-order?cartItemIds=${params}` })
    },
    async deleteGood(no) {
      const { data } = await deleteCartItem({no: no})
      this.$store.dispatch('user/updateCart',{"email": this.email})
      this.init()
    },
    groupChange(result) {
      if (result.length == this.list.length) {
        this.checkAll = true
      } else {
        this.checkAll = false
      }
      this.result = result
    },
    allCheck(value) {
      if (!this.checkAll) {
        this.result = this.list.map(item => item.id)
      } else {
        this.result = []
      }
    }
  }
}
</script>

<style lang="less" scoped>
.height100 {
	height: 100vh;
}
.flex-column-center{ 
	display: flex;
	flex-flow: column;
	justify-content: center;
	align-items: center;
}
.vue-cropper {
  	background: #000;
  	.cropper-view-box {
	  	outline: 1px solid #fff !important;
	  	outline-color: #fff !important;
 	}
}
.popup_bottom{
  width: 100%;
  height: 50px;
  display: flex;
  align-items: center;
  .bottom_item{
    flex:1;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
  }
}
</style>
<style lang="less">
  @import '../common/style/mixin';
  .colon {
    display: inline-block;
    margin: 0 4px;
    color: #ee0a24;
  }
  .block {
    display: inline-block;
    width: 22px;
    color: #fff;
    font-size: 12px;
    text-align: center;
    background-color: #ee0a24;
  }
  .works-box {
    .cart-header {
      position: fixed;
      top: 0;
      left: 0;
      z-index: 10000;
      .fj();
      .wh(100%, 44px);
      line-height: 44px;
      padding: 0 10px;
      .boxSizing();
      color: #252525;
      background: #fff;
      border-bottom: 1px solid #dcdcdc;
      .cart-name {
        font-size: 14px;
      }
    }
    .cart-body {
      margin: 60px 0 100px 0;
      padding-left: 10px;
      .good-item {
        display: flex;
        .good-img {
          img {
            .wh(100px, 100px)
          }
        }
        .good-desc {
          display: flex;
          flex-direction: column;
          justify-content: space-between;
          flex: 1;
          padding: 20px;
          .good-title {
            display: flex;
            justify-content: space-between;
          }
          .good-btn {
            display: flex;
            justify-content: space-between;
            .price {
              font-size: 16px;
              color: red;
              line-height: 28px;
            }
            .van-icon-delete {
              font-size: 20px;
              margin-top: 4px;
            }
          }
        }
      }
      .delete-button {
        width: 50px;
        height: 100%;
      }
    }
    .empty {
      width: 50%;
      margin: 0 auto;
      text-align: center;
      margin-top: 200px;
      .van-icon-smile-o {
        font-size: 50px;
      }
      .title {
        font-size: 16px;
        margin-bottom: 20px;
      }
    }
    .submit-all {
      margin-bottom: 50px;
      .van-checkbox {
        margin-left: 10px
      }
      .van-submit-bar__text {
        margin-right: 10px
      }
      .van-submit-bar__button {
        background: @primary;
      }
    }
    .van-checkbox__icon--checked .van-icon {
      background-color: @primary;
      border-color: @primary;
    }
  }
</style>
