<script setup lang="ts">
const value = defineModel<number>();

const props = defineProps({
  min: { type: Number, default: 0 },
  max: { type: Number, default: 100 },
  step: { type: Number, default: 1 },
});
if (value.value === null || value.value === undefined) {
  value.value = Math.ceil(props.max / 2);
}
</script>

<template>
  <div class="flex items-center gap-3">
    <input
      class="w-full accent-neutral"
      type="range"
      :min="props.min"
      :max="props.max"
      :step="props.step"
      v-model.number="value"
    />
    <span class="text-sm text-neutral w-8 text-right">{{ value }}</span>
  </div>
</template>
