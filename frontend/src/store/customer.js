import axios from "axios"

const state = {
    customer: {},
    orders: [],
}

const getters = {
    info: state => state.customer,
    id: state => state.customer.id,
    orders: state => state.orders,
}

const actions = {
    async get({dispatch, rootGetters}){
        await dispatch("getCustomer", rootGetters.user.id);
    },

    async getCustomer({commit, rootGetters}, customerID){
        const config = {headers: {"session-id": rootGetters.sessionID}};

        const resp = await axios.get(`/api/customer/${customerID}`, config);
        commit("setCustomer", resp.data);
    },

    async getOrders({commit, rootGetters}){
        const customerID = rootGetters.user.id;
        const config = {headers: {"session-id": rootGetters.sessionID}};
        const resp = await axios.get(`/api/customer/${customerID}/orders`, config);
        commit("setOrders", resp.data);
    },
}

const mutations = {
    setCustomer(state, customer){
        state.customer = customer;
    },
    setOrders(state, orders){
        state.orders = orders;
    }

}

export default {
    state,
    getters,
    actions,
    mutations,
    namespaced: true,
}
