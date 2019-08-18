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
          label='Category Name'
          label-for='name-input'
        >
          <b-form-input
            id="example-input-1"
            name="example-input-1"
            v-model='$v.category.category_name.$model'
            :state="$v.category.category_name.$dirty ? !$v.category.category_name.$error : null"
            aria-describedby="input-1-live-feedback"
            required
          ></b-form-input>
          <b-form-invalid-feedback
          id="input-2-live-feedback"
          v-if="!$v.category.category_name.required" >
          This is a required field.
        </b-form-invalid-feedback>
        <b-form-invalid-feedback
          id="input-2-live-feedback"
          v-if="!$v.category.category_name.minLength" >
          Category must have at least {{$v.category.category_name.$params.minLength.min}} letters.
        </b-form-invalid-feedback>
        </b-form-group>
      </form>
    </b-modal>
  </div>
</template>

<script>
import { validationMixin } from 'vuelidate';
import { required, minLength } from 'vuelidate/lib/validators';
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  mixins: [validationMixin],
  data() {
    return {
      category: {
        category_name: '',
      },
      nameState: null,
      errors: {},
    };
  },
  validations: {
    category: {
      category_name: {
        required,
        minLength: minLength(3),
      },
    },
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
        variant,
        solid: true,
      });
    },
    handleSubmit() {
      // Exit when the form isn't valid
      this.$v.category.$touch();
      if (!this.checkFormValidity()) {
        return;
      }
      if (this.$v.$anyError) {
        return;
      }
      axios
        .post('category/', this.category)
        .then((response) => {
          this.$store.dispatch('createCategory', response.data);
          if (response.status === 201) {
            this.makeToast(
              'success',
              `Category "${response.data.category_name}" was created successfully`,
            );
          }
          this.$emit('loadCategories');
        })
        .catch((error) => {
          this.errors = error.response.data;
          if (error.response.status === 409) {
            this.makeToast('danger', 'Category already exists!');
          }
        });
      // Hide the modal manually
      this.$nextTick(() => {
        this.$refs.modal.hide();
      });
    },
  },
  computed: {
    ...mapGetters(['categories']),
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
