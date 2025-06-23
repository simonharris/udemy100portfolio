<script setup>
import { RouterView } from 'vue-router'
import { reactive } from 'vue'
import PageHeader from '@/components/PageHeader.vue'
import PageFooter from '@/components/PageFooter.vue'
</script>

<template>

<PageHeader :config="pageConfig" />

<div class="container-lg">

<router-view v-slot="{ Component }">
    <Transition name="myfade" >
      <component :is="Component" :config="pageConfig"  @update-config="updateConfig" />
    </Transition>
</router-view>


</div>

<PageFooter />

</template>


<script>

export default {
  data() {
    return {
      pageConfig: {
        title: 'Default title',
        headline: 'Default headline'
      }
    }
  },
  methods: {
    updateConfig(newConfig) {
      this.pageConfig = newConfig;
    }
  }
}

</script>


<style scoped>
.myfade-enter-active {
  transition: all 0.5s ease;
}

.myfade-enter-from,
.myfade-leave-to {
  /* transform: translateX(-10px); */
  opacity: 0;
}

</style>
