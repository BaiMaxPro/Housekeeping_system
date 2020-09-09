import axios from "axios"

const state = {
    session: {},
    loggedIn: false,
}

const getters = {
    session: state => state.session,
    sessionID: state => state.session.id,
    user: state => state.session.user,
    loggedIn: state => state.loggedIn,
}

const actions = {
    async recoverSession({commit}){
        const sid = sessionStorage.getItem('sessionID');
        if(sid){
            const config = {headers: {"session-id": sid}};
            try{
                const resp = await axios.get("/api/login", config);
                commit("setSession", resp.data);
                commit("setLoggedIn", true);
            } catch (error) {
                commit("setSession", {});
                commit("setLoggedIn", false);
            }
        }
    },

    async login({commit}, {username, password}){
        const config = {headers: {username, password}};
        try {
            const resp = await axios.post("/api/login", {}, config);
            commit("setSession", resp.data);
            commit("setLoggedIn", true);
        } catch (error) {
            commit("setSession", {});
            commit("setLoggedIn", false);
            throw error;
        }
    },

    async logout({getters, commit}){
        const config = {headers: {"session-id": getters.sessionID}};

        try {
            await axios.delete('/api/login', config);
        } finally {
            commit("setSession", {});
            commit("setLoggedIn", false);
        }
    }
}

const mutations = {
    setSession(state, session){
        state.session = session;
        if(session){
            sessionStorage.setItem('sessionID', session.id);
        } else {
            sessionStorage.removeItem('sessionID');
        }
    },

    setLoggedIn(state, loggedIn){
        state.loggedIn = loggedIn;
    },
}

export default {
    state,
    getters,
    actions,
    mutations,
}
