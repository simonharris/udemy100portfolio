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
      path: '/:slug',
      component: {
        data() {
          return {
            project: { name: 'My Project' },
          };
        },
        render() {
          return h('div', 'Hello! ' + this.project.name);
        },
      },
    },
  ],
})

export default router
