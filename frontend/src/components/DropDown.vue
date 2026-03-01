<script setup lang="ts">
import { ref, computed } from 'vue';

const props = defineProps({
  options: {
    type: Array,
    required: true,
  },
  modelValue: {
    default: null,
  },
});

const emit = defineEmits(['update:modelValue']);

const isDropDownVisible = ref<boolean>(false);
const selectedOption = ref<string | null>(null);
const toggleOptionSelect = (option: string) => {
  selectedOption.value = option;
  isDropDownVisible.value = false;
  emit('update:modelValue', option.value);
};
const mappedSelectedOption = computed(() => {
  return selectedOption.value?.name || selectedOption.value || 'Please select something';
});
const changeDropDownVisibility = computed(() => {
  if (isDropDownVisible.value == true) {
    isDropDownVisible.value = false;
  } else {
    isDropDownVisible.value = true;
  }
  isDropDownVisible.value;
});
</script>

<template>
  <div class="inline-block cursor-pointer">
    <div
      class="inline-flex w-full justify-center gap-x-1.5 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-xs inset-ring-1 inset-ring-gray-300 hover:bg-gray-50"
      @click="changeDropDownVisibility"
    >
      <div>
        {{ mappedSelectedOption }}
      </div>
    </div>
    <div
      v-if="isDropDownVisible"
      class="w-56 origin-top-right rounded-md bg-white shadow-lg outline-1 outline-black/5 transition transition-discrete [--anchor-gap:--spacing(2)] data-closed:scale-95 data-closed:transform data-closed:opacity-0 data-enter:duration-100 data-enter:ease-out data-leave:duration-75 data-leave:ease-in absolute"
    >
      <div
        v-for="(option, index) in props.options"
        :key="index"
        class="block px-4 py-2 text-sm text-gray-700 focus:bg-gray-100 focus:text-gray-900 focus:outline-hidden"
        @click="toggleOptionSelect(option)"
      >
        {{ option.name || option }}
      </div>
    </div>
  </div>
</template>
