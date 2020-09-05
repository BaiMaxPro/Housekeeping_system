<template>
  <p>Home</p>
</template>

<script>

export default {
  name: 'Home',
  mounted(){
    this.$store.dispatch("updateDrawer", {})
  },
  components: {

  }
}
</script>
