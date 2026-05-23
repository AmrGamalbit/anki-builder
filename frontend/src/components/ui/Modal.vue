<script setup lang="ts">
defineProps({ isOpen: false });
</script>

<template>
  <Teleport to="body">
    <div class="modal fixed inset-0 bg-gray-500/75 flex-center z-50" v-if="isOpen">
      <div class="bg-white rounded-xl shadow p-6 transition-all flex flex-col items-center">
        <slot />
      </div>
    </div>
  </Teleport>
</template>
