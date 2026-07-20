<script setup lang="ts">
import type { CSSProperties } from 'vue';

const props = defineProps<{
  term: string;
  textAlign: CSSProperties['textAlign'];
}>();
const emit = defineEmits<{ update: [field: string, value: string] }>();
</script>

<template>
  <div class="group relative">
    <input
      class="w-full bg-transparent border-none outline-none cursor-text p-2 hover:ring-1 hover:ring-dashed hover:ring-gray-400 rounded transition-all placeholder:text-gray-400 placeholder:italic"
      :style="{ textAlign: props.textAlign }"
      placeholder="Enter term..."
      @change="$emit('update', 'term', ($event.target as HTMLInputElement).value)"
      :value="props.term"
      @click.stop
    />
  </div>
</template>
