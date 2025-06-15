<script setup>
import { RouterLink, RouterView } from 'vue-router'
import CommonFooter from './components/CommonFooter.vue'
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
  <transition name="fade" mode="out-in">
    <RouterView />
  </transition>
</div>

<CommonFooter />

</template>


<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>