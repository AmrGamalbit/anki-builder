<script setup lang="ts">
import { ref, watch } from 'vue';
import DropDown from '@/components/DropDown.vue';

const props = defineProps(['modelValue']);
const emit = defineEmits(['update:modelValue']);

const options = ref({
  includePronunciation: false,
  includePicture: false,
  definitionSource: 'dictionary',
  definitionProvider: 'oxford',
});

watch(
  options,
  (newVal) => {
    emit('update:modelValue', newVal);
  },
  {
    deep: true,
    immediate: true,
  },
);
</script>

<template>
  <h3 class="text-2xl font-medium">Options</h3>
  <div class="p-2">
    <div class="general-options">
      <ul class="flex-col accent-neutral">
        <li class="flex gap-2">
          <input
            type="checkbox"
            id="include-pronunciation"
            class="cursor-pointer"
            v-model="options.includePronunciation"
          />
          <label for="include-pronunciation">Include Pronunciations</label>
        </li>
        <li class="flex gap-2">
          <input
            type="checkbox"
            id="include-photos"
            class="cursor-pointer"
            v-model="options.includePicture"
          />
          <label for="include-picture">Include Pictures</label>
        </li>
      </ul>
    </div>
    <div class="mt-2 flex justify-between">
      <h4 class="font-medium">Definition Source</h4>
      <div class="flex gap-2">
        <DropDown
          :options="[
            { name: 'Dictionary', value: 'dictionary' },
            { name: 'AI', value: 'ai' },
          ]"
          v-model="options.definitionSource"
          id="definition-source"
        />
        <DropDown
          :options="[{ name: 'Groq', value: 'groq' }]"
          v-model="option"
          v-if="options.definitionSource == 'ai'"
          id="definition-provider"
        />
        <DropDown
          :options="[{ name: 'Oxford', value: 'oxford' }]"
          v-model="options.definitionProvider"
          v-else
          id="definition-provider"
        />
      </div>
    </div>
  </div>
</template>

<!-- <style scoped>
h3 {
  margin: 10px 0;
}

.general-options ul {
  list-style-type: none;
}

.format-options {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.definition-options {
  display: flex;
  justify-content: space-between;
}

.definition-options-choices {
  display: flex;
  gap: 10px;
}
</style> -->
