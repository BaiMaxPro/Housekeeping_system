import axios from "axios"

const state = {
    employee: {},
    orders: [],
}

const getters = {
    info: state => state.employee,
    id: state => state.employee.id,
    orders: state => state.orders,
}

const actions = {
    async get({dispatch, rootGetters}){
        await dispatch("getEmployee", rootGetters.user.id);
    },

    async getEmployee({commit, rootGetters}, employeeID){
        const config = {headers: {"session-id": rootGetters.sessionID}};

        const resp = await axios.get(`/api/employee/${employeeID}`, config);
        commit("setEmployee", resp.data);
    },

    async getOrders({commit, rootGetters}){
        const employeeID = rootGetters.user.id;
        const config = {headers: {"session-id": rootGetters.sessionID}};
        const resp = await axios.get(`/api/employee/${employeeID}/orders`, config);
        commit("setOrders", resp.data);
    },
}

const mutations = {
    setEmployee(state, employee){
        state.employee = employee;
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
