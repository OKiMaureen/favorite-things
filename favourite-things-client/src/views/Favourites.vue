<template>
    <div >
    <b-table hover small
    :items="items"
    :fields="fields"
    :per-page="perPage"
    :current-page="currentPage"
    class='margin capitalize'>
        <template slot="actions" slot-scope="row">
        <b-button
        size="sm"
        v-b-modal.modal-scrollable-2
        @click="getFavouriteDetails($event, row.item)"
        class="mr-2 action-btn"
        >
        Details
        </b-button>
        <b-button
        variant="info"
        size="sm"
        @click="editFavourite($event, row.item)"
        class="mr-2 action-btn"
        >
         Update
        </b-button>
        <b-button
        variant="danger"
        size="sm"
        v-b-modal.modal-1
        @click="deleteFavourite($event, row.item)"
        class="mr-2 action-btn">
         Delete
        </b-button>
        <b-button  variant="primary" size="sm" @click='logDetails($event, row.item)'
        class="mr-2 action-btn">
        Logs
        </b-button>
        </template>
    </b-table>
    <b-pagination v-if='showPagination'
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
    ></b-pagination>
    <div v-if='showAlert' class='alert'>
      No favourites created yet!
    </div>
    <div v-if='showFavouriteCategoryAlert' class='alert'>
      No favourites created for this category yet!
    </div>
    <CreateCategory />
     <CreateFavourite
     />
     <FavouriteDetails
     :favourite ='favourite'
     />
     <DeleteModal
     :favourite ='favourite'
     @loadFavourites='()=>loadFavourites()'
     />
    </div>
</template>
<script>
import { mapGetters } from 'vuex';
import axios from 'axios';
import CreateCategory from '@/components/CreateCategory.vue';
import CreateFavourite from '@/components/CreateFavourite.vue';
import FavouriteDetails from '@/components/FavouriteDetails.vue';
import DeleteModal from '@/components/DeleteModal.vue';

export default {
  name: 'Favourites',
  components: {
    CreateCategory,
    CreateFavourite,
    FavouriteDetails,
    DeleteModal,
  },
  data() {
    return {
      perPage: 12,
      currentPage: 1,
      favourite: {},
      showAlert: false,
      showPagination: true,
      showFavouriteCategoryAlert: false,
      items: [],
      fields: [
        {
          key: 'title',
          label: 'Title',
        },
        {
          key: 'ranking',
          label: 'Rank',
        },
        {
          key: 'category',
          label: 'Category',
        },
        {
          key: 'actions',
          label: 'Actions',
        },
      ],
    };
  },
  methods: {
    getFavouriteDetails(event, item) {
      this.favourite = item;
    },
    editFavourite(event, item) {
      const { id } = item;
      this.$router.push({ name: 'favouriteEdit', params: { id } });
    },
    deleteFavourite(event, item) {
      this.favourite = item;
    },
    logDetails(event, item) {
      const { id } = item;
      this.$router.push({ name: 'favouriteLogs', params: { id } });
    },
    loadFavourites() {
      const categoryId = this.$route.params.id;
      if (categoryId) {
        axios.get(`category\\${this.$route.params.id}`).then((response) => {
          if (
            response.data.favourite_things === undefined
            || response.data.favourite_things.length === 0
          ) {
            this.showFavouriteCategoryAlert = true;
            this.showPagination = false;
          }
          this.$store.dispatch(
            'getCategoryFavourites',
            response.data.favourite_things,
          );
          this.items = this.categoryFavourites;
        });
      } else {
        axios.get('favourite/').then((response) => {
          if (response.data === undefined || response.data.length === 0) {
            this.showAlert = true;
          }
          this.$store.dispatch('getFavourites', response.data);
          this.items = this.favourites;
        });
      }
    },
  },
  created() {
    this.loadFavourites();
    this.$store.watch(
      state => this.$store.state.favouriteThings,
      (newValue, oldValue) => {
        if (oldValue.length !== newValue.length) {
          this.loadFavourites();
        }
      },
    );
  },
  computed: {
    ...mapGetters(
      [
        'favourites',
        'categoryFavourites',
      ],
    ),
    rows() {
        return this.items.length
    },
  },
};
</script>
<style scoped>
@media screen and (min-width: 1280px) {
  .table {
    width: 90% !important;
    margin-bottom: 1rem;
    color: #212529;
    margin-top: 8% !important;
    text-align: center;
    margin-left: 5% !important;
  }
  .action-btn {
    width: 12% !important;
    height: 10% !important;
    font-size: 12px !important;
  }
}
.table {
  width: 90% !important;
  margin-bottom: 1rem;
  color: #212529;
  margin-top: 22%;
  margin-left: 5% !important;
}
.action-btn {
  width: 50%;
  height: 2% !important;
  font-size: 6px;
}
.capitalize {
  text-transform: capitalize;
}
.alert {
  font-size: 20px;
}
.pagination {
    width: 20% !important;
    margin-left: 40% !important;
}
</style>
