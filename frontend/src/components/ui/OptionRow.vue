<script setup lang="ts">
import Toggle from './BaseToggle.vue';
import ButtonGroup from './BaseButtonGroup.vue';
import Dropdown from './BaseDropdown.vue';

interface OptionItem {
  label: string;
  value: string;
}

interface Option {
  label: string;
  type: 'boolean' | 'select' | 'choice';
  items?: OptionItem[];
}

const components = {
  boolean: Toggle,
  select: ButtonGroup,
  choice: Dropdown,
};

defineProps<{ option: Option }>();
const optionValue = defineModel();
</script>

<template>
  <div class="flex items-center justify-between">
    <span>{{ option.label }}</span>
    <component
      :is="components[option.type]"
      v-bind="option.items ? { options: option.items } : {}"
      v-model="optionValue"
      @click="console.log(optionValue)"
    />
  </div>
</template>
