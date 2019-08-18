<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="success" fixed="top">
      <b-navbar-brand to="/">MY FAVOURITE THINGS</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item to="/favourites" >{{link1}}</b-nav-item>
          <b-nav-item to="/categories" right>{{link2}}</b-nav-item>
          <b-nav-item href="#" right>
          <b-button
          variant="outline-primary"
          size="sm" v-b-modal.modal-prevent-closing>
          Create Category
          </b-button>
          <b-button
          variant="outline-primary"
          size="sm"
          v-b-modal.modal-scrollable
          type="submit">
          Create Favourite Thing
          </b-button>
         </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
  </template>

<script>
export default {
  name: 'NavigationBar',
  props: {
    link1: String,
    link2: String,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.bg-success {
    background-color:#07575b !important;
}
.navbar-dark .navbar-nav .nav-link:hover {
    color: white;
}
.nav-link {
    display: block;
    padding: 0.5rem 1rem;
    text-align: left;
}
.navbar-brand {
    font-size: 1rem;
}
.btn-sm, .btn-group-sm > .btn {
    margin-right: 10px;
}
.btn-outline-primary {
    color: #66a5ad;
    border-color: #66a5ad;
}
.btn-outline-primary:hover {
    color: #fff;
    background-color: #66a5ad;
    border-color: #66a5ad;
}
a.nav-link.router-link-exact-active.router-link-active {
    font-weight: 700;
    color: white;
}
</style>
