import Vue from 'vue'
import Vuex from 'vuex'

import session from "./session"
import drawer from "./drawer"

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    session,
    drawer,
  }
})
