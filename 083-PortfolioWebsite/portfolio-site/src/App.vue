<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
<div class="container-fluid">
    <div class="container-lg" id="app">

    <h1><router-link to="/">Simon's Page</router-link></h1>

    <p><router-link to="/hello">Go to Hello</router-link></p>

    </div>
</div>

  <RouterView />
</template>

<script>

export default {
  data() {
    return {
      // your data here
    }
  },
  mounted() {
    console.log('Component mounted3!')
  },
  watch: {
    $route(to, from) {
      if (to.path === '/hello') {
        // Do your cool stuff here
        console.log("Route changed to /hello");
        // Add your extra cool stuff logic here
      }
    }
  },
  methods: {
    // your methods here
  }
}
</script>

<style scoped>

</style>
