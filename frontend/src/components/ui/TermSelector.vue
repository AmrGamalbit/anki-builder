<script setup lang="ts">
import { ref } from 'vue';

const props = defineProps<{ loading: boolean }>();
const terms = defineModel<Record<string, string>>('terms', { default: () => {} });
const selected = defineModel<string[]>('selected', { default: () => [] });
const newTerm = ref('');
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

function addTerm() {
  const trimmed = newTerm.value.trim().replace(/,/g, '');
  if (!trimmed || trimmed in terms.value) {
    newTerm.value = '';
  } else {
    terms.value[trimmed] = '';
    newTerm.value = '';
  }
}

function toggleTerm(term: string) {
  if (selected.value?.includes(term)) {
    selected.value = selected.value.filter((t) => t != term);
  } else {
    selected.value = [...selected.value, term];
  }
}
</script>

<template>
  <div
    class="flex min-h-10 flex-wrap items-center gap-2 w-full bg-white text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-1.5 shadow-sm transition duration-300 ease hover:border-slate-300 focus-within:border-slate-400 focus-within:shadow"
  >
    <div class="flex flex-wrap items-center gap-2" v-if="!props.loading">
      <div
        v-for="(level, term) in terms"
        @click="toggleTerm(term)"
        :key="term"
        class="inline-flex flex-col select-none h-fit items-center justify-center rounded-md px-3 py-1 text-sm font-semibold text-white shadow-sm transition-opacity hover:opacity-90"
        :class="{ 'opacity-40': !selected.includes(term) }"
        :style="{ backgroundColor: getLevelColor(level) }"
      >
        {{ term }}
        <span class="text-xs">{{ level }}</span>
      </div>
      <input
        ref="tagInput"
        v-model="newTerm"
        type="text"
        placeholder="+ Add word..."
        class="flex-1 min-w-[100px] h-7 bg-transparent text-sm font-medium text-slate-700 placeholder:text-slate-400 focus:outline-none border-none p-0"
        @keydown.enter.prevent="addTerm"
        @keydown.comma.prevent="addTerm"
      />
    </div>
    <div class="flex flex-wrap items-center gap-2" v-else>
      <div
        v-for="i in 15"
        :key="i"
        class="h-8 bg-gray-400 rounded animate-pulse"
        :style="{ width: 60 + Math.random() * 60 + 'px' }"
      ></div>
    </div>
  </div>
</template>
