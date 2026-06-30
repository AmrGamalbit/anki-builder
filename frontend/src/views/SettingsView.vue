<script setup lang="ts">
import AppearanceSection from '@/components/settings/AppearanceSection.vue';
import ApiKeysSection from '@/components/settings/ApiKeysSection.vue';
</script>

<template>
  <section class="font-koho p-10 md:p-16 bg-surface text-neutral">
    <AppearanceSection />
    <hr class="m-5" />
    <ApiKeysSection />
  </section>
</template>
