<script setup lang="ts">
import Toggle from './Toggle.vue';
import ButtonGroup from './ButtonGroup.vue';
import Dropdown from './Dropdown.vue';
import ColorPicker from './ColorPicker.vue';
import Range from './Range.vue';

interface OptionItem {
  label: string;
  value: string;
}

interface Option {
  label: string;
  type: 'boolean' | 'select' | 'choice' | 'color' | 'range';
  items?: OptionItem[];
  props?: {};
}

const components = {
  boolean: Toggle,
  select: ButtonGroup,
  choice: Dropdown,
  range: Range,
  color: ColorPicker,
};

defineProps<{ option: Option }>();
const optionValue = defineModel();
</script>

<template>
  <div class="flex items-center justify-between">
    <span class="text-nowrap text-gray-900 dark:text-gray-100">{{ option.label }}</span>
    <component
      :is="components[option.type]"
      v-bind="option.items ? { options: option.items } : option.props"
      v-model="optionValue"
    />
  </div>
</template>
