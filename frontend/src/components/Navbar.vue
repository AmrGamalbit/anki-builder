<script setup lang="ts"></script>

<template>
  <nav class="bg-neutral flex justify-between align-center text-surface p-2 font-bold">
    <RouterLink class="cursor-pointer text-2xl" to="/">AnkiBuilder</RouterLink>
    <ul class="flex list-none gap-2">
      <li><button class="cursor-pointer">Export</button></li>
      <li><button class="cursor-pointer">Settings</button></li>
    </ul>
  </nav>
</template>
