<template>
  <div class="about">
    <s-header :name="'About'"></s-header>
    <div class="about-body">
      <van-divider :style="{ color: 'rgb(23, 157, 254)', borderColor: 'rgb(23, 157, 254)', fontSize: '20px', fontWeight: 500 }">introduce</van-divider>
      <div>Unicard
      </div>
      <van-divider :style="{ color: 'rgb(23, 157, 254)', borderColor: 'rgb(23, 157, 254)', fontSize: '20px', fontWeight: 500 }"></van-divider>
      <div style="margin: auto;">
        <div class="share-body" style="text-align: center;">
          <qr-code id="imageWrapper" :appSrc="appSrc" :logoSrc="logoSrc" :size="300"></qr-code>
          <van-field :value="appSrc"/>
          <van-share-sheet
            v-model="showShare"
            :options="options"
            @select="onSelect"
            title="立即分享给好友"
            cancel-text="cancel"
          />
          <div style="margin: 16px;">
            <van-button round block type="info"  @click="showShare=true">add</van-button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import sHeader from '@/components/SimpleHeader'
import QrCode from '@/components/QrCode'
import Clipboard from 'clipboard'
import { Toast } from 'vant'
import html2canvas from 'html2canvas';
let Base64 = require('js-base64').Base64

export default {
  components: {
    sHeader,
    QrCode
  },// mixins: [Clipboard],
  data() {
    return {
      logoSrc: require('../assets/logo.png'),
      showShare: false,
      options: [
        // { name: 'Facebook', icon: 'https://upload.wikimedia.org/wikipedia/commons/4/44/Facebook_Logo.png' },
        { name: '复制链接', icon: 'link', className: "copy"},
        { name: '二维码', icon: 'qrcode' },
      ],
      list: [],
      isLoading: false,
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
    },
    paramsEmail:{
      //getter
      get:function(){
        return this.email
      },
      //setter
      set:function(newValue){
        // 这里由于该计算属性被赋值，将被调用
      }
    },
  },
  async created() {
    
  },
  methods: {
    onSelect(option) {
      if(option.name === '复制链接') {
        this.$copyText(this.appSrc).then( e => {
          Toast("已复制到剪切板，请分享");
        }, function (e) {
          Toast("该浏览器不支持自动复制");
          console.log(e)
        })
      } else if(option.name === '二维码') {
          html2canvas(document.getElementById("imageWrapper")).then(canvas => {
          let saveUrl = canvas.toDataURL('image/png')
          let aLink = document.createElement('a')
          let blob = this.base64ToBlob(saveUrl)
          let evt = document.createEvent('HTMLEvents')
          evt.initEvent('click', true, true)
          aLink.download = '二维码.jpg'
          aLink.href = URL.createObjectURL(blob)
          aLink.click()
        });
      } else {
        window.location.href = 'https://www.facebook.com/sharer.php?u=' + this.appSrc;
      }
      // Toast(option.name);
    },
    //这里把图片转base64
	    base64ToBlob (code) {
	       let parts = code.split(';base64,')
	       let contentType = parts[0].split(':')[1]
	       let raw = window.atob(parts[1])
	       let rawLength = raw.length
	       let uInt8Array = new Uint8Array(rawLength)
	       for (let i = 0; i < rawLength; ++i) {
	           uInt8Array[i] = raw.charCodeAt(i)
	       }
	       return new Blob([uInt8Array], {type: contentType})
	   },
  }
}
</script>

<style lang="less" scoped>
  .about {
    box-sizing: border-box;
    padding: 20px;
    .about-body {
      margin-top: 44px;
      font-size: 16px;
      a {
        color: #007fff;
      }
    }
  }
</style>
