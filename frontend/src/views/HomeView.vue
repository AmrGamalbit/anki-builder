<script setup lang="ts">
import Hero from '@/components/hero/Hero.vue';
import Features from '@/components/hero/Features.vue';
</script>

<template>
  <Hero />
  <Features />
  <RouterLink class="btn-primary ml-auto mr-16" to="/generator">Start Generating</RouterLink>
</template>
