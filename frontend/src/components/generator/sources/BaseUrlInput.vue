<script setup lang="ts">
import { computed } from 'vue';
import OptionRow from '@/components/ui/OptionField.vue';

const props = defineProps({
  sourceType: String,
});
const model = defineModel();
model.value.options = {
  type: props.sourceType,
  vocabulary_level: 'b1',
  max_cards: 20,
  include_idioms: true,
};
const placeholder = computed(() => {
  if (props.sourceType == 'web') {
    return 'https://';
  } else {
    return 'https://www.youtube.com/watch?v=...';
  }
});
const options = {
  vocabulary_level: {
    label: 'Vocabulary Level',
    type: 'select',
    items: [
      { label: 'A1', value: 'a1' },
      { label: 'A2', value: 'a2' },
      { label: 'B1', value: 'b1' },
      { label: 'B2', value: 'b2' },
      { label: 'C1', value: 'c1' },
      { label: 'C2', value: 'C2' },
    ],
  },
  max_cards: {
    label: 'Max Cards',
    type: 'range',
    props: { min: 1, max: 40, step: 1 },
  },
  include_idioms: {
    label: 'Include idioms',
    type: 'boolean',
  },
};
</script>

<template>
  <section>
    <div>
      <input
        type="url"
        :placeholder="placeholder"
        v-model="model.content"
        class="bg-white dark:text-gray-900 w-full h-10 rounded-md rounded-bl-sm rounded-br-sm border border-gray-300 border-dashed focus:outline-none p-2 text-gray-900 placeholder:text-gray-400"
      />
      <div class="flex flex-col gap-2 p-3">
        <OptionRow
          v-for="(option, key) in options"
          :option="option"
          :key="key"
          v-model="model.options[key]"
        />
      </div>
    </div>
  </section>
</template>
