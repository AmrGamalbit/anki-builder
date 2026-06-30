<script setup lang="ts">
import { useDark } from '@vueuse/core';
import OptionRow from '@/components/ui/OptionField.vue';

const isDark = useDark();
</script>

<template>
  <div>
    <h2 class="text-3xl text-neutral mb-10 font-medium">UI</h2>
    <div class="p-2">
      <OptionRow
        :option="{
          label: 'Dark Mode',
          type: 'boolean',
        }"
        v-model="isDark"
      />
    </div>
  </div>
</template>
