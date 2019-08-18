

const actions = {
  createCategory({ commit }, payload) {
    commit('CREATE_CATEGORY', payload);
  },
  getCategories({ commit }, payload) {
    commit('GET_CATEGORIES', payload);
  },
  getCategoryFavourites({ commit }, payload) {
    commit('GET_CATEGORY_FAVOURITES', payload);
  },
  createFavourite({ commit }, payload) {
    commit('CREATE_FAVOURITE', payload);
  },
  getFavourites({ commit }, payload) {
    commit('GET_FAVOURITES', payload);
  },
  getFavourite({ commit }, payload) {
    commit('GET_FAVOURITE', payload);
  },
  updateFavourite({ commit }, payload) {
    commit('UPDATE_FAVOURITE', payload);
  },
  deleteFavourite({ commit }, payload) {
    commit('DELETE_FAVOURITE', payload);
  },
  deleteCategoryFavourite({ commit }, payload) {
    commit('DELETE_CATEGORY_FAVOURITE', payload);
  },
  getFavouriteLogs({ commit }, payload) {
    commit('GET_FAVOURITE_LOG', payload);
  },
};
export default actions;
