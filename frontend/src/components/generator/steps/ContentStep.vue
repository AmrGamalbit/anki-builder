<script setup lang="ts">
import { ref, watch } from 'vue';
import FileInput from './words/FileInput.vue';
import TextInput from './words/TextInput.vue';
import UrlInput from './words/UrlInput.vue';
import { useGeneratorStore } from '@/stores/generator.ts';

const generatorStore = useGeneratorStore();
const options = ['Paste Text', 'CSV File', 'Web Article', 'Youtube'];
const selectedInputIndex = ref<number>(0);
const inputComponents = [
  { component: TextInput, type: 'text' },
  { component: FileInput, type: 'file' },
  { component: UrlInput, type: 'web' },
  { component: UrlInput, type: 'youtube' },
];
generatorStore.contentType = inputComponents[selectedInputIndex.value]?.type;
watch(selectedInputIndex, (newVal) => {
  generatorStore.contentType = inputComponents[newVal]?.type;
  generatorStore.content = '';
});
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
        :class="selectedInputIndex === index ? 'bg-primary w-1/2 text-neutral font-semibold' : ''"
        v-for="(option, index) in options"
        :key="index"
        @click="selectedInputIndex = index"
      >
        {{ option }}
      </li>
    </ul>
    <component
      :is="inputComponents[selectedInputIndex]?.component"
      :url-type="inputComponents[selectedInputIndex]?.type"
      v-model:options="generatorStore.contentOptions"
      v-model:content="generatorStore.content"
    />
  </section>
</template>
