<script setup lang="ts">
import { ref } from 'vue';
import FileInput from '@/components/ui/FileInput.vue';
import SingleWordInput from '@/components/ui/WordInput.vue';
import TextInput from '@/components/ui/TextInput.vue';

const options = ['Single Word', 'Paste Text', 'CSV File'];
const active = defineModel('selectedSource');
const content = defineModel('content');
</script>

<template>
  <ul
    class="list-none flex justify-around bg-neutral text-surface rounded-tl-sm rounded-tr-sm items-stretch"
  >
    <li
      class="cursor-pointer items-center p-2.5 flex-center"
      :class="active === index ? 'bg-primary w-1/2' : ''"
      v-for="(option, index) in options"
      :key="index"
      @click="active = index"
    >
      {{ option }}
    </li>
  </ul>
  <SingleWordInput v-if="acitve == 0" v-model="content" />
  <TextInput v-else-if="acitve == 1" v-model="content" />
  <FileInput v-else v-model="content" />
</template>
