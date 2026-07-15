<script setup lang="ts">
import { EyeSlashIcon, EyeIcon } from '@heroicons/vue/16/solid';
import { ref, computed } from 'vue';
import { syncApiKeys } from '@/api/auth';

const showKey = ref(false);
const id = `api-key-${Math.random().toString(36).slice(2)}`;
const props = defineProps<{
  label: string;
}>();
const providerKey = props.label.toLowerCase();
const apiKey = ref(JSON.parse(localStorage.getItem('apikeys') ?? '{}')[providerKey] ?? '');
async function saveApiKey(newValue: string) {
  const savedKeys = JSON.parse(localStorage.getItem('apikeys') ?? '{}');
  savedKeys[providerKey] = newValue;
  localStorage.setItem('apikeys', JSON.stringify(savedKeys));
  apiKey.value = newValue;
  await syncApiKeys();
}
const isFocused = ref(false);
const maskedKey = computed(() => {
  if (!apiKey.value) return;
  return apiKey.value.slice(0, 4) + '•'.repeat(Math.max(apiKey.value.length - 4, 0));
});
</script>

<template>
  <div class="relative">
    <input
      type="text"
      :id="id"
      placeholder="••••••••"
      class="w-full px-4 py-2.5 bg-white border border-gray-500 rounded-lg text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500 block transition-all"
      :value="isFocused ? apiKey : maskedKey"
      @blur="
        saveApiKey(($event.target as HTMLInputElement).value);
        isFocused = false;
      "
      @focus="isFocused = true"
    />
    <label :for="id" class="absolute -top-3 left-3 px-5 text-sm text-neutral bg-accent rounded">{{
      props.label
    }}</label>
    <button
      type="button"
      class="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-400 hover:text-gray-600 focus:outline-none"
    >
      <div @click="showKey = !showKey" class="cursor-pointer">
        <Transition mode="out-in">
          <EyeIcon class="h-5 w-5 text-gray-500" v-if="showKey" />
          <EyeSlashIcon class="h-5 w-5 text-gray-500" v-else />
        </Transition>
      </div>
    </button>
  </div>
</template>

<style>
.v-enter-active,
.v-leave-active {
  transition: opacity 0.15s ease;
}
.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
