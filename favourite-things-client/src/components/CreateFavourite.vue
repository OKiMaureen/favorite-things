<template>
  <div>
    <b-modal
      id="modal-scrollable"
      ref="modal"
      scrollable
      title="Create Favourite Thing"
      ok-variant="info"
      ok-title="Submit"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form id="form"
      data-metadata='[{ "": "", "": "" }]'
      ref="form"
      @submit.stop.prevent='handleSubmit'>
        <b-form-group
          label='Title'
          label-for='name-input'
        >
          <b-form-input
            id="example-input-1"
            name="example-input-1"
            v-model='$v.title.$model'
            :state="$v.title.$dirty ? !$v.title.$error : null"
            aria-describedby="input-1-live-feedback"
            required
          ></b-form-input>
          <b-form-invalid-feedback id="input-2-live-feedback" v-if="!$v.title.required" >
          This is a required field.
        </b-form-invalid-feedback>
        <b-form-invalid-feedback id="input-2-live-feedback" v-if="!$v.title.minLength" >
          TItle must have at least {{$v.title.$params.minLength.min}} letters.
        </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group
          label='Description'
          label-for='name-input'
        >
          <b-form-input
           id="example-input-1"
            name="example-input-1"
            v-model='$v.description.$model'
            :state="$v.description.$dirty ? !$v.description.$error : null"
            aria-describedby="input-1-live-feedback"
          ></b-form-input>
          <b-form-invalid-feedback id="input-2-live-feedback" v-if="!$v.description.minLength" >
          Desription must have at least {{$v.description.$params.minLength.min}} letters.
        </b-form-invalid-feedback>
           </b-form-group>
          <b-form-group
          label='Ranking'
          label-for='name-input'
        >
          <b-form-input
            id="example-input-1"
            name="example-input-1"
            v-model='$v.ranking.$model'
            :state="$v.ranking.$dirty ? !$v.ranking.$error : null"
            aria-describedby="input-2-live-feedback"
            required
          ></b-form-input>
          <b-form-invalid-feedback id="input-2-live-feedback" v-if="!$v.ranking.required" >
          This is a required field.
        </b-form-invalid-feedback>
        <b-form-invalid-feedback id="input-2-live-feedback" >
         Ranking must be a positive number from 1
        </b-form-invalid-feedback>
        </b-form-group>
        <b-form-group
          :state="$v.category.$dirty ? !$v.category.$error : null"
          label='Category'
          label-for='name-input'
          required
        >
        </b-form-group>
        <b-form-select
          id="example-input-1"
          name="example-input-1"
          v-model='$v.category.$model'
          :state="$v.category.$dirty ? !$v.category.$error : null"
          aria-describedby="input-2-live-feedback"
          required
           class="mb-3">
        <option :value="null" disabled>
        Choose Category</option>
         <option
         v-for="category in categories"
        :key="category.id"
        :value="category.category_name"
         >{{ category.category_name }}</option>
        </b-form-select>
        <b-form-invalid-feedback id="input-2-live-feedback" v-if="!$v.category.required" >
          This is a required field.
        </b-form-invalid-feedback>
        <b-row class="my-1">
        <b-col sm="10">
        <b-form-group
          label='Metadata'
        >
        </b-form-group>
        </b-col>
        <b-col sm="2">
        <b-button @click="addMetadata" size="sm" variant="outline-info">Add</b-button>
        </b-col>
         </b-row>
         <b-row class="my-1" v-for="(metadata, index) in metadata" :key="index" >
        <b-col sm="5">
          <b-form-input
          v-model='metadata.key'
          id='name-input'
          placeholder="Label"
          ></b-form-input>
        </b-col>
        <b-col sm="5">
          <b-form-input
            v-model='metadata.value'
            id='name-input'
            placeholder="Value"
          ></b-form-input>
        </b-col>
         <b-col sm="2">
         <b-button @click="deleteMetadata(index)" size="sm" variant="outline-danger">X</b-button>
        </b-col>
      </b-row>
      </form>
    </b-modal>
  </div>
</template>

<script>
import { validationMixin } from 'vuelidate';
import {
  required,
  minLength,
  numeric,
  minValue,
} from 'vuelidate/lib/validators';
import Vue from 'vue';
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  mixins: [validationMixin],
  data() {
    return {
      title: '',
      description: '',
      ranking: 1,
      category: null,
      metadata: [
        {
          key: '',
          value: '',
        },
      ],
      nameState: null,
      errors: {},
      selected: null,
    };
  },
  validations: {
    title: {
      required,
      minLength: minLength(2),
    },
    description: {
      minLength: minLength(3),
    },
    ranking: {
      required,
      numeric,
      minValue: minValue(1),
    },
    category: {
      required,
    },
  },
  methods: {
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.nameState = valid ? 'valid' : 'invalid';
      return valid;
    },
    resetModal() {
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
      this.$v.$touch();
      if (!this.checkFormValidity()) {
        return;
      }
      if (this.$v.$anyError) {
        return;
      }
      const metadata = {};
      const { title, description, category } = this;
      const ranking = parseInt(this.ranking, 10);
      this.metadata.forEach((item) => {
        if (item.key !== '' && item.value !== '') {
          metadata[item.key] = item.value;
        }
      });
      axios
        .post('favourite/', {
          title,
          description,
          category,
          ranking,
          metadata,
        })
        .then((response) => {
          this.$store.dispatch('createFavourite', response.data);
          if (response.status === 201) {
            this.makeToast(
              'success',
              `Favourite thing "${response.data.title}" was created successfully`,
            );
          }
        })
        .catch((error) => {
          if (
            error.response.data[0]
            === 'The Favorite thing already exists for this category'
          ) {
            this.makeToast(
              'danger',
              'The Favourite thing is already created for this category!',
            );
          }
          this.errors = error.response.data;
        });
      // Hide the modal manually
      this.$nextTick(() => {
        this.$refs.modal.hide();
      });
    },
    addMetadata() {
      this.metadata.push(
        Vue.util.extend(
          {},
          {
            title: '',
            metadata: '',
            description: '',
            ranking: 1,
            category: null,
          },
        ),
      );
    },
    deleteMetadata(index) {
      Vue.delete(this.metadata, index);
    },
  },
  computed: {
    ...mapGetters(['categories']),
  },
  mounted() {
    axios.get('category/')
      .then((response) => {
        this.$store.dispatch('getCategories', response.data);
      });
  },
};
</script>
<style scoped>
.btn-primary {
  color: #fff;
  background-color: #07575b;
  border-color: #07575b;
}
button.btn.btn-outline-danger.btn-sm {
  border: none !important;
  padding: 8px;
  font-weight: 800;
}
</style>
