<script setup>
import { API_HOST } from '@/config';
</script>

<template>

<div class="row">
    <div v-for="project in projects" class="p-1 col-sm-6 col-md-4 col-lg-3">
        <div class="position-relative">
            <router-link :to="'/' + project.slug">
            <img :src="API_HOST + '/static/thumbs/' + project.thumbnail" class="img-fluid img-thumbnail mb-2">
            </router-link>

            <div class="position-absolute bottom-0 start-0 bg-secondary w-100 p-2" style="--bs-bg-opacity: .8">
                <h4 class="fs-6">
                    <router-link style="color: white; text-decoration: none;"   :to="'/' + project.slug">{{ project.name }}</router-link>
                </h4>
                <p class="fs-6">{{  project.headline }}</p>
            </div>
        </div>
    </div>
</div>

</template>


<script>

export default {
    data() {
        return {
            projects: []
        }
    },
    methods: {
        // ...
    },
    mounted() {
            fetch(API_HOST + '/api/list')
            .then(response => response.json())
            .then(data => this.projects = data.projects)
    },
}

</script>