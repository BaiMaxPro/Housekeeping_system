<template>
  <span>
      <v-btn outlined v-if="!loggedIn" to="/login">
        <v-icon>mdi-account</v-icon>
        <span>登录</span>
      </v-btn>
      <v-btn outlined v-else>
        <v-icon>mdi-account</v-icon>
        <span>{{ user.username }} 已登录</span>
      </v-btn>
  </span>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'LoginButton',
  
  computed: {
    ...mapGetters(['loggedIn', 'user']),
  },

  mounted() {
    this.$store.dispatch('recoverSession');
  },

}
</script>

<style>

</style>