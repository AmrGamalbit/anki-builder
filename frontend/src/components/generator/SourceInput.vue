<script setup lang="ts">
import { ref, watch } from 'vue';

import FileInput from './sources/BaseFileInput.vue';
import TextInput from './sources/BaseTextInput.vue';
import UrlInput from './sources/BaseUrlInput.vue';
const options = ['Paste Text', 'CSV File', 'Web Article', 'Youtube'];
const selectedSource = ref<number>(0);
const sourceValues = defineModel();
watch(selectedSource, () => {
  sourceValues.value.content = '';
});
</script>

<template>
  <section>
    <h2 class="text-4xl text-neutral font-medium">Source</h2>
    <hr class="m-5" />
    <ul
      class="list-none flex justify-around bg-neutral text-surface rounded-tl-sm rounded-tr-sm items-stretch"
    >
      <li
        class="cursor-pointer items-center p-2.5 flex-center"
        :class="selectedSource === index ? 'bg-primary w-1/2 text-neutral font-semibold' : ''"
        v-for="(option, index) in options"
        :key="index"
        @click="selectedSource = index"
      >
        {{ option }}
      </li>
    </ul>
    <TextInput v-if="selectedSource == 0" v-model="sourceValues" />
    <FileInput v-else-if="selectedSource == 1" v-model="sourceValues" />
    <UrlInput v-else-if="selectedSource == 2" :source-type="'web'" v-model="sourceValues" />
    <UrlInput v-else :source-type="'youtube'" v-model="sourceValues" />
    <div class="flex justify-between items-center px-3">
      <h2>Deck Name</h2>
      <div class="w-48 max-w-sm min-w-[200px]">
        <input
          class="inline-flex h-9 w-48 bg-white placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow"
          placeholder="Type here..."
          v-model="sourceValues.deck_name"
        />
      </div>
    </div>
  </section>
</template>
