<template>
  <v-data-table :headers="headers" :items="orders" :items-per-page="5" :loading="loading" class="elevation-1">
    <template v-slot:[`item.stat`]="{ item }">
      {{ getStatsText(item.stat) }}
    </template>

  </v-data-table>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data(){
    return{
      loading: false,
      headers: [
        {text: "时间", value: "order_time"},
        {text: "项目", value: "item"},
        {text: "顾客姓名", value: "customer.name"},
        {text: "订单状态", value: "stat"}
      ]
    }
  },
  computed: {
    ...mapGetters("employee", ["orders"]),
  },
  async mounted() {
    this.loading = true;
    await this.$store.dispatch("employee/getOrders");
    this.loading = false;
  },

  methods: {
    getStatsText(stat){
      const statMap = {0: "未开始", 1:"已开始", 2:"已完成"}
      return statMap[stat]
    }
  }
}
</script>