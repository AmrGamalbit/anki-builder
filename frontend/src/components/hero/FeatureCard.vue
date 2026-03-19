<script setup lang="ts">
defineProps({
  title: String,
  content: String,
});
</script>

<template>
  <div class="bg-neutral p-6 rounded-2xl">
    <h3 class="mb-2 text-2xl text-accent dark:text-gray-900 font-semibold">{{ title }}</h3>
    <p class="text-surface">
      {{ content }}
    </p>
  </div>
</template>
