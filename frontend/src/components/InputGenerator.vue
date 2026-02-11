<script setup lang="ts">
import SourceOptions from '@/components/GeneratorSourceOptions.vue';
import FormatOptions from '@/components/GeneratorFormatOptions.vue';
</script>

<template>
  <div class="deck-generator" id="deck-generator">
    <h2>Input</h2>
    <hr />
    <form action="" class="deck-generator__form">
      <SourceOptions />
      <label for="deck-generator__input"></label>
      <textarea name="Words Input" id="deck-generator__input"></textarea>
      <hr />
      <FormatOptions />
      <button type="submit">Generate Anki Deck</button>
    </form>
  </div>
</template>

<style scoped>
.deck-generator {
  margin: 20px;
  font-family: 'Inter', sans-serif;
  background-color: #062743;
  padding: 50px;
  color: #e5e7eb;
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
  background-color: #c4ffdd;
  font-family: inherit;
  font-size: inherit;
  border: none;
  border-radius: 5px;
  padding: 10px;
  font-weight: bold;
}
</style>
