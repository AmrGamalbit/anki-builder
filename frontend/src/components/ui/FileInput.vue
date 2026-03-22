<script setup lang="ts">
import '@/assets/global.css';

const file = defineModel();
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
            @change="
              (e) => {
                file = e.target.files[0];
              }
            "
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
