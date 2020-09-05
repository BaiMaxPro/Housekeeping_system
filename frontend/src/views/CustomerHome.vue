<template>
  <div>
    <v-card  height = "400" width="200" class="card-left">
        <v-navigation-drawer permanent>
            <v-list-item>
                <v-list-item-content>
                <v-list-item-title class="title">
                    应用列表
                </v-list-item-title>
                <!-- <v-list-item-subtitle>
                    用户
                </v-list-item-subtitle> -->
                </v-list-item-content>
            </v-list-item>
            
            <v-divider></v-divider>

            <v-list dense nav>
                <v-list-item v-for="item in items" :key="item.title" link>
                    <v-list-item-icon>
                        <v-icon>{{ item.icon }}</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                        <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item-content>
                </v-list-item>
            </v-list>
        </v-navigation-drawer>
    </v-card>
    <v-card height="800" width="75%" class="card-right">
<!-- 试使用横向列表排列card -->
    </v-card> 
  </div>
</template>

<script>
export default {
    data: () => ({
        items : [
            {
                icon: 'account-circle' ,
                title:'会员中心'
            },
            {
                icon: 'account-circle' ,
                title:'个人信息'
            },
            {
                icon: 'account-circle' ,
                title:'订单系统'
            },
        ],
        right: null,
  }),
}
</script>

<style>
    .card-left{
        position : relative;
        left : 1% ;
        top : 10px ;
        min-width: 200px;
        max-width: 200px;
    }
    .card-right{
        position : relative;
        left: 230px;
        top : -390px ;
    }
</style>