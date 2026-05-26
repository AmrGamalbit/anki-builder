<script setup lang="ts">
import { ref, watch } from 'vue';

import FileInput from './sources/BaseFileInput.vue';
import TextInput from './sources/BaseTextInput.vue';
import UrlInput from './sources/BaseUrlInput.vue';
const options = ['Paste Text', 'CSV File', 'Web Article', 'Youtube'];
const selectedSource = ref<number>(0);
const soruceOptions = defineModel();
watch(selectedSource, () => {
  soruceOptions.value.content = '';
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
    <TextInput v-if="selectedSource == 0" v-model="soruceOptions" />
    <FileInput v-else-if="selectedSource == 1" v-model="soruceOptions" />
    <UrlInput v-else-if="selectedSource == 2" :source-type="'web'" v-model="soruceOptions" />
    <UrlInput v-else :source-type="'youtube'" v-model="soruceOptions" />
  </section>
</template>
