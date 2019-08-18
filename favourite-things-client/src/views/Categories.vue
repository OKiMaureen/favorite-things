<template>
    <div class='margin'>
      <div>
      <b-card-group deck >
         <b-card align="center" v-for="(category, index) in categories" :key="index">
        <b-card-title class="capitalize">{{category.category_name}}</b-card-title>
           <b-button @click="viewFavourites(category.id)">View Favourites</b-button>
      </b-card>
      </b-card-group>
      <div v-show="showAlert" class="alert">
      No categories created yet!
      </div>
      </div>
      <CreateCategory 
       @loadCategories="()=>loadCategories()"/>
      <CreateFavourite />
    </div>
</template>
<script>
import { mapGetters } from 'vuex';
import axios from 'axios';
import CreateCategory from '@/components/CreateCategory.vue';
import CreateFavourite from '@/components/CreateFavourite.vue';
export default {
  name: 'Categories',
  components: {
    CreateCategory,
    CreateFavourite,
  },
  data() {
    return {
      showAlert:false,
    }
  },
  methods: {
    viewFavourites(id) {
      this.$router.push({ name: 'categoryFavourites', params: { id} });
    },
    loadCategories(){
     axios.get('category/')
      .then((response) => {
        if(response.data === undefined || response.data === 0 ){
          this.showAlert = true;
        }
        this.$store.dispatch('getCategories', response.data);
      });
    }

  },
  created() {
    this.$store.watch(
    (state)=>{
      return this.$store.state.categories 
    },
    (newValue, oldValue)=>{
      if(oldValue.length !== newValue.length){
         this.loadCategories()
      }
  },
  )
    this.loadCategories()
    
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
    margin-top: 60px !important;
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
.capitalize{
  text-transform: capitalize
}
.alert{
  font-size: 20px;
}
button.btn.btn-info{
  background-color: none !important;
}
</style>
