<script setup lang="ts">
import {
  DocumentTextIcon,
  SparklesIcon,
  PencilSquareIcon,
  ArrowDownTrayIcon,
} from '@heroicons/vue/16/solid';

const steps = [
  {
    id: 0,
    icon: DocumentTextIcon,
    title: 'Add your content',
    desc: 'Paste text, upload a file, add a URL, or drop an image.',
  },
  {
    id: 1,
    icon: SparklesIcon,
    title: 'Generate your cards',
    desc: 'AI or dictionary sources extract vocabulary and build definitions automatically.',
  },
  {
    id: 2,
    icon: PencilSquareIcon,
    title: 'Review and edit',
    desc: "Browse your cards, tweak definitions, and remove anything you don't need.",
  },
  {
    id: 3,
    icon: ArrowDownTrayIcon,
    title: 'Export to Anki',
    desc: 'Download a ready-to-use .apkg file and import it straight into Anki.',
  },
];
</script>
<template>
  <div class="w-full flex justify-center items-start">
    <TransitionGroup name="fade" tag="div" class="flex flex-wrap gap-8 justify-center" appear>
      <div
        v-for="step in steps"
        :key="step.id"
        class="flex flex-col items-center text-center max-w-48 gap-3"
        :style="{ transitionDelay: `${step.id * 0.2}s` }"
      >
        <div class="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center">
          <component :is="step.icon" class="w-6 h-6 text-primary" />
        </div>
        <h3 class="text-sm font-medium text-gray-900">{{ step.title }}</h3>
        <p class="text-xs text-gray-600 leading-relaxed">{{ step.desc }}</p>
      </div>
    </TransitionGroup>
  </div>
</template>
<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition:
    opacity 0.5s ease,
    transform 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(12px);
}
</style>
