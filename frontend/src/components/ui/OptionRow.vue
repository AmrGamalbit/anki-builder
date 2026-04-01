<script setup lang="ts">
import Toggle from './BaseToggle.vue';
import ButtonGroup from './BaseButtonGroup.vue';
import Dropdown from './BaseDropdown.vue';
import ColorPicker from './BaseColorPicker.vue';
import Range from './BaseRange.vue';

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
    <span class="text-nowrap">{{ option.label }}</span>
    <component
      :is="components[option.type]"
      v-bind="option.items ? { options: option.items } : option.props"
      v-model="optionValue"
    />
  </div>
</template>
