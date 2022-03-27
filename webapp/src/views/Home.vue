<template>
  <div>
    <header class="home-header wrap" :class="{'active' : headerScroll}">
        <span class="app-name">UniEcard</span>
    </header>
    <nav-bar></nav-bar>
    
    <swiper :list="swiperList"></swiper>

    <div class="category-list">
      <div class="item" v-for="item in categoryList" v-bind:key="item.categoryId">
        <div class="gnzs-item" @click="categoryTemplate(item.categoryId)">   
        <img :src="item.imgUrl" :class="item.categoryId==category?'imgChoose':''"><br>
        <span>{{item.name}}</span>
        </div>
      </div>
    </div>

    <div class="good"  :style="{ paddingBottom: '50px'}">
      <!-- <header class="good-header">รูปแบบเทมเพลต</header> -->
      <div class="good-box">
        <div class="good-item" v-for="item in templates" :key="item.id" @click="goToTemplateShow(item.key)">
          <img :src="prefix(item.coverUrl)" alt="">
          <div class="good-desc">
            <div class="title"  style="margin-bottom:5px;">
              {{ item.name }}
            </div>
            <div class="price">จำนวนเข้าชม: {{ item.pageViews }} </div>
          </div>
        </div>
      </div>
    </div>
  
    <div class="contact"  @click="backTop" v-show="headerScroll">
      <div class="btn" >
        <van-icon class="icon-backTop" name="arrow-up" size="25" />
      </div>
    </div>

  </div>
</template>

<script>
import navBar from '@/components/NavBar'
import swiper from '@/components/Swiper'
import { okCode, errorCode } from "../config/settings";
import { getTemplateList, getSwipeList } from '../service/home'
import { Toast } from 'vant'

export default {
  name: 'home',
  data() {
    return {
      swiperList: [],
      headerScroll: false,
      templates: [],
      tmp: [],
      scrollType:false,
      queryForm: {
        pageNo: 1,
        pageSize: 1000,
        name: ""
      },
      category: "all",
      categoryList: [
        {
          name: 'ทั้งหมด',
          imgUrl: 'https://h5.hunbei.com/static/hunbei/img/newIndex/gnzs5.png',
          categoryId: 'all'
        }, {
          name: 'ปกติ',
          imgUrl: 'https://h5.hunbei.com/static/hunbei/img/newIndex/gnzs4.png',
          categoryId: 'normal'
        }, {
          name: 'ซิลเวอร์',
          imgUrl: 'https://h5.hunbei.com/static/hunbei/img/newIndex/gnzs3.png',
          categoryId: "vip"
        }, {
          name: 'โกลด์',
          imgUrl: 'https://h5.hunbei.com/static/hunbei/img/newIndex/gnzs10.png',
          categoryId: "super"
        }, {
          name: 'กำหนดเอง',
          imgUrl: 'https://h5.hunbei.com/static/hunbei/img/newIndex/gnzs8.png',
          categoryId: "customize"
        }
      ],
    }
  },
  components: {
    navBar,
    swiper
  },
  watch: {
    queryForm:{
      handler(newVal,oldVal){
          this.TemplateList();
        },
        deep:true
    }
  },
  async mounted() {
    window.addEventListener('scroll', this.pageScroll)
    Toast.loading({
      message: 'กำลังเข้าสู่ระบบ...',
      forbidClick: true
    });
    getSwipeList().then((res) => {
      const { code, msg, data } = res;
      if (code === okCode) {
        this.swiperList = data;
        setTimeout((_) => {
          Toast.clear()
        }, 300);
      } else {
        Toast.fail('ขณะนี้ระบบขัดข้องอยู่ระหว่างการแก้ไข, กรุณาทำรายการใหม่ภายหลัง!');
      }
    });
    this.TemplateList();
  },
  methods: {
    categoryTemplate(_type) {
      this.category = _type
      if (_type == 'all') {
        this.templates = this.tmp
      } else{
      var storeTmp = []
      for (var i = 0; i < this.tmp.length; i++) {
        if(this.tmp[i]['tags'].indexOf(_type) > -1){
          storeTmp.push(this.tmp[i])
        }
      }
      this.templates = storeTmp
      }
    },
    TemplateList() {
      getTemplateList(this.queryForm).then((res) => {
      const { code, msg, data } = res;
      if (code === okCode) {
        this.tmp = data.data;
        this.templates = data.data;
        setTimeout((_) => {
          Toast.clear()
        }, 300);
      } else {
        Toast.fail('ขณะนี้ระบบขัดข้องอยู่ระหว่างการแก้ไข, กรุณาทำรายการใหม่ภายหลัง!');
      }
    });
    },
    backTop(){
      	document.documentElement.scrollTop = 0
        window.pageYOffset = 0
        document.body.scrollTop = 0
      	/*注意：是给滚动的父元素设置，也就是设置了overflow：auto的元素*/
   	},
    pageScroll() {
      let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
      scrollTop > 100 ? this.headerScroll = true : this.headerScroll = false
    },
    goToTemplateShow(id) {
      // this.$router.push({ path: `works/${id}` })
      window.location.href="https://www.uniecard.com/api/v1/h5/viewer/template/"+ id
    }
  }
}
</script>
<style scoped lang="less" >
  .app{
    display: flex;
    flex: 1;
    height: 100%;
    
    flex-direction: column;
  }

  .contact{
    position:fixed;
    right: 0px;
    bottom: 60px;
    height: 56px;
    
    overflow:hidden;
    transition: width .6s;

    .btn{
      font-size: 14px;
      text-align: center;
      border-radius: 10px 0px 0px 10px;
      padding: 6px 5px;
      background-color: #3c93ef35;
    }
  }

