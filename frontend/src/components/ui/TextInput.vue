<script setup lang="ts">
const props = defineProps(['modelValue']);
const emits = defineEmits(['update:modelValue']);
</script>

<template>
  <div>
    <label for="deck-generator__input" class="sr-only">Place your words, separated by commas</label>
    <textarea
      name="Words Input"
      id="deck-generator__input"
      class="bg-white w-full h-50 rounded-bl-sm rounded-br-sm border border-gray-300 border-dashed focus:outline-none p-2"
      placeholder="Place your words, separated by commas"
      @input="$emit('update:modelValue', $event.target.value)"
    ></textarea>
  </div>
</template>
