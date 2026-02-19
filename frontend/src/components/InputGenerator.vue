<script setup lang="ts">
import SourceOptions from '@/components/GeneratorSourceOptions.vue';
import FormatOptions from '@/components/GeneratorFormatOptions.vue';

const text = defineModel();

async function generateDeck() {
  const response = await fetch('http://127.0.0.1:8000/generate-deck', {
    method: 'POST',
    body: JSON.stringify({
      words: text.value.split(','),
      include_ponunciation: false,
      include_photos: false,
      definition_source: 'ai',
    }),
    headers: {
      'Content-type': 'application/json',
    },
  });
  const data = await response.json();
  console.log(data)
}
</script>

<template>
  <section class="p-20 bg-surface text-neutral font-koho">
    <h2 class="text-4xl font-semibold">Input</h2>
    <form action="" class="mt-10">
      <SourceOptions />
      <label for="deck-generator__input"></label>
      <textarea
        name="Words Input"
        id="deck-generator__input"
        class="w-full h-50 rounded-bl-sm rounded-br-sm border-4 border-primary-muted border-t-0 focus:outline-none p-2"
        placeholder="Place your words, separated by commas"
        v-model="text"
      ></textarea>
      <FormatOptions />
      <button
        type="submit"
        class="bg-primary text-surface font-semibold p-2 rounded-sm cursor-pointer block ml-auto mt-10"
        @click.prevent="generateDeck"
      >
        Generate Anki Deck
      </button>
    </form>
  </section>
</template>
<!--
<style scoped>
.deck-generator {
  margin: 20px;
  font-family: 'Inter', sans-serif;
  background-color: var(--bg-secondary);
  padding: 50px;
  color: var(--primary-color);
  display: flex;
  flex-direction: column;
  gap: 10px;
  border-radius: 10px;
  width: 100%;
  height: 80vh;
}

.deck-generator__form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

#deck-generator__input {
  width: 100%;
  height: 100px;
  border-radius: 10px;
}

button {
  background-color: var(--button-primary);
  color: var(--color-primary);
  font-family: inherit;
  font-size: inherit;
  border: none;
  border-radius: 5px;
  padding: 10px;
  font-weight: bold;
  cursor: pointer;
}
</style> -->
