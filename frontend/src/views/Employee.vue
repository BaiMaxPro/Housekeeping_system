<template>
  <div class="fill-height">
    <Home v-if="currentPage == 'home'" />
    <Info v-if="currentPage == 'info'" />
    <Order v-if="currentPage == 'order'" />
  </div>
</template>

<script>

import Home from "../components/employee/Home.vue"
import Info from "../components/employee/Info.vue"
import Order from "../components/employee/Order.vue"

export default {
  mounted: function(){
    this.setDrawer();
    this.$store.dispatch("employee/get");
  },

  data: () => ({

  }),

  computed: {
    currentPage: function(){
      return this.$route.params.page
    },
  },

  components: {
    Home,
    Info,
    Order,
  },

  methods: {
    setDrawer(){
      this.$store.dispatch('updateDrawer', {
        title: "雇员应用",
        items: [
          {title: "雇员中心", icon: "mdi-account-heart",href:"./home"},
          {title: "基本信息", icon: "mdi-account",href:"./info"},
          {title: "订单中心", icon: "mdi-sticker-check-outline",href:"./order"},
        ]
      })
    }
  }
};
</script>

<style>

</style>