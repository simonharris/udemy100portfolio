import { createRouter, createWebHistory } from 'vue-router'
import { h } from 'vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: {
        render: () => h('div', 'Home page'),
      },
    },
    {
      path: '/hello',
      component: {
        render: () => h('div', 'Hello!'),
      },
    },
  ],
})

export default router
