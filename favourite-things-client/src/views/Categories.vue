<template>
    <div class='margin'>
      <div>
      <b-card-group deck >
         <b-card align="center" v-for="(category, index) in categories" :key="index">
        <b-card-title>{{category.category_name}}</b-card-title>
          <a href="#" class="card-link">View Favourites</a>
      </b-card>

      </b-card-group>
      </div>
      <CreateCategory />
    </div>
</template>
<script>
import { mapGetters } from 'vuex';
import axios from 'axios';
import CreateCategory from '@/components/CreateCategory.vue';
// import Card from '@/components/Card.vue';
export default {
  name: 'Categories',
  components: {
    CreateCategory,
  },
  mounted() {
    axios.get('category/')
      .then((response) => {
        this.$store.dispatch('getCategory', response.data);
      });
  },
  computed: {
    ...mapGetters([
      'categories',
    ]),
  },
};
</script>
<style>
@media (min-width: 576px){
  .card-deck{
  margin-top: 1px !important;
  /* margin-right: 30px; */
  /* margin-left: 70px !important; */
}
.card{
  margin-top: 40px !important;
  margin-left: 10px !important;
}
.card-deck .card {
    flex: 0 1 auto !important;
}
.margin{
  text-align: center;
  padding-left:2%;
  padding-right:2%;
}
}
.card{
  margin-top: 20px;
  flex-direction: column;
}
.card-deck {
    /* margin-left: 20px !important; */
    margin-top: 60px !important;
    /* margin-right: 30px; */
    display: flex !important;
}
.card-body {
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
}
.card-body:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
}
a.card-link{
  color:#07575b;
}
.margin{
  text-align: center;
  padding-left:25px;
  padding-right:25px;
}
</style>
