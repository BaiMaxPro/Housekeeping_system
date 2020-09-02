<template>
  <v-app>
    <v-app-bar app dark>
      <v-toolbar-title>家政服务管理</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn v-if="!loggedIn" to="/login">登录</v-btn>
      <v-btn v-else>{{ user.username }}已登录</v-btn>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',

  components: {
  },

  computed: {
    ...mapGetters(['loggedIn', 'user']),
  },

  mounted() {
    this.$store.dispatch("recoverSession");
  },

  data: () => ({
  }),
};
</script>
