<script setup lang="ts">
import DropDown from '@/components/ui/BaseDropdown.vue';

const languagePair = defineModel();
</script>

<template>
  <section class="flex items-center justify-center gap-3 my-5">
    <DropDown
      :options="[{ name: 'English', value: 'en' }]"
      v-model="languagePair.source_language"
    />

    <svg class="w-24 h-6 shrink-0 stroke-neutral" viewBox="0 0 96 24" fill="none">
      <line x1="0" y1="12" x2="72" y2="12" stroke-width="2" stroke-dasharray="6 3">
        <animate
          attributeName="stroke-dashoffset"
          from="18"
          to="0"
          dur="0.8s"
          repeatCount="indefinite"
        />
      </line>
      <polyline
        points="76,5 90,12 76,19"
        stroke-width="2"
        stroke-linejoin="round"
        stroke-linecap="round"
        fill="none"
      />
    </svg>

    <DropDown
      :options="[{ name: 'English', value: 'en' }]"
      v-model="languagePair.target_language"
    />
  </section>
</template>
