<script setup lang="ts">
import { computed } from 'vue';

const props = defineProps<{
  appearanceOptions: {
    color: string;
  };
}>();

const shimmerStyle = computed(() => {
  return {
    background: `linear-gradient(
      90deg, 
      transparent 0%, 
      ${props.appearanceOptions.color}15 50%, 
      transparent 100%
    )`,
  };
});
</script>

<template>
  <div
    class="relative h-full w-full overflow-hidden rounded-xl flex flex-col justify-between p-6 border border-gray-100/10 box-border"
    :style="{ backgroundColor: `${appearanceOptions.color}05` }"
  >
    <div class="shimmer-overlay absolute inset-0 pointer-events-none" :style="shimmerStyle"></div>

    <div class="flex flex-col gap-3 relative z-10">
      <div
        class="h-5 w-7/12 rounded-md"
        :style="{ backgroundColor: appearanceOptions.color, opacity: 0.25 }"
      ></div>
      <div
        class="h-3.5 w-4/12 rounded-md"
        :style="{ backgroundColor: appearanceOptions.color, opacity: 0.15 }"
      ></div>
    </div>

    <div class="flex items-center justify-between relative z-10 mt-auto pt-4">
      <div
        class="h-4 w-3/12 rounded-md"
        :style="{ backgroundColor: appearanceOptions.color, opacity: 0.15 }"
      ></div>
      <div
        class="h-6 w-6 rounded-full"
        :style="{ backgroundColor: appearanceOptions.color, opacity: 0.2 }"
      ></div>
    </div>
  </div>
</template>

<style scoped>
.shimmer-overlay {
  transform: translateX(-100%);
  animation: shimmer 1.8s infinite linear;
}

@keyframes shimmer {
  100% {
    transform: translateX(100%);
  }
}
</style>
