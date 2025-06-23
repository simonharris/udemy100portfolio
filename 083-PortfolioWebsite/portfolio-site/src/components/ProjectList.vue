<script setup>
import { API_HOST } from '@/config';
</script>

<template>

<div class="row">
    <div v-for="project in projects" class="p-2 col-sm-6 col-md-4 col-lg-3">
        <div class="position-relative project-preview Ximg-thumbnail">
            <router-link :to="'/' + project.slug">
            <img :src="API_HOST + '/static/thumbs/' + project.thumbnail" class="img-fluid img-zoom img-thumbnail Xmb-2">
            </router-link>

            <div class="position-absolute bottom-0 start-0 bg-secondary w-100 h-overlay p-2">
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
    name: 'ProjectList',
    components: {
        //
    },
    data() {
        return {
            projects: [],
            pageConfig: {
                'title': "Simon's Projects",
                'headline': "I'll find something to put here",
            }
        }
    },
    methods: {
        // ...
    },
    mounted() {
        fetch(API_HOST + '/api/list')
            .then(response => response.json())
            .then(data => this.projects = data.projects);
        this.$emit('update-config', this.pageConfig );
    },
}

</script>

<style scoped>
.project-preview {
    overflow: hidden;
}

.img-zoom {
  transition: transform 0.4s ease;
}

.img-zoom:hover {
  transform: scale(1.1); /* adjust the scale value to your liking */
}
</style>