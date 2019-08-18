const mutations = {
  GET_CATEGORIES(state, payload) {
    state.categories = payload;
  },
  GET_CATEGORY_FAVOURITES(state, payload) {
    state.categoryFavouriteThings = payload;
  },
  CREATE_CATEGORY(state, payload) {
    state.categories = [
      ...state.categories, payload,
    ];
  },
  CREATE_FAVOURITE(state, payload) {
    state.favouriteThings = [
      ...state.favouriteThings, payload,
    ];
  },
  GET_FAVOURITES(state, payload) {
    state.favouriteThings = payload;
  },
  GET_FAVOURITE(state, payload) {
    state.favouriteThing = payload;
  },
  UPDATE_FAVOURITE(state, payload) {
    state.favouriteThing = payload;
  },
  DELETE_FAVOURITE(state, payload) {
    const index = state.favouriteThings.findIndex(item => item.id === payload.id);
    state.favouriteThings.splice(index, 1);
  },
  DELETE_CATEGORY_FAVOURITE(state, payload) {
    const index = state.categoryFavouriteThings.findIndex(item => item.id === payload.id);
    state.categoryFavouriteThings.splice(index, 1);
  },
  GET_FAVOURITE_LOG(state, payload) {
    state.favouriteLogs = payload;
  },
};
export default mutations;
