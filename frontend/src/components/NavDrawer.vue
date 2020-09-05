<template>
  <v-navigation-drawer app clipped v-model=shown v-if="showDrawer">
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
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters(["drawer", "showDrawer", "showDrawerTitle", "showDrawerItems"]),
  },
  props: ['shown'],
}
</script>

<style>

</style>