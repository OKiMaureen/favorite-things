<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="success" fixed="top">
      <b-navbar-brand href="#">MY FAVOURITE THINGS</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item href="#" right>Favourite Things</b-nav-item>
          <b-nav-item href="#" right>Categories</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'NavigationBar',
  // props: {
  //   msg: String,
  // },
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

</style>
