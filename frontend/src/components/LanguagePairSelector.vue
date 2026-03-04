<script setup lang="ts">
import { ref, watch } from 'vue';
import DropDown from './DropDown.vue';

const languagePair = ref({
    sourceLanguage: 'en',
    targetLanguage: 'en',
})

const props = defineProps<{
    modelValue: object | null
}>()
const emit = defineEmits(['update:modelValue']);

watch(
    languagePair,
    (newVal: Record<string, string>) => {
        emit('update:modelValue', newVal);
    },
    {
        deep: true,
        immediate: true,
    },
);
</script>

<template>
    <section class="m-5 flex justify-evenly">
        <DropDown :options="[{
            name: 'English',
            value: 'en'
        }]" v-model="languagePair.sourceLanguage" />
        <DropDown :options="[{
            name: 'English',
            value: 'en'
        }]" v-model="languagePair.targetLanguage" />
    </section>
</template>
