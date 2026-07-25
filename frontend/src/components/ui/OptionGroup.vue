<script setup lang="ts">
import OptionField from './OptionField.vue';
import type { SchemaField } from '@/types/schema.ts';

const props = defineProps<{ schema: Record<string, SchemaField> }>();
const values = defineModel<Record<string, unknown>>();
</script>

<template>
  <TransitionGroup tag="div" name="fade" v-if="props.schema && values">
    <OptionField
      v-for="(option, key) in props.schema"
      :key="key"
      :option="option"
      v-model="values![key]"
    />
  </TransitionGroup>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition:
    opacity 0.2s ease,
    transform 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}
</style>
