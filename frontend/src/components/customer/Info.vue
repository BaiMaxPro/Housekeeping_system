<template>
    <v-card elevation="2" outline>
        <v-card-title>个人信息</v-card-title>
        <v-card-text class="text--primary">
        <v-text-field v-model="form.name" label="姓名" outlined required></v-text-field> 
        <v-text-field v-model="form.gender" label="性别" outlined required></v-text-field> 
        <v-text-field v-model="form.tel" label="电话" outlined required></v-text-field> 
        <v-text-field v-model="form.address" label="地址" outlined required></v-text-field> 
        </v-card-text>
        <v-card-actions>
        <v-btn color="blue" text> 保存 </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
export default {
    mounted(){
      this.form = this.$store.getters["customer/info"]
    },
    data: () => ({
        form: {
            name: "",
            gender: "",
            tel:"",
            address:"",
        },
    }),
}
</script>

<style>

</style>