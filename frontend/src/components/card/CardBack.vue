<script setup lang="ts">
import { ref, type CSSProperties } from 'vue';
import { PlayCircleIcon } from '@heroicons/vue/16/solid';

const props = defineProps<{
  definition: string;
  audioUrl: string | null;
  textAlign: CSSProperties['textAlign'];
}>();
const emit = defineEmits<{ update: [field: string, value: string] }>();
const audioRef = ref<HTMLAudioElement | null>(null);
</script>

<template>
  <div class="w-full">
    <div class="group relative">
      <textarea
        class="w-full bg-transparent border-none outline-none cursor-text p-2 m-0 hover:ring-1 hover:ring-gray-400 rounded resize-none transition-all placeholder:text-gray-400 placeholder:italic overflow-hidden"
        :style="{ textAlign: props.textAlign }"
        :value="props.definition"
        @change="$emit('update', 'definition', ($event.target as HTMLInputElement).value)"
        placeholder="Enter definition..."
        @click.stop
      />
    </div>
    <div v-if="props.audioUrl" class="flex items-center justify-center w-full">
      <audio controls :src="props.audioUrl" class="hidden" ref="audioRef"></audio>
      <button @click.stop="audioRef?.play()">
        <PlayCircleIcon class="w-6 h-6" />
      </button>
    </div>
  </div>
</template>
