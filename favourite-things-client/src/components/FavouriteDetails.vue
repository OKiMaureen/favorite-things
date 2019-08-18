<template>
  <div class="card-container">
    <b-modal
    id="modal-scrollable-2"
    ref="modal"
    ok-variant="info"
    scrollable
    title="Favourite Thing Details"
    >
    <div >
    <b-row class="my-1">
        <b-col sm="4" >
        <div class="detail-key">
          Title:
        </div>
        </b-col>
        <b-col sm="8">
         <div class="capitalize">
           {{favourite.title}}
        </div>
        </b-col>
        <b-col sm="4">
        <div class="detail-key">
          Description:
        </div>
        </b-col>
        <b-col sm="8">
         <div class="capitalize">
          {{favourite.description}}
        </div>
        </b-col>
        <b-col sm="4">
        <div class="detail-key">
          Rank:
        </div>
        </b-col>
        <b-col sm="8">
         <div class="capitalize">
           {{favourite.ranking}}
        </div>
        </b-col>
        <b-col sm="4">
        <div class="detail-key">
          Category:
        </div>
        </b-col>
        <b-col sm="8">
        <div class="capitalize">
         {{favourite.category}}
        </div>
        </b-col>
        <b-col sm="4">
        <div class="detail-key">
          Created Date:
        </div>
        </b-col>
        <b-col sm="8">
        <div class="capitalize">
         {{formatDate(favourite.created_at)}}
        </div>
        </b-col>
        <b-col sm="4">
        <div class="detail-key">
          Modified Date:
        </div>
        </b-col>
        <b-col sm="8">
        <div class="capitalize">
         {{formatDate(favourite.updated_at)}}
        </div>
        </b-col>
        <b-col sm="4">
        <div class="detail-key" >
          Metadata:
        </div >
        </b-col>
        <b-col sm="8">
        <div v-for="(value, name, index) in favourite.metadata" :key="index">
        <b-row>
        <b-col sm="6">
        <div class="metadata-key capitalize">
           {{name}}:
        </div>
        </b-col>
        <b-col sm="6">
          <div class="capitalize">
            {{value}}
          </div >
        </b-col>
        </b-row>
        </div>
        </b-col>
        </b-row>
      </div>
   </b-modal>
  </div>
</template>

<script>
import { format } from 'date-fns';
import { mapGetters } from 'vuex';

export default {
  props: {
    favourite: {
      type: Object,
    },
  },
  computed: {
    ...mapGetters([
      'categories',
      'favourites',
    ]),
  },
  methods: {
    formatDate(date) {
      return format(new Date(date), 'ddd Do, MMM YYYY hh:mmA');
    },
  },
};
</script>
<style scoped>
.detail-key{
  font-size: 20px;
  color: #07575b;
  margin-bottom: 10px;
}
.margin{
margin-bottom: 5px;
}
.metadata-key{
  color: #07575b;
  font-size: 16px;
}
.capitalize{
  text-transform: capitalize
}
</style>
