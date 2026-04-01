<script setup lang="ts">
import { useDark } from '@vueuse/core';
import OptionRow from '@/components/ui/OptionRow.vue';
import Alert from '@/components/ui/BaseAlert.vue';
import DeckStyleEditor from '@/components/settings/DeckStyleEditor.vue';
import { computed, onMounted, ref } from 'vue';
import { onBeforeRouteLeave } from 'vue-router';

const baseUrl = import.meta.env.VITE_API_URL;
const savedCardStyles = ref(null);

async function getDefaultStyles() {
  const response = await fetch(`${baseUrl}/styles`, {
    method: 'GET',
  });
  return await response.json();
}

const cardStyles = ref({
  font_family: `'Segoe UI', sans-serif`,
  font_size: 16,
  line_height: 1.4,
  padding: 20,
  text_align: 'center',
  accent_color: 'blue',
  background_color: '#ffffff',
  color: '#1a1a1a',
  night_mode: true,
});
const isDark = useDark();
const showSuccess = ref(false);

onMounted(async () => {
  savedCardStyles.value = await getDefaultStyles();
  cardStyles.value = await getDefaultStyles();
  cardStyles.value['night_mode'] = true;
});

const haveUnsavedChanges = computed(() => {
  if (JSON.stringify(cardStyles.value) !== JSON.stringify(savedCardStyles.value)) {
    return true;
  }
  return false;
});

async function saveSettings() {
  console.log(JSON.stringify(cardStyles.value));
  const response = await fetch(`${baseUrl}/styles`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(cardStyles.value),
  });
  if (response.status == 200) {
    return true;
  } else {
    return false;
  }
}

onBeforeRouteLeave(async () => {
  if (haveUnsavedChanges.value) {
    showSuccess.value = await saveSettings();
  }
});
</script>

<template>
  <section class="font-koho p-10 md:p-16 bg-surface text-neutral">
    <h2 class="text-4xl text-neutral mb-10 font-medium">Settings</h2>
    <OptionRow
      :option="{
        label: 'Dark Mode',
        type: 'boolean',
      }"
      v-model="isDark"
    />
    <hr class="m-5" />
    <DeckStyleEditor v-model="cardStyles" />
    <Alert :intent="'success'" :title="'Card styles updated successfully'" v-model="showSuccess" />
  </section>
</template>
