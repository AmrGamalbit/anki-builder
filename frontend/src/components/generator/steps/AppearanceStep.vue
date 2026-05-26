<script setup lang="ts">
import type { StyleOptions } from '@/types/option';
import type { SchemaField } from '@/types/schema';
import OptionField from '@/components/ui/OptionField.vue';

const styleSchema: Record<string, SchemaField> = {
  fontFamily: {
    label: 'Font family',
    type: 'choice' as const,
    items: [
      { label: 'System Default', value: 'system-ui, sans-serif' },
      { label: 'Inter', value: `'Inter', sans-serif` },
      { label: 'Noto Sans', value: `'Noto Sans', sans-serif` },
      { label: 'Merriweather', value: `'Merriweather', serif` },
      { label: 'Georgia', value: 'Georgia, serif' },
      { label: 'JetBrains Mono', value: `'JetBrains Mono', monospace` },
    ],
  },
  fontSize: { label: 'Font size', type: 'range' as const, props: { min: 14, max: 40, step: 1 } },
  lineHeight: {
    label: 'Line height',
    type: 'range' as const,
    props: { min: 1, max: 2, step: 0.1 },
  },
  padding: { label: 'Padding', type: 'range' as const, props: { min: 5, max: 30, step: 1 } },
  textAlign: {
    label: 'Text algin',
    type: 'select' as const,
    items: [
      { label: 'Left', value: 'left' },
      { label: 'Center', value: 'center' },
      { label: 'Right', value: 'right' },
    ],
  },
  accentColor: { label: 'Accent color', type: 'color' as const },
  backgroundColor: { label: 'Card background', type: 'color' as const },
  color: { label: 'Text color', type: 'color' as const },
  nightMode: { label: 'Night mode', type: 'boolean' as const },
};

const styleOptions = defineModel<StyleOptions>({
  default: {
    fontFamily: 'system-ui, sans-serif',
    fontSize: 16,
    lineHeight: 1.5,
    padding: 16,
    textAlign: 'left',
    accentColor: '#5B8DEF',
    backgroundColor: '#FFFFFF',
    color: '#1A1A1A',
    nightMode: false,
  },
});
</script>

<template>
  <section>
    <h2 class="text-4xl text-neutral font-medium">Appearance</h2>
    <hr class="m-5" />
    <div class="flex flex-col gap-4">
      <OptionField
        v-for="(option, key) in styleSchema"
        :key="key"
        :option="option"
        v-model="styleOptions[key]"
      />
    </div>
  </section>
</template>
