<template>
  <div>
    <v-app-bar clipped-left app>
      <v-app-bar-nav-icon @click.stop="drawerShown = !drawerShown" v-if="showDrawer"></v-app-bar-nav-icon>
      <v-toolbar-title>家政服务管理</v-toolbar-title>

      <v-spacer></v-spacer>
      <LoginButton />
    </v-app-bar>

    <v-navigation-drawer app clipped v-model=drawerShown v-if="showDrawer">
      
      <v-list-item v-if="showDrawerTitle">
        <v-list-item-content>
          <v-list-item-title class="title">{{ drawer.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider v-if="showDrawerTitle"></v-divider>

      <v-list dense nav v-if="showDrawerItems">
        <v-list-item v-for="item in drawer.items" :key="item.title" link>
          <v-list-item-icon v-if="item.icon">
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </div>

</template>

<script>
import { mapGetters } from 'vuex'

import LoginButton from "./LoginButton.vue"

export default {
  components: {
    LoginButton,
  },
  computed: {
    ...mapGetters(["drawer", "showDrawer", "showDrawerTitle", "showDrawerItems"]),
  },
  data(){
    return {
      drawerShown: true,
    }
  }
}
</script>

<style>

</style>