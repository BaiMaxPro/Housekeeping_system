<template>
  <span>
      <v-btn outlined v-if="!loggedIn" to="/login">
        <v-icon>mdi-account</v-icon>
        <span>登录</span>
      </v-btn>
      <v-menu open-on-hover v-else offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn outlined v-bind="attrs" v-on="on">
            <v-icon>mdi-account</v-icon>
            <span>{{ user.username }} 已登录</span>
          </v-btn>
        </template>

        <v-list>
          <v-list-item :to="userHome.link">
            <v-list-item-title>{{ userHome.name }}</v-list-item-title>
          </v-list-item>
          <v-list-item v-on:click="logout">
            <v-list-item-title>退出登录</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
  </span>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'LoginButton',
  
  computed: {
    ...mapGetters(['loggedIn', 'user']),
    userHome: function(){
      if(this.user.role == "customer") return {name: "顾客中心", link: "/customer/home"};
      if(this.user.role == "employee") return {name: "员工中心", link: "/employee/home"};
      return {name: "用户中心", link: "/"};
    },
  },

  mounted() {
    this.$store.dispatch('recoverSession');
  },

  methods: {
    logout: async function(){
      await this.$store.dispatch('logout');
    },
  }

}
</script>

<style>

</style>