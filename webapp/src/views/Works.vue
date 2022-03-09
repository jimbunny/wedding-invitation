<template>
    <!-- <s-header :name="'Works'"></s-header> -->
    <div style="width:100%;height:100%;">
      <header class="simple-header-left">
        <div  style="color:red;width:40px;text-align:center;margin-top:10px;border-radius: 10px;"  @click="goToHome">
          <img style="width:40px;" :src="require('../assets/back.png')" alt="">
          </div>
        <div style="color:red;width:40px;text-align:center;margin-top:10px;border-radius: 10px;"  @click="goToAbout">
          <img style="width:40px;" :src="require('../assets/LINE1.png')" alt="">
        </div>
      </header>
    <div style="width:100%;height:100%;">
      <iframe id="iframeId" style="width:100%;height:100%;" frameborder=0 scrolling=auto :src=iframeUrl></iframe>
    </div>
    </div>
</template>

<script>
import { Toast } from 'vant'
import sHeader from '@/components/SimpleHeader'

export default {
  components: {
    // sHeader
  },
  data() {
    return {
      iframeUrl: '',
    }
  },
  components: {
    sHeader,
    // VueCropper
  },
  async mounted() {
     const { id } = this.$route.params
     this.iframeUrl = 'http://127.0.0.1:5678/api/v1/h5/work/' + id.toString()
  },
  computed: {
  },
  methods: {
    goToAbout() {
      this.$router.push({ path: '/about' })
    },
    goToHome() {
      this.$router.push({ path: '/home' })
    },
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
<style lang="less" scoped>
  @import '../common/style/mixin';
  .simple-header-left {
    position: fixed;
    top: 0px;
    left: 0px;
    opacity: 0.8;
    z-index: 10000;
    .fj();
    .wh(100%, 44px);
    line-height: 34px;
    padding: 0 10px;
    .boxSizing();
    color: #252525;
    // border-bottom: 1px solid #dcdcdc;
    .simple-header-name {
      font-size: 14px;
    }
  }
  
</style>
