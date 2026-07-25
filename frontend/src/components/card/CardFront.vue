<script setup lang="ts">
import type { CSSProperties } from 'vue';

const props = defineProps<{
  textAlign: CSSProperties['textAlign'];
}>();
const term = defineModel<string>();
</script>

<template>
  <div class="group relative">
    <input
      class="w-full bg-transparent border-none outline-none cursor-text p-2 hover:ring-1 hover:ring-dashed hover:ring-gray-400 rounded transition-all placeholder:text-gray-400 placeholder:italic"
      :style="{ textAlign: props.textAlign }"
      placeholder="Enter term..."
      v-model="term"
      @click.stop
    />
  </div>
</template>
