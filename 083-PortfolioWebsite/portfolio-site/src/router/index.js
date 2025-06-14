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
        methods: {
          async fetchDetails(slug) {
            fetch('http://127.0.0.1:5000/api/detail/' + slug, {
              method: "GET",
              headers: {},
            })
            .then((response) => {
              response.json().then((data) => {
                this.project = data.project;
                console.log(this.project.name);
              });
            })
            .catch((err) => {
                console.error(err);
            })
          }
        },
        watch: {
          $route: {
            handler(to, from) {
              console.log("Route now changed to:", to.params.slug);
              if (to.params.slug != undefined) {
                this.fetchDetails(to.params.slug);
              }
            },
            immediate: true
          }
        }
      },
    },
  ],
})

export default router
