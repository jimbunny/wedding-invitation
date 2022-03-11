<template>
  <div class="about">
    <!-- <s-header :name="'ติดต่อ'"></s-header> -->
    <div class="about-body">
      <van-divider :style="{ color: 'rgb(23, 157, 254)', borderColor: 'rgb(23, 157, 254)', fontSize: '20px', fontWeight: 500 }">เกี่ยวกับเรา</van-divider>
      <div>Unicard
      </div>
      <van-divider :style="{ color: 'rgb(23, 157, 254)', borderColor: 'rgb(23, 157, 254)', fontSize: '20px', fontWeight: 500 }"></van-divider>
      <div style="margin: auto;">
        <div class="share-body" style="text-align: center;">
          <qr-code id="imageWrapper" :appSrc="appSrc" :logoSrc="logoSrc" :size="300"></qr-code>
          <van-field input-align="center" :value="appSrc" disabled/>
          <div style="margin: 16px;">
            <van-button round block type="info"  @click="goUrl(appSrc)">ติดต่อ UniEcard</van-button>
          </div>
        </div>
      </div>
    </div>
    <nav-bar></nav-bar>
  </div>
</template>

<script>
import sHeader from '@/components/SimpleHeader'
import QrCode from '@/components/QrCode'
import navBar from '@/components/NavBar'

export default {
  components: {
    // sHeader,
    QrCode,
    navBar
  },// mixins: [Clipboard],
  data() {
    return {
      logoSrc: require('../assets/logo.png'),
    }
  },
  computed: {
    appSrc:{
      //getter
      get:function(){
        return 'https://line.me/ti/p/ygpofTh9w1'
      },
      //setter
      set:function(newValue){
        // 这里由于该计算属性被赋值，将被调用
      }
    }
  },
  async created() {
    
  },
  methods: {
    goUrl(url){
      window.location.href = url
    },
  }
}
</script>

<style lang="less" scoped>
  .about {
    box-sizing: border-box;
    padding: 20px;
    .about-body {
      margin-top: 0px;
      font-size: 16px;
      a {
        color: #007fff;
      }
    }
  }
</style>
