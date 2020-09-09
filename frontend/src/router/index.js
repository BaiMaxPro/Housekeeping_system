import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/customer/:page',
    name: 'Customer',
    component: () => import('../views/Customer.vue')
  },
  {
    path: '/employee/:page',
    name: 'Employee',
    component: () => import('../views/Employee.vue')
  },
  { path: '/customer', redirect: '/customer/home' },
  { path: '/employee', redirect: '/employee/home' },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
