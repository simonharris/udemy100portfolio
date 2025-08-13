
<template>
<div class="container-fluid p-0">
  <div class="container-lg">
     <div class="col fs-1 pt-2">
        <a href="/" title="Projects Home"><i class="bi bi-house-fill"></i></a>
     </div>
        <hr class="mt-0">
    <div class="row pt-4">
      <h1 class="display-2"><router-link to="/">{{ config.title }}</router-link></h1>

      <p class="lead">{{ config.headline }}</p>

    </div>
        <hr>
  </div>
</div>
</template>

<script>
export default {
    props: {
        config: Object
    },
}
</script>