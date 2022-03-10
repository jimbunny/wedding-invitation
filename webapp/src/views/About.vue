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
          <van-field :value="appSrc" disabled/>
          <van-share-sheet
            v-model="showShare"
            :options="options"
            @select="onSelect"
            title="เพิ่มเพื่อน"
            cancel-text="ยกเลิก"
          />
          <div style="margin: 16px;">
            <van-button round block type="info"  @click="goUrl(appSrc)">Add Friend</van-button>
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
import Clipboard from 'clipboard'
import { Toast } from 'vant'
import html2canvas from 'html2canvas';
let Base64 = require('js-base64').Base64
import navBar from '@/components/NavBar'

export default {
  components: {
    sHeader,
    QrCode,
    navBar
  },// mixins: [Clipboard],
  data() {
    return {
      logoSrc: require('../assets/logo.png'),
      showShare: false,
      options: [
        // { name: 'Facebook', icon: 'https://upload.wikimedia.org/wikipedia/commons/4/44/Facebook_Logo.png' },
        { name: 'คัดลอกลิ้ง', icon: 'link', className: "copy"},
        { name: 'คิวอาร์โค้ด', icon: 'qrcode' },
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
    goUrl(url){
      window.location.href = url
    },
    copyUrl() {
      this.$copyText(this.appSrc).then( e => {
        Toast("คัดลอกเรียบร้อย โปรดเพิ่มเพื่อนผ่าน Line");
      }, function (e) {
        Toast("บราวเซอร์ไม่รองรับการคัดลอก");
        console.log(e)
      })
    },
    onSelect(option) {
      if(option.name === 'คัดลอกลิ้ง') {
        this.$copyText(this.appSrc).then( e => {
          Toast("คัดลอกเรียบร้อย โปรดเพิ่มเพื่อนผ่าน Line");
        }, function (e) {
          Toast("บราวเซอร์ไม่รองรับการคัดลอก");
          console.log(e)
        })
      } else if(option.name === 'คิวอาร์โค้ด') {
          html2canvas(document.getElementById("imageWrapper")).then(canvas => {
          let saveUrl = canvas.toDataURL('image/png')
          let aLink = document.createElement('a')
          let blob = this.base64ToBlob(saveUrl)
          let evt = document.createEvent('HTMLEvents')
          evt.initEvent('click', true, true)
          aLink.download = 'คิวอาร์โค้ด.jpg'
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
