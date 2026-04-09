<script setup lang="ts">
import FeatureCard from '@/components/hero/FeatureCard.vue';
</script>

<template>
  <section class="font-koho p-10 md:p-16 bg-surface">
    <h2 class="text-center text-4xl text-neutral mb-10 font-medium">Features</h2>
    <div class="flex flex-col md:flex-row gap-5 text-[1.1rem] text-surface">
      <FeatureCard
        title="Multiple Sources"
        content="Turn anything into a deck. Paste text, upload a CSV, drop a YouTube link, or enter a web article URL — AnkiBuilder handles it all."
      />
      <FeatureCard
        title="Smart Vocabulary Extraction"
        content="Powered by AI, AnkiBuilder automatically identifies difficult words and idioms that are worth learning, so you don't have to pick them manually."
      />
      <FeatureCard
        title="Make It Yours"
        content="Customize your cards to match your style. Adjust colors, fonts, and layout so your deck looks exactly the way you want it — because good design makes studying more enjoyable."
      />
    </div>
  </section>
</template>
