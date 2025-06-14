<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>

<div class="container-fluid item-block-in">
  <div class="container-lg">
        <div class="row pt-4">
          <h1 class="display-2"><router-link to="/">Simon's Page</router-link></h1>
          <p class="lead">Some placeholder text and maybe a link or two</p>
        </div>
      </div>
</div>

<div class="container-lg">
<div class="row">
<div v-for="project in projects" class="p-1 col-sm-6 col-md-4 col-lg-3">

    <div class="position-relative">
      <router-link :to="'/' + project.slug">
      <img :src="'http://127.0.0.1:5000/static/thumbs/' + project.thumbnail" class="img-fluid img-thumbnail mb-2">
      </router-link>

      <div class="position-absolute bottom-0 start-0 bg-secondary w-100 p-2" style="--bs-bg-opacity: .8">

      <h4 class="fs-6">
            <router-link style="color: white; text-decoration: none;" :to="'/' + project.slug">{{ project.name }}</router-link>
      </h4>
      <p class="fs-6">{{  project.headline }}</p>

      </div>
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
