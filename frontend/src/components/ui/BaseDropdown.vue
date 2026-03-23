<script setup lang="ts">
import { ref, computed, onMounted, onBeforeUnmount } from 'vue';
import { useBreakpoints, breakpointsTailwind } from '@vueuse/core';

interface Option {
  label: string;
  value: string;
}

const props = defineProps<{
  options: Option[];
  modelValue: string | null;
}>();

const emit = defineEmits(['update:modelValue']);

const breakpoints = useBreakpoints(breakpointsTailwind);
const isMobile = breakpoints.smaller('md');

const isDropDownVisible = ref<boolean>(false);
const selectedOption = ref<Option | null>(null);

const toggleOptionSelect = (option: Option) => {
  selectedOption.value = option;
  isDropDownVisible.value = false;
  emit('update:modelValue', option.value);
};

const mappedSelectedOption = computed(() => {
  const placeholder = isMobile.value ? 'Select...' : 'Please Select Something';
  return selectedOption.value?.label || selectedOption.value || placeholder;
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
    <div
      v-if="isDropDownVisible"
      class="z-50 min-w-max overflow-y-auto max-h-60 origin-top-right rounded-md bg-white shadow-lg outline-1 outline-black/5 transition transition-discrete [--anchor-gap:--spacing(2)] data-closed:scale-95 data-closed:transform data-closed:opacity-0 data-enter:duration-100 data-enter:ease-out data-leave:duration-75 data-leave:ease-in absolute"
    >
      <div
        v-for="(option, index) in props.options"
        :key="index"
        class="block px-4 py-2 text-sm text-gray-700 focus:bg-gray-100 focus:text-gray-900 focus:outline-hidden"
        @click="toggleOptionSelect(option)"
      >
        {{ option.label }}
      </div>
    </div>
  </div>
</template>
