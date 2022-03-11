<template>
  <div class="about">
    <!-- <s-header :name="'ติดต่อ'"></s-header> -->
    <div class="about-body">
       <van-divider :style="{ color: 'rgb(23, 157, 254)', borderColor: 'rgb(23, 157, 254)', fontSize: '20px', fontWeight: 500 }">เกี่ยวกับเรา</van-divider>
        <div>
        UniEcard (ยูนิอีการ์ด) จะทำให้การ์ดแต่งงานของคุณแตกต่าง น่าจดจำ และประทับใจมากยิ่งขึ้นมากกว่าเดิม ทางเราให้บริการการ์ดแต่งงานในรูปแบบออนไลน์ โดยว่าที่เจ้าบ่าวเจ้าสาว สามารถแชร์ความรักของท่านผ่านทางโซเชียลมีเดีย (Social Media) ได้อย่างเต็มที่ ผู้รับชมจะได้รับประสบการณ์ความรักและเป็นพยานรักของท่านในครั้งนี้ ที่ต่างออกไปจากรูปแบบเดิมโดยสิ้นเชิง
        <br><br>
        ขั้นตอนการสั่งซื้อ<br>
        (1) เลือกรูปแบบเทมเพลต<br>
        (2) ติดต่อ UniEcard ทางไลน์<br>
        (3) เลือกโปรโมชั่นและฟังก์ชั่นของการ์ด<br>
        (4) วางเงินมัดจำ และจัดเตรียมข้อมูลให้ UniEcard<br>
        (5) UniEcard ส่งแบบร่างการ์ด<br>
        (6) จ่ายเงินส่วนสุดท้าย พร้อมรับ UniEcard<br>
        <br>  
        หมายเหตุ ลูกค้าจะได้การ์ดแต่งงานออนไลน์รูปแบบ Link และสามารถแก้ไขข้อมูลได้ตามจำนวนครั้งของโปรโมชั่นที่ซ
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
      padding-bottom: 50px;
      a {
        color: #007fff;
      }
    }
  }
</style>
