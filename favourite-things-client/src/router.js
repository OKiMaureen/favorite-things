import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Categories from './views/Categories.vue';
import Favourites from './views/Favourites.vue';
import EditFavourite from './views/EditFavourite.vue';
import AuditLogs from './views/AuditLogs.vue';
import NotFound from './views/NotFound.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/categories',
      name: 'categories',
      component: Categories,
    },
    {
      path: '/favourites',
      name: 'favourites',
      component: Favourites,
    },
    {
      path: '/category/:id/favourites',
      name: 'categoryFavourites',
      component: Favourites,
    },
    {
      path: '/favourite/:id/edit',
      name: 'favouriteEdit',
      component: EditFavourite,
    },
    {
      path: '/favourite/:id/logs',
      name: 'favouriteLogs',
      component: AuditLogs,
    },
    {
      path: '*',
      component: NotFound,
    },
  ],
});
