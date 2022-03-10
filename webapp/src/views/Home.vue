<template>
  <div>
    <header class="home-header wrap" :class="{'active' : headerScroll}">
        <span class="app-name">UniEcard</span>
        <!-- <img class="logo" :src="require('../assets/logo.png')" alt=""> -->
        <!--<div class="header-search">-->
            <!--<span class="app-name">JP</span>
            <i class="iconfont icon-search"></i> -->
            <!--<router-link tag="span" class="search-title" to="./product-list?from=home">  please input keyword
            </router-link>
        </div>-->
    </header>
    <nav-bar></nav-bar>
    
    <swiper :list="swiperList"></swiper>

    <div class="good"  :style="{ paddingBottom: '50px'}">
      <header class="good-header">template</header>
      <div class="good-box">
        <div class="good-item" v-for="item in templates" :key="item.id" @click="goToTemplateShow(item.key)">
          <img :src="prefix(item.coverUrl)" alt="">
          <div class="good-desc">
            <div class="title"  style="margin-bottom:5px;">
              {{ item.name }}
            </div>
            <div class="price">pageViews: {{ item.pageViews }} </div>
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
import { getLocal } from '@/common/js/utils'
import { Toast } from 'vant'

export default {
  name: 'home',
  data() {
    return {
      swiperList: [],
      headerScroll: false,
      templates: [],
      scrollType:false,
      queryForm: {
        pageNo: 1,
        pageSize: 1000,
        name: ""
      },
      name:""
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
    onChange(e) {
      this.setData({
        value: e.detail,
      });
    },
    onSearch() {
      Toast('搜索' + this.data.key);
    },
    onClick() {
      Toast('搜索' + this.data.key);
    },
    TemplateList() {
      getTemplateList(this.queryForm).then((res) => {
      const { code, msg, data } = res;
      if (code === okCode) {
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
      this.$router.push({ path: `works/${id}` })
      // window.location.href=url
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
