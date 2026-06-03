<script setup lang="ts">
import type { SchemaField } from '@/types/schema';
import OptionField from '@/components/ui/OptionField.vue';
import PreviewCard from '@/components/ui/PreviewCard.vue';
import { useGeneratorStore } from '@/stores/generator';

const generatorStore = useGeneratorStore();
const appearanceOptionsSchema = {
  typography: {
    label: 'Typography',
    options: {
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
      fontSize: {
        label: 'Font size',
        type: 'range' as const,
        props: { min: 14, max: 40, step: 1 },
      },
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
    },
  },
  colors: {
    label: 'Colors',
    options: {
      accentColor: { label: 'Accent color', type: 'color' as const },
      backgroundColor: { label: 'Card background', type: 'color' as const },
      color: { label: 'Text color', type: 'color' as const },
      nightMode: { label: 'Night mode', type: 'boolean' as const },
    },
  },
};
const appearanceOptions = generatorStore.appearanceOptions;
</script>

<template>
  <section>
    <h2 class="text-4xl text-neutral font-medium">Appearance</h2>
    <hr class="m-5" />
    <div class="flex flex-col md:flex-row gap-10">
      <div class="flex flex-col gap-6 justify-around">
        <div v-for="(group, groupKey) in appearanceOptionsSchema" :key="groupKey">
          <h3 class="text-sm font-bold mb-3 text-primary">{{ group.label }}</h3>
          <div class="flex flex-col gap-4">
            <OptionField
              class="gap-20"
              v-for="(option, key) in group.options"
              :key="key"
              :option="option"
              v-model="appearanceOptions[key as keyof typeof appearanceOptions]"
            />
          </div>
        </div>
      </div>

      <div class="sticky top-4 self-start flex flex-col gap-4 flex-1 mb-4 md:mb-0">
        <p class="text-sm font-bold text-primary">Preview</p>
        <PreviewCard />
      </div>
    </div>
  </section>
</template>
