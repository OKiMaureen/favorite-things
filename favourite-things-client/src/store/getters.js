const getters = {
  categories: state => state.categories,
  favourites: state => state.favouriteThings,
  category: state => state.category,
  favourite: state => state.favourite,
  categoryFavourites: state => state.categoryFavouriteThings,
  favouriteLogs: state => state.favouriteLogs,
};

export default getters;
