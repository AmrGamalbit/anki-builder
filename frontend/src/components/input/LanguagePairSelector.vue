<script setup lang="ts">
import DropDown from '@/components/ui/BaseDropdown.vue';

const sourceLanguage = defineModel('sourceLanguage');
const targetLanguage = defineModel('targetLanguage');
const displayNames = new Intl.DisplayNames(['en'], { type: 'language' });
const languageCodes = [
  'en',
  'ar',
  'fr',
  'de',
  'es',
  'pt',
  'it',
  'nl',
  'ru',
  'zh',
  'ja',
  'ko',
  'hi',
  'tr',
  'pl',
  'sv',
  'da',
  'fi',
  'nb',
  'cs',
  'ro',
  'hu',
  'el',
  'he',
  'fa',
  'id',
  'ms',
  'th',
  'vi',
  'uk',
];
const languages = languageCodes.map((code) => {
  return { label: displayNames.of(code), value: code };
});
</script>

<template>
  <section class="flex items-center justify-center gap-3 mb-5">
    <DropDown :options="languages" v-model="sourceLanguage" />

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

    <DropDown :options="languages" v-model="targetLanguage" />
  </section>
</template>
