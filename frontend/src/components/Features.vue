<script setup lang="ts">
import FeatureCard from '@/components/FeatureCard.vue';
</script>

<template>
  <section class="font-koho p-16">
    <h2 class="text-center text-4xl text-neutral mb-10 font-medium">Features</h2>
    <div class="grid grid-cols-3 gap-5 text-[1.1rem] text-surface">
      <FeatureCard
        title="Feature 1"
        content="Lorem ipsum dolor sit, amet consectetur adipisicing elit. Accusantium assumenda fugit atque accusamus nam inventore quae ducimus sequi perspiciatis! Debitis?"
      />
      <FeatureCard
        title="Feature 2"
        content="Lorem ipsum dolor sit, amet consectetur adipisicing elit. Accusantium assumenda fugit atque accusamus nam inventore quae ducimus sequi perspiciatis! Debitis?"
      />
      <FeatureCard
        title="Feature 3"
        content="Lorem ipsum dolor sit, amet consectetur adipisicing elit. Accusantium assumenda fugit atque accusamus nam inventore quae ducimus sequi perspiciatis! Debitis?"
      />
    </div>
    <RouterLink class="btn-primary ml-auto mt-10" to="/generator">Start Generating</RouterLink>
  </section>
</template>
