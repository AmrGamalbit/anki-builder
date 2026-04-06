<script setup lang="ts">
import OptionRow from '../ui/OptionRow.vue';

const cardStyles = defineModel();

const options = {
  font_family: {
    label: 'Font family',
    type: 'choice',
    items: [
      { label: 'System Default', value: 'system-ui, sans-serif' },
      { label: 'Inter', value: `'Inter', sans-serif` },
      { label: 'Noto Sans', value: `'Noto Sans', sans-serif` },
      { label: 'Merriweather', value: `'Merriweather', serif` },
      { label: 'Georgia', value: 'Georgia, serif' },
      { label: 'JetBrains Mono', value: `'JetBrains Mono', monospace` },
    ],
  },
  font_size: { label: 'Font size', type: 'range', props: { min: 14, max: 40, step: 1 } },
  line_height: { label: 'Line height', type: 'range', props: { min: 1, max: 2, step: 0.1 } },
  padding: { label: 'Padding', type: 'range', props: { min: 5, max: 30, step: 1 } },
  text_align: {
    label: 'Text algin',
    type: 'select',
    items: [
      { label: 'Left', value: 'left' },
      { label: 'Center', value: 'center' },
      { label: 'Right', value: 'right' },
    ],
  },
  accent_color: { label: 'Accent color', type: 'color' },
  background_color: { label: 'Card background', type: 'color' },
  color: { label: 'Text color', type: 'color' },
  night_mode: { label: 'Night mode', type: 'boolean' },
};
</script>

<template>
  <section>
    <h2 class="text-4xl text-neutral font-medium">Style</h2>
    <hr class="m-5" />
    <div class="flex flex-col gap-4">
      <OptionRow
        v-for="(option, key) in options"
        :key="key"
        :option="option"
        v-model="cardStyles[key]"
      />
    </div>
  </section>
</template>
