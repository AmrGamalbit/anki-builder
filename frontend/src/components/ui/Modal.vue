<script setup lang="ts">
import { XMarkIcon } from '@heroicons/vue/16/solid';

const isOpen = defineModel<boolean>();
const props = defineProps<{ title?: string; class?: string }>();
</script>

<template>
  <Teleport to="body">
    <div class="modal fixed inset-0 bg-gray-500/75 flex-center z-50" v-if="isOpen">
      <div
        class="bg-white rounded-xl shadow transition-all flex justify-between flex-row-reverse items-start p-6"
        :class="props.class"
      >
        <button class="cursor-pointer" @click="isOpen = false">
          <XMarkIcon class="w-5 h-5 text-gray-400 hover:text-gray-600" />
        </button>
        <div class="overflow-y-auto flex-1 w-full h-full">
          <slot />
        </div>
      </div>
    </div>
  </Teleport>
</template>
