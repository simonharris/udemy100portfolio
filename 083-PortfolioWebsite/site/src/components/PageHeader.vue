
<template>
<div class="container-fluid">
  <div class="container-lg">
        <hr>
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