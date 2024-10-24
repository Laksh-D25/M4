<template>
    <loader class="z-100"/>
    <div class="relative">
        <Navbar class="z-40"/>
        <Toast v-if="show" :message="toastMessage" :type="toastType" @close="show = false" class="z-100"/>
        <div class="z-0">
            <RouterView />
        </div>
        <Footer class="z-40"/>
    </div>
</template>

<script setup>
import { useToast } from './useToast.js';
import { RouterView } from 'vue-router';
import loader from './components/loader.vue';
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';

const { show, toastMessage, toastType } = useToast();
</script>