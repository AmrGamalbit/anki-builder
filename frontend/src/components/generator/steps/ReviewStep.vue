<script setup lang="ts">
import { useGeneratorStore } from '@/stores/generator';
import { ref } from 'vue';
import CardCarousel from '@/components/ui/CardCarousel.vue';
import CardDrawer from '@/components/CardDrawer.vue';
import { Bars3Icon } from '@heroicons/vue/16/solid';

const generatorStore = useGeneratorStore();
const index = ref(0);
const showCardDrawer = ref(false);
</script>

<template>
  <section>
    <h2 class="text-4xl text-neutral font-medium">Review</h2>
    <hr class="m-5" />
    <div class="flex justify-between">
      <div class="flex flex-col gap-5 flex-1">
        <div class="flex justify-between items-center">
          <h2 class="text-gray-900 dark:text-gray-100">Deck Name</h2>
          <div class="w-48 max-w-sm min-w-[200px]">
            <input
              class="inline-flex h-9 w-48 bg-white placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md px-3 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow"
              placeholder="Type here..."
              v-model="generatorStore.deckName"
            />
          </div>
        </div>
        <div class="flex">
          <div class="snap-center shrink-0 w-full max-w-[450px] mx-auto" @click="index++">
            <CardCarousel />
          </div>
        </div>
      </div>
      <div>
        <Transition name="drawer">
          <div
            v-if="showCardDrawer"
            class="fixed inset-0 z-50 bg-black/30"
            @click.self="showCardDrawer = false"
          >
            <CardDrawer @close="showCardDrawer = false" />
          </div>
          <div v-else>
            <button
              @click="showCardDrawer = true"
              class="fixed right-0 top-1/2 w-10 h-10 text-gray-600 cursor-pointer flex items-center justify-center bg-surface shadow-md rounded-l-md hover:bg-gray-50 transition-colors"
            >
              <Bars3Icon />
            </button>
          </div>
        </Transition>
      </div>
    </div>
  </section>
</template>

<style scoped>
.drawer-enter-active,
.drawer-leave-active {
  transition: opacity 0.25s ease-out;
}

.drawer-enter-from,
.drawer-leave-to {
  opacity: 0;
}

.drawer-enter-active > *,
.drawer-leave-active > * {
  transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

.drawer-enter-from > *,
.drawer-leave-to > * {
  transform: translateX(100%);
}
</style>
