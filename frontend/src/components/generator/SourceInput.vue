<script setup lang="ts">
import { ref } from 'vue';

import FileInput from './sources/BaseFileInput.vue';
import TextInput from './sources/BaseTextInput.vue';
import WordInput from './sources/BaseWordInput.vue';
const options = ['Single Word', 'Paste Text', 'CSV File'];
const selectedSource = ref<number>(1);
const sourceValues = defineModel();
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
    <WordInput v-if="selectedSource == 0" v-model="sourceValues" />
    <TextInput v-else-if="selectedSource == 1" v-model="sourceValues" />
    <FileInput v-else v-model="sourceValues" />
  </section>
</template>
