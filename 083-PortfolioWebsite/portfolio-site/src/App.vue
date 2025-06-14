<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="row">
    <h1><router-link to="/">Simon's Page</router-link></h1>
  </div>


<div class="row">
<div v-for="project in projects" class="p-1 col-sm-6 col-md-4 col-lg-3">

    <div class="item-block-in">
      <router-link :to="'/' + project.slug">
      <img :src="'http://127.0.0.1:5000/static/thumbs/' + project.thumbnail" class="img-fluid img-thumbnail mb-2">
      </router-link>

      <div class="p-2">
        <h4>
            <router-link :to="'/' + project.slug">{{ project.name }}</router-link>
        </h4>
        <p>{{  project.headline }}</p>
      </div>
    </div>
</div>
</div>

  <RouterView />
</template>

<script>

export default {
  data() {
    return {
      projects: []
    }
  },
  methods: {
    // ...
  },
  mounted() {
        fetch('http://127.0.0.1:5000/api/list')
        .then(response => response.json())
        .then(data => this.projects = data.projects)
  },
  // watch: {
  //   $route: {
  //     handler(to, from) {
  //       console.log("Route now changed to:", to.params.slug);
  //       if (to.params.slug != undefined) {
  //         this.fetchDetails(to.params.slug);
  //       }
  //     },
  //     immediate: true
  //   }
  // }
}
</script>

<style scoped>

</style>
