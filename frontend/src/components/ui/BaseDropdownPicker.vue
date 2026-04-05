<script setup lang="ts">
defineProps({ options: Array });

const selectedOption = defineModel('selectedOption');
const isDropDownVisible = defineModel('isDropDownVisible');

const toggleOptionSelect = (option) => {
  selectedOption.value = option.value;
  isDropDownVisible.value = false;
};
</script>
<template>
  <div
    class="z-50 min-w-max overflow-y-auto max-h-60 origin-top-right rounded-md bg-white shadow-lg outline-1 outline-black/5 transition transition-discrete [--anchor-gap:--spacing(2)] data-closed:scale-95 data-closed:transform data-closed:opacity-0 data-enter:duration-100 data-enter:ease-out data-leave:duration-75 data-leave:ease-in absolute"
  >
    <div
      v-for="(option, index) in options"
      :key="index"
      class="block px-4 py-2 text-sm text-gray-700 select-none focus:bg-gray-100 focus:text-gray-900 focus:outline-hidden"
      @click="toggleOptionSelect(option)"
    >
      {{ option.label }}
    </div>
  </div>
</template>
