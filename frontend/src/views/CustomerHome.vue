<template>
  <div>
    CustomerHome
  </div>
</template>

<script>
export default {
  mounted: function(){
    this.setDrawer()
  },

  data: () => ({

  }),

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