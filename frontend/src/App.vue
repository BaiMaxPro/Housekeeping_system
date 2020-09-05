<template>
  <v-app>

    <NavDrawer />

    <v-main class="mx-2 my-2">
      <router-view></router-view>
    </v-main>

  </v-app>
</template>

<script>
import { mapGetters } from 'vuex';
import NavDrawer from "./components/NavDrawer.vue"
export default {
  name: 'App',

  components: {
    NavDrawer,
  },

  computed: {
    ...mapGetters(["showDrawer"]),
  },

  data(){
    return {

    }
  },
};
</script>
