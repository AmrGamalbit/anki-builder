<script setup lang="ts">
import OptionField from './OptionField.vue';
import type { SchemaField } from '@/types/schema.ts';

const props = defineProps<{ schema: Record<string, SchemaField> }>();
const values = defineModel<Record<string, unknown>>();
</script>

<template>
  <div v-if="props.schema && values">
    <OptionField
      v-for="(option, key) in props.schema"
      :key="key"
      :option="option"
      v-model="values![key]"
    />
  </div>
</template>
