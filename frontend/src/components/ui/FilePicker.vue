<script setup lang="ts">
import { ref } from 'vue';
import { CloudArrowUpIcon, DocumentIcon, XMarkIcon } from '@heroicons/vue/24/outline';

const props = defineProps<{ accept: string; label?: string }>();
const content = defineModel<File | null>({ default: null });

const isDragging = ref(false);

function handleFile(file: File | null) {
  content.value = file;
}

function handleDrop(e: DragEvent) {
  isDragging.value = false;
  const file = e.dataTransfer?.files?.[0] ?? null;
  handleFile(file);
}

function handleChange(e: Event) {
  const file = (e.target as HTMLInputElement).files?.[0] ?? null;
  handleFile(file);
}
</script>

<template>
  <div
    class="w-full py-9 rounded-b-sm border border-dashed transition-colors"
    :class="isDragging ? 'border-primary bg-primary/5' : 'border-gray-300 bg-white'"
    @dragover.prevent="isDragging = true"
    @dragleave.prevent="isDragging = false"
    @drop.prevent="handleDrop"
  >
    <div v-if="!content" class="flex flex-col items-center gap-4">
      <CloudArrowUpIcon class="w-10 h-10 text-gray-400" />
      <div class="flex flex-col items-center gap-2">
        <p class="text-gray-900 text-sm font-medium">Drag and drop your file here or</p>
        <label class="cursor-pointer">
          <input type="file" class="hidden" :accept="props.accept" @change="handleChange" />
          <span
            class="flex w-28 h-9 px-2 bg-primary rounded-full text-white text-xs font-semibold items-center justify-center"
          >
            Choose file
          </span>
        </label>
        <p class="text-gray-400 text-xs">
          {{ props.label ?? 'Supported file types: ' + props.accept }}
        </p>
      </div>
    </div>

    <div v-else class="flex items-center justify-between px-6">
      <div class="flex items-center gap-3">
        <DocumentIcon class="w-8 h-8 text-primary" />
        <div>
          <p class="text-sm font-medium text-gray-900">{{ content.name }}</p>
          <p class="text-xs text-gray-400">{{ (content.size / 1024).toFixed(1) }} KB</p>
        </div>
      </div>
      <button @click.prevent="handleFile(null)" class="text-gray-400 hover:text-gray-600">
        <XMarkIcon class="w-5 h-5" />
      </button>
    </div>
  </div>
</template>
