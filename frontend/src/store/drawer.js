const state = {
    drawer: {},
}

const getters = {
    drawer: state => state.drawer,
    showDrawer: state => Object.keys(state.drawer).length != 0,
    showDrawerTitle: state => "title" in state.drawer,
    showDrawerItems: state => "items" in state.drawer && state.drawer.items.length > 0, 
}

const actions = {
    async updateDrawer({commit}, drawer){
        commit("setDrawer", drawer)
    },
}

const mutations = {
    setDrawer(state, drawer){
        state.drawer = drawer
    },

}

export default {
    state,
    getters,
    actions,
    mutations,
}
