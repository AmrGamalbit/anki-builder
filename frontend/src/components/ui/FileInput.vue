<script setup lang="ts">
import InputGenerator from '@/components/InputGenerator.vue';
import '@/assets/global.css';

const props = defineProps(['modelValue']);
const emits = defineEmits(['update:modelValue']);

async function handleSubmit() {
  const response = await fetch('http://127.0.0.1:8000/generate-deck', {
    method: 'POST',
    body: formData,
    headers: {
      'Content-type': 'multipart/form-data',
    },
  });
  const data = await response.json();
}
</script>

<template>
  <div class="w-full py-9 bg-white rounded-sm border border-dashed border-gray-300">
    <div class="flex flex-col items-center gap-4">
      <div class="flex flex-col items-center gap-1">
        <svg
          width="40"
          height="40"
          viewBox="0 0 40 40"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        ></svg>
        <p class="text-gray-400 text-xs">CSV, XLC or XLCX, smaller than 15MB</p>
      </div>

      <div class="flex flex-col items-center gap-2">
        <p class="text-gray-900 text-sm font-medium">Drag and Drop your file here or</p>
        <label class="cursor-pointer">
          <input
            type="file"
            class="hidden"
            @change="$emit('update:modelValue', $event.target.files[0])"
          />
          <span
            class="flex w-28 h-9 px-2 bg-primary-muted rounded-full shadow text-white text-xs font-semibold items-center justify-center"
          >
            Choose File
          </span>
        </label>
      </div>
    </div>
  </div>
</template>
