<script setup lang="ts"></script>

<template>
  <div>
    <label for="single-word-input" class="sr-only">Type a single word</label>
    <input
      type="text"
      name="Single Word Input"
      id="single-word-input"
      pattern="^\S+$"
      class="w-full h-50 rounded-bl-sm rounded-br-sm border border-gray-300 border-dashed focus:outline-none p-2 text-center text-3xl font-light"
    />
  </div>
</template>
