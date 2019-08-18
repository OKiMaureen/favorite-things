<template>
  <div class="edit-form">
     <b-card bg-variant="light">
      <form id="form"
      data-metadata='[{ "": "", "": "" }]'
      ref="form"
      @submit.stop.prevent='handleSubmit'>
      <b-form-group
      label-cols-lg="3"
      label="Edit Favourite Thing"
      label-size="lg"
      label-class="font-weight-bold pt-0"
      class="mb-0"
    >
    <b-form-group
          label='Title'
          label-for='name-input'
          label-cols="4" label-cols-lg="2"
        >
          <b-form-input
            id="example-input-1"
            name="example-input-1"
            v-model='$v.title.$model'
            :state="$v.title.$dirty ? !$v.title.$error : null"
            aria-describedby="input-1-live-feedback"
            required
            class="capitalize"
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
          abel-for='name-input'
          label-cols="4" label-cols-lg="2"
          class="capitalize"
        >
          <b-form-input
           id="example-input-1"
            name="example-input-1"
            v-model='$v.description.$model'
            :state="$v.description.$dirty ? !$v.description.$error : null"
            aria-describedby="input-1-live-feedback"
            class="capitalize"
          ></b-form-input>
          <b-form-invalid-feedback id="input-2-live-feedback" v-if="!$v.description.minLength" >
          Desription must have at least {{$v.description.$params.minLength.min}} letters.
        </b-form-invalid-feedback>
           </b-form-group>
          <b-form-group
          label='Ranking'
          label-for='name-input'
          abel-for='name-input'
          label-cols="4" label-cols-lg="2"
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
          abel-for='name-input'
          label-cols="4" label-cols-lg="2"
        >
        <b-form-select
          id="example-input-1"
          name="example-input-1"
          v-model='$v.category.$model'
          :state="$v.category.$dirty ? !$v.category.$error : null"
          aria-describedby="input-2-live-feedback"
          required
          class="capitalize"
          >
        <option :value="null" disabled>
        Choose Category</option>
         <option
         v-for="category in categories"
        :key="category.id"
        :value="category.category_name"
         >{{ category.category_name }}</option>
        </b-form-select>
        </b-form-group>
        <b-form-invalid-feedback id="input-2-live-feedback" v-if="!$v.category.required" >
          This is a required field.
        </b-form-invalid-feedback>
        <b-row class="my-1">
        <b-col sm="10">
        <b-form-group
          label='Metadata'
          label-for='name-input'
          label-cols="4" label-cols-lg="2"
        >
        </b-form-group>
        </b-col>
        <b-col sm="2">
        <b-button @click="addMetadata" size="sm" variant="outline-info">Add</b-button>
        </b-col>
         </b-row>
         <b-form-group
          label-for='name-input'
          label-cols="4" label-cols-lg="2"
        >
        <b-row class="my-1" v-for="(metadata, index) in metadata" :key="index" >
        <b-col sm="5">
          <b-form-input
          v-model='metadata.key'
          id='name-input'
          placeholder="Label"
          class="capitalize"
          ></b-form-input>
        </b-col>
        <b-col sm="5">
          <b-form-input
            v-model='metadata.value'
            id='name-input'
            placeholder="Value"
            class="capitalize"
          ></b-form-input>
        </b-col>
         <b-col sm="2">
         <b-button @click="deleteMetadata(index)" size="sm" variant="outline-danger">X</b-button>
        </b-col>
      </b-row>
         </b-form-group>
         <b-form-group
        label-cols-sm="0"
      >
      <b-button @click="handleOk" variant="info" >
          Submit
        </b-button>
         <b-button @click="cancel" variant="info">
          Cancel
        </b-button>
      </b-form-group>
      </b-form-group>
      </form>
      </b-card>
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
    handleOk(event) {
      event.preventDefault();
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
        .put(`favourite\\${this.$route.params.id}\\`, {
          title,
          description,
          category,
          ranking,
          metadata,
        })
        .then((response) => {
          this.makeToast('success', `Favourite thing "${response.data.title}" updated successfully`);
          this.$router.push({
            name: 'favourites',
          });
        })
        .catch((error) => {
          if (
            error.response.data[0]
            === 'The Favourite thing already exists for this category'
          ) {
            this.makeToast(
              'danger',
              'The Favourite thing already exists for this category!',
            );
          }
          this.errors = error.response.data;
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
    cancel() {
      this.$router.push({
        name: 'favourites',
      });
    },
  },
  computed: {
    ...mapGetters(['favourites', 'categories']),
  },
  mounted() {
    axios.get('category/').then((response) => {
      this.$store.dispatch('getCategories', response.data);
    });

    axios
      .get(`favourite\\${this.$route.params.id}`)
      .then((response) => {
        const favouriteThing = response.data;
        this.title = favouriteThing.title;
        this.category = favouriteThing.category;
        this.description = favouriteThing.description;
        this.ranking = favouriteThing.ranking;
        const array = Object.entries(favouriteThing.metadata);
        const obj = array.map(arr => (
          {
            key: arr[0],
            value: arr[1],
          }
        ));
        this.metadata = obj;
      })
      .catch((error) => {
        this.error = error.response.data;
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
.edit-form {
  margin-top: 10%;
}
.card {
  width: 80% !important;
  margin-left: 10% !important;
}
.capitalize {
  text-transform: capitalize;
}
.btn-info {
  margin-right: 10px;
}
</style>
