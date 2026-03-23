<script setup lang="ts">
import {
  AdjustmentsHorizontalIcon,
  RectangleStackIcon,
  InformationCircleIcon,
} from '@heroicons/vue/16/solid';
</script>

<template>
  <nav
    class="bg-neutral dark:bg-gray-900 dark:text-white flex justify-between items-center text-surface p-2 font-bold"
  >
    <RouterLink class="group flex items-center gap-2 select-none" to="/">
      <span
        class="text-2xl font-black tracking-tight relative after:absolute after:bottom-0 after:left-0 after:h-0.5 after:w-0 after:bg-primary after:transition-all after:duration-300 hover:after:w-full hover:text-accent transition-colors select-none"
      >
        Anki<span class="text-primary">Builder</span>
      </span>
    </RouterLink>
    <ul class="flex list-none gap-5">
      <li>
        <RouterLink
          to="/generator"
          class="cursor-pointer hover:text-accent transition-colors select-none"
        >
          <RectangleStackIcon class="w-5 h-5" />
        </RouterLink>
      </li>
      <li>
        <RouterLink
          to="/settings"
          class="cursor-pointer hover:text-accent transition-colors select-none"
        >
          <AdjustmentsHorizontalIcon class="w-5 h-5" />
        </RouterLink>
      </li>
      <li>
        <RouterLink
          to="/about"
          class="cursor-pointer hover:text-accent transition-colors select-none"
        >
          <InformationCircleIcon class="w-5 h-5" />
        </RouterLink>
      </li>
    </ul>
  </nav>
</template>
