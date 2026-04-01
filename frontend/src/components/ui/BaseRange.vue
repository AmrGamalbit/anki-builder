<script setup lang="ts">
const value = defineModel();

const props = defineProps({
  min: { type: Number, default: 0 },
  max: { type: Number, default: 100 },
  step: { type: Number, default: 1 },
});
</script>

<template>
  <div class="flex items-center gap-3">
    <input
      class="w-full accent-neutral"
      type="range"
      :min="props.min"
      :max="props.max"
      :step="props.step"
      v-model="value"
    />
    <span class="text-sm text-muted-foreground w-8 text-right">{{ value }}</span>
  </div>
</template>
