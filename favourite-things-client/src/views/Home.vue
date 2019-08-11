<template>
  <div >
  <!-- <NavigationBar link1='Favourite Things' link2='Categories' /> -->
  <div class="bg-overlay">
    <div class="align-center">
      <h3>
        My Favourite Things
      </h3>
      <p>
        Categorize and rank your favourite things to your heart desires!
      </p>
      <b-button variant="outline-primary" v-b-modal.modal-prevent-closing >
        Create Category
      </b-button>
    </div>
  </div>
  <CreateCategory />
  </div>
</template>

<script>
// // @ is an alias to /src
import CreateCategory from '@/components/CreateCategory.vue';

export default {
  name: 'Home',
  data() {
    return {
      image: require('../assets/images/favourite-background.jpg'),
    };
  },
  components: {
    // NavigationBar,
    CreateCategory,

  },
};
</script>
<style scoped>
 .bg-overlay {
    background: linear-gradient(rgba(0,0,0,.7), rgba(0,0,0,.7)),
    url("../assets/images/favourite-background.jpg");
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center center;
    color: #fff;
    height: 100%;
    width: 100%;
    position: absolute;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
}
.align-center{
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
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
</style>
