<script setup lang="ts">
import { ref, watch } from 'vue';
import FileInput from './inputs/FileInput.vue';
import TextInput from './inputs/TextInput.vue';
import UrlInput from './inputs/UrlInput.vue';
import { useGeneratorStore } from '@/stores/generator.ts';
import { storeToRefs } from 'pinia';

const generatorStore = useGeneratorStore();
const { content, contentOptions, contentType } = storeToRefs(generatorStore);
const selectedInputIndex = ref<number>(0);
const inputSources = [
  { label: 'Paste Text', component: TextInput, type: 'text' },
  { label: 'CSV File', component: FileInput, type: 'file' },
  { label: 'Web Article', component: UrlInput, type: 'article' },
  { label: 'Youtube', component: UrlInput, type: 'youtube' },
];
watch(
  selectedInputIndex,
  (newVal) => {
    contentType.value = inputSources[newVal]?.type as string;
    content.value = '';
  },
  { immediate: true },
);
</script>

<template>
  <section>
    <h2 class="text-4xl text-neutral font-medium">Content</h2>
    <hr class="m-5" />
    <ul
      class="list-none flex justify-around bg-neutral text-surface rounded-tl-sm rounded-tr-sm items-stretch"
    >
      <li
        class="cursor-pointer items-center p-2.5 flex-center"
        :class="selectedInputIndex === index ? 'bg-primary w-1/2 text-neutral font-semibold rounded-tl-sm rounded-tr-sm' : ''"
        v-for="(option, index) in inputSources"
        :key="index"
        @click="selectedInputIndex = index"
      >
        {{ option.label }}
      </li>
    </ul>
    <component
      :is="inputSources[selectedInputIndex]?.component"
      :urlType="inputSources[selectedInputIndex]?.type"
      v-model:options="contentOptions[contentType as keyof typeof contentOptions]"
      v-model:content="content"
    />
  </section>
</template>
