<script setup lang="ts">
import { ref } from 'vue';
import { XMarkIcon } from '@heroicons/vue/16/solid';

const tagColors: string[] = [
  '#2563eb', // Blue
  '#7c3aed', // Violet
  '#c026d3', // Fuchsia
  '#e11d48', // Rose
  '#ea580c', // Orange
  '#16a34a', // Green
  '#0d9488', // Teal
  '#0284c7', // Sky Blue (Darkened for contrast)
  '#4f46e5', // Indigo
  '#9333ea', // Purple
  '#d97706', // Amber (Darkened for contrast)
  '#059669', // Emerald
  '#475569', // Slate
  '#dc2626', // Red
];
const tags = defineModel<string[]>({ default: () => [] });
const props = defineProps<{ maxTags: number }>();
const newTag = ref('');

function getTagColor(name: string): string {
  const index =
    name.split('').reduce((acc, char) => acc + char.charCodeAt(0), 0) % tagColors.length;
  return tagColors[index]!;
}

function handleBackspace() {
  if (newTag.value == '' && tags.value.length > 0) {
    tags.value.pop();
  }
}

function addTag() {
  if (tags.value.length >= props.maxTags) return;
  const trimmed = newTag.value.trim().replace(/,/g, '');
  if (!trimmed || tags.value.includes(trimmed)) {
    newTag.value = '';
    return;
  }
  tags.value = [...tags.value, trimmed];
  newTag.value = '';
}

function removeTag(index: number) {
  tags.value.splice(index, 1);
}
</script>
<template>
  <div
    class="flex min-h-10 flex-wrap items-center gap-2 w-full bg-white text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-1.5 shadow-sm transition duration-300 ease hover:border-slate-300 focus-within:border-slate-400 focus-within:shadow cursor-text"
  >
    <div
      v-for="(tag, index) in tags"
      :key="tag"
      class="inline-flex h-7 items-center justify-center rounded-md px-3 text-sm font-semibold text-white shadow-sm transition-opacity hover:opacity-90"
      :style="{ backgroundColor: getTagColor(tag) }"
    >
      {{ tag }}
      <button
        type="button"
        class="inline-flex items-center justify-center rounded-full hover:bg-black/20 focus:outline-none p-0.5 transition-colors"
        @click.stop="removeTag(index)"
      >
        <XMarkIcon class="w-3.5 h-3.5 stroke-[2.5]" />
      </button>
    </div>

    <input
      ref="tagInput"
      v-model="newTag"
      type="text"
      placeholder="Enter a tag..."
      class="flex-1 min-w-[100px] h-7 bg-transparent text-sm font-medium text-slate-700 placeholder:text-slate-400 focus:outline-none border-none p-0"
      @keydown.enter.prevent="addTag"
      @keydown.comma.prevent="addTag"
      @keydown.delete="handleBackspace"
    />
  </div>
</template>
