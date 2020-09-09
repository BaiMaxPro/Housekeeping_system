<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-card class="mx-auto" max-width="420">
        <form class="mx-10 my-10">
          <v-text-field v-model="form.username" label="用户名" outlined required></v-text-field> 
          <v-text-field v-model="form.password" label="密码" type="password" outlined required></v-text-field> 
          <v-btn block v-on:click="login">登录</v-btn>
        </form>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    form: {
      username: "",
      password: "",
    },
  }),

  mounted() {
    this.$store.dispatch("updateDrawer", {})

    if(this.$store.getters.loggedIn){
      this.redirect();
    }

  },

  methods: {
    async login(){
      try{
        await this.$store.dispatch("login", {...this.form});
        this.redirect();
      } catch (err) {
        this.$dialog.notify.error(
          err.response.data.error, {position: 'bottom-right'}
        );
      }
    },

    async redirect(){
      const role = this.$store.getters.user.role;
      const name = role.charAt(0).toUpperCase() + role.slice(1);
      console.log({name});
      this.$router.push({name, params: { page: "home" }});
    }
  }
}
</script>
