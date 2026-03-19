<script setup lang="ts">
import FeatureCard from '@/components/hero/FeatureCard.vue';
</script>

<template>
  <section class="font-koho p-10 md:p-16 bg-surface">
    <h2 class="text-center text-4xl text-neutral mb-10 font-medium">Features</h2>
    <div class="flex flex-col md:flex-row gap-5 text-[1.1rem] text-surface">
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
  </section>
</template>