.imgChoose{
    // box-shadow: 0px 0px 16px rgb(0 0 0 / 8%);
    // transform: translateY(-10px);
    // -webkit-transform: translateY(-10px);
    box-shadow: 0 0 15px #149dfe;
    padding:0px
}
.imgChoose:hover {
    box-shadow: 0 0 15px #149dfe;
    padding:0px 
}
</style>
<style lang="less" scoped >
  @import '../common/style/mixin';
  .home-header {
      position: fixed;
      left: 0;
      top: 0;
      .wh(100%, 50px);
      .fj();
      line-height: 50px;
      padding: 0 15px;
      .boxSizing();
      font-size: 15px;
      color: #fff;
      z-index: 10000;
      .app-name {
        padding: 0 10px;
        color: @primary;
        font-size: 20px;
        font-weight: bold;
      }
      &.active {
        background: @primary;
        .app-name {
          padding: 0 10px;
          color: #fff;
          font-size: 20px;
          font-weight: bold;
        }
        .login {
          color: #fff;
        }
      }
      .header-search {
          display: flex;
          .wh(74%, 20px);
          line-height: 20px;
          margin: 10px 0;
          padding: 5px 0;
          color: #232326;
          background: rgba(255, 255, 255, .7);
          border-radius: 20px;
          .app-name {
              padding: 0 10px;
              color: @primary;
              font-size: 20px;
              font-weight: bold;
              border-right: 1px solid #666;
          }
          .icon-search {
              padding: 0 10px;
              font-size: 17px;
          }
          .search-title {
              font-size: 12px;
              color: #666;
              line-height: 21px;
              margin-left:10px;
          }
      }
      .icon-iconyonghu{
        color: #fff;
        font-size: 22px;
      }
      .login {
        color: @primary;
        line-height: 52px;
        .van-icon-manager-o {
          font-size: 20px;
          vertical-align: -3px;
        }
      }
  }
  .category-list {
    display: flex;
    flex-shrink: 0;
    flex-wrap: wrap;
    width: 100%;
    padding-bottom: 13px;
    .item {
      display: flex;
      flex-direction: column;
      width: 20%;
      text-align: center;
      .gnzs-item{
        img {
          .wh(40px, 40px);
          margin: 13px auto 8px auto;
        }
      }
    }
  }
  .good {
    .good-header {
      background: #f9f9f9;
      height: 50px;
      line-height: 50px;
      text-align: center;
      color: @primary;
      font-size: 16px;
      font-weight: 500;
    }
    .good-box {
      display: flex;
      justify-content: flex-start;
      flex-wrap: wrap;
      .good-item {
        box-sizing: border-box;
        width: 50%;
        border-bottom: 1PX solid #e9e9e9;
        padding: 10px 10px;
        img {
          display: block;
          width: 120px;
          margin: 0 auto;
        }
        .good-desc {
          text-align: center;
          font-size: 14px;
          padding: 10px 0;
          .title {
            color: #222333;
          }
          .price {
            color: @primary;
          }
        }
        &:nth-child(2n + 1) {
          border-right: 1PX solid #e9e9e9;
        }
      }
    }
  }
  .floor-list {
      width: 100%;
      padding-bottom: 50px;
      .floor-head {
        width: 100%;
        height: 40px;
        background: #F6F6F6;
      }
      .floor-content {
        display: flex;
        flex-shrink: 0;
        flex-wrap: wrap;
        width: 100%;
        .boxSizing();
        .floor-category {
          width: 50%;
          padding: 10px;
          border-right: 1px solid #dcdcdc;
          border-bottom: 1px solid #dcdcdc;
          .boxSizing();
          &:nth-child(2n) {
            border-right: none;
          }
          p {
            font-size: 17px;
            color: #333;
            &:nth-child(2) {
              padding: 5px 0;
              font-size: 13px;
              color: @primary;
            }
          }
          .floor-products {
            .fj();
            width: 100%;
            img {
              .wh(65px, 65px);
            }
          }
      }
    }
  }
</style>
