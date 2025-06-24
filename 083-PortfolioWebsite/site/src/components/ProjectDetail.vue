<script setup>
import { API_HOST } from '@/config';
</script>

<template>

<div class="row">

    <div class="col-md-4">
        <img :src="API_HOST + '/static/thumbs/' + project.thumbnail" class="img-fluid img-thumbnail mb-2">
    </div>

    <div class="col-md-8">
        <p class="breadcrumb"><router-link :to="'/'">Projects</router-link>&nbsp;&raquo; {{ project.name }}</p>
        <p v-html="project.description"></p>
        <p v-if="project.url" class="btn-visit">
            <a :href="project.url" class="btn btn-light text-secondary " role="button">Visit Project</a>
        </p>
    </div>
</div>

</template>

<script>

export default {
    data() {
        return {
            project: { name: 'Project Placeholder' },
            isThumbnailExpanded: false,
        };
    },
    props: {
        config: Object,
    },
    computed: {
        // ...
    },
    methods: {
        async fetchDetails(slug) {
            fetch(API_HOST + '/api/detail/' + slug, {
                method: "GET",
                headers: {},
            })
            .then((response) => {
                response.json().then((data) => {
                    this.project = data.project;
                    this.$emit('update-config', {
                        title: data.project.name,
                        headline: data.project.headline
                    });
                });
            })
            .catch((err) => {
                console.error(err);
            })
        },
    },
    watch: {
        $route: {
        handler(to, from) {
            if (to.params.slug != undefined) {
                this.fetchDetails(to.params.slug);
            }
        },
        immediate: true
        }
    }
}

</script>

<style scoped>
/* .img-thumbnail {
  cursor: pointer;
} */

</style>