<script setup lang="ts">
import MagicIcon from './navbar-icons/MagicIcon.vue';
import SliderIcon from './navbar-icons/SlidersIcon.vue';
import QuestionIcon from './navbar-icons/QuestionIcon.vue';
</script>

<template>
  <nav class="bg-neutral flex justify-between items-center text-surface p-2 font-bold">
    <RouterLink class="cursor-pointer text-3xl" to="/">AnkiBuilder</RouterLink>
    <ul class="flex list-none gap-5">
      <li>
        <RouterLink to="/generator" class="cursor-pointer">
          <MagicIcon />
        </RouterLink>
      </li>
      <li>
        <RouterLink to="/settings" class="cursor-pointer">
          <SliderIcon />
        </RouterLink>
      </li>
      <li>
        <RouterLink to="/about" class="cursor-pointer">
          <QuestionIcon />
        </RouterLink>
      </li>
    </ul>
  </nav>
</template>
