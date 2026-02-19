<script setup lang="ts">
import { ref } from 'vue';

const options = ['Single Word', 'Paste Text', 'CSV File'];
const active = ref()
function addClass() {
  active;
}
</script>

<template>
  <ul
    class="list-none flex justify-around bg-neutral text-surface rounded-tl-sm rounded-tr-sm items-stretch"
  >
    <li
      :class="`cursor-pointer items-center p-2.5 flex-center ${active === index ? 'bg-primary w-1/2' : ''}`"
      v-for="(option, index) in options"
      @click="active = index"
    >
      {{ option }}
    </li>

    <!-- <li class="cursor-pointer bg-primary items-center p-2.5 w-full flex-center" @click="addClass">Single Word</li>
    <li class="cursor-pointer items-center p-2.5 flex-center">Paste Text</li>
    <li class="cursor-pointer items-center p-2.5 flex-center">CSV File</li> -->
  </ul>
</template>

<!-- <style scoped>
.deck-generator__source-options {
  list-style-type: none;
  display: flex;
  background-color: var(--bg-primary);
  padding: 10px;
  border-radius: 10px;
  justify-content: space-around;
}
</style> -->
