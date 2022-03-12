<template>
    <div style="width:100%;height:100%;">
      <header class="simple-header-left">
        <div  style="color:blue;width:40px;text-align:center;margin-top:10px;border-radius: 10px;">
          <img style="width:35px;" :src="require('../assets/back.png')" alt="" @click="goToHome">
          <img style="width:40px;" :src="require('../assets/LINE1.png')" alt="" @click="goToAbout">
          </div>
        <!-- <div style="color:red;width:40px;text-align:center;margin-top:10px;border-radius: 10px;"  @click="goToAbout">
          <img style="width:40px;" :src="require('../assets/LINE1.png')" alt="">
        </div> -->
      </header>
      <div class="show_iframe">
        <iframe ref="iframe" scrolling="yes" frameborder="0" wicket:id="mainPage" :src=iframeUrl></iframe>
      </div>
    </div>
</template>

<script>
import { Toast } from 'vant'
import sHeader from '@/components/SimpleHeader'


export default {
  components: {
    // sHeader,
  },
  data() {
    return {
      iframeUrl: '',
      loading: true,
    }
  },
  components: {
    sHeader,
    // VueCropper
  },
  async mounted() {
    // this.startLoading()
    const { id } = this.$route.params
    this.iframeUrl = 'https://www.uniecard.com/api/v1/h5/work/' + id.toString()
      
    // const { iframe } = this.$refs;
    // // IE和非IE浏览器，监听iframe加载事件不一样，需要兼容
    // const that = this;
    // if (iframe.attachEvent) {
    //   // IE
    //   iframe.attachEvent('onload', () => {
    //     that.stateChange();
    //   });
    // } else {
    //   // 非IE
    //   iframe.onload = function () {
    //     that.stateChange();
    //   };
    // }
  },
  computed: {
  },
  methods: {
    stateChange() {
      this.loading = false;
      this.endLoading()
    },
    startLoading() {
      // 开始加载
      Toast.loading({
          message: 'loading...',
          forbidClick: true,
      });
    },endLoading() {
      // 结束加载
      Toast.clear()
    },
    goToAbout() {
      // this.$router.push({ path: '/about' })
      window.location.href="https://lin.ee/qO0UuXf"
    },
    goToHome() {
      this.$router.push({ path: '/home' })
    },
  }
}
</script>

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
  .show_iframe{
    -webkit-overflow-scrolling: touch;
    overflow-y: 
    scroll;position: absolute;
    top: 0;
    right: 0;
    left: 0;
    bottom: 0;
  }
  .show_iframe iframe {
    position: absolute;
    bottom: 0;
    height: 100%;
    width: 100%
  }
</style>
