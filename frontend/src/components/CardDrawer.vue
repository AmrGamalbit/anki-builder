<script setup lang="ts">
import { useGeneratorStore } from '@/stores/generator';
import { XMarkIcon, Bars3Icon } from '@heroicons/vue/16/solid';
import draggableComponent from 'vuedraggable';

const generatorStore = useGeneratorStore();
const emit = defineEmits<{ close: [] }>();
</script>

<template>
  <div
    class="h-full w-80 md:w-96 bg-surface ml-auto flex flex-col border-l border-surface -shadow-2xl"
  >
    <div
      class="flex items-center justify-between p-2 border-b border-surface bg-surface/80 backdrop-blur-sm"
    >
      <div class="flex items-center gap-2">
        <h3 class="font-semibold text-neutral tracking-wide text-base">Card List</h3>
        <span class="px-2 py-0.5 text-xs font-medium bg-gray-100 text-gray-600 rounded-full">
          {{ generatorStore.cards.length }}
        </span>
      </div>

      <button
        @click="$emit('close')"
        class="w-8 h-8 text-neutral hover:text-accent hover:bg-neutral rounded-lg transition-all cursor-pointer flex items-center justify-center focus:outline-none focus:ring-2 focus:ring-gray-200"
        aria-label="Close drawer"
      >
        <XMarkIcon class="w-5 h-5" />
      </button>
    </div>
    <div class="overflow-y-auto flex scrollbar-thin relative">
      <table class="table-auto text-sm flex-1">
        <thead
          class="bg-primary text-gray-50 uppercase text-sm tracking-wide rounded-2xl sticky top-0"
        >
          <tr>
            <th class="px-4 py-3"></th>
            <th class="px-2 py-3 font-medium w-px whitespace-nowrap">#</th>
            <th class="px-4 py-3 text-left font-medium" @click="">Term</th>
            <th class="px-4 py-3 text-left font-medium" @click="">Definition</th>
          </tr>
        </thead>
        <draggableComponent
          v-model="generatorStore.cards"
          tag="tbody"
          item-key="id"
          handle=".drag-handle"
          ghost-class="opacity-30"
          animation="200"
        >
          <template #item="{ element: card, index }">
            <tr
              class="border-t border-surface even:bg-neutral odd:bg-surface even:text-surface odd:text-neutral transition-colors"
            >
              <td class="drag-handle w-px align-middle">
                <button class="cursor-grap w-4 h-4 ml-1 cursor-grab active:cursor-grabbing">
                  <Bars3Icon />
                </button>
              </td>
              <td class="px-2 py-3 w-px whitespace-nowrap text-center select-none">
                {{ index + 1 }}
              </td>
              <td class="px-4 py-3">
                <input
                  class="field-sizing-content p-0 bg-transparent border-none outline-none placeholder:text-neutral/40 placeholder:font-semibold align-middle"
                  v-model="card.term"
                  placeholder="..."
                />
              </td>
              <td class="px-4 py-3">
                <textarea
                  rows="1"
                  class="field-sizing-content whitespace-nowrap bg-transparent p-0 border-none outline-none resize-none placeholder:text-neutral/40 placeholder:font-semibold align-middle"
                  placeholder="..."
                  v-model="card.definition"
                />
              </td></tr
          ></template>
        </draggableComponent>
      </table>
    </div>
  </div>
</template>
