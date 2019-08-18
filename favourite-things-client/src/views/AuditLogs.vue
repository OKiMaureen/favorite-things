<template>
   <div class="edit-form">
		
		  <b-card bg-variant="light">
				 <b-row class="my-1">
				<b-col sm=8>
				<div class="title">Audit Logs</div>
				</b-col>
				<b-col sm=4>
				<b-button @click="back" variant="info">
         Go back
     </b-button>
		 </b-col>
		 </b-row>
			<b-list-group >
				<b-list-group-item v-for="(favouriteLog, index) in favouriteLogs" :key="index">{{favouriteLog}}</b-list-group-item>
</b-list-group>
<div v-if="showAlert" class="alert">
      No Logs yet!
    </div>
		<b-button @click="back" variant="info">
         Back
    </b-button>
 </b-card >
  </div>
</template>
<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
	data() {
		return {
			 showAlert: false,
		}
	},
methods:{
  loadFavouriteLogs() {
				axios.get(`favourite\\${this.$route.params.id}\\logs`)
				.then(response => {
					if (
            response.data.logs === undefined ||
            response.data.logs.length === 0
          ) {
						this.showAlert = true;
					}
          this.$store.dispatch("getFavouriteLogs", response.data.logs);
      });
		},
	back(){
		this.$router.push({
              name: 'favourites',
            });
	}
},
created() {
	this.loadFavouriteLogs()
},
computed: {
    ...mapGetters([
			"favouriteLogs",
      ])
  }

}
</script>
<style scoped>
	.list-group {
	width: 90% !important;
  margin-bottom: 1rem;
  color: #212529;
  margin-top: 5%;
  margin-left: 5% !important;
  text-align: left !important;
	}
	.edit-form{
  margin-top: 10%;
}
.card {
    width: 80% !important;
    margin-left: 10% !important;
    
}
.card-body{
	padding-top: none !important;
}
.title{
	font-size: 26px;
}
</style>
