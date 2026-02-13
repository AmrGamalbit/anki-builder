<script setup lang="ts">
import FeatureCard from '@/components/FeatureCard.vue';
</script>

<template>
  <section class="font-koho p-16">
    <h2 class="text-center text-4xl text-neutral mb-10 font-medium">Features</h2>
    <div class="grid grid-cols-3 gap-5 text-[1.1rem] text-surface">
      <FeatureCard />
      <FeatureCard />
      <FeatureCard />
    </div>
  </section>
</template>
