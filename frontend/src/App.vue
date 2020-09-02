<template>
  <v-app>
    <v-btn class="mx-auto" to="/login">Login</v-btn>
    <router-view></router-view>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {
  },

  data: () => ({
  }),
};
</script>
