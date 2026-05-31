<script setup lang="ts">
import {
  CheckCircleIcon,
  ExclamationCircleIcon,
  InformationCircleIcon,
  XCircleIcon,
  XMarkIcon,
} from '@heroicons/vue/16/solid';
import { cva } from 'class-variance-authority';
import { computed } from 'vue';

const isVisible = defineModel();
const props = withDefaults(
  defineProps<{
    intent: 'info' | 'success' | 'warning' | 'danger';
    title: String;
    content?: String;
  }>(),
  {
    intent: 'info',
  },
);

const iconComponents = {
  info: InformationCircleIcon,
  success: CheckCircleIcon,
  warning: ExclamationCircleIcon,
  danger: XCircleIcon,
};

const containerClass = computed(() => {
  return cva('fixed bottom-4 left-4 z-100 flex p-4 rounded-md space-x-3', {
    variants: {
      intent: {
        info: 'bg-blue-100',
        success: 'bg-green-100',
        warning: 'bg-orange-100',
        danger: 'bg-red-100',
      },
    },
  })({
    intent: props.intent,
  });
});

const iconClass = computed(() => {
  return cva('w-6 h-6', {
    variants: {
      intent: {
        info: 'text-blue-700',
        success: 'text-green-700',
        warning: 'text-orange-700',
        danger: 'text-red-700',
      },
    },
  })({
    intent: props.intent,
  });
});

const titleClass = computed(() => {
  return cva('font-medium', {
    variants: {
      intent: {
        info: 'text-blue-900',
        success: 'text-green-900',
        warning: 'text-orange-700',
        danger: 'text-red-700',
      },
    },
  })({
    intent: props.intent,
  });
});

const contentClass = computed(() => {
  return cva('text-sm', {
    variants: {
      intent: {
        info: 'text-blue-800',
        success: 'text-green-800',
        warning: 'text-orange-700',
        danger: 'text-red-700',
      },
    },
  })({
    intent: props.intent,
  });
});

const closeButtonClass = computed(() => {
  return cva('cursor-pointer p-0.5 rounded-md -m-1', {
    variants: {
      intent: {
        info: 'text-blue-900/70 hover:text-blue-900 hover:bg-blue-200',
        success: 'text-green-900/70 hover:text-green-900 hover:bg-green-200',
        warning: 'text-orange-900/70 hover:text-orange-900 hover:bg-orange-200',
        danger: 'text-red-900/70 hover:text-red-900 hover:bg-red-200',
      },
    },
  })({
    intent: props.intent,
  });
});

const iconCompontent = computed(() => {
  return iconComponents[props.intent];
});
</script>

<template>
  <Transition leave-active-class="duration-300" leave-to-class="opacity-0">
    <div :class="containerClass" v-if="isVisible">
      <div class="shrink-0"><component :is="iconCompontent" :class="iconClass" /></div>
      <div class="flex-1 space-y-2">
        <h2 :class="titleClass">{{ props.title }}</h2>
        <div :class="contentClass">{{ props.content }}</div>
      </div>
      <div class="shrink-0">
        <button :class="closeButtonClass" @click="isVisible = false">
          <XMarkIcon class="w-6 h-6" />
        </button>
      </div>
    </div>
  </Transition>
</template>
