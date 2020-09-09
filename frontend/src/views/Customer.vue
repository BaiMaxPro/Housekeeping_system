<template>
  <div class="fill-height">
    <Home v-if="currentPage == 'home'" />
  </div>
</template>

<script>

import Home from "../components/customer/Home.vue"

export default {
  mounted: function(){
    this.setDrawer()
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