<template>
  <div class="fill-height">
    <!-- 对于router link进行判断渲染相应组件 -->
    <Home />
  </div>
</template>

<script>

import Home from "../components/customer/Home.vue"

export default {
  mounted: function(){
    this.setDrawer()
  },

  // props: ["active"],

  data: () => ({

  }),

  components: {
    Home,
  },

  methods: {
    setDrawer(){
      this.$store.dispatch('updateDrawer', {
        title: "测试测试",
        items: [
          {title: "测试1"},
          {title: "测试2"},
          {title: "测试3", icon: "mdi-account"},
        ]
      })
    }
  }
};
</script>

<style>

</style>