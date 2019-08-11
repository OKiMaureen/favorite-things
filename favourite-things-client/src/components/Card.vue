<template>
   <!-- <div class= 'dir'>
      <b-card align="center" v-for="(category, index) in categories" :key="index">
        <b-card-title>{{category.category_name}}</b-card-title>
          <a href="#" class="card-link">View Favourites</a>
      </b-card>
</div> -->
 <div>
      <b-card align="center">
        <b-card-title>New</b-card-title>
          <a href="#" class="card-link">View Favourites</a>
      </b-card>
</div>
</template>
<script>
  export default {
  name: 'Card',
  }
</script>
<style>
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
</style>
