<template>
  <div>
    <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Create Category"
      ok-variant="info"
      ok-title="Submit"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent='handleSubmit'>
        <b-form-group
          :state='nameState'
          label='Category Name'
          label-for='name-input'
          invalid-feedback='Category Name is required'
        >
          <b-form-input
            id='name-input'
            v-model='category.category_name'
            :state="nameState"
            required
          ></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      category: {
        category_name: '',
      },
      nameState: null,
      errors: {},
    };
  },
  methods: {
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.nameState = valid ? 'valid' : 'invalid';
      return valid;
    },
    resetModal() {
      this.category.category_name = '';
      this.nameState = null;
    },
    handleOk(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      this.handleSubmit();
    },
    makeToast(variant, body) {
        this.$bvToast.toast(body, {
          variant: variant,
          solid: true
        })
      },
    handleSubmit() {
      // Exit when the form isn't valid
      if (!this.checkFormValidity()) {
        return;
      }
      axios
        .post('category/', this.category)
        .then((response) => {
          this.$store.dispatch('createCategory', response.data);
          if(response.status==201){
            this.makeToast('success', `Category "${response.data.category_name }" was created successfully`);
          }
        })
        .catch((error) => {
          this.errors = error.response.data;
          if(error.response.status==409){
            this.makeToast('danger', 'Category already exists!');
          }
        });
      
      // Hide the modal manually
      this.$nextTick(() => {
        this.$refs.modal.hide();
      });
    },
  },
};
</script>
<style scoped>
.btn-primary {
    color: #fff;
    background-color: #07575b;
    border-color: #07575b;
}
</style>
