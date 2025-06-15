import { createRouter, createWebHistory } from 'vue-router'
import { h } from 'vue';

import ProjectDetail from '../components/ProjectDetail.vue'
import ProjectList from '../components/ProjectList.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: ProjectList,
    },
    {
      path: '/:slug',
      component: ProjectDetail,
    },
  ],
})

export default router
