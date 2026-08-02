<script setup lang="ts">
import { ref } from 'vue';

const props = defineProps<{ candidates: Record<string, string> }>();
const selectedWords = defineModel<string[]>();
const newWord = ref('');
const levelColors: Record<string, string> = {
  A1: '#16a34a', // green — beginner, easy
  A2: '#0d9488', // teal
  B1: '#0284c7', // blue
  B2: '#7c3aed', // violet
  C1: '#c026d3', // fuchsia
  C2: '#dc2626', // red — advanced, hardest
};

function getLevelColor(level: string): string {
  return levelColors[String(level).toUpperCase()] ?? '#475569';
}

function addWord() {
  const trimmed = newWord.value.trim().replace(/,/g, '');
  if (!trimmed || selectedWords.value.includes(trimmed)) {
    newWord.value = '';
    return;
  }
  selectedWords.value = [...selectedWords.value, trimmed];
  newWord.value = '';
}

function toggleWord(word: string) {
  if (selectedWords.value?.includes(word)) {
    selectedWords.value = selectedWords.value.filter((w) => w != word);
  } else {
    selectedWords.value = [...(selectedWords.value ?? []), word];
  }
}
</script>

<template>
  <div
    class="flex min-h-10 flex-wrap items-center gap-2 w-full bg-white text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-1.5 shadow-sm transition duration-300 ease hover:border-slate-300 focus-within:border-slate-400 focus-within:shadow"
  >
    <div
      v-for="(level, term) in props.candidates"
      @click="toggleWord(term)"
      :key="term"
      class="inline-flex flex-col select-none h-fit items-center justify-center rounded-md px-3 py-1 text-sm font-semibold text-white shadow-sm transition-opacity hover:opacity-90"
      :class="{ 'opacity-40': !selectedWords?.includes(term) }"
      :style="{ backgroundColor: getLevelColor(level) }"
    >
      {{ term }}
      <span class="text-xs">{{ level }}</span>
    </div>
    <input
      ref="tagInput"
      v-model="newWord"
      type="text"
      placeholder="+ Add word..."
      class="flex-1 min-w-[100px] h-7 bg-transparent text-sm font-medium text-slate-700 placeholder:text-slate-400 focus:outline-none border-none p-0"
      @keydown.enter.prevent="addWord"
      @keydown.comma.prevent="addWord"
    />
  </div>
</template>
