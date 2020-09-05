<template>
  <v-app>
    <v-app-bar clipped-left app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" v-if="showDrawer"></v-app-bar-nav-icon>
      <v-toolbar-title>家政服务管理</v-toolbar-title>

      <v-spacer></v-spacer>

      <LoginButton />

    </v-app-bar>

    <NavDrawer v-bind:shown="drawer" />

    <v-main class="mx-2 my-2">
      <router-view></router-view>
    </v-main>

  </v-app>
</template>

<script>
import { mapGetters } from 'vuex';
import LoginButton from "./components/LoginButton.vue"
import NavDrawer from "./components/NavDrawer.vue"
export default {
  name: 'App',

  components: {
    LoginButton,
    NavDrawer,
  },

  computed: {
    ...mapGetters(["showDrawer"]),
  },

  data: () => ({
    drawer: true,
  }),
};
</script>
