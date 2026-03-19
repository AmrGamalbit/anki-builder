<script setup lang="ts">
import { useDark } from '@vueuse/core';
import OptionRow from '@/components/ui/OptionRow.vue';

const isDark = useDark();
</script>

<template>
  <section class="font-koho p-16 bg-surface text-neutral">
    <h2 class="text-4xl text-neutral mb-10 font-medium">Settings</h2>
    <OptionRow
      :option="{
        label: 'Dark Mode',
        type: 'boolean',
      }"
      v-model="isDark"
    />
  </section>
</template>
