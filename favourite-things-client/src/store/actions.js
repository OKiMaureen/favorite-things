const actions = {
  createCategory({ commit }, payload) {
    commit('CREATE_CATEGORY', payload);
  },
  getCategory({ commit }, payload) {
    commit('GET_CATEGORY', payload);
  },
};
export default actions;
