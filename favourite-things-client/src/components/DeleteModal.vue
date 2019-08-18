<template>
  <div>
    <b-modal id="modal-1"
    title="Delete Favourite"
    ok-variant="danger"
    ok-title="Delete"
    @ok="handleOk"
    >
    <p
    class="my-4">
    Aww... "{{favourite.title}}" is no longer your favourite thing? Are you sure you want to delete?
    </p>
    </b-modal>
  </div>
</template>
<script>
import axios from 'axios';

export default {
  props: {
    favourite: {
      type: Object,
    },
  },
  methods: {
    handleOk() {
      this.handleSubmit();
    },
    makeToast(variant, body) {
      this.$bvToast.toast(body, {
        variant,
        solid: true,
      });
    },
    handleSubmit() {
      axios.delete(`favourite\\${this.favourite.id}\\`)
        .then((response) => {
          if (response.status === 204) {
            this.$store.dispatch('deleteFavourite', response.data);
            this.$store.dispatch('deleteCategoryFavourite', response.data);
            this.makeToast(
              'success',
              `Favourite thing "${this.favourite.title}" was deleted successfully`,
            );
          }
          this.$emit('loadFavourites');
          this.$emit('loadFavourites');
        });
    },
  },
};
</script>
