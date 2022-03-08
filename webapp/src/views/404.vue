<template>
    
    <div class="404-box">
      <s-header :name="'404'"></s-header>
      <div class="about-body">
        <div style=" position: absolute;top: 50%;left: 50%;height: 30%;width: 20%;margin: -15% 0 0 -25%;">
          <img style="width:200px" :src="require('../assets/404.png')" alt="">  
        </div>
      </div>
    </div>
</template>
<script>
import sHeader from '@/components/SimpleHeader'
export default {
  components: {
    sHeader,
  },
  data() {
    return {

    }
  },
  computed: {
  },
  mounted() {
  },
  activated() {
  },
  methods: {
  }
}
</script>