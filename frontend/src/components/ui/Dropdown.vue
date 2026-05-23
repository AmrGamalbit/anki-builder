<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';
import { useBreakpoints, breakpointsTailwind } from '@vueuse/core';
import BaseDropdownPicker from './DropdownPicker.vue';

interface Option {
  label: string;
  value: string;
}

const props = defineProps<{
  options: Option[];
}>();

const breakpoints = useBreakpoints(breakpointsTailwind);
const isMobile = breakpoints.smaller('md');

const isDropDownVisible = ref<boolean>(false);
const selectedOption = defineModel<string | null>();

const mappedSelectedOption = computed(() => {
  const placeholder = isMobile.value ? 'Select...' : 'Please Select Something';
  return props.options.find((o) => o.value == selectedOption.value)?.label || placeholder;
});

const changeDropDownVisibility = () => {
  isDropDownVisible.value = !isDropDownVisible.value;
};

const closeDropdown = () => {
  isDropDownVisible.value = false;
};

onMounted(() => {
  window.addEventListener('click', closeDropdown);
});

onBeforeUnmount(() => {
  window.removeEventListener('click', closeDropdown);
});
</script>

<template>
  <div class="inline-block cursor-pointer">
    <div
      class="inline-flex w-18 md:w-48 justify-center gap-x-1.5 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-xs inset-ring-1 inset-ring-gray-300 hover:bg-gray-50"
      @click.stop="changeDropDownVisibility"
    >
      <div>
        {{ mappedSelectedOption }}
      </div>
    </div>
    <BaseDropdownPicker
      v-if="isDropDownVisible"
      :options="props.options"
      v-model:selected-option="selectedOption"
      v-model:is-drop-down-visible="isDropDownVisible"
    />
  </div>
</template>
