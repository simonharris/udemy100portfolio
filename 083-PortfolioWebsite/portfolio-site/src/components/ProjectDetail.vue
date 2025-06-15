<script setup>
import { h } from 'vue';
import { API_HOST } from '@/config';
</script>

<template>

<div class="row">
    <h4>HELLO PROJECT {{  project.name  }}</h4>

    <div class="col-lg-4">
        <img :src="API_HOST + '/static/thumbs/' + project.thumbnail" class="img-fluid img-thumbnail mb-2">
    </div>

    <div class="col-lg-8">
        <p class="lead">{{ project.headline }}</p>
        <p>{{ project.description }}</p>
    </div>

</div>

</template>


<script>

export default {
    data() {
        return {
            project: { name: 'Project Placeholder' },
        };
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
            if (to.params.slug != undefined) {
                this.fetchDetails(to.params.slug);
            }
        },
        immediate: true
        }
    }
}

</script>